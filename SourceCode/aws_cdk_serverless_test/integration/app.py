import logging

from aws_cdk.core import App

from aws_cdk_serverless_test.integration.infrastructure import Infrastructure

# Set up logging.
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

app = App()
Infrastructure(app)
app.synth()
