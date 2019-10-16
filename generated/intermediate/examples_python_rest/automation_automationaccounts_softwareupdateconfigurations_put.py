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
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
AUTOMATION_ACCOUNT_NAME = "myautomationaccount"
SOFTWARE_UPDATE_CONFIGURATION_NAME = "mysoftwareupdateconfiguration"

BODY = {
  "properties": {
    "updateConfiguration": {
      "operatingSystem": "Windows",
      "duration": "PT2H0M",
      "windows": {
        "excludedKbNumbers": [
          "168934",
          "168973"
        ],
        "includedUpdateClassifications": "Critical",
        "rebootSetting": "IfRequired"
      },
      "azureVirtualMachines": [
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-01",
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-02",
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-03"
      ],
      "nonAzureComputerNames": [
        "box1.contoso.com",
        "box2.contoso.com"
      ],
      "targets": {
        "azureQueries": [
          {
            "scope": [
              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources",
              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067"
            ],
            "tagSettings": {
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
              "filterOperator": "All"
            },
            "locations": [
              "Japan East",
              "UK South"
            ]
          }
        ],
        "nonAzureQueries": [
          {
            "functionAlias": "SavedSearch1",
            "workspaceId": "WorkspaceId1"
          },
          {
            "functionAlias": "SavedSearch2",
            "workspaceId": "WorkspaceId2"
          }
        ]
      }
    },
    "scheduleInfo": {
      "frequency": "Hour",
      "startTime": "2017-10-19T12:22:57+00:00",
      "timeZone": "America/Los_Angeles",
      "interval": "1",
      "expiryTime": "2018-11-09T11:22:57+00:00",
      "advancedSchedule": {
        "weekDays": [
          "Monday",
          "Thursday"
        ]
      }
    },
    "tasks": {
      "preTask": {
        "source": "HelloWorld",
        "parameters": {
          "COMPUTERNAME": "Computer1"
        }
      },
      "postTask": {
        "source": "GetCache",
        "parameters": null
      }
    }
  }
}

API_VERSION = '2017-05-15-preview'

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
    request = service_client.put("/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Automation/automationAccounts/" + AUTOMATION_ACCOUNT_NAME + "/softwareUpdateConfigurations/" + SOFTWARE_UPDATE_CONFIGURATION_NAME, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()