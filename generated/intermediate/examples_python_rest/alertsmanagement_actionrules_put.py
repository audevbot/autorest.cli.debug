# PutActionRule
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
ACTION_RULE_NAME = "myactionrule"

BODY = {
  "location": "Global",
  "tags": {},
  "properties": {
    "scope": {
      "scopeType": "ResourceGroup",
      "values": [
        "/subscriptions/1e3ff1c0-771a-4119-a03b-be82a51e232d/resourceGroups/alertscorrelationrg"
      ]
    },
    "conditions": {
      "severity": {
        "operator": "Equals",
        "values": [
          "Sev0",
          "Sev2"
        ]
      },
      "monitorService": {
        "operator": "Equals",
        "values": [
          "Platform",
          "Application Insights"
        ]
      },
      "monitorCondition": {
        "operator": "Equals",
        "values": [
          "Fired"
        ]
      },
      "targetResourceType": {
        "operator": "NotEquals",
        "values": [
          "Microsoft.Compute/VirtualMachines"
        ]
      }
    },
    "type": "Suppression",
    "suppressionConfig": {
      "recurrenceType": "Daily",
      "schedule": {
        "startDate": "12/09/2018",
        "endDate": "12/18/2018",
        "startTime": "06:00:00",
        "endTime": "14:00:00"
      }
    },
    "description": "Action rule on resource group for daily suppression",
    "status": "Enabled"
  }
}

API_VERSION = '2019-05-05-preview'

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
    request = service_client.put("/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.AlertsManagement/actionRules/" + ACTION_RULE_NAME, query_parameters)
    response = service_client.send(request, header_parameters, BODY, **operation_config)
    print(response.text)


if __name__ == "__main__":
    run_example()