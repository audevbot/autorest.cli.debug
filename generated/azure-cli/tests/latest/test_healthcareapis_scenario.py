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
        self.cmd('healthcareapis create  --resource-group "rg1" --resource-name "service1" --kind "fhir-R4" --location "westus2" --cosmos-db-offer-throughput "1000" --authentication-authority "https://login.microsoftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc" --authentication-audience "https://azurehealthcareapis.com" --authentication-smart-proxy-enabled true --cors-origins "*" --cors-headers "*" --cors-methods "DELETE,GET,OPTIONS,PATCH,POST,PUT" --cors-max-age "1440" --cors-allow-credentials false', checks=[
        ])

        self.cmd('healthcareapis create  --resource-group "rg1" --resource-name "service2" --kind "fhir-R4" --location "westus2"', checks=[
        ])

        self.cmd('healthcareapis create  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

        self.cmd('healthcareapis create  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

# create_or_update -- update
        self.cmd('healthcareapis update  --resource-group "rg1" --resource-name "service1" --kind "fhir-R4" --location "westus2" --cosmos-db-offer-throughput "1000" --authentication-authority "https://login.microsoftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc" --authentication-audience "https://azurehealthcareapis.com" --authentication-smart-proxy-enabled true --cors-origins "*" --cors-headers "*" --cors-methods "DELETE,GET,OPTIONS,PATCH,POST,PUT" --cors-max-age "1440" --cors-allow-credentials false', checks=[
        ])

        self.cmd('healthcareapis update  --resource-group "rg1" --resource-name "service2" --kind "fhir-R4" --location "westus2"', checks=[
        ])

        self.cmd('healthcareapis update  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

        self.cmd('healthcareapis update  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

# delete -- delete
        self.cmd('healthcareapis delete  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

        self.cmd('healthcareapis delete  --resource-group "rg1" --resource-name "service2"', checks=[
        ])

        self.cmd('healthcareapis delete  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

        self.cmd('healthcareapis delete  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

# list -- list
        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

        self.cmd('healthcareapis list  --resource-group "rg1"', checks=[
        ])

# get -- show
        self.cmd('healthcareapis show  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

        self.cmd('healthcareapis show  --resource-group "rg1" --resource-name "service2"', checks=[
        ])

        self.cmd('healthcareapis show  --resource-group "rg1" --resource-name "service1"', checks=[
        ])

        self.cmd('healthcareapis show  --resource-group "rg1" --resource-name "service1"', checks=[
        ])
