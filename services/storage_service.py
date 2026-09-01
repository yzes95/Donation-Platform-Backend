"""AWS S3 Storage service for document uploads."""
import boto3
from config.settings import settings


class StorageService:
    """Handles secure file uploads (medical reports, eviction notices) to AWS S3."""

    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID or None,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY or None,
        )
        self.bucket = settings.AWS_S3_BUCKET_NAME
