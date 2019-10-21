# CosmosDBDatabaseAccountCreateMax
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
from azure.mgmt.cosmosdb import CosmosDB
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
DATABASE_ACCOUNT_NAME = "mydatabaseaccount"
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"
SUBNET_NAME = "mysubnet"

BODY = {
  "location": "westus",
  "kind": "GlobalDocumentDB",
  "properties": {
    "database_account_offer_type": "Standard",
    "ip_range_filter": "10.10.10.10",
    "is_virtual_network_filter_enabled": True,
    "virtual_network_rules": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
        "ignore_missing_vnet_service_endpoint": False
      }
    ],
    "locations": [
      {
        "failover_priority": "0",
        "location_name": "southcentralus",
        "is_zone_redundant": False
      },
      {
        "failover_priority": "1",
        "location_name": "eastus",
        "is_zone_redundant": False
      }
    ],
    "consistency_policy": {
      "default_consistency_level": "BoundedStaleness",
      "max_interval_in_seconds": "10",
      "max_staleness_prefix": "200"
    }
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
    mgmt_client = CosmosDB(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.database_accounts.create_or_update(RESOURCE_GROUP, DATABASE_ACCOUNT_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()