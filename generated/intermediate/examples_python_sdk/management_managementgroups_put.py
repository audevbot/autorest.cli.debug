# PutManagementGroup
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
from azure.mgmt.managementgroups import ManagementGroupsClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
MANAGEMENT_GROUP_NAME = "mymanagementgroup"

BODY = {
  "id": "/providers/Microsoft.Management/managementGroups/ChildGroup",
  "type": "/providers/Microsoft.Management/managementGroups",
  "name": "ChildGroup",
  "properties": {
    "tenant_id": "20000000-0000-0000-0000-000000000000",
    "display_name": "ChildGroup",
    "details": {
      "parent": {
        "id": "/providers/Microsoft.Management/managementGroups/RootGroup"
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
    mgmt_client = ManagementGroupsClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.management_groups.create_or_update(MANAGEMENT_GROUP_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()