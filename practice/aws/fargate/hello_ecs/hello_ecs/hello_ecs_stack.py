from aws_cdk import core as cdk

import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecsp

class HelloEcsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecsp.ApplicationLoadBalancedFargateService(self, "MyWebServer",
            task_image_options=ecsp.ApplicationLoadBalancedTaskImageOptions(
                # image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")),
                image=ecs.ContainerImage.from_registry("public.ecr.aws/f0e4c8e7/nginx-test:latest")),
            public_load_balancer=True
        )
