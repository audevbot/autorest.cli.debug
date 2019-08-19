# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimgmtScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_apimgmt')
    def test_apimgmt(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

# create_or_update -- create
        self.cmd('aro create  --resource-group "rg1" --name "clustername1" --location "location1" --open-shift-version "v3.11"', checks=[
        ])

        self.cmd('aro create  --resource-group "rg1" --name "clustername1"', checks=[
        ])

# create_or_update -- update
        self.cmd('aro update  --resource-group "rg1" --name "clustername1" --location "location1" --open-shift-version "v3.11"', checks=[
        ])

        self.cmd('aro update  --resource-group "rg1" --name "clustername1"', checks=[
        ])

# delete -- delete
        self.cmd('aro delete  --resource-group "rg1" --name "clustername1"', checks=[
        ])

        self.cmd('aro delete  --resource-group "rg1" --name "clustername1"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('aro list  --resource-group "rg1"', checks=[
        ])

        self.cmd('aro list  --resource-group "rg1"', checks=[
        ])

# list -- list
        self.cmd('aro list  --resource-group "rg1"', checks=[
        ])

        self.cmd('aro list  --resource-group "rg1"', checks=[
        ])

# get -- show
        self.cmd('aro show  --resource-group "rg1" --name "clustername1"', checks=[
        ])

        self.cmd('aro show  --resource-group "rg1" --name "clustername1"', checks=[
        ])
