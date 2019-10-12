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

        # Delete Azure Firewall
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls/{AZURE_FIREWALL_NAME}?api-version=2018-11-01 '
                 , checks=[
                          ])

        # Get Azure Firewall
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls/{AZURE_FIREWALL_NAME}?api-version=2018-11-01 '
                 , checks=[
                          ])

        # Create Azure Firewall
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
                 '          "public_ip_address": {'
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
                 '                  "protocol_type": "Https",'
                 '                  "port": "443"'
                 '                }'
                 '              ],'
                 '              "target_fqdns": ['
                 '                "www.test.com"'
                 '              ],'
                 '              "source_addresses": ['
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
                 '              "source_addresses": ['
                 '                "*"'
                 '              ],'
                 '              "destination_addresses": ['
                 '                "1.2.3.4"'
                 '              ],'
                 '              "destination_ports": ['
                 '                "443"'
                 '              ],'
                 '              "protocols": ['
                 '                "TCP"'
                 '              ],'
                 '              "translated_address": "1.2.3.5",'
                 '              "translated_port": "8443"'
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
                 '              "source_addresses": ['
                 '                "192.168.1.1-192.168.1.12",'
                 '                "10.1.4.12-10.1.4.255"'
                 '              ],'
                 '              "destination_ports": ['
                 '                "443-444",'
                 '                "8443"'
                 '              ],'
                 '              "destination_addresses": ['
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

        # List all Azure Firewalls for a given resource group
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/azureFirewalls?api-version=2018-11-01 '
                 , checks=[
                          ])

        # List all Azure Firewalls for a given subscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Network/azureFirewalls?api-version=2018-11-01 '
                 , checks=[
                          ])