# NameSpaceNetworkRuleSetCreate
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
from azure.mgmt.servicebus import ServiceBusManagementClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
NAMESPACE_NAME = "my"
NETWORK_RULE_SET_NAME = "mynetworkruleset"
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"
SUBNET_NAME = "mysubnet"

BODY = {
  "properties": {
    "default_action": "Deny",
    "virtual_network_rules": [
      {
        "subnet": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        },
        "ignore_missing_vnet_service_endpoint": True
      },
      {
        "subnet": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        },
        "ignore_missing_vnet_service_endpoint": False
      },
      {
        "subnet": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        },
        "ignore_missing_vnet_service_endpoint": False
      }
    ],
    "ip_rules": [
      {
        "ip_mask": "1.1.1.1",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.2",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.3",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.4",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.5",
        "action": "Allow"
      }
    ]
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
    mgmt_client = ServiceBusManagementClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.namespaces.create_or_update_network_rule_set(RESOURCE_GROUP, NAMESPACE_NAME, NETWORK_RULE_SET_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()