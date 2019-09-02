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

        # recoveryservices_locations_checknameavailability_post
        body = (
                 '{'
                 '  "name": "swaggerExample",'
                 '  "type": "Microsoft.RecoveryServices/Vaults"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/locations/{LOCATION_NAME}/checkNameAvailability?api-version=2016-06-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # recoveryservices_locations_checknameavailability_post_1
        body = (
                 '{'
                 '  "name": "swaggerExample2",'
                 '  "type": "Microsoft.RecoveryServices/Vaults"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/locations/{LOCATION_NAME}/checkNameAvailability?api-version=2016-06-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # recoveryservices_vaults_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.RecoveryServices/vaults?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_vaults_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_vaults_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_vaults_put
        body = (
                 '{'
                 '  "properties": {},'
                 '  "sku": {'
                 '    "name": "Standard"'
                 '  },'
                 '  "location": "West US"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # recoveryservices_vaults_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_vaults_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.RecoveryServices/operations?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_vaults_extendedinformation_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}/extendedInformation/{EXTENDED_INFORMATION_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # recoveryservices_vaults_extendedinformation_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "integrityKey": "J99wzS27fmJ+Wjot7xO5wA==",'
                 '    "algorithm": "None"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}/extendedInformation/{EXTENDED_INFORMATION_NAME}?api-version=2016-06-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # recoveryservices_vaults_extendedinformation_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}/extendedInformation/{EXTENDED_INFORMATION_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])