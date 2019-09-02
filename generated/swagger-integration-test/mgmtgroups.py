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

        # management_managementgroups_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.Management/managementGroups?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_managementgroups_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_managementgroups_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_managementgroups_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_managementgroups_put
        body = (
                 '{'
                 '  "id": "/providers/Microsoft.Management/managementGroups/ChildGroup",'
                 '  "type": "/providers/Microsoft.Management/managementGroups",'
                 '  "name": "ChildGroup",'
                 '  "properties": {'
                 '    "tenantId": "20000000-0000-0000-0000-000000000000",'
                 '    "displayName": "ChildGroup",'
                 '    "details": {'
                 '      "parent": {'
                 '        "id": "/providers/Microsoft.Management/managementGroups/RootGroup"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # management_managementgroups_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_managementgroups_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_managementgroups_descendants_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}/descendants?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # management_managementgroups_put_1
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}/subscriptions/{sub}?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # management_managementgroups_delete_1
        self.cmd('rest '
                 '--method delete '
                 '--uri /providers/Microsoft.Management/managementGroups/{MANAGEMENT_GROUP_NAME}/subscriptions/{sub}?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # management_checknameavailability_post
        body = (
                 '{'
                 '  "name": "nameTocheck",'
                 '  "type": "/providers/Microsoft.Management/managementGroups"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Management/checkNameAvailability?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # management_starttenantbackfill_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Management/startTenantBackfill?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # management_tenantbackfillstatus_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Management/tenantBackfillStatus?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])

        # management_getentities_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Management/getEntities?api-version=2018-01-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])