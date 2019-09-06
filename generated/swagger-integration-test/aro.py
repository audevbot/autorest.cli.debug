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

        # List Managed Clusters
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ContainerService/openShiftManagedClusters?api-version=2019-04-30 '
                 , checks=[
                          ])

        # Get Managed Clusters by Resource Group
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ContainerService/openShiftManagedClusters?api-version=2018-09-30-preview '
                 , checks=[
                          ])

        # Get OpenShift Managed Cluster
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ContainerService/openShiftManagedClusters/{OPEN_SHIFT_MANAGED_CLUSTER_NAME}?api-version=2019-04-30 '
                 , checks=[
                          ])

        # Create/Update OpenShift Managed Cluster
        body = (
                 '{'
                 '  "location": "location1",'
                 '  "tags": {'
                 '    "tier": "production",'
                 '    "archv2": ""'
                 '  },'
                 '  "properties": {'
                 '    "openShiftVersion": "v3.11",'
                 '    "networkProfile": {'
                 '      "vnetCidr": "10.0.0.0/8"'
                 '    },'
                 '    "masterPoolProfile": {'
                 '      "name": "master",'
                 '      "count": "3",'
                 '      "vmSize": "Standard_D4s_v3",'
                 '      "osType": "Linux",'
                 '      "subnetCidr": "10.0.0.0/24"'
                 '    },'
                 '    "agentPoolProfiles": ['
                 '      {'
                 '        "name": "infra",'
                 '        "role": "infra",'
                 '        "count": "2",'
                 '        "vmSize": "Standard_D4s_v3",'
                 '        "osType": "Linux",'
                 '        "subnetCidr": "10.0.0.0/24"'
                 '      },'
                 '      {'
                 '        "name": "compute",'
                 '        "role": "compute",'
                 '        "count": "4",'
                 '        "vmSize": "Standard_D4s_v3",'
                 '        "osType": "Linux",'
                 '        "subnetCidr": "10.0.0.0/24"'
                 '      }'
                 '    ],'
                 '    "routerProfiles": ['
                 '      {'
                 '        "name": "default"'
                 '      }'
                 '    ],'
                 '    "authProfile": {'
                 '      "identityProviders": ['
                 '        {'
                 '          "name": "Azure AD",'
                 '          "provider": {'
                 '            "kind": "AADIdentityProvider",'
                 '            "clientId": "clientId",'
                 '            "secret": "secret",'
                 '            "tenantId": "tenantId",'
                 '            "customerAdminGroupId": "customerAdminGroupId"'
                 '          }'
                 '        }'
                 '      ]'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ContainerService/openShiftManagedClusters/{OPEN_SHIFT_MANAGED_CLUSTER_NAME}?api-version=2019-04-30 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Update OpenShift Managed Cluster Tags
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ContainerService/openShiftManagedClusters/{OPEN_SHIFT_MANAGED_CLUSTER_NAME}?api-version=2019-04-30 '
                 , checks=[
                          ])

        # Delete OpenShift Managed Cluster
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ContainerService/openShiftManagedClusters/{OPEN_SHIFT_MANAGED_CLUSTER_NAME}?api-version=2019-04-30 '
                 , checks=[
                          ])