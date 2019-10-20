# Create/Update OpenShift Managed Cluster
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
from azure.mgmt.containerservice import OpenShift
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
OPEN_SHIFT_MANAGED_CLUSTER_NAME = "myopenshiftmanagedcluster"

BODY = {
  "location": "location1",
  "tags": {
    "tier": "production",
    "archv2": ""
  },
  "properties": {
    "open_shift_version": "v3.11",
    "network_profile": {
      "vnet_cidr": "10.0.0.0/8"
    },
    "master_pool_profile": {
      "name": "master",
      "count": "3",
      "vm_size": "Standard_D4s_v3",
      "os_type": "Linux",
      "subnet_cidr": "10.0.0.0/24"
    },
    "agent_pool_profiles": [
      {
        "name": "infra",
        "role": "infra",
        "count": "2",
        "vm_size": "Standard_D4s_v3",
        "os_type": "Linux",
        "subnet_cidr": "10.0.0.0/24"
      },
      {
        "name": "compute",
        "role": "compute",
        "count": "4",
        "vm_size": "Standard_D4s_v3",
        "os_type": "Linux",
        "subnet_cidr": "10.0.0.0/24"
      }
    ],
    "router_profiles": [
      {
        "name": "default"
      }
    ],
    "auth_profile": {
      "identity_providers": [
        {
          "name": "Azure AD",
          "provider": {
            "kind": "AADIdentityProvider",
            "client_id": "clientId",
            "secret": "secret",
            "tenant_id": "tenantId",
            "customer_admin_group_id": "customerAdminGroupId"
          }
        }
      ]
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
    mgmt_client = OpenShift(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.open_shift_managed_clusters.create_or_update(RESOURCE_GROUP, OPEN_SHIFT_MANAGED_CLUSTER_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()