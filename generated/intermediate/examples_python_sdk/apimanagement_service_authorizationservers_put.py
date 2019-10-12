# ApiManagementCreateAuthorizationServer
#
# This script expects that the following environment vars are set:
#
# AZURE_TENANT: your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: your Azure Active Directory Application Client ID
# AZURE_SECRET: your Azure Active Directory Application Secret
# AZURE_SUBSCRIPTION_ID: your Azure Subscription Id

import os
import traceback
from azure.common.credentials import ServicePrincipalCredentials
from msrestazure.azure_exceptions import CloudError
from msrestazure.azure_configuration import AzureConfiguration
from msrest.service_client import ServiceClient
from msrest.polling import LROPoller
from msrestazure.polling.arm_polling import ARMPolling
from msrest.pipeline import ClientRawResponse
from azure.mgmt.apimanagement import ApiManagementClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
SERVICE_NAME = "myservice"
AUTHORIZATION_SERVER_NAME = "myauthorizationserver"

BODY = {
  "properties": {
    "display_name": "test2",
    "description": "test server",
    "client_registration_endpoint": "https://www.contoso.com/apps",
    "authorization_endpoint": "https://www.contoso.com/oauth2/auth",
    "authorization_methods": [
      "GET"
    ],
    "token_endpoint": "https://www.contoso.com/oauth2/token",
    "support_state": True,
    "default_scope": "read write",
    "grant_types": [
      "authorizationCode",
      "implicit"
    ],
    "bearer_token_sending_methods": [
      "authorizationHeader"
    ],
    "client_id": "1",
    "client_secret": "2",
    "resource_owner_username": "un",
    "resource_owner_password": "pwd"
  }
}

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()
    mgmt_client = ApiManagementClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.authorization_server.create_or_update(RESOURCE_GROUP, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()