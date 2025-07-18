import pysftp

SFTP_HOST = "5.189.154.248"
SFTP_PORT = 22
SFTP_USER = "auzan"
SFTP_PASS = "Passwd093"

REMOTE_FILE_PATH = "/uploads/transformed_post_ekraf_full.csv"
LOCAL_UPLOAD_FILE = "transformed_post_ekraf_full.csv"

def download_from_sftp():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    print(f"\nAttempting to connect to {SFTP_HOST} to download...")
    try:
        with pysftp.Connection(
            host=SFTP_HOST,
            port=SFTP_PORT,
            username=SFTP_USER,
            password=SFTP_PASS,
            cnopts=cnopts,
        ) as sftp:
            print("Connection to SFTP server sccessful")
            print(f"Uploading '{LOCAL_UPLOAD_FILE}' to '{REMOTE_FILE_PATH}'...")
            sftp.put(LOCAL_UPLOAD_FILE, REMOTE_FILE_PATH)
            print("File uploaded successfully!")
    except Exception as e:
        print(f"An unexpected error occured during download: {e}")

download_from_sftp()