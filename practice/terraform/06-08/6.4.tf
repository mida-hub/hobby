resource "aws_s3_bucket" "alb_log" {
  bucket = "mida-alb-log-pragmatic-terraform"

  lifecycle_rule {
    enabled = true

    expiration {
      days = "180"
    }
  }
}