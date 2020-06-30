import boto3
from CreationPhase import createBucket

createBucket.createBucket()

s3 = boto3.client('s3')
filename = 'HistoricalQuotes.csv'


def uploader():
    try:
        s3.upload_file(filename, createBucket.bucket, filename)
        print(f'{filename} uploaded successfully!')
    except:
        print(f"{filename} already exists on bucket {createBucket.bucket}!")
