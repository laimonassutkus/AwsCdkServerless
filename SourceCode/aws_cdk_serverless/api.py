from aws_cdk.aws_apigatewayv2 import CfnRoute
from aws_cdk.aws_lambda import Function
from aws_cdk.core import Stack, CfnOutput
from b_cfn_api_v2.api import Api
from b_cfn_lambda_integration.lambda_integration import LambdaIntegration


class CatApi(Api):
    def __init__(
            self,
            scope: Stack,
            create_backend: Function,
            read_backend: Function,
            update_backend: Function,
            delete_backend: Function
    ) -> None:
        super().__init__(
            scope=scope,
            id='CatApi',
            name='CatApi',
            protocol_type='HTTP',
            cors_configuration=Api.CorsProperty(
                allow_methods=['GET', 'PUT', 'POST', 'OPTIONS', 'DELETE'],
                allow_origins=['*'],
                allow_headers=[
                    'Content-Type',
                    'Authorization',
                ],
                max_age=300
            )
        )

        # 1. Enable default stage, and call it version 1.
        self.enable_default_stage('V1')

        self.build_route(
            id='CreateRoute',
            route_key='POST /create',
            integration=self.build_integration(
                id='CreateIntegration',
                function=create_backend
            )
        )

        self.build_route(
            id='ReadRoute',
            route_key='GET /read',
            integration=self.build_integration(
                id='ReadIntegration',
                function=read_backend
            )
        )

        self.build_route(
            id='UpdateRoute',
            route_key='PUT /update',
            integration=self.build_integration(
                id='UpdateIntegration',
                function=update_backend
            )
        )

        self.build_route(
            id='DeleteRoute',
            route_key='DELETE /delete',
            integration=self.build_integration(
                id='DeleteIntegration',
                function=delete_backend
            )
        )

        # Expose API url for easy access.
        CfnOutput(
            scope=scope,
            id='ApiUrlOutput',
            value=self.full_url
        )

    def build_integration(self, id: str, function: Function) -> LambdaIntegration:
        return LambdaIntegration(
            scope=self.stack,
            api=self,
            integration_name=id,
            lambda_function=function
        )

    def build_route(self, id: str, route_key: str, integration: LambdaIntegration) -> CfnRoute:
        return CfnRoute(
            scope=self.stack,
            id=id,
            api_id=self.ref,
            route_key=route_key,
            target=f'integrations/{integration.ref}',
        )
