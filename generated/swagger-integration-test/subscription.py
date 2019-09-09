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

        # getPendingSubscriptionOperations
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.Subscription/subscriptionOperations?api-version=2018-03-01-preview '
                 , checks=[
                          ])

        # createSubscription
        body = (
                 '{'
                 '  "offerType": "MS-AZR-0017P",'
                 '  "displayName": "Test Ea Azure Sub",'
                 '  "owners": ['
                 '    {'
                 '      "objectId": "973034ff-acb7-409c-b731-e789672c7b31"'
                 '    },'
                 '    {'
                 '      "objectId": "67439a9e-8519-4016-a630-f5f805eba567"'
                 '    }'
                 '  ],'
                 '  "additionalParameters": {'
                 '    "customData": {'
                 '      "key1": "value1",'
                 '      "key2": True'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /providers/Microsoft.Billing/enrollmentAccounts/{ENROLLMENT_ACCOUNT_NAME}/providers/Microsoft.Subscription/createSubscription?api-version=2018-03-01-preview '
                 '--body "{body}"'
                 , checks=[
                          ])