# EventSubscriptions_CreateOrUpdateForCustomTopic_HybridConnectionDestination
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
from azure.mgmt.eventgrid import EventGridManagementClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
EVENT_SUBSCRIPTION_NAME = "myeventsubscription"
RESOURCE_GROUP = "myresourcegroup"
NAMESPACE_NAME = "my"
HYBRID_CONNECTION_NAME = "myhybridconnection"
STORAGE_ACCOUNT_NAME = "mystorageaccount"

BODY = {
  "properties": {
    "destination": {
      "endpoint_type": "HybridConnection",
      "properties": {
        "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Relay/namespaces/" + NAMESPACE_NAME + "/hybridConnections/" + HYBRID_CONNECTION_NAME + ""
      }
    },
    "filter": {
      "is_subject_case_sensitive": False,
      "subject_begins_with": "ExamplePrefix",
      "subject_ends_with": "ExampleSuffix"
    },
    "dead_letter_destination": {
      "endpoint_type": "StorageBlob",
      "properties": {
        "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
        "blob_container_name": "contosocontainer"
      }
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
    mgmt_client = EventGridManagementClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()