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
        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "petstore" --path "petstore" --value "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml" --format "openapi-link"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "petstore" --path "petstore" --value "http://petstore.swagger.io/v2/swagger.json" --format "swagger-link-json"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "petstore" --path "collector" --value "https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl" --format "wadl-link-json"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi" --path "currency" --value "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL" --format "wsdl-link"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi" --path "currency" --value "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL" --format "wsdl-link" --api-type "soap"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup" --description "apidescription5200" --display-name "apiname1463" --service-url "http://newechoapi.cloudapp.net/api" --path "newapiPath"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api;rev=3" --api-revision-description "Creating a Revision of an existing API" --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" --service-url "http://echoapi.cloudapp.net/apiv3" --path "echo"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "echoapiv3" --description "Create Echo API into a new Version using Existing Version Set and Copy all Operations." --api-version "v4" --is-current true --api-version-set-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }}" --subscription-required true --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" --display-name "Echo API2" --service-url "http://echoapi.cloudapp.net/api" --path "echo2"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api2" --description "Copy of Existing Echo Api including Operations." --is-current true --subscription-required true --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" --display-name "Echo API2" --service-url "http://echoapi.cloudapp.net/api" --path "echo2"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup" --description "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters." --display-name "Swagger Petstore" --service-url "http://petstore.swagger.io/v2" --path "petstore"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api" --display-name "Echo API New" --service-url "http://echoapi.cloudapp.net/api2" --path "newecho"', checks=[
        ])

        self.cmd('apimgmt api create  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "petstore" --path "petstore" --value "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml" --format "openapi-link"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "petstore" --path "petstore" --value "http://petstore.swagger.io/v2/swagger.json" --format "swagger-link-json"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "petstore" --path "collector" --value "https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl" --format "wadl-link-json"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi" --path "currency" --value "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL" --format "wsdl-link"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi" --path "currency" --value "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL" --format "wsdl-link" --api-type "soap"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup" --description "apidescription5200" --display-name "apiname1463" --service-url "http://newechoapi.cloudapp.net/api" --path "newapiPath"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api;rev=3" --api-revision-description "Creating a Revision of an existing API" --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" --service-url "http://echoapi.cloudapp.net/apiv3" --path "echo"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "echoapiv3" --description "Create Echo API into a new Version using Existing Version Set and Copy all Operations." --api-version "v4" --is-current true --api-version-set-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }}" --subscription-required true --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" --display-name "Echo API2" --service-url "http://echoapi.cloudapp.net/api" --path "echo2"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api2" --description "Copy of Existing Echo Api including Operations." --is-current true --subscription-required true --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" --display-name "Echo API2" --service-url "http://echoapi.cloudapp.net/api" --path "echo2"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup" --description "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters." --display-name "Swagger Petstore" --service-url "http://petstore.swagger.io/v2" --path "petstore"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api" --display-name "Echo API New" --service-url "http://echoapi.cloudapp.net/api2" --path "newecho"', checks=[
        ])

        self.cmd('apimgmt api update  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "petstore"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "petstore"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "petstore"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api;rev=3"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "echoapiv3"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api2"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

        self.cmd('apimgmt api delete  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

# list_by_tags -- list
        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt api list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "petstore"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "petstore"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "petstore"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "soapApi"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api;rev=3"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "echoapiv3"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api2"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

        self.cmd('apimgmt api show  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api release create  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev" --notes "yahooagain"', checks=[
        ])

        self.cmd('apimgmt api release create  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev" --notes "yahooagain"', checks=[
        ])

        self.cmd('apimgmt api release create  --resource-group "rg1" --service-name "apimService1" --api-id "5a5fcc09124a7fa9b89f2f1d" --release-id "testrev"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api release update  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev" --notes "yahooagain"', checks=[
        ])

        self.cmd('apimgmt api release update  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev" --notes "yahooagain"', checks=[
        ])

        self.cmd('apimgmt api release update  --resource-group "rg1" --service-name "apimService1" --api-id "5a5fcc09124a7fa9b89f2f1d" --release-id "testrev"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api release delete  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev"', checks=[
        ])

        self.cmd('apimgmt api release delete  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev"', checks=[
        ])

        self.cmd('apimgmt api release delete  --resource-group "rg1" --service-name "apimService1" --api-id "5a5fcc09124a7fa9b89f2f1d" --release-id "testrev"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api release list  --resource-group "rg1" --service-name "apimService1" --api-id "a1"', checks=[
        ])

        self.cmd('apimgmt api release list  --resource-group "rg1" --service-name "apimService1" --api-id "a1"', checks=[
        ])

        self.cmd('apimgmt api release list  --resource-group "rg1" --service-name "apimService1" --api-id "5a5fcc09124a7fa9b89f2f1d"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api release show  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev"', checks=[
        ])

        self.cmd('apimgmt api release show  --resource-group "rg1" --service-name "apimService1" --api-id "a1" --release-id "testrev"', checks=[
        ])

        self.cmd('apimgmt api release show  --resource-group "rg1" --service-name "apimService1" --api-id "5a5fcc09124a7fa9b89f2f1d" --release-id "testrev"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api operation create  --resource-group "rg1" --service-name "apimService1" --api-id "PetStoreTemplate2" --operation-id "newoperations" --description "This can only be done by the logged in user." --display-name "createUser2" --method "POST" --url-template "/user1"', checks=[
        ])

        self.cmd('apimgmt api operation create  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api" --operation-id "operationId" --display-name "Retrieve resource" --method "GET" --url-template "/resource"', checks=[
        ])

        self.cmd('apimgmt api operation create  --resource-group "rg1" --service-name "apimService1" --api-id "57d2ef278aa04f0888cba3f3" --operation-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api operation update  --resource-group "rg1" --service-name "apimService1" --api-id "PetStoreTemplate2" --operation-id "newoperations" --description "This can only be done by the logged in user." --display-name "createUser2" --method "POST" --url-template "/user1"', checks=[
        ])

        self.cmd('apimgmt api operation update  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api" --operation-id "operationId" --display-name "Retrieve resource" --method "GET" --url-template "/resource"', checks=[
        ])

        self.cmd('apimgmt api operation update  --resource-group "rg1" --service-name "apimService1" --api-id "57d2ef278aa04f0888cba3f3" --operation-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api operation delete  --resource-group "rg1" --service-name "apimService1" --api-id "PetStoreTemplate2" --operation-id "newoperations"', checks=[
        ])

        self.cmd('apimgmt api operation delete  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api" --operation-id "operationId"', checks=[
        ])

        self.cmd('apimgmt api operation delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d2ef278aa04f0888cba3f3" --operation-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# list_by_api -- list
        self.cmd('apimgmt api operation list  --resource-group "rg1" --service-name "apimService1" --api-id "PetStoreTemplate2"', checks=[
        ])

        self.cmd('apimgmt api operation list  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api"', checks=[
        ])

        self.cmd('apimgmt api operation list  --resource-group "rg1" --service-name "apimService1" --api-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api operation show  --resource-group "rg1" --service-name "apimService1" --api-id "PetStoreTemplate2" --operation-id "newoperations"', checks=[
        ])

        self.cmd('apimgmt api operation show  --resource-group "rg1" --service-name "apimService1" --api-id "echo-api" --operation-id "operationId"', checks=[
        ])

        self.cmd('apimgmt api operation show  --resource-group "rg1" --service-name "apimService1" --api-id "57d2ef278aa04f0888cba3f3" --operation-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api operation policy create  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --operation-id "5600b57e7e8880006a080001" --policy-id "policy" --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt api operation policy create  --resource-group "rg1" --service-name "apimService1" --api-id "testapi" --operation-id "testoperation" --policy-id "policy"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api operation policy update  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --operation-id "5600b57e7e8880006a080001" --policy-id "policy" --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt api operation policy update  --resource-group "rg1" --service-name "apimService1" --api-id "testapi" --operation-id "testoperation" --policy-id "policy"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api operation policy delete  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --operation-id "5600b57e7e8880006a080001" --policy-id "policy"', checks=[
        ])

        self.cmd('apimgmt api operation policy delete  --resource-group "rg1" --service-name "apimService1" --api-id "testapi" --operation-id "testoperation" --policy-id "policy"', checks=[
        ])

# list_by_operation -- list
        self.cmd('apimgmt api operation policy list  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --operation-id "5600b57e7e8880006a080001"', checks=[
        ])

        self.cmd('apimgmt api operation policy list  --resource-group "rg1" --service-name "apimService1" --api-id "testapi" --operation-id "testoperation"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api operation policy show  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --operation-id "5600b57e7e8880006a080001" --format "xml" --policy-id "policy"', checks=[
        ])

        self.cmd('apimgmt api operation policy show  --resource-group "rg1" --service-name "apimService1" --api-id "testapi" --operation-id "testoperation" --policy-id "policy"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt tag create  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1" --display-name "tag1"', checks=[
        ])

        self.cmd('apimgmt tag create  --resource-group "rg1" --service-name "apimService1" --tag-id "temptag" --display-name "temp tag"', checks=[
        ])

        self.cmd('apimgmt tag create  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt tag update  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1" --display-name "tag1"', checks=[
        ])

        self.cmd('apimgmt tag update  --resource-group "rg1" --service-name "apimService1" --tag-id "temptag" --display-name "temp tag"', checks=[
        ])

        self.cmd('apimgmt tag update  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt tag delete  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1"', checks=[
        ])

        self.cmd('apimgmt tag delete  --resource-group "rg1" --service-name "apimService1" --tag-id "temptag"', checks=[
        ])

        self.cmd('apimgmt tag delete  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1"', checks=[
        ])

# list_by_operation -- list
        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# list_by_product -- list
        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# list_by_api -- list
        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt tag list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt tag show  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1"', checks=[
        ])

        self.cmd('apimgmt tag show  --resource-group "rg1" --service-name "apimService1" --tag-id "temptag"', checks=[
        ])

        self.cmd('apimgmt tag show  --resource-group "rg1" --service-name "apimService1" --tag-id "tagId1"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api policy create  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy" --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt api policy create  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy" --value "<policies>\r\n     <inbound>\r\n     <base />\r\n  <set-header name=\"newvalue\" exists-action=\"override\">\r\n   <value>\"@(context.Request.Headers.FirstOrDefault(h => h.Ke==\"Via\"))\" </value>\r\n    </set-header>\r\n  </inbound>\r\n      </policies>" --format "rawxml"', checks=[
        ])

        self.cmd('apimgmt api policy create  --resource-group "rg1" --service-name "apimService1" --api-id "loggerId" --policy-id "policy"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api policy update  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy" --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt api policy update  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy" --value "<policies>\r\n     <inbound>\r\n     <base />\r\n  <set-header name=\"newvalue\" exists-action=\"override\">\r\n   <value>\"@(context.Request.Headers.FirstOrDefault(h => h.Ke==\"Via\"))\" </value>\r\n    </set-header>\r\n  </inbound>\r\n      </policies>" --format "rawxml"', checks=[
        ])

        self.cmd('apimgmt api policy update  --resource-group "rg1" --service-name "apimService1" --api-id "loggerId" --policy-id "policy"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api policy delete  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy"', checks=[
        ])

        self.cmd('apimgmt api policy delete  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy"', checks=[
        ])

        self.cmd('apimgmt api policy delete  --resource-group "rg1" --service-name "apimService1" --api-id "loggerId" --policy-id "policy"', checks=[
        ])

# list_by_api -- list
        self.cmd('apimgmt api policy list  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001"', checks=[
        ])

        self.cmd('apimgmt api policy list  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001"', checks=[
        ])

        self.cmd('apimgmt api policy list  --resource-group "rg1" --service-name "apimService1" --api-id "loggerId"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api policy show  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy" --format "xml"', checks=[
        ])

        self.cmd('apimgmt api policy show  --resource-group "rg1" --service-name "apimService1" --api-id "5600b57e7e8880006a040001" --policy-id "policy" --format "rawxml"', checks=[
        ])

        self.cmd('apimgmt api policy show  --resource-group "rg1" --service-name "apimService1" --api-id "loggerId" --policy-id "policy"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api schema create  --resource-group "rg1" --service-name "apimService1" --api-id "59d6bb8f1f7fab13dc67ec9b" --schema-id "ec12520d-9d48-4e7b-8f39-698ca2ac63f1" --content-type "application/vnd.ms-azure-apim.xsd+xml"', checks=[
        ])

        self.cmd('apimgmt api schema create  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --schema-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api schema update  --resource-group "rg1" --service-name "apimService1" --api-id "59d6bb8f1f7fab13dc67ec9b" --schema-id "ec12520d-9d48-4e7b-8f39-698ca2ac63f1" --content-type "application/vnd.ms-azure-apim.xsd+xml"', checks=[
        ])

        self.cmd('apimgmt api schema update  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --schema-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api schema delete  --resource-group "rg1" --service-name "apimService1" --api-id "59d6bb8f1f7fab13dc67ec9b" --schema-id "ec12520d-9d48-4e7b-8f39-698ca2ac63f1"', checks=[
        ])

        self.cmd('apimgmt api schema delete  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --schema-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# list_by_api -- list
        self.cmd('apimgmt api schema list  --resource-group "rg1" --service-name "apimService1" --api-id "59d6bb8f1f7fab13dc67ec9b"', checks=[
        ])

        self.cmd('apimgmt api schema list  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api schema show  --resource-group "rg1" --service-name "apimService1" --api-id "59d6bb8f1f7fab13dc67ec9b" --schema-id "ec12520d-9d48-4e7b-8f39-698ca2ac63f1"', checks=[
        ])

        self.cmd('apimgmt api schema show  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --schema-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api diagnostic create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api diagnostic update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api diagnostic delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api diagnostic list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a"', checks=[
        ])

        self.cmd('apimgmt api diagnostic list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a"', checks=[
        ])

        self.cmd('apimgmt api diagnostic list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api diagnostic show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt api diagnostic show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api issue create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --created-date "2018-02-01T22:21:20.467Z" --state "open" --title "New API issue" --description "New API issue description" --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"', checks=[
        ])

        self.cmd('apimgmt api issue create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --state "closed"', checks=[
        ])

        self.cmd('apimgmt api issue create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api issue update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --created-date "2018-02-01T22:21:20.467Z" --state "open" --title "New API issue" --description "New API issue description" --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"', checks=[
        ])

        self.cmd('apimgmt api issue update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --state "closed"', checks=[
        ])

        self.cmd('apimgmt api issue update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api issue delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

        self.cmd('apimgmt api issue delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

        self.cmd('apimgmt api issue delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api issue list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a"', checks=[
        ])

        self.cmd('apimgmt api issue list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a"', checks=[
        ])

        self.cmd('apimgmt api issue list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api issue show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

        self.cmd('apimgmt api issue show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

        self.cmd('apimgmt api issue show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api issue comment create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb" --text "Issue comment." --created-date "2018-02-01T22:21:20.467Z" --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"', checks=[
        ])

        self.cmd('apimgmt api issue comment create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api issue comment update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb" --text "Issue comment." --created-date "2018-02-01T22:21:20.467Z" --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"', checks=[
        ])

        self.cmd('apimgmt api issue comment update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api issue comment delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb"', checks=[
        ])

        self.cmd('apimgmt api issue comment delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api issue comment list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

        self.cmd('apimgmt api issue comment list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api issue comment show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb"', checks=[
        ])

        self.cmd('apimgmt api issue comment show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id "599e29ab193c3c0bd0b3e2fb"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api issue attachment create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3" --title "Issue attachment." --content-format "image/jpeg" --content "IEJhc2U2NA=="', checks=[
        ])

        self.cmd('apimgmt api issue attachment create  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api issue attachment update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3" --title "Issue attachment." --content-format "image/jpeg" --content "IEJhc2U2NA=="', checks=[
        ])

        self.cmd('apimgmt api issue attachment update  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api issue attachment delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

        self.cmd('apimgmt api issue attachment delete  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api issue attachment list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

        self.cmd('apimgmt api issue attachment list  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api issue attachment show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

        self.cmd('apimgmt api issue attachment show  --resource-group "rg1" --service-name "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --attachment-id "57d2ef278aa04f0888cba3f3"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt api tagdescription create  --resource-group "rg1" --service-name "apimService1" --api-id "5931a75ae4bbd512a88c680b" --tag-id "tagId1" --description "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API" --external-docs-url "http://some.url/additionaldoc" --external-docs-description "Description of the external docs resource"', checks=[
        ])

        self.cmd('apimgmt api tagdescription create  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --tag-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt api tagdescription update  --resource-group "rg1" --service-name "apimService1" --api-id "5931a75ae4bbd512a88c680b" --tag-id "tagId1" --description "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API" --external-docs-url "http://some.url/additionaldoc" --external-docs-description "Description of the external docs resource"', checks=[
        ])

        self.cmd('apimgmt api tagdescription update  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --tag-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt api tagdescription delete  --resource-group "rg1" --service-name "apimService1" --api-id "5931a75ae4bbd512a88c680b" --tag-id "tagId1"', checks=[
        ])

        self.cmd('apimgmt api tagdescription delete  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --tag-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt api tagdescription list  --resource-group "rg1" --service-name "apimService1" --api-id "5931a75ae4bbd512a88c680b"', checks=[
        ])

        self.cmd('apimgmt api tagdescription list  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650"', checks=[
        ])

# get -- show
        self.cmd('apimgmt api tagdescription show  --resource-group "rg1" --service-name "apimService1" --api-id "5931a75ae4bbd512a88c680b" --tag-id "tagId1"', checks=[
        ])

        self.cmd('apimgmt api tagdescription show  --resource-group "rg1" --service-name "apimService1" --api-id "59d5b28d1f7fab116c282650" --tag-id "59d5b28e1f7fab116402044e"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt apiversionset create  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1" --description "Version configuration" --display-name "api set 1" --versioning-scheme "Segment"', checks=[
        ])

        self.cmd('apimgmt apiversionset create  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1" --description "Version configuration" --display-name "api set 1" --versioning-scheme "Segment"', checks=[
        ])

        self.cmd('apimgmt apiversionset create  --resource-group "rg1" --service-name "apimService1" --version-set-id "a1"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt apiversionset update  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1" --description "Version configuration" --display-name "api set 1" --versioning-scheme "Segment"', checks=[
        ])

        self.cmd('apimgmt apiversionset update  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1" --description "Version configuration" --display-name "api set 1" --versioning-scheme "Segment"', checks=[
        ])

        self.cmd('apimgmt apiversionset update  --resource-group "rg1" --service-name "apimService1" --version-set-id "a1"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt apiversionset delete  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1"', checks=[
        ])

        self.cmd('apimgmt apiversionset delete  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1"', checks=[
        ])

        self.cmd('apimgmt apiversionset delete  --resource-group "rg1" --service-name "apimService1" --version-set-id "a1"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt apiversionset list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt apiversionset list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt apiversionset list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt apiversionset show  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1"', checks=[
        ])

        self.cmd('apimgmt apiversionset show  --resource-group "rg1" --service-name "apimService1" --version-set-id "api1"', checks=[
        ])

        self.cmd('apimgmt apiversionset show  --resource-group "rg1" --service-name "apimService1" --version-set-id "a1"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt authorizationserver create  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer" --description "test server" --token-endpoint "https://www.contoso.com/oauth2/token" --support-state true --default-scope "read write" --client-secret "2" --resource-owner-username "un" --resource-owner-password "pwd" --display-name "test2" --client-registration-endpoint "https://www.contoso.com/apps" --authorization-endpoint "https://www.contoso.com/oauth2/auth" --client-id "1"', checks=[
        ])

        self.cmd('apimgmt authorizationserver create  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer" --client-secret "updated" --client-id "update"', checks=[
        ])

        self.cmd('apimgmt authorizationserver create  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer2"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt authorizationserver update  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer" --description "test server" --token-endpoint "https://www.contoso.com/oauth2/token" --support-state true --default-scope "read write" --client-secret "2" --resource-owner-username "un" --resource-owner-password "pwd" --display-name "test2" --client-registration-endpoint "https://www.contoso.com/apps" --authorization-endpoint "https://www.contoso.com/oauth2/auth" --client-id "1"', checks=[
        ])

        self.cmd('apimgmt authorizationserver update  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer" --client-secret "updated" --client-id "update"', checks=[
        ])

        self.cmd('apimgmt authorizationserver update  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer2"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt authorizationserver delete  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer"', checks=[
        ])

        self.cmd('apimgmt authorizationserver delete  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer"', checks=[
        ])

        self.cmd('apimgmt authorizationserver delete  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer2"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt authorizationserver list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt authorizationserver list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt authorizationserver list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt authorizationserver show  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer"', checks=[
        ])

        self.cmd('apimgmt authorizationserver show  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer"', checks=[
        ])

        self.cmd('apimgmt authorizationserver show  --resource-group "rg1" --service-name "apimService1" --authsid "newauthServer2"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt backend create  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend" --description "Service Fabric Test App 1" --url "fabric:/mytestapp/mytestservice" --protocol "http"', checks=[
        ])

        self.cmd('apimgmt backend create  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend" --description "description5308" --url "https://backendname2644/" --protocol "http"', checks=[
        ])

        self.cmd('apimgmt backend create  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend" --description "description5308"', checks=[
        ])

        self.cmd('apimgmt backend create  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt backend update  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend" --description "Service Fabric Test App 1" --url "fabric:/mytestapp/mytestservice" --protocol "http"', checks=[
        ])

        self.cmd('apimgmt backend update  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend" --description "description5308" --url "https://backendname2644/" --protocol "http"', checks=[
        ])

        self.cmd('apimgmt backend update  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend" --description "description5308"', checks=[
        ])

        self.cmd('apimgmt backend update  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt backend delete  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend"', checks=[
        ])

        self.cmd('apimgmt backend delete  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend"', checks=[
        ])

        self.cmd('apimgmt backend delete  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend"', checks=[
        ])

        self.cmd('apimgmt backend delete  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt backend list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt backend list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt backend list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt backend list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt backend show  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend"', checks=[
        ])

        self.cmd('apimgmt backend show  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend"', checks=[
        ])

        self.cmd('apimgmt backend show  --resource-group "rg1" --service-name "apimService1" --backend-id "proxybackend"', checks=[
        ])

        self.cmd('apimgmt backend show  --resource-group "rg1" --service-name "apimService1" --backend-id "sfbackend"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt cache create  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia" --description "Redis cache instances in West India" --connection-string "contoso5.redis.cache.windows.net,ssl=true,password=..." --resource-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}"', checks=[
        ])

        self.cmd('apimgmt cache create  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia" --description "Update Cache in west India"', checks=[
        ])

        self.cmd('apimgmt cache create  --resource-group "rg1" --service-name "apimService1" --cache-id "southindia"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt cache update  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia" --description "Redis cache instances in West India" --connection-string "contoso5.redis.cache.windows.net,ssl=true,password=..." --resource-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}"', checks=[
        ])

        self.cmd('apimgmt cache update  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia" --description "Update Cache in west India"', checks=[
        ])

        self.cmd('apimgmt cache update  --resource-group "rg1" --service-name "apimService1" --cache-id "southindia"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt cache delete  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia"', checks=[
        ])

        self.cmd('apimgmt cache delete  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia"', checks=[
        ])

        self.cmd('apimgmt cache delete  --resource-group "rg1" --service-name "apimService1" --cache-id "southindia"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt cache list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt cache list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt cache list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt cache show  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia"', checks=[
        ])

        self.cmd('apimgmt cache show  --resource-group "rg1" --service-name "apimService1" --cache-id "westindia"', checks=[
        ])

        self.cmd('apimgmt cache show  --resource-group "rg1" --service-name "apimService1" --cache-id "southindia"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt certificate create  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert" --data "****************Base 64 Encoded Certificate *******************************" --password "****Certificate Password******"', checks=[
        ])

        self.cmd('apimgmt certificate create  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt certificate update  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert" --data "****************Base 64 Encoded Certificate *******************************" --password "****Certificate Password******"', checks=[
        ])

        self.cmd('apimgmt certificate update  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt certificate delete  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert"', checks=[
        ])

        self.cmd('apimgmt certificate delete  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt certificate list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt certificate list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt certificate show  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert"', checks=[
        ])

        self.cmd('apimgmt certificate show  --resource-group "rg1" --service-name "apimService1" --certificate-id "tempcert"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1" --publisher-email "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Developer" --sku-capacity "1" --location "Central US"', checks=[
        ])

        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1" --virtual-network-type "External" --publisher-email "admin@live.com" --publisher-name "contoso" --sku-name "Premium" --sku-capacity "1" --location "Central US"', checks=[
        ])

        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1" --publisher-email "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Consumption" --location "West US"', checks=[
        ])

        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1" --publisher-email "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Basic" --sku-capacity "1" --location "Central US"', checks=[
        ])

        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1" --publisher-email "foobar@live.com" --publisher-name "Contoso Vnext"', checks=[
        ])

        self.cmd('apimgmt create  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1" --publisher-email "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Developer" --sku-capacity "1" --location "Central US"', checks=[
        ])

        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1" --virtual-network-type "External" --publisher-email "admin@live.com" --publisher-name "contoso" --sku-name "Premium" --sku-capacity "1" --location "Central US"', checks=[
        ])

        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1" --publisher-email "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Consumption" --location "West US"', checks=[
        ])

        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1" --publisher-email "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Basic" --sku-capacity "1" --location "Central US"', checks=[
        ])

        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1" --publisher-email "foobar@live.com" --publisher-name "Contoso Vnext"', checks=[
        ])

        self.cmd('apimgmt update  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt delete  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

# list -- list
        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

        self.cmd('apimgmt list  --resource-group "rg1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt diagnostic create  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/azuremonitor"', checks=[
        ])

        self.cmd('apimgmt diagnostic create  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/applicationinsights"', checks=[
        ])

        self.cmd('apimgmt diagnostic create  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt diagnostic update  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/azuremonitor"', checks=[
        ])

        self.cmd('apimgmt diagnostic update  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id "/loggers/applicationinsights"', checks=[
        ])

        self.cmd('apimgmt diagnostic update  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt diagnostic delete  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt diagnostic delete  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt diagnostic delete  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt diagnostic list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt diagnostic list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt diagnostic list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt diagnostic show  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt diagnostic show  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

        self.cmd('apimgmt diagnostic show  --resource-group "rg1" --service-name "apimService1" --diagnostic-id "applicationinsights"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt template create  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage" --subject "Your request for $IssueName was successfully received."', checks=[
        ])

        self.cmd('apimgmt template create  --resource-group "rg1" --service-name "apimService1" --name "applicationApprovedNotificationMessage" --subject "Your application $AppName is published in the gallery" --body "<!DOCTYPE html >\r\n<html>\r\n  <head />\r\n  <body>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Dear $DevFirstName $DevLastName,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">\r\n          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href=\"http://$DevPortalUrl/Applications/Details/$AppId\">here</a>.\r\n        </p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Best,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">The $OrganizationName API Team</p>\r\n  </body>\r\n</html>"', checks=[
        ])

        self.cmd('apimgmt template create  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt template update  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage" --subject "Your request for $IssueName was successfully received."', checks=[
        ])

        self.cmd('apimgmt template update  --resource-group "rg1" --service-name "apimService1" --name "applicationApprovedNotificationMessage" --subject "Your application $AppName is published in the gallery" --body "<!DOCTYPE html >\r\n<html>\r\n  <head />\r\n  <body>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Dear $DevFirstName $DevLastName,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">\r\n          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href=\"http://$DevPortalUrl/Applications/Details/$AppId\">here</a>.\r\n        </p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Best,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">The $OrganizationName API Team</p>\r\n  </body>\r\n</html>"', checks=[
        ])

        self.cmd('apimgmt template update  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt template delete  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage"', checks=[
        ])

        self.cmd('apimgmt template delete  --resource-group "rg1" --service-name "apimService1" --name "applicationApprovedNotificationMessage"', checks=[
        ])

        self.cmd('apimgmt template delete  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt template list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt template list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt template list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt template show  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage"', checks=[
        ])

        self.cmd('apimgmt template show  --resource-group "rg1" --service-name "apimService1" --name "applicationApprovedNotificationMessage"', checks=[
        ])

        self.cmd('apimgmt template show  --resource-group "rg1" --service-name "apimService1" --name "newIssueNotificationMessage"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt group create  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup" --display-name "temp group"', checks=[
        ])

        self.cmd('apimgmt group create  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup" --display-name "NewGroup (samiraad.onmicrosoft.com)" --description "new group to test" --type "external" --external-id "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"', checks=[
        ])

        self.cmd('apimgmt group create  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup" --display-name "temp group"', checks=[
        ])

        self.cmd('apimgmt group create  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt group update  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup" --display-name "temp group"', checks=[
        ])

        self.cmd('apimgmt group update  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup" --display-name "NewGroup (samiraad.onmicrosoft.com)" --description "new group to test" --type "external" --external-id "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"', checks=[
        ])

        self.cmd('apimgmt group update  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup" --display-name "temp group"', checks=[
        ])

        self.cmd('apimgmt group update  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt group delete  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt group delete  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup"', checks=[
        ])

        self.cmd('apimgmt group delete  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt group delete  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt group list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt group list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt group list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt group list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt group show  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt group show  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup"', checks=[
        ])

        self.cmd('apimgmt group show  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt group show  --resource-group "rg1" --service-name "apimService1" --group-id "aadGroup"', checks=[
        ])

# create -- create
        self.cmd('apimgmt group user create  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup" --user-id "59307d350af58404d8a26300"', checks=[
        ])

        self.cmd('apimgmt group user create  --resource-group "rg1" --service-name "apimService1" --group-id "templategroup" --user-id "59307d350af58404d8a26300"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt group user delete  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup" --user-id "59307d350af58404d8a26300"', checks=[
        ])

        self.cmd('apimgmt group user delete  --resource-group "rg1" --service-name "apimService1" --group-id "templategroup" --user-id "59307d350af58404d8a26300"', checks=[
        ])

# list -- list
        self.cmd('apimgmt group user list  --resource-group "rg1" --service-name "apimService1" --group-id "tempgroup"', checks=[
        ])

        self.cmd('apimgmt group user list  --resource-group "rg1" --service-name "apimService1" --group-id "templategroup"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt identityprovider create  --resource-group "rg1" --service-name "apimService1" --name "facebook" --client-id "facebookid" --client-secret "facebookapplicationsecret"', checks=[
        ])

        self.cmd('apimgmt identityprovider create  --resource-group "rg1" --service-name "apimService1" --name "facebook" --client-id "updatedfacebookid" --client-secret "updatedfacebooksecret"', checks=[
        ])

        self.cmd('apimgmt identityprovider create  --resource-group "rg1" --service-name "apimService1" --name "aad"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt identityprovider update  --resource-group "rg1" --service-name "apimService1" --name "facebook" --client-id "facebookid" --client-secret "facebookapplicationsecret"', checks=[
        ])

        self.cmd('apimgmt identityprovider update  --resource-group "rg1" --service-name "apimService1" --name "facebook" --client-id "updatedfacebookid" --client-secret "updatedfacebooksecret"', checks=[
        ])

        self.cmd('apimgmt identityprovider update  --resource-group "rg1" --service-name "apimService1" --name "aad"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt identityprovider delete  --resource-group "rg1" --service-name "apimService1" --name "facebook"', checks=[
        ])

        self.cmd('apimgmt identityprovider delete  --resource-group "rg1" --service-name "apimService1" --name "facebook"', checks=[
        ])

        self.cmd('apimgmt identityprovider delete  --resource-group "rg1" --service-name "apimService1" --name "aad"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt identityprovider list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt identityprovider list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt identityprovider list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt identityprovider show  --resource-group "rg1" --service-name "apimService1" --name "facebook"', checks=[
        ])

        self.cmd('apimgmt identityprovider show  --resource-group "rg1" --service-name "apimService1" --name "facebook"', checks=[
        ])

        self.cmd('apimgmt identityprovider show  --resource-group "rg1" --service-name "apimService1" --name "aad"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt logger create  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId" --logger-type "azureEventHub" --description "adding a new logger"', checks=[
        ])

        self.cmd('apimgmt logger create  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId" --logger-type "applicationInsights" --description "adding a new logger"', checks=[
        ])

        self.cmd('apimgmt logger create  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger create  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt logger update  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId" --logger-type "azureEventHub" --description "adding a new logger"', checks=[
        ])

        self.cmd('apimgmt logger update  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId" --logger-type "applicationInsights" --description "adding a new logger"', checks=[
        ])

        self.cmd('apimgmt logger update  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger update  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt logger delete  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger delete  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger delete  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger delete  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt logger list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt logger list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt logger list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt logger list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt logger show  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger show  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger show  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

        self.cmd('apimgmt logger show  --resource-group "rg1" --service-name "apimService1" --logger-id "loggerId"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt notification create  --resource-group "rg1" --service-name "apimService1" --name "RequestPublisherNotificationMessage"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt notification update  --resource-group "rg1" --service-name "apimService1" --name "RequestPublisherNotificationMessage"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt notification list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt notification show  --resource-group "rg1" --service-name "apimService1" --name "RequestPublisherNotificationMessage"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt notification recipientuser create  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id "576823d0a40f7e74ec07d642"', checks=[
        ])

        self.cmd('apimgmt notification recipientuser create  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id "576823d0a40f7e74ec07d642"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt notification recipientuser update  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id "576823d0a40f7e74ec07d642"', checks=[
        ])

        self.cmd('apimgmt notification recipientuser update  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id "576823d0a40f7e74ec07d642"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt notification recipientuser delete  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id "576823d0a40f7e74ec07d642"', checks=[
        ])

        self.cmd('apimgmt notification recipientuser delete  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id "576823d0a40f7e74ec07d642"', checks=[
        ])

# list_by_notification -- list
        self.cmd('apimgmt notification recipientuser list  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage"', checks=[
        ])

        self.cmd('apimgmt notification recipientuser list  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt notification recipientemail create  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --email "foobar@live.com"', checks=[
        ])

        self.cmd('apimgmt notification recipientemail create  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --email "contoso@live.com"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt notification recipientemail update  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --email "foobar@live.com"', checks=[
        ])

        self.cmd('apimgmt notification recipientemail update  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --email "contoso@live.com"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt notification recipientemail delete  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --email "foobar@live.com"', checks=[
        ])

        self.cmd('apimgmt notification recipientemail delete  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage" --email "contoso@live.com"', checks=[
        ])

# list_by_notification -- list
        self.cmd('apimgmt notification recipientemail list  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage"', checks=[
        ])

        self.cmd('apimgmt notification recipientemail list  --resource-group "rg1" --service-name "apimService1" --notification-name "RequestPublisherNotificationMessage"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt openidconnectprovider create  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3" --display-name "templateoidprovider3" --metadata-endpoint "https://oidprovider-template3.net" --client-id "oidprovidertemplate3"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider create  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect2" --client-secret "updatedsecret"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider create  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt openidconnectprovider update  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3" --display-name "templateoidprovider3" --metadata-endpoint "https://oidprovider-template3.net" --client-id "oidprovidertemplate3"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider update  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect2" --client-secret "updatedsecret"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider update  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt openidconnectprovider delete  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider delete  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect2"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider delete  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt openidconnectprovider list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt openidconnectprovider show  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider show  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect2"', checks=[
        ])

        self.cmd('apimgmt openidconnectprovider show  --resource-group "rg1" --service-name "apimService1" --opid "templateOpenIdConnect3"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt policy create  --resource-group "rg1" --service-name "apimService1" --policy-id "policy" --value "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt policy create  --resource-group "rg1" --service-name "apimService1" --policy-id "policy"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt policy update  --resource-group "rg1" --service-name "apimService1" --policy-id "policy" --value "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt policy update  --resource-group "rg1" --service-name "apimService1" --policy-id "policy"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt policy delete  --resource-group "rg1" --service-name "apimService1" --policy-id "policy"', checks=[
        ])

        self.cmd('apimgmt policy delete  --resource-group "rg1" --service-name "apimService1" --policy-id "policy"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt policy list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt policy list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt policy show  --resource-group "rg1" --service-name "apimService1" --policy-id "policy" --format "xml"', checks=[
        ])

        self.cmd('apimgmt policy show  --resource-group "rg1" --service-name "apimService1" --policy-id "policy"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt portalsetting signin create  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

        self.cmd('apimgmt portalsetting signin create  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt portalsetting signin update  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

        self.cmd('apimgmt portalsetting signin update  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

# get -- show
        self.cmd('apimgmt portalsetting signin show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt portalsetting signin show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt portalsetting signup create  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

        self.cmd('apimgmt portalsetting signup create  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt portalsetting signup update  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

        self.cmd('apimgmt portalsetting signup update  --resource-group "rg1" --name "apimService1" --enabled true', checks=[
        ])

# get -- show
        self.cmd('apimgmt portalsetting signup show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt portalsetting signup show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt portalsetting delegation create  --resource-group "rg1" --name "apimService1" --url "http://contoso.com/delegation" --validation-key "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q=="', checks=[
        ])

        self.cmd('apimgmt portalsetting delegation create  --resource-group "rg1" --name "apimService1" --url "http://contoso.com/delegation" --validation-key "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q=="', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt portalsetting delegation update  --resource-group "rg1" --name "apimService1" --url "http://contoso.com/delegation" --validation-key "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q=="', checks=[
        ])

        self.cmd('apimgmt portalsetting delegation update  --resource-group "rg1" --name "apimService1" --url "http://contoso.com/delegation" --validation-key "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q=="', checks=[
        ])

# get -- show
        self.cmd('apimgmt portalsetting delegation show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

        self.cmd('apimgmt portalsetting delegation show  --resource-group "rg1" --name "apimService1"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt product create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --display-name "Test Template ProductName 4"', checks=[
        ])

        self.cmd('apimgmt product create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --display-name "Test Template ProductName 4"', checks=[
        ])

        self.cmd('apimgmt product create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt product update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --display-name "Test Template ProductName 4"', checks=[
        ])

        self.cmd('apimgmt product update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --display-name "Test Template ProductName 4"', checks=[
        ])

        self.cmd('apimgmt product update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt product delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

        self.cmd('apimgmt product delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

        self.cmd('apimgmt product delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# list_by_tags -- list
        self.cmd('apimgmt product list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt product list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt product list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt product list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt product list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt product list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt product show  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

        self.cmd('apimgmt product show  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

        self.cmd('apimgmt product show  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt product api create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --api-id "echo-api"', checks=[
        ])

        self.cmd('apimgmt product api create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --api-id "echo-api"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt product api update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --api-id "echo-api"', checks=[
        ])

        self.cmd('apimgmt product api update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --api-id "echo-api"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt product api delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --api-id "echo-api"', checks=[
        ])

        self.cmd('apimgmt product api delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --api-id "echo-api"', checks=[
        ])

# list_by_product -- list
        self.cmd('apimgmt product api list  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

        self.cmd('apimgmt product api list  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt product group create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --group-id "templateGroup"', checks=[
        ])

        self.cmd('apimgmt product group create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --group-id "templateGroup"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt product group update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --group-id "templateGroup"', checks=[
        ])

        self.cmd('apimgmt product group update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --group-id "templateGroup"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt product group delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --group-id "templateGroup"', checks=[
        ])

        self.cmd('apimgmt product group delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --group-id "templateGroup"', checks=[
        ])

# list_by_product -- list
        self.cmd('apimgmt product group list  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

        self.cmd('apimgmt product group list  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt product policy create  --resource-group "rg1" --service-name "apimService1" --product-id "5702e97e5157a50f48dce801" --policy-id "policy" --value "<policies>\r\n  <inbound>\r\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\r\n    <log-to-eventhub logger-id=\"16\">\r\n                      @( string.Join(\",\", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) \r\n                  </log-to-eventhub>\r\n    <quota-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(context.Request.Method == &quot;POST&quot; ? 1:2)\" />\r\n    <base />\r\n  </inbound>\r\n  <backend>\r\n    <base />\r\n  </backend>\r\n  <outbound>\r\n    <base />\r\n  </outbound>\r\n</policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt product policy create  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --policy-id "policy"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt product policy update  --resource-group "rg1" --service-name "apimService1" --product-id "5702e97e5157a50f48dce801" --policy-id "policy" --value "<policies>\r\n  <inbound>\r\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\r\n    <log-to-eventhub logger-id=\"16\">\r\n                      @( string.Join(\",\", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) \r\n                  </log-to-eventhub>\r\n    <quota-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(context.Request.Method == &quot;POST&quot; ? 1:2)\" />\r\n    <base />\r\n  </inbound>\r\n  <backend>\r\n    <base />\r\n  </backend>\r\n  <outbound>\r\n    <base />\r\n  </outbound>\r\n</policies>" --format "xml"', checks=[
        ])

        self.cmd('apimgmt product policy update  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --policy-id "policy"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt product policy delete  --resource-group "rg1" --service-name "apimService1" --product-id "5702e97e5157a50f48dce801" --policy-id "policy"', checks=[
        ])

        self.cmd('apimgmt product policy delete  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --policy-id "policy"', checks=[
        ])

# list_by_product -- list
        self.cmd('apimgmt product policy list  --resource-group "rg1" --service-name "apimService1" --product-id "5702e97e5157a50f48dce801"', checks=[
        ])

        self.cmd('apimgmt product policy list  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct"', checks=[
        ])

# get -- show
        self.cmd('apimgmt product policy show  --resource-group "rg1" --service-name "apimService1" --product-id "5702e97e5157a50f48dce801" --policy-id "policy" --format "xml"', checks=[
        ])

        self.cmd('apimgmt product policy show  --resource-group "rg1" --service-name "apimService1" --product-id "testproduct" --policy-id "policy"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt property create  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2" --secret true --display-name "prop3name" --value "propValue"', checks=[
        ])

        self.cmd('apimgmt property create  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2" --secret true', checks=[
        ])

        self.cmd('apimgmt property create  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt property update  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2" --secret true --display-name "prop3name" --value "propValue"', checks=[
        ])

        self.cmd('apimgmt property update  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2" --secret true', checks=[
        ])

        self.cmd('apimgmt property update  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt property delete  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

        self.cmd('apimgmt property delete  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

        self.cmd('apimgmt property delete  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt property list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt property list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt property list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt property show  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

        self.cmd('apimgmt property show  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

        self.cmd('apimgmt property show  --resource-group "rg1" --service-name "apimService1" --prop-id "testprop2"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt subscription create  --resource-group "rg1" --service-name "apimService1" --sid "testsub" --owner-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}" --scope "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }}" --display-name "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription create  --resource-group "rg1" --service-name "apimService1" --sid "testsub" --display-name "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription create  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt subscription update  --resource-group "rg1" --service-name "apimService1" --sid "testsub" --owner-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}" --scope "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }}" --display-name "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription update  --resource-group "rg1" --service-name "apimService1" --sid "testsub" --display-name "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription update  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt subscription delete  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription delete  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription delete  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

# list -- list
        self.cmd('apimgmt subscription list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt subscription list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt subscription list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt subscription show  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription show  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

        self.cmd('apimgmt subscription show  --resource-group "rg1" --service-name "apimService1" --sid "testsub"', checks=[
        ])

# create_or_update -- create
        self.cmd('apimgmt user create  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b" --email "foobar@outlook.com" --first-name "foo" --last-name "bar" --confirmation "signup"', checks=[
        ])

        self.cmd('apimgmt user create  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b" --email "foobar@outlook.com" --first-name "foo" --last-name "bar"', checks=[
        ])

        self.cmd('apimgmt user create  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

# create_or_update -- update
        self.cmd('apimgmt user update  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b" --email "foobar@outlook.com" --first-name "foo" --last-name "bar" --confirmation "signup"', checks=[
        ])

        self.cmd('apimgmt user update  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b" --email "foobar@outlook.com" --first-name "foo" --last-name "bar"', checks=[
        ])

        self.cmd('apimgmt user update  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

# delete -- delete
        self.cmd('apimgmt user delete  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

        self.cmd('apimgmt user delete  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

        self.cmd('apimgmt user delete  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

# list_by_service -- list
        self.cmd('apimgmt user list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt user list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

        self.cmd('apimgmt user list  --resource-group "rg1" --service-name "apimService1"', checks=[
        ])

# get -- show
        self.cmd('apimgmt user show  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

        self.cmd('apimgmt user show  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])

        self.cmd('apimgmt user show  --resource-group "rg1" --service-name "apimService1" --user-id "5931a75ae4bbd512288c680b"', checks=[
        ])
