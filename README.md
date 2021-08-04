# RTG-Datauploader

Script for uploading files to AWS S3 Bucket

## Prerequisites

- Python: 3.5+

## Installation

### Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows

```bat
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python upload-to-s3.py --source /path/to/file --bucket aws-bucket-name --access-key=AWSACCESSKEYID --secret-key=SECRETKEY
```
