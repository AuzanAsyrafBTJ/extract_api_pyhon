import csv
from ast import literal_eval

with open("post.csv", mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    data = list(reader)

    transformed_data = []
    for item in data:
        # Convert string representation of dict to actual dict
        try:
            user_dict = literal_eval(item.get("user", "{}"))
        except:
            user_dict = {}
        
        # Handle categories and tags which might also be string representations of lists
        try:
            categories = literal_eval(item.get("categories", "[]"))
        except:
            categories = []
            
        try:
            tags = literal_eval(item.get("tags", "[]"))
        except:
            tags = []

        transformed = {
            "id": item.get("id"),
            "title": item.get("title"),
            "slug": item.get("slug"),
            "excerpt": item.get("excerpt"),
            "thumbnail_seo": item.get("thumbnail_seo"),
            "published_at": item.get("published_at"),
            "published": item.get("published"),
            "likes": item.get("likes"),
            "views": item.get("views"),
            "meta_title": item.get("meta_title"),
            "meta_description": item.get("meta_description"),
            "meta_keywords": item.get("meta_keywords"),
            "user_id": item.get("user_id"),
            "created_at": item.get("created_at"),
            "updated_at": item.get("updated_at"),
            "user_name": user_dict.get("name"),
            "user_email": user_dict.get("email"),
            "categories": "|".join([str(c.get("title", "")) for c in categories]),
            "tags": "|".join([str(t.get("name", "")) for t in tags]),
            "attachments": item.get("attachments"),
            "liked": item.get("liked")
            
        }
        transformed_data.append(transformed)

    if transformed_data:
        headers = transformed_data[0].keys()
        with open("transformed_post_ekraf_full.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(transformed_data)
        
        print("CSV berhasil disimpan sebagai 'transformed_post_ekraf.csv'")