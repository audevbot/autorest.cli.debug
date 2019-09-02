# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import time
import mock
import unittest

from azure_devtools.scenario_tests.const import MOCKED_SUBSCRIPTION_ID
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, LiveScenarioTest, ResourceGroupPreparer, create_random_name, live_only, record_only
from azure.cli.core.util import get_file_json


class ResourceGroupScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_rg_scenario')
    def test_resource_group(self, resource_group):

        self.cmd('group create -n {rg} -l westus --tag a=b c', checks=[
            self.check('name', '{rg}'),
            self.check('tags', {'a': 'b', 'c': ''})
        ])

        self.kwargs['sub'] = self.get_subscription_id()
        self.kwargs['name'] = 'zimsxyzname'

        # network_azurefirewalls_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls/{AZURE_FIREWALL_NAME}?api-version=2018-11-01 '
                 , checks=[
                          ])

        # network_azurefirewalls_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls/{AZURE_FIREWALL_NAME}?api-version=2018-11-01 '
                 , checks=[
                          ])

        # network_azurefirewalls_put
        body = (
                 '{'
                 '  "tags": {'
                 '    "key1": "value1"'
                 '  },'
                 '  "properties": {'
                 '    "ipConfigurations": ['
                 '      {'
                 '        "name": "azureFirewallIpConfiguration",'
                 '        "properties": {'
                 '          "subnet": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""'
                 '          },'
                 '          "publicIPAddress": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/publicIPAddresses/" + PUBLIC_IP_ADDRESS_NAME + ""'
                 '          }'
                 '        }'
                 '      }'
                 '    ],'
                 '    "applicationRuleCollections": ['
                 '      {'
                 '        "name": "apprulecoll",'
                 '        "properties": {'
                 '          "priority": "110",'
                 '          "action": {'
                 '            "type": "Deny"'
                 '          },'
                 '          "rules": ['
                 '            {'
                 '              "name": "rule1",'
                 '              "description": "Deny inbound rule",'
                 '              "protocols": ['
                 '                {'
                 '                  "protocolType": "Https",'
                 '                  "port": "443"'
                 '                }'
                 '              ],'
                 '              "targetFqdns": ['
                 '                "www.test.com"'
                 '              ],'
                 '              "sourceAddresses": ['
                 '                "216.58.216.164",'
                 '                "10.0.0.0/24"'
                 '              ]'
                 '            }'
                 '          ]'
                 '        }'
                 '      }'
                 '    ],'
                 '    "natRuleCollections": ['
                 '      {'
                 '        "name": "natrulecoll",'
                 '        "properties": {'
                 '          "priority": "112",'
                 '          "action": {'
                 '            "type": "Dnat"'
                 '          },'
                 '          "rules": ['
                 '            {'
                 '              "name": "DNAT-HTTPS-traffic",'
                 '              "description": "D-NAT all outbound web traffic for inspection",'
                 '              "sourceAddresses": ['
                 '                "*"'
                 '              ],'
                 '              "destinationAddresses": ['
                 '                "1.2.3.4"'
                 '              ],'
                 '              "destinationPorts": ['
                 '                "443"'
                 '              ],'
                 '              "protocols": ['
                 '                "TCP"'
                 '              ],'
                 '              "translatedAddress": "1.2.3.5",'
                 '              "translatedPort": "8443"'
                 '            }'
                 '          ]'
                 '        }'
                 '      }'
                 '    ],'
                 '    "networkRuleCollections": ['
                 '      {'
                 '        "name": "netrulecoll",'
                 '        "properties": {'
                 '          "priority": "112",'
                 '          "action": {'
                 '            "type": "Deny"'
                 '          },'
                 '          "rules": ['
                 '            {'
                 '              "name": "L4-traffic",'
                 '              "description": "Block traffic based on source IPs and ports",'
                 '              "sourceAddresses": ['
                 '                "192.168.1.1-192.168.1.12",'
                 '                "10.1.4.12-10.1.4.255"'
                 '              ],'
                 '              "destinationPorts": ['
                 '                "443-444",'
                 '                "8443"'
                 '              ],'
                 '              "destinationAddresses": ['
                 '                "*"'
                 '              ],'
                 '              "protocols": ['
                 '                "TCP"'
                 '              ]'
                 '            }'
                 '          ]'
                 '        }'
                 '      }'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls/{AZURE_FIREWALL_NAME}?api-version=2018-11-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_azurefirewalls_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls?api-version=2018-11-01 '
                 , checks=[
                          ])

        # network_azurefirewalls_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Network/azureFirewalls?api-version=2018-11-01 '
                 , checks=[
                          ])