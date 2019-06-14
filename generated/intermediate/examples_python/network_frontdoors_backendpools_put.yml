# Create or update specific Backend Pool
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
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
FRONT_DOOR_NAME = "myfrontdoor"
BACKEND_POOL_NAME = "mybackendpool"
LOAD_BALANCING_SETTING_NAME = "myloadbalancingsetting"
HEALTH_PROBE_SETTING_NAME = "myhealthprobesetting"

BODY = {
  "name": "backendPool1",
  "properties": {
    "backends": [
      {
        "address": "w3.contoso.com",
        "httpPort": "80",
        "httpsPort": "443",
        "weight": "1",
        "priority": "2"
      },
      {
        "address": "contoso.com.website-us-west-2.othercloud.net",
        "httpPort": "80",
        "httpsPort": "443",
        "weight": "2",
        "priority": "1"
      },
      {
        "address": "contoso1.azurewebsites.net",
        "httpPort": "80",
        "httpsPort": "443",
        "weight": "1",
        "priority": "1"
      }
    ],
    "loadBalancingSettings": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""
    },
    "healthProbeSettings": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""
    }
  }
}

API_VERSION = '2019-04-01'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials


def run_example():
    credentials = get_credentials()

    config = AzureConfiguration('https://management.azure.com')
    service_client = ServiceClient(credentials, config)

    query_parameters = {}
    query_parameters['api-version'] = API_VERSION

    header_parameters = {}
    header_parameters['Content-Type'] = 'application/json; charset=utf-8'

    operation_config = {}
    request = service_client.put("/subscriptions/" + SUBSCRIPTION + "/resourceGroups/" + RESOURCE_GR + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_N + "/backendPools/" + BACKEND_POOL_N, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()