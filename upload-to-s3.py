import argparse
import os

import boto3
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Upload file to AWS S3 bucket")

parser.add_argument(
    "--source",
    type=str,
    help="File to be uploaded",
    required=True
)
parser.add_argument(
    "--bucket",
    type=str,
    help="AWS S3 bucket name",
    required=True
)
parser.add_argument(
    "--access-key",
    type=str,
    help="AWS access key (AWS_ACCESS_KEY_ID)",
    required=False,
    default=None
)
parser.add_argument(
    "--secret-key",
    type=str,
    help="AWS secret access key (AWS_SECRET_ACCESS_KEY)",
    required=False,
    default=None
)


def upload(access_key, secret_key, bucket, filepath):
    client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    filesize = os.stat(filepath).st_size
    filename = os.path.basename(filepath)

    with tqdm(total=filesize, unit="bytes",
              unit_scale=True, unit_divisor=1024) as progress, \
         open(filepath, "rb") as source:
        client.upload_fileobj(
            Fileobj=source,
            Bucket=bucket,
            Key=filename,
            Callback=(
                lambda bytes_transferred, p=progress:
                    p.update(bytes_transferred)
            )
        )


if __name__ == "__main__":
    args = parser.parse_args()
    upload(
        access_key=args.access_key,
        secret_key=args.secret_key,
        bucket=args.bucket,
        filepath=args.source
    )
