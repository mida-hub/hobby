resource "aws_s3_bucket" "force-destroy" {
  bucket        = "mida-force-destroy-pragmatic-terraform"
  force_destroy = true
}
