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

        # ApiManagementListApis
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApi
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiContract
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiRevisionContract
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiUsingOai3Import
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "openapi-link",'
                 '    "value": "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml",'
                 '    "path": "petstore"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiUsingSwaggerImport
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "swagger-link-json",'
                 '    "value": "http://petstore.swagger.io/v2/swagger.json",'
                 '    "path": "petstore"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiUsingWadlImport
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "wadl-link-json",'
                 '    "value": "https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl",'
                 '    "path": "collector"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateSoapToRestApiUsingWsdlImport
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "wsdl-link",'
                 '    "value": "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL",'
                 '    "path": "currency",'
                 '    "wsdlSelector": {'
                 '      "wsdlServiceName": "CurrencyConvertor",'
                 '      "wsdlEndpointName": "CurrencyConvertorSoap"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "wsdl-link",'
                 '    "value": "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL",'
                 '    "path": "currency",'
                 '    "apiType": "soap",'
                 '    "wsdlSelector": {'
                 '      "wsdlServiceName": "CurrencyConvertor",'
                 '      "wsdlEndpointName": "CurrencyConvertorSoap"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApi
        body = (
                 '{'
                 '  "properties": {'
                 '    "description": "apidescription5200",'
                 '    "authenticationSettings": {'
                 '      "oAuth2": {'
                 '        "authorizationServerId": "authorizationServerId2283",'
                 '        "scope": "oauth2scope2580"'
                 '      }'
                 '    },'
                 '    "subscriptionKeyParameterNames": {'
                 '      "header": "header4520",'
                 '      "query": "query3037"'
                 '    },'
                 '    "displayName": "apiname1463",'
                 '    "serviceUrl": "http://newechoapi.cloudapp.net/api",'
                 '    "path": "newapiPath",'
                 '    "protocols": ['
                 '      "https",'
                 '      "http"'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiRevisionFromExistingApi
        body = (
                 '{'
                 '  "properties": {'
                 '    "path": "echo",'
                 '    "serviceUrl": "http://echoapi.cloudapp.net/apiv3",'
                 '    "sourceApiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",'
                 '    "apiRevisionDescription": "Creating a Revision of an existing API"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiNewVersionUsingExistingApi
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "Echo API2",'
                 '    "description": "Create Echo API into a new Version using Existing Version Set and Copy all Operations.",'
                 '    "subscriptionRequired": True,'
                 '    "serviceUrl": "http://echoapi.cloudapp.net/api",'
                 '    "path": "echo2",'
                 '    "protocols": ['
                 '      "http",'
                 '      "https"'
                 '    ],'
                 '    "isCurrent": True,'
                 '    "apiVersion": "v4",'
                 '    "sourceApiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",'
                 '    "apiVersionSetId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apiVersionSets/" + API_VERSION_SET_NAME + ""'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiClone
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "Echo API2",'
                 '    "description": "Copy of Existing Echo Api including Operations.",'
                 '    "subscriptionRequired": True,'
                 '    "serviceUrl": "http://echoapi.cloudapp.net/api",'
                 '    "path": "echo2",'
                 '    "protocols": ['
                 '      "http",'
                 '      "https"'
                 '    ],'
                 '    "isCurrent": True,'
                 '    "sourceApiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + ""'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiWithOpenIdConnect
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "Swagger Petstore",'
                 '    "description": "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.",'
                 '    "serviceUrl": "http://petstore.swagger.io/v2",'
                 '    "path": "petstore",'
                 '    "protocols": ['
                 '      "https"'
                 '    ],'
                 '    "authenticationSettings": {'
                 '      "openid": {'
                 '        "openidProviderId": "testopenid",'
                 '        "bearerTokenSendingMethods": ['
                 '          "authorizationHeader"'
                 '        ]'
                 '      }'
                 '    },'
                 '    "subscriptionKeyParameterNames": {'
                 '      "header": "Ocp-Apim-Subscription-Key",'
                 '      "query": "subscription-key"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiUsingImportOverrideServiceUrl
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "swagger-link",'
                 '    "value": "http://apimpimportviaurl.azurewebsites.net/api/apidocs/",'
                 '    "path": "petstoreapi123",'
                 '    "serviceUrl": "http://petstore.swagger.wordnik.com/api"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateApi
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteApi
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApisByTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apisByTags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiRevisions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/revisions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiReleases
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiRelease
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiRelease
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiRelease
        body = (
                 '{'
                 '  "properties": {'
                 '    "apiId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",'
                 '    "notes": "yahooagain"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateApiRelease
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteApiRelease
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiOperations
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiOperation
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiOperation
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiOperationPetStore
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiOperation
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "createUser2",'
                 '    "method": "POST",'
                 '    "urlTemplate": "/user1",'
                 '    "templateParameters": [],'
                 '    "description": "This can only be done by the logged in user.",'
                 '    "request": {'
                 '      "description": "Created user object",'
                 '      "queryParameters": [],'
                 '      "headers": [],'
                 '      "representations": ['
                 '        {'
                 '          "contentType": "application/json",'
                 '          "schemaId": "592f6c1d0af5840ca8897f0c",'
                 '          "typeName": "User"'
                 '        }'
                 '      ]'
                 '    },'
                 '    "responses": ['
                 '      {'
                 '        "statusCode": "200",'
                 '        "description": "successful operation",'
                 '        "representations": ['
                 '          {'
                 '            "contentType": "application/xml"'
                 '          },'
                 '          {'
                 '            "contentType": "application/json"'
                 '          }'
                 '        ],'
                 '        "headers": []'
                 '      }'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateApiOperation
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteApiOperation
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiOperationPolicies
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiOperationPolicy
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiOperationPolicy
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiOperationPolicy
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "xml",'
                 '    "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiOperationPolicy
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiOperationTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiOperationTag
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiOperationTag
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiOperationTag
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiOperationTag
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiTag
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiTag
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiTag
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiTag
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProductTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadProductTag
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetProductTag
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateProductTag
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteProductTag
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadTag
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetTag
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateTag
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "tag1"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateTag
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteTag
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiProducts
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/products?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiPolicies
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiPolicy
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiPolicy
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiPolicy
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "xml",'
                 '    "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateApiPolicyNonXmlEncoded
        body = (
                 '{'
                 '  "properties": {'
                 '    "value": "<policies>\r\n     <inbound>\r\n     <base />\r\n  <set-header name=\"newvalue\" exists-action=\"override\">\r\n   <value>\"@(context.Request.Headers.FirstOrDefault(h => h.Ke==\"Via\"))\" </value>\r\n    </set-header>\r\n  </inbound>\r\n      </policies>",'
                 '    "format": "rawxml"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiPolicy
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiSchemas
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiSchema
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiSchema
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiSchema
        body = (
                 '{'
                 '  "properties": {'
                 '    "contentType": "application/vnd.ms-azure-apim.xsd+xml",'
                 '    "document": {'
                 '      "value": "<s:schema elementFormDefault=\"qualified\" targetNamespace=\"http://ws.cdyne.com/WeatherWS/\" xmlns:tns=\"http://ws.cdyne.com/WeatherWS/\" xmlns:s=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://schemas.xmlsoap.org/wsdl/soap12/\" xmlns:mime=\"http://schemas.xmlsoap.org/wsdl/mime/\" xmlns:soap=\"http://schemas.xmlsoap.org/wsdl/soap/\" xmlns:tm=\"http://microsoft.com/wsdl/mime/textMatching/\" xmlns:http=\"http://schemas.xmlsoap.org/wsdl/http/\" xmlns:soapenc=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:wsdl=\"http://schemas.xmlsoap.org/wsdl/\" xmlns:apim-wsdltns=\"http://ws.cdyne.com/WeatherWS/\">\r\n  <s:element name=\"GetWeatherInformation\">\r\n    <s:complexType />\r\n  </s:element>\r\n  <s:element name=\"GetWeatherInformationResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"GetWeatherInformationResult\" type=\"tns:ArrayOfWeatherDescription\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"ArrayOfWeatherDescription\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"unbounded\" name=\"WeatherDescription\" type=\"tns:WeatherDescription\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"WeatherDescription\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Description\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"PictureURL\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"GetCityForecastByZIP\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ZIP\" type=\"s:string\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:element name=\"GetCityForecastByZIPResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"GetCityForecastByZIPResult\" type=\"tns:ForecastReturn\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"ForecastReturn\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Success\" type=\"s:boolean\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ResponseText\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"State\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"City\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WeatherStationCity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ForecastResult\" type=\"tns:ArrayOfForecast\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"ArrayOfForecast\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"unbounded\" name=\"Forecast\" nillable=\"true\" type=\"tns:Forecast\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"Forecast\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Date\" type=\"s:dateTime\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Desciption\" type=\"s:string\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Temperatures\" type=\"tns:temp\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"ProbabilityOfPrecipiation\" type=\"tns:POP\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"temp\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"MorningLow\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"DaytimeHigh\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"POP\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Nighttime\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Daytime\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"GetCityWeatherByZIP\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ZIP\" type=\"s:string\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:element name=\"GetCityWeatherByZIPResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"GetCityWeatherByZIPResult\" type=\"tns:WeatherReturn\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"WeatherReturn\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Success\" type=\"s:boolean\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ResponseText\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"State\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"City\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WeatherStationCity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Description\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Temperature\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"RelativeHumidity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Wind\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Pressure\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Visibility\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WindChill\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Remarks\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"ArrayOfWeatherDescription\" nillable=\"true\" type=\"tns:ArrayOfWeatherDescription\" />\r\n  <s:element name=\"ForecastReturn\" nillable=\"true\" type=\"tns:ForecastReturn\" />\r\n  <s:element name=\"WeatherReturn\" type=\"tns:WeatherReturn\" />\r\n</s:schema>"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiSchema
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiDiagnostics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiDiagnostic
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiDiagnostic
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiDiagnostic
        body = (
                 '{'
                 '  "properties": {'
                 '    "alwaysLog": "allErrors",'
                 '    "loggerId": "/loggers/applicationinsights",'
                 '    "sampling": {'
                 '      "samplingType": "fixed",'
                 '      "percentage": "50"'
                 '    },'
                 '    "frontend": {'
                 '      "request": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      },'
                 '      "response": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      }'
                 '    },'
                 '    "backend": {'
                 '      "request": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      },'
                 '      "response": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateApiDiagnostic
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteApiDiagnostic
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiIssues
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiIssue
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiIssue
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiIssue
        body = (
                 '{'
                 '  "properties": {'
                 '    "title": "New API issue",'
                 '    "description": "New API issue description",'
                 '    "createdDate": "2018-02-01T22:21:20.467Z",'
                 '    "state": "open",'
                 '    "userId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateApiIssue
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteApiIssue
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiIssueComments
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiIssueComment
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiIssueComment
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiIssueComment
        body = (
                 '{'
                 '  "properties": {'
                 '    "text": "Issue comment.",'
                 '    "createdDate": "2018-02-01T22:21:20.467Z",'
                 '    "userId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiIssueComment
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiIssueAttachments
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiIssueAttachment
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiIssueAttachment
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiIssueAttachment
        body = (
                 '{'
                 '  "properties": {'
                 '    "title": "Issue attachment.",'
                 '    "contentFormat": "image/jpeg",'
                 '    "content": "IEJhc2U2NA=="'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiIssueAttachment
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiTagDescriptions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiTagDescription
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiTagDescription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiTagDescription
        body = (
                 '{'
                 '  "properties": {'
                 '    "description": "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API",'
                 '    "externalDocsUrl": "http://some.url/additionaldoc",'
                 '    "externalDocsDescription": "Description of the external docs resource"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteApiTagDescription
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiOperationsByTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operationsByTags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListApiVersionSets
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadApiVersionSet
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiVersionSet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateApiVersionSet
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "api set 1",'
                 '    "versioningScheme": "Segment",'
                 '    "description": "Version configuration"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateApiVersionSet
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteApiVersionSet
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListAuthorizationServers
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadAuthorizationServer
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetAuthorizationServer
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateAuthorizationServer
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "test2",'
                 '    "description": "test server",'
                 '    "clientRegistrationEndpoint": "https://www.contoso.com/apps",'
                 '    "authorizationEndpoint": "https://www.contoso.com/oauth2/auth",'
                 '    "authorizationMethods": ['
                 '      "GET"'
                 '    ],'
                 '    "tokenEndpoint": "https://www.contoso.com/oauth2/token",'
                 '    "supportState": True,'
                 '    "defaultScope": "read write",'
                 '    "grantTypes": ['
                 '      "authorizationCode",'
                 '      "implicit"'
                 '    ],'
                 '    "bearerTokenSendingMethods": ['
                 '      "authorizationHeader"'
                 '    ],'
                 '    "clientId": "1",'
                 '    "clientSecret": "2",'
                 '    "resourceOwnerUsername": "un",'
                 '    "resourceOwnerPassword": "pwd"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateAuthorizationServer
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteAuthorizationServer
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListBackends
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadBackend
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetBackend
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateBackendServiceFabric
        body = (
                 '{'
                 '  "properties": {'
                 '    "description": "Service Fabric Test App 1",'
                 '    "protocol": "http",'
                 '    "url": "fabric:/mytestapp/mytestservice",'
                 '    "properties": {'
                 '      "serviceFabricCluster": {'
                 '        "managementEndpoints": ['
                 '          "https://somecluster.com"'
                 '        ],'
                 '        "clientCertificatethumbprint": "EBA029198AA3E76EF0D70482626E5BCF148594A6",'
                 '        "serverX509Names": ['
                 '          {'
                 '            "name": "ServerCommonName1",'
                 '            "issuerCertificateThumbprint": "IssuerCertificateThumbprint1"'
                 '          }'
                 '        ],'
                 '        "maxPartitionResolutionRetries": "5"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateBackendProxyBackend
        body = (
                 '{'
                 '  "properties": {'
                 '    "description": "description5308",'
                 '    "url": "https://backendname2644/",'
                 '    "protocol": "http",'
                 '    "tls": {'
                 '      "validateCertificateChain": True,'
                 '      "validateCertificateName": True'
                 '    },'
                 '    "proxy": {'
                 '      "url": "http://192.168.1.1:8080",'
                 '      "username": "Contoso\\admin",'
                 '      "password": "opensesame"'
                 '    },'
                 '    "credentials": {'
                 '      "query": {'
                 '        "sv": ['
                 '          "xx",'
                 '          "bb",'
                 '          "cc"'
                 '        ]'
                 '      },'
                 '      "header": {'
                 '        "x-my-1": ['
                 '          "val1",'
                 '          "val2"'
                 '        ]'
                 '      },'
                 '      "authorization": {'
                 '        "scheme": "Basic",'
                 '        "parameter": "opensesma"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateBackend
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteBackend
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementBackendReconnect
        body = (
                 '{'
                 '  "properties": {'
                 '    "after": "PT3S"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}/reconnect?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementListCaches
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadCache
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetCache
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateCache
        body = (
                 '{'
                 '  "properties": {'
                 '    "connectionString": "contoso5.redis.cache.windows.net,ssl=true,password=...",'
                 '    "description": "Redis cache instances in West India",'
                 '    "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Cache/Redis/" + REDIS_NAME + ""'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateCache
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteCache
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListCertificates
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadCertificate
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetCertificate
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateCertificate
        body = (
                 '{'
                 '  "properties": {'
                 '    "data": "****************Base 64 Encoded Certificate *******************************",'
                 '    "password": "****Certificate Password******"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteCertificate
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListOperations
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.ApiManagement/operations?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListSKUs-Dedicated
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/skus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListSKUs-Consumption
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/skus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementRestoreService
        body = (
                 '{'
                 '  "storageAccount": "teststorageaccount",'
                 '  "accessKey": "**************************************************",'
                 '  "containerName": "backupContainer",'
                 '  "backupName": "apimService1backup_2017_03_19"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/restore?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateBackup
        body = (
                 '{'
                 '  "storageAccount": "teststorageaccount",'
                 '  "accessKey": "**************************************************",'
                 '  "containerName": "backupContainer",'
                 '  "backupName": "apimService1backup_2017_03_19"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backup?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateService
        body = (
                 '{'
                 '  "properties": {'
                 '    "publisherEmail": "apim@autorestsdk.com",'
                 '    "publisherName": "autorestsdk"'
                 '  },'
                 '  "sku": {'
                 '    "name": "Developer",'
                 '    "capacity": "1"'
                 '  },'
                 '  "location": "Central US",'
                 '  "tags": {'
                 '    "tag1": "value1",'
                 '    "tag2": "value2",'
                 '    "tag3": "value3"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateMultiRegionServiceWithCustomHostname
        body = (
                 '{'
                 '  "location": "Central US",'
                 '  "sku": {'
                 '    "name": "Premium",'
                 '    "capacity": "1"'
                 '  },'
                 '  "properties": {'
                 '    "publisherEmail": "admin@live.com",'
                 '    "publisherName": "contoso",'
                 '    "additionalLocations": ['
                 '      {'
                 '        "location": "North Europe",'
                 '        "sku": {'
                 '          "name": "Premium",'
                 '          "capacity": "1"'
                 '        },'
                 '        "virtualNetworkConfiguration": {'
                 '          "subnetResourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""'
                 '        }'
                 '      }'
                 '    ],'
                 '    "hostnameConfigurations": ['
                 '      {'
                 '        "type": "Proxy",'
                 '        "hostName": "proxyhostname1.contoso.com",'
                 '        "encodedCertificate": "************Base 64 Encoded Pfx Certificate************************",'
                 '        "certificatePassword": "**************Password of the Certificate************************************************"'
                 '      },'
                 '      {'
                 '        "type": "Proxy",'
                 '        "hostName": "proxyhostname2.contoso.com",'
                 '        "encodedCertificate": "************Base 64 Encoded Pfx Certificate************************",'
                 '        "certificatePassword": "**************Password of the Certificate************************************************",'
                 '        "negotiateClientCertificate": True'
                 '      },'
                 '      {'
                 '        "type": "Portal",'
                 '        "hostName": "portalhostname1.contoso.com",'
                 '        "encodedCertificate": "************Base 64 Encoded Pfx Certificate************************",'
                 '        "certificatePassword": "**************Password of the Certificate************************************************"'
                 '      }'
                 '    ],'
                 '    "virtualNetworkConfiguration": {'
                 '      "subnetResourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""'
                 '    },'
                 '    "virtualNetworkType": "External"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateServiceHavingMsi
        body = (
                 '{'
                 '  "properties": {'
                 '    "publisherEmail": "apim@autorestsdk.com",'
                 '    "publisherName": "autorestsdk"'
                 '  },'
                 '  "sku": {'
                 '    "name": "Consumption"'
                 '  },'
                 '  "identity": {'
                 '    "type": "SystemAssigned"'
                 '  },'
                 '  "location": "West US",'
                 '  "tags": {'
                 '    "tag1": "value1",'
                 '    "tag2": "value2",'
                 '    "tag3": "value3"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateServiceWithSystemCertificates
        body = (
                 '{'
                 '  "properties": {'
                 '    "certificates": ['
                 '      {'
                 '        "encodedCertificate": "*******Base64 encoded Certificate******************",'
                 '        "certificatePassword": "Password",'
                 '        "storeName": "CertificateAuthority"'
                 '      }'
                 '    ],'
                 '    "publisherEmail": "apim@autorestsdk.com",'
                 '    "publisherName": "autorestsdk"'
                 '  },'
                 '  "sku": {'
                 '    "name": "Basic",'
                 '    "capacity": "1"'
                 '  },'
                 '  "location": "Central US",'
                 '  "tags": {'
                 '    "tag1": "value1",'
                 '    "tag2": "value2",'
                 '    "tag3": "value3"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateServiceDisableTls10
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementUpdateServicePublisherDetails
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceGetService
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceGetServiceHavingMsi
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceGetMultiRegionInternalVnet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceDeleteService
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListServiceBySubscriptionAndResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListServiceBySubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ApiManagement/service?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceGetSsoToken
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/getssotoken?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementServiceCheckNameAvailability
        body = (
                 '{'
                 '  "name": "apimService1"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ApiManagement/checkNameAvailability?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementApplyNetworkConfigurationUpdates
        body = (
                 '{'
                 '  "location": "west us"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/applynetworkconfigurationupdates?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementListDiagnostics
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadDiagnostic
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetDiagnostic
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateDiagnostic
        body = (
                 '{'
                 '  "properties": {'
                 '    "alwaysLog": "allErrors",'
                 '    "loggerId": "/loggers/azuremonitor",'
                 '    "sampling": {'
                 '      "samplingType": "fixed",'
                 '      "percentage": "50"'
                 '    },'
                 '    "frontend": {'
                 '      "request": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      },'
                 '      "response": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      }'
                 '    },'
                 '    "backend": {'
                 '      "request": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      },'
                 '      "response": {'
                 '        "headers": ['
                 '          "Content-type"'
                 '        ],'
                 '        "body": {'
                 '          "bytes": "512"'
                 '        }'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateDiagnostic
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteDiagnostic
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListEmailTemplates
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadEmailTemplate
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetEmailTemplate
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateEmailTemplate
        body = (
                 '{'
                 '  "properties": {'
                 '    "subject": "Your request for $IssueName was successfully received."'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateEmailTemplate
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteEmailTemplate
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListGroups
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadGroup
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateGroup
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "temp group"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateGroupExternal
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "NewGroup (samiraad.onmicrosoft.com)",'
                 '    "description": "new group to test",'
                 '    "type": "external",'
                 '    "externalId": "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateGroup
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteGroup
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListGroupUsers
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadGroupUser
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateGroupUser
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users/{USER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteGroupUser
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListIdentityProviders
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadIdentityProvider
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetIdentityProvider
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateIdentityProvider
        body = (
                 '{'
                 '  "properties": {'
                 '    "clientId": "facebookid",'
                 '    "clientSecret": "facebookapplicationsecret"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateIdentityProvider
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteIdentityProvider
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListIssues
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/issues?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetIssue
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListLoggers
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadLogger
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetLogger
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateEHLogger
        body = (
                 '{'
                 '  "properties": {'
                 '    "loggerType": "azureEventHub",'
                 '    "description": "adding a new logger",'
                 '    "credentials": {'
                 '      "name": "hydraeventhub",'
                 '      "connectionString": "Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********="'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementCreateAILogger
        body = (
                 '{'
                 '  "properties": {'
                 '    "loggerType": "applicationInsights",'
                 '    "description": "adding a new logger",'
                 '    "credentials": {'
                 '      "instrumentationKey": "11................a1"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateLogger
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteLogger
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceGetNetworkStatus
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/networkstatus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementServiceGetNetworkStatusByLocation
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/locations/{LOCATION_NAME}/networkstatus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListNotifications
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetNotification
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateNotification
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementListNotificationRecipientUsers
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadNotificationRecipientUser
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers/{RECIPIENT_USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateNotificationRecipientUser
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers/{RECIPIENT_USER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteNotificationRecipientUser
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers/{RECIPIENT_USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListNotificationRecipientEmails
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadNotificationRecipientEmail
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails/{RECIPIENT_EMAIL_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateNotificationRecipientEmail
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails/{RECIPIENT_EMAIL_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteNotificationRecipientEmail
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails/{RECIPIENT_EMAIL_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListOpenIdConnectProviders
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadOpenIdConnectProvider
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetOpenIdConnectProvider
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateOpenIdConnectProvider
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "templateoidprovider3",'
                 '    "metadataEndpoint": "https://oidprovider-template3.net",'
                 '    "clientId": "oidprovidertemplate3"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateOpenIdConnectProvider
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteOpenIdConnectProvider
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListPolicies
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadPolicy
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetPolicy
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetPolicyFormat
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreatePolicy
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "xml",'
                 '    "value": "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeletePolicy
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListPolicySnippets
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policySnippets?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadSignInSettings
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsGetSignIn
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsUpdateSignIn
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsUpdateSignIn
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadSignUpSettings
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsGetSignUp
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsUpdateSignUp
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsUpdateSignUp
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadDelegationSettings
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsGetDelegation
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsUpdateDelegation
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementPortalSettingsUpdateDelegation
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProducts
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadProduct
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetProduct
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateProduct
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "Test Template ProductName 4"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateProduct
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteProduct
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProductsByTags
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/productsByTags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProductApis
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadProductApi
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateProductApi
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteProductApi
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProductGroups
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadProductGroup
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateProductGroup
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteProductGroup
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProductSubscriptions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProductPolicies
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadProductPolicy
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetProductPolicy
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateProductPolicy
        body = (
                 '{'
                 '  "properties": {'
                 '    "format": "xml",'
                 '    "value": "<policies>\r\n  <inbound>\r\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\r\n    <log-to-eventhub logger-id=\"16\">\r\n                      @( string.Join(\",\", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) \r\n                  </log-to-eventhub>\r\n    <quota-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(context.Request.Method == &quot;POST&quot; ? 1:2)\" />\r\n    <base />\r\n  </inbound>\r\n  <backend>\r\n    <base />\r\n  </backend>\r\n  <outbound>\r\n    <base />\r\n  </outbound>\r\n</policies>"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementDeleteProductPolicy
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListProperties
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadProperty
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetProperty
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateProperty
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "prop3name",'
                 '    "value": "propValue",'
                 '    "tags": ['
                 '      "foo",'
                 '      "bar"'
                 '    ],'
                 '    "secret": True'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateProperty
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteProperty
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetQuotaCounterKeys
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementUpdateQuotaCounterKey
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetQuotaCounterKeysByQuotaPeriod
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}/periods/{PERIOD_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementUpdateQuotaCounterKeyByQuotaPeriod
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}/periods/{PERIOD_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListRegions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/regions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByApi
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByUser
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByOperation
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByProduct
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByGeo
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsBySubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByTime
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetReportsByRequest
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListSubscriptions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadSubscription
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetSubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateSubscription
        body = (
                 '{'
                 '  "properties": {'
                 '    "ownerId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + "",'
                 '    "scope": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/products/" + PRODUCT_NAME + "",'
                 '    "displayName": "testsub"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateSubscription
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteSubscription
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementSubscriptionRegeneratePrimaryKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementSubscriptionRegenerateSecondaryKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}/regenerateSecondaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementListTagResources
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tagResources?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadTenantAccess
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetTenantAccess
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementUpdateTenantAccess
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementTenantAccessRegenerateKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementTenantAccessRegenerateKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementGetTenantAccess
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementTenantAccessRegenerateKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementTenantAccessRegenerateKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementTenantConfigurationDeploy
        body = (
                 '{'
                 '  "properties": {'
                 '    "branch": "master"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/deploy?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementTenantConfigurationSave
        body = (
                 '{'
                 '  "properties": {'
                 '    "branch": "master"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/save?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementTenantConfigurationValidate
        body = (
                 '{'
                 '  "properties": {'
                 '    "branch": "master"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/validate?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementTenantAccessSyncState
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/syncState?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListUsers
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementHeadUser
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetUser
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementCreateUser
        body = (
                 '{'
                 '  "properties": {'
                 '    "firstName": "foo",'
                 '    "lastName": "bar",'
                 '    "email": "foobar@outlook.com",'
                 '    "confirmation": "signup"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUpdateUser
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementDeleteUser
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementUserGenerateSsoUrl
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/generateSsoUrl?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementUserToken
        body = (
                 '{'
                 '  "properties": {'
                 '    "keyType": "primary",'
                 '    "expiry": "2019-04-21T00:44:24.2845269Z"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/token?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementListUserGroups
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/groups?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListUserSubscriptions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementListUserIdentities
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/identities?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementUserConfirmationPasswordSend
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/confirmations/{CONFIRMATION_NAME}/send?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # ApiManagementGetApiExportInOpenApi2dot0
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # ApiManagementGetApiExportInOpenApi3dot0
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])