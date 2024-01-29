import boto3
import numpy as np

BUCKET = "ingest"
KEY = "source/large_file"


def boto3_read(i: int) -> None:
    client = boto3.client(
        "s3",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin",
        endpoint_url="http://localhost:9000",
    )
    with client.get_object(Bucket=BUCKET, Key=KEY)["Body"] as body:
        print(f"Read: ({i}): Starting to read")
        body.read()
        print(f"Read: ({i}): Finished")


def boto3_write(size: int) -> None:
    s3 = boto3.client(
        "s3",
        aws_access_key_id="minioadmin",
        aws_secret_access_key="minioadmin",
        endpoint_url="http://localhost:9000",
    )
    # Quickly initialize a large byte array
    data = np.zeros((size), dtype=np.uint8).tobytes()
    print(f"Write: {len(data):,} bytes to write.")

    # Create bucket if it doesn't exist
    buckets = s3.list_buckets()
    if BUCKET not in [b["Name"] for b in buckets["Buckets"]]:
        s3.create_bucket(Bucket=BUCKET)

    # Write the large file
    res = s3.put_object(Bucket=BUCKET, Key=KEY, Body=data)
    print(f"Write: HTTP {res['ResponseMetadata']['HTTPStatusCode']}")
