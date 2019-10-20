# Creates or updates a WAF policy within a resource group
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
from azure.mgmt.network import NetworkManagementClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
APPLICATION_GATEWAY_WEB_APPLICATION_FIREWALL_POLICY_NAME = "myapplicationgatewaywebapplicationfirewallpolicy"

BODY = {
  "location": "WestUs",
  "properties": {
    "custom_rules": [
      {
        "name": "Rule1",
        "priority": "1",
        "rule_type": "MatchRule",
        "action": "Block",
        "match_conditions": [
          {
            "match_variables": [
              {
                "variable_name": "RemoteAddr"
              }
            ],
            "operator": "IPMatch",
            "match_values": [
              "192.168.1.0/24",
              "10.0.0.0/24"
            ]
          }
        ]
      },
      {
        "name": "Rule2",
        "priority": "2",
        "rule_type": "MatchRule",
        "match_conditions": [
          {
            "match_variables": [
              {
                "variable_name": "RemoteAddr"
              }
            ],
            "operator": "IPMatch",
            "match_values": [
              "192.168.1.0/24"
            ]
          },
          {
            "match_variables": [
              {
                "variable_name": "RequestHeaders",
                "selector": "UserAgent"
              }
            ],
            "operator": "Contains",
            "match_values": [
              "Windows"
            ]
          }
        ],
        "action": "Block"
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
    mgmt_client = NetworkManagementClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.web_application_firewall_policies.create_or_update(RESOURCE_GROUP, APPLICATION_GATEWAY_WEB_APPLICATION_FIREWALL_POLICY_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()