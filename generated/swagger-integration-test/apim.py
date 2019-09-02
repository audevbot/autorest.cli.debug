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

        # apimanagement_service_apis_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_put
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

        # apimanagement_service_apis_put_1
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

        # apimanagement_service_apis_put_2
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

        # apimanagement_service_apis_put_3
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

        # apimanagement_service_apis_put_4
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

        # apimanagement_service_apis_put_5
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

        # apimanagement_service_apis_put_6
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

        # apimanagement_service_apis_put_7
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

        # apimanagement_service_apis_put_8
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

        # apimanagement_service_apis_put_9
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

        # apimanagement_service_apis_put_10
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

        # apimanagement_service_apis_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apisbytags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apisByTags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_revisions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/revisions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_releases_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_releases_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_releases_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_releases_put
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

        # apimanagement_service_apis_releases_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_releases_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/releases/{RELEASE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_put
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

        # apimanagement_service_apis_operations_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_policies_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_policies_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_policies_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_policies_put
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

        # apimanagement_service_apis_operations_policies_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_tags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_tags_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_tags_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_tags_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_apis_operations_tags_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operations/{OPERATION_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tags_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tags_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tags_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_apis_tags_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_tags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_tags_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_tags_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_tags_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_products_tags_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tags_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tags_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tags_put
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

        # apimanagement_service_tags_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tags_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tags/{TAG_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_products_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/products?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_policies_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_policies_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_policies_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_policies_put
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

        # apimanagement_service_apis_policies_put_1
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

        # apimanagement_service_apis_policies_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_schemas_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_schemas_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_schemas_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_schemas_put
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

        # apimanagement_service_apis_schemas_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/schemas/{SCHEMA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_diagnostics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_diagnostics_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_diagnostics_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_diagnostics_put
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

        # apimanagement_service_apis_diagnostics_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_diagnostics_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_put
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

        # apimanagement_service_apis_issues_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_comments_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_comments_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_comments_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_comments_put
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

        # apimanagement_service_apis_issues_comments_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/comments/{COMMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_attachments_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_attachments_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_attachments_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_issues_attachments_put
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

        # apimanagement_service_apis_issues_attachments_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/issues/{ISSUE_NAME}/attachments/{ATTACHMENT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tagdescriptions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tagdescriptions_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tagdescriptions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_tagdescriptions_put
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

        # apimanagement_service_apis_tagdescriptions_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/tagDescriptions/{TAG_DESCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_operationsbytags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}/operationsByTags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apiversionsets_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apiversionsets_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apiversionsets_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apiversionsets_put
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

        # apimanagement_service_apiversionsets_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apiversionsets_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apiVersionSets/{API_VERSION_SET_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_authorizationservers_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_authorizationservers_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_authorizationservers_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_authorizationservers_put
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

        # apimanagement_service_authorizationservers_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_authorizationservers_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/authorizationServers/{AUTHORIZATION_SERVER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_backends_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_backends_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_backends_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_backends_put
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

        # apimanagement_service_backends_put_1
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

        # apimanagement_service_backends_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_backends_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/backends/{BACKEND_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_backends_reconnect_post
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

        # apimanagement_service_caches_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_caches_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_caches_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_caches_put
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

        # apimanagement_service_caches_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_caches_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/caches/{CACHE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_certificates_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_certificates_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_certificates_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_certificates_put
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

        # apimanagement_service_certificates_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/certificates/{CERTIFICATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.ApiManagement/operations?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_skus_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/skus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_skus_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/skus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_restore_post
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

        # apimanagement_service_backup_post
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

        # apimanagement_service_put
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

        # apimanagement_service_put_1
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

        # apimanagement_service_put_2
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

        # apimanagement_service_put_3
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

        # apimanagement_service_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_patch_1
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get_4
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ApiManagement/service?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_getssotoken_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/getssotoken?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_checknameavailability_post
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

        # apimanagement_service_applynetworkconfigurationupdates_post
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

        # apimanagement_service_diagnostics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_diagnostics_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_diagnostics_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_diagnostics_put
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

        # apimanagement_service_diagnostics_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_diagnostics_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/diagnostics/{DIAGNOSTIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_templates_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_templates_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_templates_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_templates_put
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

        # apimanagement_service_templates_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_templates_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/templates/{TEMPLATE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_put
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

        # apimanagement_service_groups_put_1
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

        # apimanagement_service_groups_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_users_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_users_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_groups_users_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users/{USER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_groups_users_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/groups/{GROUP_NAME}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_identityproviders_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_identityproviders_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_identityproviders_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_identityproviders_put
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

        # apimanagement_service_identityproviders_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_identityproviders_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/identityProviders/{IDENTITY_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_issues_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/issues?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_issues_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/issues/{ISSUE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_loggers_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_loggers_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_loggers_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_loggers_put
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

        # apimanagement_service_loggers_put_1
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

        # apimanagement_service_loggers_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_loggers_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/loggers/{LOGGER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_networkstatus_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/networkstatus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_locations_networkstatus_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/locations/{LOCATION_NAME}/networkstatus?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientusers_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientusers_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers/{RECIPIENT_USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientusers_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers/{RECIPIENT_USER_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientusers_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientUsers/{RECIPIENT_USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientemails_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientemails_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails/{RECIPIENT_EMAIL_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientemails_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails/{RECIPIENT_EMAIL_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_notifications_recipientemails_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/notifications/{NOTIFICATION_NAME}/recipientEmails/{RECIPIENT_EMAIL_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_openidconnectproviders_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_openidconnectproviders_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_openidconnectproviders_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_openidconnectproviders_put
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

        # apimanagement_service_openidconnectproviders_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_openidconnectproviders_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/openidConnectProviders/{OPENID_CONNECT_PROVIDER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_policies_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_policies_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_policies_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_policies_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_policies_put
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

        # apimanagement_service_policies_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_policysnippets_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/policySnippets?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signin_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signin_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signin_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signin_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "enabled": True'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signin?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signup_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signup_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signup_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_signup_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "enabled": True,'
                 '    "termsOfService": {'
                 '      "enabled": True,'
                 '      "text": "Terms of service text.",'
                 '      "consentRequired": True'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/signup?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_delegation_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_delegation_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_delegation_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_portalsettings_delegation_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "url": "http://contoso.com/delegation",'
                 '    "validationKey": "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==",'
                 '    "subscriptions": {'
                 '      "enabled": True'
                 '    },'
                 '    "userRegistration": {'
                 '      "enabled": True'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/portalsettings/delegation?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_products_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_put
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

        # apimanagement_service_products_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_productsbytags_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/productsByTags?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_apis_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_apis_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_apis_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis/{API_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_products_apis_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_groups_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_groups_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_groups_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_products_groups_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/groups/{GROUP_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_policies_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_policies_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_policies_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_products_policies_put
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

        # apimanagement_service_products_policies_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/products/{PRODUCT_NAME}/policies/{POLICY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_properties_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_properties_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_properties_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_properties_put
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

        # apimanagement_service_properties_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_properties_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/properties/{PROPERTY_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_quotas_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_quotas_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_quotas_periods_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}/periods/{PERIOD_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_quotas_periods_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/quotas/{QUOTA_NAME}/periods/{PERIOD_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_regions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/regions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_4
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_5
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_6
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_reports_get_7
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/reports/{REPORT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get_5
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_get_6
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_put_4
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

        # apimanagement_service_patch_2
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_delete_1
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_regenerateprimarykey_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_regeneratesecondarykey_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/subscriptions/{sub}/regenerateSecondaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_tagresources_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tagResources?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tenant_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tenant_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tenant_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tenant_regenerateprimarykey_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/regeneratePrimaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_tenant_regeneratesecondarykey_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/regenerateSecondaryKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_tenant_git_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/git?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_tenant_git_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/git/{GIT_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_tenant_git_post_1
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/git/{GIT_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_tenant_deploy_post
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

        # apimanagement_service_tenant_save_post
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

        # apimanagement_service_tenant_validate_post
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

        # apimanagement_service_tenant_syncstate_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/tenant/{TENANT_NAME}/syncState?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_head
        self.cmd('rest '
                 '--method head '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_put
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

        # apimanagement_service_users_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_generatessourl_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/generateSsoUrl?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_users_token_post
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

        # apimanagement_service_users_groups_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/groups?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/subscriptions/{sub}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_identities_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/identities?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_users_confirmations_send_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/users/{USER_NAME}/confirmations/{CONFIRMATION_NAME}/send?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # apimanagement_service_apis_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # apimanagement_service_apis_get_4
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ApiManagement/service/{name}/apis/{API_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])