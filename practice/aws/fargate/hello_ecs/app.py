#!/usr/bin/env python3

from aws_cdk import core

from hello_ecs.hello_ecs_stack import HelloEcsStack


app = core.App()
HelloEcsStack(app, "hello-ecs")

app.synth()
