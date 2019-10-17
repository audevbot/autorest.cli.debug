# CreatePool - Full Example
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
from azure.mgmt.batch import BatchManagement
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
BATCH_ACCOUNT_NAME = "mybatchaccount"
POOL_NAME = "mypool"
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"
SUBNET_NAME = "mysubnet"
APPLICATION_NAME = "myapplication"
CERTIFICATE_NAME = "mycertificate"

BODY = {
  "properties": {
    "display_name": "my-pool-name",
    "vm_size": "STANDARD_D4",
    "inter_node_communication": "Enabled",
    "max_tasks_per_node": "13",
    "task_scheduling_policy": {
      "node_fill_type": "Pack"
    },
    "deployment_configuration": {
      "cloud_service_configuration": {
        "os_family": "4",
        "os_version": "WA-GUEST-OS-4.45_201708-01"
      }
    },
    "network_configuration": {
      "subnet_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
      "endpoint_configuration": {
        "inbound_nat_pools": [
          {
            "name": "testnat",
            "protocol": "TCP",
            "backend_port": "12001",
            "frontend_port_range_start": "15000",
            "frontend_port_range_end": "15100",
            "network_security_group_rules": [
              {
                "access": "Allow",
                "source_address_prefix": "192.100.12.45",
                "priority": "150"
              },
              {
                "access": "Deny",
                "source_address_prefix": "*",
                "priority": "3500"
              }
            ]
          }
        ]
      }
    },
    "scale_settings": {
      "fixed_scale": {
        "target_dedicated_nodes": "6",
        "target_low_priority_nodes": "28",
        "resize_timeout": "PT8M",
        "node_deallocation_option": "TaskCompletion"
      }
    },
    "metadata": [
      {
        "name": "metadata-1",
        "value": "value-1"
      },
      {
        "name": "metadata-2",
        "value": "value-2"
      }
    ],
    "start_task": {
      "command_line": "cmd /c SET",
      "resource_files": [
        {
          "http_url": "https://testaccount.blob.core.windows.net/example-blob-file",
          "file_path": "c:\\temp\\gohere",
          "file_mode": "777"
        }
      ],
      "environment_settings": [
        {
          "name": "MYSET",
          "value": "1234"
        }
      ],
      "user_identity": {
        "auto_user": {
          "scope": "Pool",
          "elevation_level": "Admin"
        }
      },
      "max_task_retry_count": "6",
      "wait_for_success": True
    },
    "user_accounts": [
      {
        "name": "username1",
        "password": "examplepassword",
        "elevation_level": "Admin",
        "linux_user_configuration": {
          "ssh_private_key": "sshprivatekeyvalue",
          "uid": "1234",
          "gid": "4567"
        }
      }
    ],
    "application_packages": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/applications/" + APPLICATION_NAME + "",
        "version": "asdf"
      }
    ],
    "certificates": [
      {
        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/certificates/" + CERTIFICATE_NAME + "",
        "store_location": "LocalMachine",
        "store_name": "MY",
        "visibility": [
          "RemoteUser"
        ]
      }
    ],
    "application_licenses": [
      "app-license0",
      "app-license1"
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
    mgmt_client = BatchManagement(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()