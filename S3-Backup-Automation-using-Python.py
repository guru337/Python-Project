import boto3
import os
import datetime

# AWS S3 Configuration
bucket_name = 's3-bucket-name'
local_folder = '/path/to/your/local/folder'
s3 = boto3.client('s3')

# Create a date-stamped folder in S3
today = datetime.datetime.now().strftime('%Y-%m-%d')
s3_folder = f'backups/{today}/'

def upload_files():
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_folder)
            s3_key = s3_folder + relative_path.replace("\\", "/")  # for Windows/Linux compatibility

            try:
                s3.upload_file(local_path, bucket_name, s3_key)
                print(f"Uploaded: {s3_key}")
            except Exception as e:
                print(f"Failed to upload {s3_key}: {str(e)}")

if __name__ == "__main__":
    upload_files()
