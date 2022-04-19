from aws_cdk.core import App

from aws_cdk_serverless_test.integration.infrastructure import Infrastructure

app = App()
Infrastructure(app)
app.synth()
