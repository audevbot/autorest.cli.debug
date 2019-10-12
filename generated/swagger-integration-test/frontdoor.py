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

        # CheckNameAvailability
        body = (
                 '{'
                 '  "name": "sampleName",'
                 '  "type": "Microsoft.Network/frontDoors"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Network/checkFrontDoorNameAvailability?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # CheckNameAvailabilityWithSubscription
        body = (
                 '{'
                 '  "name": "sampleName",'
                 '  "type": "Microsoft.Network/frontDoors/frontendEndpoints"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Network/checkFrontDoorNameAvailability?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # List all Front Doors
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Network/frontDoors?api-version=2019-04-01 '
                 , checks=[
                          ])

        # List Front Doors in a Resource Group
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors?api-version=2019-04-01 '
                 , checks=[
                          ])

        # Get Front Door
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # Create or update specific Front Door
        body = (
                 '{'
                 '  "location": "westus",'
                 '  "tags": {'
                 '    "tag1": "value1",'
                 '    "tag2": "value2"'
                 '  },'
                 '  "properties": {'
                 '    "routingRules": ['
                 '      {'
                 '        "name": "routingRule1",'
                 '        "properties": {'
                 '          "frontend_endpoints": ['
                 '            {'
                 '              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '            },'
                 '            {'
                 '              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '            }'
                 '          ],'
                 '          "accepted_protocols": ['
                 '            "Http"'
                 '          ],'
                 '          "patterns_to_match": ['
                 '            "/*"'
                 '          ],'
                 '          "route_configuration": {'
                 '            "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",'
                 '            "backend_pool": {'
                 '              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""'
                 '            }'
                 '          },'
                 '          "enabled_state": "Enabled"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "healthProbeSettings": ['
                 '      {'
                 '        "name": "healthProbeSettings1",'
                 '        "properties": {'
                 '          "path": "/",'
                 '          "protocol": "Http",'
                 '          "interval_in_seconds": "120"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "loadBalancingSettings": ['
                 '      {'
                 '        "name": "loadBalancingSettings1",'
                 '        "properties": {'
                 '          "sample_size": "4",'
                 '          "successful_samples_required": "2"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "backendPools": ['
                 '      {'
                 '        "name": "backendPool1",'
                 '        "properties": {'
                 '          "backends": ['
                 '            {'
                 '              "address": "w3.contoso.com",'
                 '              "http_port": "80",'
                 '              "https_port": "443",'
                 '              "weight": "1",'
                 '              "priority": "2"'
                 '            },'
                 '            {'
                 '              "address": "contoso.com.website-us-west-2.othercloud.net",'
                 '              "http_port": "80",'
                 '              "https_port": "443",'
                 '              "weight": "2",'
                 '              "priority": "1"'
                 '            },'
                 '            {'
                 '              "address": "contoso1.azurewebsites.net",'
                 '              "http_port": "80",'
                 '              "https_port": "443",'
                 '              "weight": "1",'
                 '              "priority": "1"'
                 '            }'
                 '          ],'
                 '          "load_balancing_settings": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""'
                 '          },'
                 '          "health_probe_settings": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""'
                 '          }'
                 '        }'
                 '      }'
                 '    ],'
                 '    "frontendEndpoints": ['
                 '      {'
                 '        "name": "frontendEndpoint1",'
                 '        "properties": {'
                 '          "host_name": "www.contoso.com",'
                 '          "session_affinity_enabled_state": "Enabled",'
                 '          "session_affinity_ttl_seconds": "60",'
                 '          "web_application_firewall_policy_link": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/" + FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME + ""'
                 '          }'
                 '        }'
                 '      },'
                 '      {'
                 '        "name": "default",'
                 '        "properties": {'
                 '          "host_name": "frontDoor1.azurefd.net"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "backendPoolsSettings": {'
                 '      "enforceCertificateNameCheck": "Enabled"'
                 '    },'
                 '    "enabledState": "Enabled"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Delete Front Door
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # FrontDoor_ValidateCustomDomain
        body = (
                 '{'
                 '  "hostName": "www.someDomain.com"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/validateCustomDomain?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # List Frontend endpoints in a Front Door
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints?api-version=2019-04-01 '
                 , checks=[
                          ])

        # Get Frontend Endpoint
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # FrontendEndpoints_EnableHttps
        body = (
                 '{'
                 '  "certificateSource": "AzureKeyVault",'
                 '  "protocolType": "ServerNameIndication",'
                 '  "keyVaultCertificateSourceParameters": {'
                 '    "vault": {'
                 '      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.KeyVault/vaults/" + VAULT_NAME + ""'
                 '    },'
                 '    "secretName": "secret1",'
                 '    "secretVersion": "00000000-0000-0000-0000-000000000000"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}/enableHttps?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # FrontendEndpoints_DisableHttps
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}/disableHttps?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Purge content from Front Door
        body = (
                 '{'
                 '  "contentPaths": ['
                 '    "/pictures.aspx",'
                 '    "/pictures/*"'
                 '  ]'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/purge?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])