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

        BODY = {}
        output = mgmt_client.azure_firewalls.delete(RESOURCE_GROUP, AZURE_FIREWALL_NAME, BODY)
        BODY = {}
        output = mgmt_client.azure_firewalls.get(RESOURCE_GROUP, AZURE_FIREWALL_NAME, BODY)
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
        output = mgmt_client.azure_firewalls.create_or_update(RESOURCE_GROUP, AZURE_FIREWALL_NAME, BODY)
        BODY = {}
        output = mgmt_client.azure_firewalls.list(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.azure_firewalls.list_all(, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()