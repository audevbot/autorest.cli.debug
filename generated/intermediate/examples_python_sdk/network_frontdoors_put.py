# Create or update specific Front Door
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
from azure.mgmt.frontdoor import FrontdoorClient
import uuid

SUBSCRIPTION_ID = os.environ['AZURE_SUBSCRIPTION_ID']
RESOURCE_GROUP = "myresourcegroup"
FRONT_DOOR_NAME = "myfrontdoor"
FRONTEND_ENDPOINT_NAME = "myfrontendendpoint"
BACKEND_POOL_NAME = "mybackendpool"
LOAD_BALANCING_SETTING_NAME = "myloadbalancingsetting"
HEALTH_PROBE_SETTING_NAME = "myhealthprobesetting"
FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME = "myfrontdoorwebapplicationfirewallpolicy"

BODY = {
  "location": "westus",
  "tags": {
    "tag1": "value1",
    "tag2": "value2"
  },
  "properties": {
    "routing_rules": [
      {
        "name": "routingRule1",
        "properties": {
          "frontend_endpoints": [
            {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
            },
            {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
            }
          ],
          "accepted_protocols": [
            "Http"
          ],
          "patterns_to_match": [
            "/*"
          ],
          "route_configuration": {
            "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",
            "backend_pool": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""
            }
          },
          "enabled_state": "Enabled"
        }
      }
    ],
    "health_probe_settings": [
      {
        "name": "healthProbeSettings1",
        "properties": {
          "path": "/",
          "protocol": "Http",
          "interval_in_seconds": "120"
        }
      }
    ],
    "load_balancing_settings": [
      {
        "name": "loadBalancingSettings1",
        "properties": {
          "sample_size": "4",
          "successful_samples_required": "2"
        }
      }
    ],
    "backend_pools": [
      {
        "name": "backendPool1",
        "properties": {
          "backends": [
            {
              "address": "w3.contoso.com",
              "http_port": "80",
              "https_port": "443",
              "weight": "1",
              "priority": "2"
            },
            {
              "address": "contoso.com.website-us-west-2.othercloud.net",
              "http_port": "80",
              "https_port": "443",
              "weight": "2",
              "priority": "1"
            },
            {
              "address": "contoso1.azurewebsites.net",
              "http_port": "80",
              "https_port": "443",
              "weight": "1",
              "priority": "1"
            }
          ],
          "load_balancing_settings": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""
          },
          "health_probe_settings": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""
          }
        }
      }
    ],
    "frontend_endpoints": [
      {
        "name": "frontendEndpoint1",
        "properties": {
          "host_name": "www.contoso.com",
          "session_affinity_enabled_state": "Enabled",
          "session_affinity_ttl_seconds": "60",
          "web_application_firewall_policy_link": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/" + FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME + ""
          }
        }
      },
      {
        "name": "default",
        "properties": {
          "host_name": "frontDoor1.azurefd.net"
        }
      }
    ],
    "backend_pools_settings": {
      "enforce_certificate_name_check": "Enabled"
    },
    "enabled_state": "Enabled"
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
    mgmt_client = FrontdoorClient(credentials, os.environ['AZURE_SUBSCRIPTION_ID'])
    response = mgmt_client.front_doors.create_or_update(RESOURCE_GROUP, FRONT_DOOR_NAME, BODY)
    if isinstance(response, LROPoller):
        while not response.done():
            response.wait(timeout=30)
        response = response.result()
    print(str(response))


if __name__ == "__main__":
    run_example()