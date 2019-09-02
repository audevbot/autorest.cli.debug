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

        # network_checkfrontdoornameavailability_post
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

        # network_checkfrontdoornameavailability_post_1
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

        # network_frontdoors_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Network/frontDoors?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_put
        body = (
                 '{'
                 '  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "",'
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
                 '          "frontendEndpoints": ['
                 '            {'
                 '              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '            },'
                 '            {'
                 '              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '            }'
                 '          ],'
                 '          "acceptedProtocols": ['
                 '            "Http"'
                 '          ],'
                 '          "patternsToMatch": ['
                 '            "/*"'
                 '          ],'
                 '          "routeConfiguration": {'
                 '            "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",'
                 '            "backendPool": {'
                 '              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""'
                 '            }'
                 '          },'
                 '          "enabledState": "Enabled"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "healthProbeSettings": ['
                 '      {'
                 '        "name": "healthProbeSettings1",'
                 '        "properties": {'
                 '          "path": "/",'
                 '          "protocol": "Http",'
                 '          "intervalInSeconds": "120"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "loadBalancingSettings": ['
                 '      {'
                 '        "name": "loadBalancingSettings1",'
                 '        "properties": {'
                 '          "sampleSize": "4",'
                 '          "successfulSamplesRequired": "2"'
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
                 '              "httpPort": "80",'
                 '              "httpsPort": "443",'
                 '              "weight": "1",'
                 '              "priority": "2"'
                 '            },'
                 '            {'
                 '              "address": "contoso.com.website-us-west-2.othercloud.net",'
                 '              "httpPort": "80",'
                 '              "httpsPort": "443",'
                 '              "weight": "2",'
                 '              "priority": "1"'
                 '            },'
                 '            {'
                 '              "address": "contoso1.azurewebsites.net",'
                 '              "httpPort": "80",'
                 '              "httpsPort": "443",'
                 '              "weight": "1",'
                 '              "priority": "1"'
                 '            }'
                 '          ],'
                 '          "loadBalancingSettings": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""'
                 '          },'
                 '          "healthProbeSettings": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""'
                 '          }'
                 '        }'
                 '      }'
                 '    ],'
                 '    "frontendEndpoints": ['
                 '      {'
                 '        "name": "frontendEndpoint1",'
                 '        "properties": {'
                 '          "hostName": "www.contoso.com",'
                 '          "sessionAffinityEnabledState": "Enabled",'
                 '          "sessionAffinityTtlSeconds": "60",'
                 '          "webApplicationFirewallPolicyLink": {'
                 '            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/" + FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME + ""'
                 '          }'
                 '        }'
                 '      },'
                 '      {'
                 '        "name": "default",'
                 '        "properties": {'
                 '          "hostName": "frontDoor1.azurefd.net"'
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

        # network_frontdoors_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_validatecustomdomain_post
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

        # network_frontdoors_routingrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/routingRules?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_routingrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/routingRules/{ROUTING_RULE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_routingrules_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/routingRules/{ROUTING_RULE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_routingrules_put
        body = (
                 '{'
                 '  "name": "routingRule1",'
                 '  "properties": {'
                 '    "frontendEndpoints": ['
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '      },'
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '      }'
                 '    ],'
                 '    "acceptedProtocols": ['
                 '      "Http"'
                 '    ],'
                 '    "patternsToMatch": ['
                 '      "/*"'
                 '    ],'
                 '    "routeConfiguration": {'
                 '      "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",'
                 '      "backendPool": {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""'
                 '      }'
                 '    },'
                 '    "enabledState": "Enabled"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/routingRules/{ROUTING_RULE_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_routingrules_put_1
        body = (
                 '{'
                 '  "name": "redirectRoutingRule1",'
                 '  "properties": {'
                 '    "frontendEndpoints": ['
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '      },'
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""'
                 '      }'
                 '    ],'
                 '    "acceptedProtocols": ['
                 '      "Https"'
                 '    ],'
                 '    "patternsToMatch": ['
                 '      "/*"'
                 '    ],'
                 '    "routeConfiguration": {'
                 '      "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorRedirectConfiguration",'
                 '      "redirectType": "Moved",'
                 '      "redirectProtocol": "HttpsOnly",'
                 '      "customHost": "www.bing.com",'
                 '      "customPath": "/api",'
                 '      "customFragment": "fragment",'
                 '      "customQueryString": "a=b"'
                 '    },'
                 '    "enabledState": "Enabled"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/routingRules/{ROUTING_RULE_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_routingrules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/routingRules/{ROUTING_RULE_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_healthprobesettings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/healthProbeSettings?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_healthprobesettings_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/healthProbeSettings/{HEALTH_PROBE_SETTING_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_healthprobesettings_put
        body = (
                 '{'
                 '  "name": "healthProbeSettings1",'
                 '  "properties": {'
                 '    "path": "/",'
                 '    "protocol": "Http",'
                 '    "intervalInSeconds": "120"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/healthProbeSettings/{HEALTH_PROBE_SETTING_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_healthprobesettings_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/healthProbeSettings/{HEALTH_PROBE_SETTING_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_loadbalancingsettings_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/loadBalancingSettings?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_loadbalancingsettings_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/loadBalancingSettings/{LOAD_BALANCING_SETTING_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_loadbalancingsettings_put
        body = (
                 '{'
                 '  "name": "loadBalancingSettings1",'
                 '  "properties": {'
                 '    "sampleSize": "4",'
                 '    "successfulSamplesRequired": "2"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/loadBalancingSettings/{LOAD_BALANCING_SETTING_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_loadbalancingsettings_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/loadBalancingSettings/{LOAD_BALANCING_SETTING_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_backendpools_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/backendPools?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_backendpools_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/backendPools/{BACKEND_POOL_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_backendpools_put
        body = (
                 '{'
                 '  "name": "backendPool1",'
                 '  "properties": {'
                 '    "backends": ['
                 '      {'
                 '        "address": "w3.contoso.com",'
                 '        "httpPort": "80",'
                 '        "httpsPort": "443",'
                 '        "weight": "1",'
                 '        "priority": "2"'
                 '      },'
                 '      {'
                 '        "address": "contoso.com.website-us-west-2.othercloud.net",'
                 '        "httpPort": "80",'
                 '        "httpsPort": "443",'
                 '        "weight": "2",'
                 '        "priority": "1"'
                 '      },'
                 '      {'
                 '        "address": "contoso1.azurewebsites.net",'
                 '        "httpPort": "80",'
                 '        "httpsPort": "443",'
                 '        "weight": "1",'
                 '        "priority": "1"'
                 '      }'
                 '    ],'
                 '    "loadBalancingSettings": {'
                 '      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""'
                 '    },'
                 '    "healthProbeSettings": {'
                 '      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/backendPools/{BACKEND_POOL_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_backendpools_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/backendPools/{BACKEND_POOL_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_frontendendpoints_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_frontendendpoints_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_frontendendpoints_put
        body = (
                 '{'
                 '  "name": "frontendEndpoint1",'
                 '  "properties": {'
                 '    "hostName": "www.contoso.com",'
                 '    "sessionAffinityEnabledState": "Enabled",'
                 '    "sessionAffinityTtlSeconds": "60",'
                 '    "webApplicationFirewallPolicyLink": {'
                 '      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/" + FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME + ""'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_frontendendpoints_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}?api-version=2019-04-01 '
                 , checks=[
                          ])

        # network_frontdoors_frontendendpoints_enablehttps_post
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

        # network_frontdoors_frontendendpoints_disablehttps_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Network/frontDoors/{FRONT_DOOR_NAME}/frontendEndpoints/{FRONTEND_ENDPOINT_NAME}/disableHttps?api-version=2019-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # network_frontdoors_purge_post
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