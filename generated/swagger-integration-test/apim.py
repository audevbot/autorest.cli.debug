# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.apimanagement
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtApiTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtApiTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.apimanagement.ApiManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_apim(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.api.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api.get(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api.get(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "openapi-link",
            "value": "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml",
            "path": "petstore"
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "swagger-link-json",
            "value": "http://petstore.swagger.io/v2/swagger.json",
            "path": "petstore"
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "wadl-link-json",
            "value": "https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl",
            "path": "collector"
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "wsdl-link",
            "value": "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL",
            "path": "currency",
            "wsdl_selector": {
              "wsdl_service_name": "CurrencyConvertor",
              "wsdl_endpoint_name": "CurrencyConvertorSoap"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "wsdl-link",
            "value": "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL",
            "path": "currency",
            "api_type": "soap",
            "wsdl_selector": {
              "wsdl_service_name": "CurrencyConvertor",
              "wsdl_endpoint_name": "CurrencyConvertorSoap"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "description": "apidescription5200",
            "authentication_settings": {
              "o_auth2": {
                "authorization_server_id": "authorizationServerId2283",
                "scope": "oauth2scope2580"
              }
            },
            "subscription_key_parameter_names": {
              "header": "header4520",
              "query": "query3037"
            },
            "display_name": "apiname1463",
            "service_url": "http://newechoapi.cloudapp.net/api",
            "path": "newapiPath",
            "protocols": [
              "https",
              "http"
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "path": "echo",
            "service_url": "http://echoapi.cloudapp.net/apiv3",
            "source_api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "api_revision_description": "Creating a Revision of an existing API"
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Echo API2",
            "description": "Create Echo API into a new Version using Existing Version Set and Copy all Operations.",
            "subscription_required": True,
            "service_url": "http://echoapi.cloudapp.net/api",
            "path": "echo2",
            "protocols": [
              "http",
              "https"
            ],
            "is_current": True,
            "api_version": "v4",
            "source_api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "api_version_set_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apiVersionSets/" + API_VERSION_SET_NAME + ""
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Echo API2",
            "description": "Copy of Existing Echo Api including Operations.",
            "subscription_required": True,
            "service_url": "http://echoapi.cloudapp.net/api",
            "path": "echo2",
            "protocols": [
              "http",
              "https"
            ],
            "is_current": True,
            "source_api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + ""
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Swagger Petstore",
            "description": "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.",
            "service_url": "http://petstore.swagger.io/v2",
            "path": "petstore",
            "protocols": [
              "https"
            ],
            "authentication_settings": {
              "openid": {
                "openid_provider_id": "testopenid",
                "bearer_token_sending_methods": [
                  "authorizationHeader"
                ]
              }
            },
            "subscription_key_parameter_names": {
              "header": "Ocp-Apim-Subscription-Key",
              "query": "subscription-key"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "swagger-link",
            "value": "http://apimpimportviaurl.azurewebsites.net/api/apidocs/",
            "path": "petstoreapi123",
            "service_url": "http://petstore.swagger.wordnik.com/api"
          }
        }
        azure_operation_poller = self.mgmt_client.api.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Echo API New",
            "service_url": "http://echoapi.cloudapp.net/api2",
            "path": "newecho"
          }
        }
        azure_operation_poller = self.mgmt_client.api.update(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api.delete(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api.list_by_tags(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_revision.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_release.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_release.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_release.get(resource_group.name, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "notes": "yahooagain"
          }
        }
        azure_operation_poller = self.mgmt_client.api_release.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "notes": "yahooagain"
          }
        }
        azure_operation_poller = self.mgmt_client.api_release.update(resource_group.name, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_release.delete(resource_group.name, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation.list_by_api(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation.get(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation.get(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "createUser2",
            "method": "POST",
            "url_template": "/user1",
            "template_parameters": [],
            "description": "This can only be done by the logged in user.",
            "request": {
              "description": "Created user object",
              "query_parameters": [],
              "headers": [],
              "representations": [
                {
                  "content_type": "application/json",
                  "schema_id": "592f6c1d0af5840ca8897f0c",
                  "type_name": "User"
                }
              ]
            },
            "responses": [
              {
                "status_code": "200",
                "description": "successful operation",
                "representations": [
                  {
                    "content_type": "application/xml"
                  },
                  {
                    "content_type": "application/json"
                  }
                ],
                "headers": []
              }
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.api_operation.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Retrieve resource",
            "method": "GET",
            "url_template": "/resource",
            "template_parameters": [],
            "request": {
              "query_parameters": [
                {
                  "name": "param1",
                  "description": "A sample parameter that is required and has a default value of \"sample\".",
                  "type": "string",
                  "default_value": "sample",
                  "required": True,
                  "values": [
                    "sample"
                  ]
                }
              ]
            },
            "responses": [
              {
                "status_code": "200",
                "description": "Returned in all cases.",
                "representations": [],
                "headers": []
              },
              {
                "status_code": "500",
                "description": "Server Error.",
                "representations": [],
                "headers": []
              }
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.api_operation.update(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation.delete(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation_policy.list_by_operation(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation_policy.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation_policy.get(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
          }
        }
        azure_operation_poller = self.mgmt_client.api_operation_policy.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_operation_policy.delete(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.list_by_operation(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_entity_state_by_operation(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_by_operation(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.assign_to_operation(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.detach_from_operation(resource_group.name, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.list_by_api(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_entity_state_by_api(resource_group.name, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_by_api(resource_group.name, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.assign_to_api(resource_group.name, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.detach_from_api(resource_group.name, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.list_by_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_entity_state_by_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_by_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.assign_to_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.detach_from_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get_entity_state(resource_group.name, SERVICE_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.get(resource_group.name, SERVICE_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "tag1"
          }
        }
        azure_operation_poller = self.mgmt_client.tag.create_or_update(resource_group.name, SERVICE_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "temp tag"
          }
        }
        azure_operation_poller = self.mgmt_client.tag.update(resource_group.name, SERVICE_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag.delete(resource_group.name, SERVICE_NAME, TAG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_product.list_by_apis(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_policy.list_by_api(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_policy.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_policy.get(resource_group.name, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
          }
        }
        azure_operation_poller = self.mgmt_client.api_policy.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "value": "<policies>\r\n     <inbound>\r\n     <base />\r\n  <set-header name=\"newvalue\" exists-action=\"override\">\r\n   <value>\"@(context.Request.Headers.FirstOrDefault(h => h.Ke==\"Via\"))\" </value>\r\n    </set-header>\r\n  </inbound>\r\n      </policies>",
            "format": "rawxml"
          }
        }
        azure_operation_poller = self.mgmt_client.api_policy.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_policy.delete(resource_group.name, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_schema.list_by_api(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_schema.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_schema.get(resource_group.name, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "content_type": "application/vnd.ms-azure-apim.xsd+xml",
            "document": {
              "value": "<s:schema elementFormDefault=\"qualified\" targetNamespace=\"http://ws.cdyne.com/WeatherWS/\" xmlns:tns=\"http://ws.cdyne.com/WeatherWS/\" xmlns:s=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://schemas.xmlsoap.org/wsdl/soap12/\" xmlns:mime=\"http://schemas.xmlsoap.org/wsdl/mime/\" xmlns:soap=\"http://schemas.xmlsoap.org/wsdl/soap/\" xmlns:tm=\"http://microsoft.com/wsdl/mime/textMatching/\" xmlns:http=\"http://schemas.xmlsoap.org/wsdl/http/\" xmlns:soapenc=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:wsdl=\"http://schemas.xmlsoap.org/wsdl/\" xmlns:apim-wsdltns=\"http://ws.cdyne.com/WeatherWS/\">\r\n  <s:element name=\"GetWeatherInformation\">\r\n    <s:complexType />\r\n  </s:element>\r\n  <s:element name=\"GetWeatherInformationResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"GetWeatherInformationResult\" type=\"tns:ArrayOfWeatherDescription\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"ArrayOfWeatherDescription\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"unbounded\" name=\"WeatherDescription\" type=\"tns:WeatherDescription\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"WeatherDescription\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Description\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"PictureURL\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"GetCityForecastByZIP\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ZIP\" type=\"s:string\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:element name=\"GetCityForecastByZIPResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"GetCityForecastByZIPResult\" type=\"tns:ForecastReturn\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"ForecastReturn\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Success\" type=\"s:boolean\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ResponseText\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"State\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"City\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WeatherStationCity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ForecastResult\" type=\"tns:ArrayOfForecast\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"ArrayOfForecast\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"unbounded\" name=\"Forecast\" nillable=\"true\" type=\"tns:Forecast\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"Forecast\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Date\" type=\"s:dateTime\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Desciption\" type=\"s:string\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Temperatures\" type=\"tns:temp\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"ProbabilityOfPrecipiation\" type=\"tns:POP\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"temp\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"MorningLow\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"DaytimeHigh\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"POP\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Nighttime\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Daytime\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"GetCityWeatherByZIP\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ZIP\" type=\"s:string\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:element name=\"GetCityWeatherByZIPResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"GetCityWeatherByZIPResult\" type=\"tns:WeatherReturn\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"WeatherReturn\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Success\" type=\"s:boolean\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ResponseText\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"State\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"City\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WeatherStationCity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Description\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Temperature\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"RelativeHumidity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Wind\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Pressure\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Visibility\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WindChill\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Remarks\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"ArrayOfWeatherDescription\" nillable=\"true\" type=\"tns:ArrayOfWeatherDescription\" />\r\n  <s:element name=\"ForecastReturn\" nillable=\"true\" type=\"tns:ForecastReturn\" />\r\n  <s:element name=\"WeatherReturn\" type=\"tns:WeatherReturn\" />\r\n</s:schema>"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api_schema.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_schema.delete(resource_group.name, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_diagnostic.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_diagnostic.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_diagnostic.get(resource_group.name, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "always_log": "allErrors",
            "logger_id": "/loggers/applicationinsights",
            "sampling": {
              "sampling_type": "fixed",
              "percentage": "50"
            },
            "frontend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            },
            "backend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api_diagnostic.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "always_log": "allErrors",
            "logger_id": "/loggers/applicationinsights",
            "sampling": {
              "sampling_type": "fixed",
              "percentage": "50"
            },
            "frontend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            },
            "backend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api_diagnostic.update(resource_group.name, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_diagnostic.delete(resource_group.name, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue.get(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "title": "New API issue",
            "description": "New API issue description",
            "created_date": "2018-02-01T22:21:20.467Z",
            "state": "open",
            "user_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""
          }
        }
        azure_operation_poller = self.mgmt_client.api_issue.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "state": "closed"
          }
        }
        azure_operation_poller = self.mgmt_client.api_issue.update(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue.delete(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_comment.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_comment.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_comment.get(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "text": "Issue comment.",
            "created_date": "2018-02-01T22:21:20.467Z",
            "user_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""
          }
        }
        azure_operation_poller = self.mgmt_client.api_issue_comment.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_comment.delete(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_attachment.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_attachment.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_attachment.get(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "title": "Issue attachment.",
            "content_format": "image/jpeg",
            "content": "IEJhc2U2NA=="
          }
        }
        azure_operation_poller = self.mgmt_client.api_issue_attachment.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_issue_attachment.delete(resource_group.name, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_tag_description.list_by_service(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_tag_description.get_entity_tag(resource_group.name, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_tag_description.get(resource_group.name, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "description": "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API",
            "external_docs_url": "http://some.url/additionaldoc",
            "external_docs_description": "Description of the external docs resource"
          }
        }
        azure_operation_poller = self.mgmt_client.api_tag_description.create_or_update(resource_group.name, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_tag_description.delete(resource_group.name, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.operation.list_by_tags(resource_group.name, SERVICE_NAME, API_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_version_set.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_version_set.get_entity_tag(resource_group.name, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_version_set.get(resource_group.name, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "api set 1",
            "versioning_scheme": "Segment",
            "description": "Version configuration"
          }
        }
        azure_operation_poller = self.mgmt_client.api_version_set.create_or_update(resource_group.name, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "api set 1",
            "versioning_scheme": "Segment",
            "description": "Version configuration"
          }
        }
        azure_operation_poller = self.mgmt_client.api_version_set.update(resource_group.name, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_version_set.delete(resource_group.name, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.authorization_server.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.authorization_server.get_entity_tag(resource_group.name, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.authorization_server.get(resource_group.name, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "test2",
            "description": "test server",
            "client_registration_endpoint": "https://www.contoso.com/apps",
            "authorization_endpoint": "https://www.contoso.com/oauth2/auth",
            "authorization_methods": [
              "GET"
            ],
            "token_endpoint": "https://www.contoso.com/oauth2/token",
            "support_state": True,
            "default_scope": "read write",
            "grant_types": [
              "authorizationCode",
              "implicit"
            ],
            "bearer_token_sending_methods": [
              "authorizationHeader"
            ],
            "client_id": "1",
            "client_secret": "2",
            "resource_owner_username": "un",
            "resource_owner_password": "pwd"
          }
        }
        azure_operation_poller = self.mgmt_client.authorization_server.create_or_update(resource_group.name, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "client_id": "update",
            "client_secret": "updated"
          }
        }
        azure_operation_poller = self.mgmt_client.authorization_server.update(resource_group.name, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.authorization_server.delete(resource_group.name, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.backend.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.backend.get_entity_tag(resource_group.name, SERVICE_NAME, BACKEND_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.backend.get(resource_group.name, SERVICE_NAME, BACKEND_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "description": "Service Fabric Test App 1",
            "protocol": "http",
            "url": "fabric:/mytestapp/mytestservice",
            "properties": {
              "service_fabric_cluster": {
                "management_endpoints": [
                  "https://somecluster.com"
                ],
                "client_certificatethumbprint": "EBA029198AA3E76EF0D70482626E5BCF148594A6",
                "server_x509names": [
                  {
                    "name": "ServerCommonName1",
                    "issuer_certificate_thumbprint": "IssuerCertificateThumbprint1"
                  }
                ],
                "max_partition_resolution_retries": "5"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.backend.create_or_update(resource_group.name, SERVICE_NAME, BACKEND_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "description": "description5308",
            "url": "https://backendname2644/",
            "protocol": "http",
            "tls": {
              "validate_certificate_chain": True,
              "validate_certificate_name": True
            },
            "proxy": {
              "url": "http://192.168.1.1:8080",
              "username": "Contoso\\admin",
              "password": "opensesame"
            },
            "credentials": {
              "query": {
                "sv": [
                  "xx",
                  "bb",
                  "cc"
                ]
              },
              "header": {
                "x-my-1": [
                  "val1",
                  "val2"
                ]
              },
              "authorization": {
                "scheme": "Basic",
                "parameter": "opensesma"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.backend.create_or_update(resource_group.name, SERVICE_NAME, BACKEND_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "description": "description5308",
            "tls": {
              "validate_certificate_chain": False,
              "validate_certificate_name": True
            }
          }
        }
        azure_operation_poller = self.mgmt_client.backend.update(resource_group.name, SERVICE_NAME, BACKEND_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.backend.delete(resource_group.name, SERVICE_NAME, BACKEND_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "after": "PT3S"
          }
        }
        azure_operation_poller = self.mgmt_client.backend.reconnect(resource_group.name, SERVICE_NAME, BACKEND_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.cache.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.cache.get_entity_tag(resource_group.name, SERVICE_NAME, CACHE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.cache.get(resource_group.name, SERVICE_NAME, CACHE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "connection_string": "contoso5.redis.cache.windows.net,ssl=true,password=...",
            "description": "Redis cache instances in West India",
            "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Cache/Redis/" + REDIS_NAME + ""
          }
        }
        azure_operation_poller = self.mgmt_client.cache.create_or_update(resource_group.name, SERVICE_NAME, CACHE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "description": "Update Cache in west India"
          }
        }
        azure_operation_poller = self.mgmt_client.cache.update(resource_group.name, SERVICE_NAME, CACHE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.cache.delete(resource_group.name, SERVICE_NAME, CACHE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.get_entity_tag(resource_group.name, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.get(resource_group.name, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "data": "****************Base 64 Encoded Certificate *******************************",
            "password": "****Certificate Password******"
          }
        }
        azure_operation_poller = self.mgmt_client.certificate.create_or_update(resource_group.name, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.delete(resource_group.name, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_operations.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service_skus.list_available_service_skus(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service_skus.list_available_service_skus(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "storage_account": "teststorageaccount",
          "access_key": "**************************************************",
          "container_name": "backupContainer",
          "backup_name": "apimService1backup_2017_03_19"
        }
        azure_operation_poller = self.mgmt_client.api_management_service.restore(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "storage_account": "teststorageaccount",
          "access_key": "**************************************************",
          "container_name": "backupContainer",
          "backup_name": "apimService1backup_2017_03_19"
        }
        azure_operation_poller = self.mgmt_client.api_management_service.backup(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "publisher_email": "apim@autorestsdk.com",
            "publisher_name": "autorestsdk"
          },
          "sku": {
            "name": "Developer",
            "capacity": "1"
          },
          "location": "Central US",
          "tags": {
            "tag1": "value1",
            "tag2": "value2",
            "tag3": "value3"
          }
        }
        azure_operation_poller = self.mgmt_client.api_management_service.create_or_update(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "Central US",
          "sku": {
            "name": "Premium",
            "capacity": "1"
          },
          "properties": {
            "publisher_email": "admin@live.com",
            "publisher_name": "contoso",
            "additional_locations": [
              {
                "location": "North Europe",
                "sku": {
                  "name": "Premium",
                  "capacity": "1"
                },
                "virtual_network_configuration": {
                  "subnet_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                }
              }
            ],
            "hostname_configurations": [
              {
                "type": "Proxy",
                "host_name": "proxyhostname1.contoso.com",
                "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
                "certificate_password": "**************Password of the Certificate************************************************"
              },
              {
                "type": "Proxy",
                "host_name": "proxyhostname2.contoso.com",
                "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
                "certificate_password": "**************Password of the Certificate************************************************",
                "negotiate_client_certificate": True
              },
              {
                "type": "Portal",
                "host_name": "portalhostname1.contoso.com",
                "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
                "certificate_password": "**************Password of the Certificate************************************************"
              }
            ],
            "virtual_network_configuration": {
              "subnet_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
            },
            "virtual_network_type": "External"
          }
        }
        azure_operation_poller = self.mgmt_client.api_management_service.create_or_update(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "publisher_email": "apim@autorestsdk.com",
            "publisher_name": "autorestsdk"
          },
          "sku": {
            "name": "Consumption"
          },
          "identity": {
            "type": "SystemAssigned"
          },
          "location": "West US",
          "tags": {
            "tag1": "value1",
            "tag2": "value2",
            "tag3": "value3"
          }
        }
        azure_operation_poller = self.mgmt_client.api_management_service.create_or_update(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "certificates": [
              {
                "encoded_certificate": "*******Base64 encoded Certificate******************",
                "certificate_password": "Password",
                "store_name": "CertificateAuthority"
              }
            ],
            "publisher_email": "apim@autorestsdk.com",
            "publisher_name": "autorestsdk"
          },
          "sku": {
            "name": "Basic",
            "capacity": "1"
          },
          "location": "Central US",
          "tags": {
            "tag1": "value1",
            "tag2": "value2",
            "tag3": "value3"
          }
        }
        azure_operation_poller = self.mgmt_client.api_management_service.create_or_update(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "custom_properties": {
              "microsoft.windows_azure.api_management.gateway.security.protocols.tls10": "false"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.api_management_service.update(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "publisher_email": "foobar@live.com",
            "publisher_name": "Contoso Vnext"
          }
        }
        azure_operation_poller = self.mgmt_client.api_management_service.update(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.get(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.get(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.get(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.delete(resource_group.name, SERVICE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_management_service.get_sso_token(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "apimService1"
        }
        azure_operation_poller = self.mgmt_client.api_management_service.check_name_availability(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "west us"
        }
        azure_operation_poller = self.mgmt_client.api_management_service.apply_network_configuration_updates(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.diagnostic.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.diagnostic.get_entity_tag(resource_group.name, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.diagnostic.get(resource_group.name, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "always_log": "allErrors",
            "logger_id": "/loggers/azuremonitor",
            "sampling": {
              "sampling_type": "fixed",
              "percentage": "50"
            },
            "frontend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            },
            "backend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.diagnostic.create_or_update(resource_group.name, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "always_log": "allErrors",
            "logger_id": "/loggers/applicationinsights",
            "sampling": {
              "sampling_type": "fixed",
              "percentage": "50"
            },
            "frontend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            },
            "backend": {
              "request": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              },
              "response": {
                "headers": [
                  "Content-type"
                ],
                "body": {
                  "bytes": "512"
                }
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.diagnostic.update(resource_group.name, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.diagnostic.delete(resource_group.name, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.email_template.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.email_template.get_entity_tag(resource_group.name, SERVICE_NAME, TEMPLATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.email_template.get(resource_group.name, SERVICE_NAME, TEMPLATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "subject": "Your request for $IssueName was successfully received."
          }
        }
        azure_operation_poller = self.mgmt_client.email_template.create_or_update(resource_group.name, SERVICE_NAME, TEMPLATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "subject": "Your application $AppName is published in the gallery",
            "body": "<!DOCTYPE html >\r\n<html>\r\n  <head />\r\n  <body>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Dear $DevFirstName $DevLastName,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">\r\n          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href=\"http://$DevPortalUrl/Applications/Details/$AppId\">here</a>.\r\n        </p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Best,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">The $OrganizationName API Team</p>\r\n  </body>\r\n</html>"
          }
        }
        azure_operation_poller = self.mgmt_client.email_template.update(resource_group.name, SERVICE_NAME, TEMPLATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.email_template.delete(resource_group.name, SERVICE_NAME, TEMPLATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group.get_entity_tag(resource_group.name, SERVICE_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group.get(resource_group.name, SERVICE_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "temp group"
          }
        }
        azure_operation_poller = self.mgmt_client.group.create_or_update(resource_group.name, SERVICE_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "NewGroup (samiraad.onmicrosoft.com)",
            "description": "new group to test",
            "type": "external",
            "external_id": "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"
          }
        }
        azure_operation_poller = self.mgmt_client.group.create_or_update(resource_group.name, SERVICE_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "temp group"
          }
        }
        azure_operation_poller = self.mgmt_client.group.update(resource_group.name, SERVICE_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group.delete(resource_group.name, SERVICE_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group_user.list(resource_group.name, SERVICE_NAME, GROUP_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group_user.check_entity_exists(resource_group.name, SERVICE_NAME, GROUP_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group_user.create(resource_group.name, SERVICE_NAME, GROUP_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.group_user.delete(resource_group.name, SERVICE_NAME, GROUP_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.identity_provider.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.identity_provider.get_entity_tag(resource_group.name, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.identity_provider.get(resource_group.name, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "client_id": "facebookid",
            "client_secret": "facebookapplicationsecret"
          }
        }
        azure_operation_poller = self.mgmt_client.identity_provider.create_or_update(resource_group.name, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "client_id": "updatedfacebookid",
            "client_secret": "updatedfacebooksecret"
          }
        }
        azure_operation_poller = self.mgmt_client.identity_provider.update(resource_group.name, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.identity_provider.delete(resource_group.name, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.issue.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.issue.get(resource_group.name, SERVICE_NAME, ISSUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.logger.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.logger.get_entity_tag(resource_group.name, SERVICE_NAME, LOGGER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.logger.get(resource_group.name, SERVICE_NAME, LOGGER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "logger_type": "azureEventHub",
            "description": "adding a new logger",
            "credentials": {
              "name": "hydraeventhub",
              "connection_string": "Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********="
            }
          }
        }
        azure_operation_poller = self.mgmt_client.logger.create_or_update(resource_group.name, SERVICE_NAME, LOGGER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "logger_type": "applicationInsights",
            "description": "adding a new logger",
            "credentials": {
              "instrumentation_key": "11................a1"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.logger.create_or_update(resource_group.name, SERVICE_NAME, LOGGER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "credentials": {
              "name": "hydraeventhub",
              "connection_string": "Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********="
            }
          }
        }
        azure_operation_poller = self.mgmt_client.logger.update(resource_group.name, SERVICE_NAME, LOGGER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.logger.delete(resource_group.name, SERVICE_NAME, LOGGER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.network_status.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.network_status.list_by_location(resource_group.name, SERVICE_NAME, LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification.get(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification.create_or_update(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_user.list_by_notification(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_user.check_entity_exists(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_user.create_or_update(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_user.delete(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_email.list_by_notification(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_email.check_entity_exists(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_EMAIL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_email.create_or_update(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_EMAIL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.notification_recipient_email.delete(resource_group.name, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_EMAIL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_id_connect_provider.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_id_connect_provider.get_entity_tag(resource_group.name, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_id_connect_provider.get(resource_group.name, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "templateoidprovider3",
            "metadata_endpoint": "https://oidprovider-template3.net",
            "client_id": "oidprovidertemplate3"
          }
        }
        azure_operation_poller = self.mgmt_client.open_id_connect_provider.create_or_update(resource_group.name, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "client_secret": "updatedsecret"
          }
        }
        azure_operation_poller = self.mgmt_client.open_id_connect_provider.update(resource_group.name, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.open_id_connect_provider.delete(resource_group.name, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.policy.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.policy.get_entity_tag(resource_group.name, SERVICE_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.policy.get(resource_group.name, SERVICE_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.policy.get(resource_group.name, SERVICE_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
          }
        }
        azure_operation_poller = self.mgmt_client.policy.create_or_update(resource_group.name, SERVICE_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.policy.delete(resource_group.name, SERVICE_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.policy_snippet.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.sign_in_settings.get_entity_tag(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.sign_in_settings.get(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enabled": True
          }
        }
        azure_operation_poller = self.mgmt_client.sign_in_settings.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enabled": True
          }
        }
        azure_operation_poller = self.mgmt_client.sign_in_settings.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.sign_up_settings.get_entity_tag(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.sign_up_settings.get(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enabled": True,
            "terms_of_service": {
              "enabled": True,
              "text": "Terms of service text.",
              "consent_required": True
            }
          }
        }
        azure_operation_poller = self.mgmt_client.sign_up_settings.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enabled": True,
            "terms_of_service": {
              "enabled": True,
              "text": "Terms of service text.",
              "consent_required": True
            }
          }
        }
        azure_operation_poller = self.mgmt_client.sign_up_settings.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.delegation_settings.get_entity_tag(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.delegation_settings.get(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "url": "http://contoso.com/delegation",
            "validation_key": "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==",
            "subscriptions": {
              "enabled": True
            },
            "user_registration": {
              "enabled": True
            }
          }
        }
        azure_operation_poller = self.mgmt_client.delegation_settings.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "url": "http://contoso.com/delegation",
            "validation_key": "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==",
            "subscriptions": {
              "enabled": True
            },
            "user_registration": {
              "enabled": True
            }
          }
        }
        azure_operation_poller = self.mgmt_client.delegation_settings.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product.get_entity_tag(resource_group.name, SERVICE_NAME, PRODUCT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product.get(resource_group.name, SERVICE_NAME, PRODUCT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Test Template ProductName 4"
          }
        }
        azure_operation_poller = self.mgmt_client.product.create_or_update(resource_group.name, SERVICE_NAME, PRODUCT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "Test Template ProductName 4"
          }
        }
        azure_operation_poller = self.mgmt_client.product.update(resource_group.name, SERVICE_NAME, PRODUCT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product.delete(resource_group.name, SERVICE_NAME, PRODUCT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product.list_by_tags(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_api.list_by_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_api.check_entity_exists(resource_group.name, SERVICE_NAME, PRODUCT_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_api.create_or_update(resource_group.name, SERVICE_NAME, PRODUCT_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_api.delete(resource_group.name, SERVICE_NAME, PRODUCT_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_group.list_by_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_group.check_entity_exists(resource_group.name, SERVICE_NAME, PRODUCT_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_group.create_or_update(resource_group.name, SERVICE_NAME, PRODUCT_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_group.delete(resource_group.name, SERVICE_NAME, PRODUCT_NAME, GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_subscriptions.list(resource_group.name, SERVICE_NAME, PRODUCT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_policy.list_by_product(resource_group.name, SERVICE_NAME, PRODUCT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_policy.get_entity_tag(resource_group.name, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_policy.get(resource_group.name, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies>\r\n  <inbound>\r\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\r\n    <log-to-eventhub logger-id=\"16\">\r\n                      @( string.Join(\",\", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) \r\n                  </log-to-eventhub>\r\n    <quota-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(context.Request.Method == &quot;POST&quot; ? 1:2)\" />\r\n    <base />\r\n  </inbound>\r\n  <backend>\r\n    <base />\r\n  </backend>\r\n  <outbound>\r\n    <base />\r\n  </outbound>\r\n</policies>"
          }
        }
        azure_operation_poller = self.mgmt_client.product_policy.create_or_update(resource_group.name, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.product_policy.delete(resource_group.name, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.property.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.property.get_entity_tag(resource_group.name, SERVICE_NAME, PROPERTY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.property.get(resource_group.name, SERVICE_NAME, PROPERTY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "prop3name",
            "value": "propValue",
            "tags": [
              "foo",
              "bar"
            ],
            "secret": True
          }
        }
        azure_operation_poller = self.mgmt_client.property.create_or_update(resource_group.name, SERVICE_NAME, PROPERTY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "tags": [
              "foo",
              "bar2"
            ],
            "secret": True
          }
        }
        azure_operation_poller = self.mgmt_client.property.update(resource_group.name, SERVICE_NAME, PROPERTY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.property.delete(resource_group.name, SERVICE_NAME, PROPERTY_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.quota_by_counter_keys.list_by_service(resource_group.name, SERVICE_NAME, QUOTA_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "calls_count": "0",
          "kb_transferred": "2.5630078125"
        }
        azure_operation_poller = self.mgmt_client.quota_by_counter_keys.update(resource_group.name, SERVICE_NAME, QUOTA_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.quota_by_period_keys.get(resource_group.name, SERVICE_NAME, QUOTA_NAME, PERIOD_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "calls_count": "0",
          "kb_transferred": "0"
        }
        azure_operation_poller = self.mgmt_client.quota_by_period_keys.update(resource_group.name, SERVICE_NAME, QUOTA_NAME, PERIOD_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.region.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_api(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_user(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_operation(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_product(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_geo(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_subscription(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_time(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.reports.list_by_request(resource_group.name, SERVICE_NAME, REPORT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription.list(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription.get_entity_tag(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription.get(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "owner_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + "",
            "scope": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/products/" + PRODUCT_NAME + "",
            "display_name": "testsub"
          }
        }
        azure_operation_poller = self.mgmt_client.subscription.create_or_update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "testsub"
          }
        }
        azure_operation_poller = self.mgmt_client.subscription.update(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription.delete(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription.regenerate_primary_key(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscription.regenerate_secondary_key(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tag_resource.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.get_entity_tag(resource_group.name, SERVICE_NAME, TENANT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.get(resource_group.name, SERVICE_NAME, TENANT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "enabled": True
        }
        azure_operation_poller = self.mgmt_client.tenant_access.update(resource_group.name, SERVICE_NAME, TENANT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.regenerate_primary_key(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.regenerate_primary_key(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.get(resource_group.name, SERVICE_NAME, TENANT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.regenerate_primary_key(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_access.regenerate_primary_key(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "branch": "master"
          }
        }
        azure_operation_poller = self.mgmt_client.tenant_configuration.deploy(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "branch": "master"
          }
        }
        azure_operation_poller = self.mgmt_client.tenant_configuration.save(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "branch": "master"
          }
        }
        azure_operation_poller = self.mgmt_client.tenant_configuration.validate(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.tenant_configuration.get_sync_state(resource_group.name, SERVICE_NAME, TENANT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user.list_by_service(resource_group.name, SERVICE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user.get_entity_tag(resource_group.name, SERVICE_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user.get(resource_group.name, SERVICE_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "first_name": "foo",
            "last_name": "bar",
            "email": "foobar@outlook.com",
            "confirmation": "signup"
          }
        }
        azure_operation_poller = self.mgmt_client.user.create_or_update(resource_group.name, SERVICE_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "first_name": "foo",
            "last_name": "bar",
            "email": "foobar@outlook.com"
          }
        }
        azure_operation_poller = self.mgmt_client.user.update(resource_group.name, SERVICE_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user.delete(resource_group.name, SERVICE_NAME, USER_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user.generate_sso_url(resource_group.name, SERVICE_NAME, USER_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "key_type": "primary",
            "expiry": "2019-04-21T00:44:24.2845269Z"
          }
        }
        azure_operation_poller = self.mgmt_client.user.get_shared_access_token(resource_group.name, SERVICE_NAME, USER_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user_group.list(resource_group.name, SERVICE_NAME, USER_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user_subscription.list(resource_group.name, SERVICE_NAME, USER_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user_identities.list(resource_group.name, SERVICE_NAME, USER_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.user_confirmation_password.send(resource_group.name, SERVICE_NAME, USER_NAME, CONFIRMATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_export.get(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.api_export.get(resource_group.name, SERVICE_NAME, API_NAME, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()