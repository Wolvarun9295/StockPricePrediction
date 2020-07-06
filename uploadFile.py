import boto3
import createBucket

s3 = boto3.client('s3')
filename = 'GOOGL.csv'


def uploader():
    try:
        s3.upload_file(filename, createBucket.bucket, filename)
        print(f'{filename} uploaded successfully!')
    except:
        print(f"{filename} already exists on bucket {createBucket.bucket}!")


uploader()
