# Create Azure Firewall
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
AZURE_FIREWALL_NAME = "myazurefirewall"
VIRTUAL_NETWORK_NAME = "myvirtualnetwork"
SUBNET_NAME = "mysubnet"
PUBLIC_IP_ADDRESS_NAME = "mypublicipaddress"

BODY = {
  "tags": {
    "key1": "value1"
  },
  "properties": {
    "ip_configurations": [
      {
        "name": "azureFirewallIpConfiguration",
        "properties": {
          "subnet": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
          },
          "public_ip_address": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/publicIPAddresses/" + PUBLIC_IP_ADDRESS_NAME + ""
          }
        }
      }
    ],
    "application_rule_collections": [
      {
        "name": "apprulecoll",
        "properties": {
          "priority": "110",
          "action": {
            "type": "Deny"
          },
          "rules": [
            {
              "name": "rule1",
              "description": "Deny inbound rule",
              "protocols": [
                {
                  "protocol_type": "Https",
                  "port": "443"
                }
              ],
              "target_fqdns": [
                "www.test.com"
              ],
              "source_addresses": [
                "216.58.216.164",
                "10.0.0.0/24"
              ]
            }
          ]
        }
      }
    ],
    "nat_rule_collections": [
      {
        "name": "natrulecoll",
        "properties": {
          "priority": "112",
          "action": {
            "type": "Dnat"
          },
          "rules": [
            {
              "name": "DNAT-HTTPS-traffic",
              "description": "D-NAT all outbound web traffic for inspection",
              "source_addresses": [
                "*"
              ],
              "destination_addresses": [
                "1.2.3.4"
              ],
              "destination_ports": [
                "443"
              ],
              "protocols": [
                "TCP"
              ],
              "translated_address": "1.2.3.5",
              "translated_port": "8443"
            }
          ]
        }
      }
    ],
    "network_rule_collections": [
      {
        "name": "netrulecoll",
        "properties": {
          "priority": "112",
          "action": {
            "type": "Deny"
          },
          "rules": [
            {
              "name": "L4-traffic",
              "description": "Block traffic based on source IPs and ports",
              "source_addresses": [
                "192.168.1.1-192.168.1.12",
                "10.1.4.12-10.1.4.255"
              ],
              "destination_ports": [
                "443-444",
                "8443"
              ],
              "destination_addresses": [
                "*"
              ],
              "protocols": [
                "TCP"
              ]
            }
          ]
        }
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
    response = mgmt_client.azure_firewalls.create_or_update(RESOURCE_GROUP, AZURE_FIREWALL_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()