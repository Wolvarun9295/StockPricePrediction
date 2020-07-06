import pandas as pd
import boto3
import uploadFile
import createBucket

client = boto3.client("s3")
path = f"s3://{createBucket.bucket}/{uploadFile.filename}"


def fetcher():
    try:
        data = pd.read_csv(path)
        print(data.head())
        return data

    except Exception:
        return print("Error! Unable to fetch the file!")


# print("\nFetching file from AWS Bucket:")
# fetcher()
