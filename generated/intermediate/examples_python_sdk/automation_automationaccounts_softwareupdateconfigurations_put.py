# Create software update configuration
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
from azure.mgmt.automation import UpdateManagementAPI
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
AUTOMATION_ACCOUNT_NAME = "myautomationaccount"
SOFTWARE_UPDATE_CONFIGURATION_NAME = "mysoftwareupdateconfiguration"

BODY = {
  "properties": {
    "update_configuration": {
      "operating_system": "Windows",
      "duration": "PT2H0M",
      "windows": {
        "excluded_kb_numbers": [
          "168934",
          "168973"
        ],
        "included_update_classifications": "Critical",
        "reboot_setting": "IfRequired"
      },
      "azure_virtual_machines": [
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-01",
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-02",
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-03"
      ],
      "non_azure_computer_names": [
        "box1.contoso.com",
        "box2.contoso.com"
      ],
      "targets": {
        "azure_queries": [
          {
            "scope": [
              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources",
              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067"
            ],
            "tag_settings": {
              "tags": [
                {
                  "tag1": [
                    "tag1Value1",
                    "tag1Value2",
                    "tag1Value3"
                  ]
                },
                {
                  "tag2": [
                    "tag2Value1",
                    "tag2Value2",
                    "tag2Value3"
                  ]
                }
              ],
              "filter_operator": "All"
            },
            "locations": [
              "Japan East",
              "UK South"
            ]
          }
        ],
        "non_azure_queries": [
          {
            "function_alias": "SavedSearch1",
            "workspace_id": "WorkspaceId1"
          },
          {
            "function_alias": "SavedSearch2",
            "workspace_id": "WorkspaceId2"
          }
        ]
      }
    },
    "schedule_info": {
      "frequency": "Hour",
      "start_time": "2017-10-19T12:22:57+00:00",
      "time_zone": "America/Los_Angeles",
      "interval": "1",
      "expiry_time": "2018-11-09T11:22:57+00:00",
      "advanced_schedule": {
        "week_days": [
          "Monday",
          "Thursday"
        ]
      }
    },
    "tasks": {
      "pre_task": {
        "source": "HelloWorld",
        "parameters": {
          "computername": "Computer1"
        }
      },
      "post_task": {
        "source": "GetCache"
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
    mgmt_client = UpdateManagementAPI(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.software_update_configurations.create(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, SOFTWARE_UPDATE_CONFIGURATION_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()