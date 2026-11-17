terraform {
  required_version = ">= 1.6, < 2.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
provider "aws" {
  region = var.region
}
variable "region" {
  type    = string
  default = "us-east-1"
}
variable "bucket_name" {
  type        = string
  description = "Globally unique synthetic lab bucket name"
}
resource "aws_s3_bucket" "evidence" {
  bucket = var.bucket_name
  tags = {
    Environment = "portfolio-lab"
  }
}
resource "aws_s3_bucket_public_access_block" "evidence" {
  bucket                  = aws_s3_bucket.evidence.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
resource "aws_s3_bucket_versioning" "evidence" {
  bucket = aws_s3_bucket.evidence.id
  versioning_configuration {
    status = "Enabled"
  }
}
resource "aws_kms_key" "evidence" {
  description             = "Customer-managed key for synthetic evidence storage"
  enable_key_rotation     = true
  deletion_window_in_days = 30
}
resource "aws_s3_bucket_server_side_encryption_configuration" "evidence" {
  bucket = aws_s3_bucket.evidence.id
  rule {
    bucket_key_enabled = true
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.evidence.arn
    }
  }
}

# S3 server access logs require an SSE-S3 destination.
resource "aws_s3_bucket" "access_logs" {
  bucket = "${var.bucket_name}-logs"
}
resource "aws_s3_bucket_public_access_block" "access_logs" {
  bucket                  = aws_s3_bucket.access_logs.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
resource "aws_s3_bucket_ownership_controls" "access_logs" {
  bucket = aws_s3_bucket.access_logs.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}
resource "aws_s3_bucket_versioning" "access_logs" {
  bucket = aws_s3_bucket.access_logs.id
  versioning_configuration {
    status = "Enabled"
  }
}
resource "aws_s3_bucket_server_side_encryption_configuration" "access_logs" {
  bucket = aws_s3_bucket.access_logs.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
data "aws_caller_identity" "current" {}
resource "aws_s3_bucket_policy" "access_logs" {
  bucket = aws_s3_bucket.access_logs.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid = "AllowEvidenceBucketLogs"
      Effect = "Allow"
      Principal = { Service = "logging.s3.amazonaws.com" }
      Action = "s3:PutObject"
      Resource = "${aws_s3_bucket.access_logs.arn}/evidence/*"
      Condition = {
        ArnLike = { "aws:SourceArn" = aws_s3_bucket.evidence.arn }
        StringEquals = { "aws:SourceAccount" = data.aws_caller_identity.current.account_id }
      }
    }]
  })
}
resource "aws_s3_bucket_logging" "evidence" {
  bucket        = aws_s3_bucket.evidence.id
  target_bucket = aws_s3_bucket.access_logs.id
  target_prefix = "evidence/"
  depends_on    = [aws_s3_bucket_policy.access_logs, aws_s3_bucket_ownership_controls.access_logs, aws_s3_bucket_server_side_encryption_configuration.access_logs]
}
