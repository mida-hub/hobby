#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk import aws_s3 as s3
class S3Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        bucket = s3.Bucket(self, 
            "MyFirstBucket", 
            versioned=True,)

app = core.App()
S3Stack(app, "S3Stack")
app.synth()
