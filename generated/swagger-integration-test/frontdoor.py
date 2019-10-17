# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

BODY = {
  "name": "sampleName",
  "type": "Microsoft.Network/frontDoors"
}
        output = mgmt_client..check_front_door_name_availability(, BODY)
BODY = {
  "name": "sampleName",
  "type": "Microsoft.Network/frontDoors/frontendEndpoints"
}
        output = mgmt_client..check_front_door_name_availability_with_subscription(, BODY)
BODY = {}
        output = mgmt_client.front_doors.list(, BODY)
BODY = {}
        output = mgmt_client.front_doors.list_by_resource_group(RESOURCE_GROUP, , BODY)
BODY = {}
        output = mgmt_client.front_doors.get(RESOURCE_GROUP, FRONT_DOOR_NAME, BODY)
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
        output = mgmt_client.front_doors.create_or_update(RESOURCE_GROUP, FRONT_DOOR_NAME, BODY)
BODY = {}
        output = mgmt_client.front_doors.delete(RESOURCE_GROUP, FRONT_DOOR_NAME, BODY)
BODY = {
  "host_name": "www.someDomain.com"
}
        output = mgmt_client.front_doors.validate_custom_domain(RESOURCE_GROUP, FRONT_DOOR_NAME, , BODY)
BODY = {}
        output = mgmt_client.frontend_endpoints.list_by_front_door(RESOURCE_GROUP, FRONT_DOOR_NAME, , BODY)
BODY = {}
        output = mgmt_client.frontend_endpoints.get(RESOURCE_GROUP, FRONT_DOOR_NAME, FRONTEND_ENDPOINT_NAME, BODY)
BODY = {
  "certificate_source": "AzureKeyVault",
  "protocol_type": "ServerNameIndication",
  "key_vault_certificate_source_parameters": {
    "vault": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.KeyVault/vaults/" + VAULT_NAME + ""
    },
    "secret_name": "secret1",
    "secret_version": "00000000-0000-0000-0000-000000000000"
  }
}
        output = mgmt_client.frontend_endpoints.enable_https(RESOURCE_GROUP, FRONT_DOOR_NAME, FRONTEND_ENDPOINT_NAME, , BODY)
BODY = {}
        output = mgmt_client.frontend_endpoints.disable_https(RESOURCE_GROUP, FRONT_DOOR_NAME, FRONTEND_ENDPOINT_NAME, , BODY)
BODY = {
  "content_paths": [
    "/pictures.aspx",
    "/pictures/*"
  ]
}
        output = mgmt_client.endpoints.purge_content(RESOURCE_GROUP, FRONT_DOOR_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()