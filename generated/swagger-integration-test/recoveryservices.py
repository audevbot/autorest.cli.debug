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

        # Availability status of Resource Name when no resource with same name, type and subscription exists, nor has been deleted within last 24 hours
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

        # Availability status of Resource Name when resource with same name, type and subscription exists
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

        # List of Recovery Services Resources in SubscriptionId
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.RecoveryServices/vaults?api-version=2016-06-01 '
                 , checks=[
                          ])

        # List of Recovery Services Resources in ResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults?api-version=2016-06-01 '
                 , checks=[
                          ])

        # Get Recovery Services Resource
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # Create of Update Recovery Services vault
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

        # Delete Recovery Services Vault
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # Update Resource
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # ListOperations
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.RecoveryServices/operations?api-version=2016-06-01 '
                 , checks=[
                          ])

        # Get ExtendedInfo of Resource
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}/extendedInformation/{EXTENDED_INFORMATION_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])

        # Put ExtendedInfo of Resource
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

        # PATCH ExtendedInfo of Resource
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.RecoveryServices/vaults/{VAULT_NAME}/extendedInformation/{EXTENDED_INFORMATION_NAME}?api-version=2016-06-01 '
                 , checks=[
                          ])