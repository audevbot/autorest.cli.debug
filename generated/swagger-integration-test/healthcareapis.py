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

        # Create or Update a service with all parameters
        body = (
                 '{'
                 '  "location": "westus2",'
                 '  "tags": {},'
                 '  "kind": "fhir-R4",'
                 '  "properties": {'
                 '    "accessPolicies": ['
                 '      {'
                 '        "object_id": "c487e7d1-3210-41a3-8ccc-e9372b78da47"'
                 '      },'
                 '      {'
                 '        "object_id": "5b307da8-43d4-492b-8b66-b0294ade872f"'
                 '      }'
                 '    ],'
                 '    "cosmosDbConfiguration": {'
                 '      "offerThroughput": "1000"'
                 '    },'
                 '    "authenticationConfiguration": {'
                 '      "authority": "https://login.microsoftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc",'
                 '      "audience": "https://azurehealthcareapis.com",'
                 '      "smartProxyEnabled": True'
                 '    },'
                 '    "corsConfiguration": {'
                 '      "origins": ['
                 '        "*"'
                 '      ],'
                 '      "headers": ['
                 '        "*"'
                 '      ],'
                 '      "methods": ['
                 '        "DELETE",'
                 '        "GET",'
                 '        "OPTIONS",'
                 '        "PATCH",'
                 '        "POST",'
                 '        "PUT"'
                 '      ],'
                 '      "maxAge": "1440",'
                 '      "allowCredentials": False'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.HealthcareApis/services/{name}?api-version=2019-09-16 '
                 '--body "{body}"'
                 , checks=[
                          ])