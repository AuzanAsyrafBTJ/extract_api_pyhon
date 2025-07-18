import requests
import csv
POSTS_URL = "https://api.ekraf.go.id/posts"

def fetch_api_data():
    print("Fetching data from {}...".format(POSTS_URL))
    try:
        print("Fetching data")
        response = requests.get(POSTS_URL, timeout=10)
        print(response, "This is response")
        response_json = response.json()
        data = response_json.get("data", [])
        # print(data, "ini data")

        print("First Row:", data[0])
        
        print("Headers:", data[0].keys())

        headers = data[0].keys()

        print("Data fetched successfully.")

        with open("post.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        print("Error fetching data from API:{}".format(e))

fetch_api_data()