resource "aws_iam_role" "example" {
    name   = "example"
    policy = data.aws_iam_policy_document.ec2_assume_role.json
}
