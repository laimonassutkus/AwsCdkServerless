import subprocess


def handler(event, context):
    out = subprocess.check_output(['/opt/bin/node_modules/aws-cdk/bin/cdk', '--version'])
    out = out.decode()
    print(out)
