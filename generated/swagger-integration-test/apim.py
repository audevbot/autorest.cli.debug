# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

        BODY = {}
        output = mgmt_client.api.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.api.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.api.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {
          "properties": {
            "format": "openapi-link",
            "value": "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml",
            "path": "petstore"
          }
        }
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {
          "properties": {
            "format": "swagger-link-json",
            "value": "http://petstore.swagger.io/v2/swagger.json",
            "path": "petstore"
          }
        }
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {
          "properties": {
            "format": "wadl-link-json",
            "value": "https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl",
            "path": "collector"
          }
        }
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
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
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
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
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
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
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {
          "properties": {
            "path": "echo",
            "service_url": "http://echoapi.cloudapp.net/apiv3",
            "source_api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "api_revision_description": "Creating a Revision of an existing API"
          }
        }
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
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
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
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
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
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
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {
          "properties": {
            "format": "swagger-link",
            "value": "http://apimpimportviaurl.azurewebsites.net/api/apidocs/",
            "path": "petstoreapi123",
            "service_url": "http://petstore.swagger.wordnik.com/api"
          }
        }
        output = mgmt_client.api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "Echo API New",
            "service_url": "http://echoapi.cloudapp.net/api2",
            "path": "newecho"
          }
        }
        output = mgmt_client.api.update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.api.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.api.list_by_tags(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_revision.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_release.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_release.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_release.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        BODY = {
          "properties": {
            "api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "notes": "yahooagain"
          }
        }
        output = mgmt_client.api_release.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        BODY = {
          "properties": {
            "api_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/apis/" + API_NAME + "",
            "notes": "yahooagain"
          }
        }
        output = mgmt_client.api_release.update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_release.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, RELEASE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation.list_by_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_operation.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
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
        output = mgmt_client.api_operation.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
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
        output = mgmt_client.api_operation.update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation_policy.list_by_operation(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_operation_policy.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation_policy.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
          }
        }
        output = mgmt_client.api_operation_policy.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_operation_policy.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.list_by_operation(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tag.get_entity_state_by_operation(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.get_by_operation(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.assign_to_operation(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.detach_from_operation(RESOURCE_GROUP, SERVICE_NAME, API_NAME, OPERATION_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.list_by_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tag.get_entity_state_by_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.get_by_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.assign_to_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.detach_from_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.list_by_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tag.get_entity_state_by_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.get_by_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.assign_to_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.detach_from_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tag.get_entity_state(RESOURCE_GROUP, SERVICE_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.get(RESOURCE_GROUP, SERVICE_NAME, TAG_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "tag1"
          }
        }
        output = mgmt_client.tag.create_or_update(RESOURCE_GROUP, SERVICE_NAME, TAG_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "temp tag"
          }
        }
        output = mgmt_client.tag.update(RESOURCE_GROUP, SERVICE_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.tag.delete(RESOURCE_GROUP, SERVICE_NAME, TAG_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_product.list_by_apis(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_policy.list_by_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_policy.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_policy.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
          }
        }
        output = mgmt_client.api_policy.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        BODY = {
          "properties": {
            "value": "<policies>\r\n     <inbound>\r\n     <base />\r\n  <set-header name=\"newvalue\" exists-action=\"override\">\r\n   <value>\"@(context.Request.Headers.FirstOrDefault(h => h.Ke==\"Via\"))\" </value>\r\n    </set-header>\r\n  </inbound>\r\n      </policies>",
            "format": "rawxml"
          }
        }
        output = mgmt_client.api_policy.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_policy.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_schema.list_by_api(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_schema.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_schema.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        BODY = {
          "properties": {
            "content_type": "application/vnd.ms-azure-apim.xsd+xml",
            "document": {
              "value": "<s:schema elementFormDefault=\"qualified\" targetNamespace=\"http://ws.cdyne.com/WeatherWS/\" xmlns:tns=\"http://ws.cdyne.com/WeatherWS/\" xmlns:s=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://schemas.xmlsoap.org/wsdl/soap12/\" xmlns:mime=\"http://schemas.xmlsoap.org/wsdl/mime/\" xmlns:soap=\"http://schemas.xmlsoap.org/wsdl/soap/\" xmlns:tm=\"http://microsoft.com/wsdl/mime/textMatching/\" xmlns:http=\"http://schemas.xmlsoap.org/wsdl/http/\" xmlns:soapenc=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:wsdl=\"http://schemas.xmlsoap.org/wsdl/\" xmlns:apim-wsdltns=\"http://ws.cdyne.com/WeatherWS/\">\r\n  <s:element name=\"GetWeatherInformation\">\r\n    <s:complexType />\r\n  </s:element>\r\n  <s:element name=\"GetWeatherInformationResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"GetWeatherInformationResult\" type=\"tns:ArrayOfWeatherDescription\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"ArrayOfWeatherDescription\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"unbounded\" name=\"WeatherDescription\" type=\"tns:WeatherDescription\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"WeatherDescription\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Description\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"PictureURL\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"GetCityForecastByZIP\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ZIP\" type=\"s:string\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:element name=\"GetCityForecastByZIPResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"GetCityForecastByZIPResult\" type=\"tns:ForecastReturn\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"ForecastReturn\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Success\" type=\"s:boolean\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ResponseText\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"State\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"City\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WeatherStationCity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ForecastResult\" type=\"tns:ArrayOfForecast\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"ArrayOfForecast\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"unbounded\" name=\"Forecast\" nillable=\"true\" type=\"tns:Forecast\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"Forecast\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Date\" type=\"s:dateTime\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Desciption\" type=\"s:string\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Temperatures\" type=\"tns:temp\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"ProbabilityOfPrecipiation\" type=\"tns:POP\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"temp\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"MorningLow\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"DaytimeHigh\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:complexType name=\"POP\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Nighttime\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Daytime\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"GetCityWeatherByZIP\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ZIP\" type=\"s:string\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:element name=\"GetCityWeatherByZIPResponse\">\r\n    <s:complexType>\r\n      <s:sequence>\r\n        <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"GetCityWeatherByZIPResult\" type=\"tns:WeatherReturn\" />\r\n      </s:sequence>\r\n    </s:complexType>\r\n  </s:element>\r\n  <s:complexType name=\"WeatherReturn\">\r\n    <s:sequence>\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"Success\" type=\"s:boolean\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"ResponseText\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"State\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"City\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WeatherStationCity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"1\" maxOccurs=\"1\" name=\"WeatherID\" type=\"s:short\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Description\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Temperature\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"RelativeHumidity\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Wind\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Pressure\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Visibility\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"WindChill\" type=\"s:string\" />\r\n      <s:element minOccurs=\"0\" maxOccurs=\"1\" name=\"Remarks\" type=\"s:string\" />\r\n    </s:sequence>\r\n  </s:complexType>\r\n  <s:element name=\"ArrayOfWeatherDescription\" nillable=\"true\" type=\"tns:ArrayOfWeatherDescription\" />\r\n  <s:element name=\"ForecastReturn\" nillable=\"true\" type=\"tns:ForecastReturn\" />\r\n  <s:element name=\"WeatherReturn\" type=\"tns:WeatherReturn\" />\r\n</s:schema>"
            }
          }
        }
        output = mgmt_client.api_schema.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_schema.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, SCHEMA_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_diagnostic.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_diagnostic.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_diagnostic.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
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
        output = mgmt_client.api_diagnostic.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
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
        output = mgmt_client.api_diagnostic.update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_diagnostic.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, DIAGNOSTIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_issue.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        BODY = {
          "properties": {
            "title": "New API issue",
            "description": "New API issue description",
            "created_date": "2018-02-01T22:21:20.467Z",
            "state": "open",
            "user_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""
          }
        }
        output = mgmt_client.api_issue.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        BODY = {
          "properties": {
            "state": "closed"
          }
        }
        output = mgmt_client.api_issue.update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue_comment.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_issue_comment.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue_comment.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        BODY = {
          "properties": {
            "text": "Issue comment.",
            "created_date": "2018-02-01T22:21:20.467Z",
            "user_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + ""
          }
        }
        output = mgmt_client.api_issue_comment.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue_comment.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, COMMENT_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue_attachment.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_issue_attachment.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue_attachment.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        BODY = {
          "properties": {
            "title": "Issue attachment.",
            "content_format": "image/jpeg",
            "content": "IEJhc2U2NA=="
          }
        }
        output = mgmt_client.api_issue_attachment.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_issue_attachment.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, ISSUE_NAME, ATTACHMENT_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_tag_description.list_by_service(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_tag_description.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_tag_description.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "description": "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API",
            "external_docs_url": "http://some.url/additionaldoc",
            "external_docs_description": "Description of the external docs resource"
          }
        }
        output = mgmt_client.api_tag_description.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_tag_description.delete(RESOURCE_GROUP, SERVICE_NAME, API_NAME, TAG_DESCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.operation.list_by_tags(RESOURCE_GROUP, SERVICE_NAME, API_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_version_set.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_version_set.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_version_set.get(RESOURCE_GROUP, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "api set 1",
            "versioning_scheme": "Segment",
            "description": "Version configuration"
          }
        }
        output = mgmt_client.api_version_set.create_or_update(RESOURCE_GROUP, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "api set 1",
            "versioning_scheme": "Segment",
            "description": "Version configuration"
          }
        }
        output = mgmt_client.api_version_set.update(RESOURCE_GROUP, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_version_set.delete(RESOURCE_GROUP, SERVICE_NAME, API_VERSION_SET_NAME, BODY)
        BODY = {}
        output = mgmt_client.authorization_server.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.authorization_server.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        BODY = {}
        output = mgmt_client.authorization_server.get(RESOURCE_GROUP, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
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
        output = mgmt_client.authorization_server.create_or_update(RESOURCE_GROUP, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        BODY = {
          "properties": {
            "client_id": "update",
            "client_secret": "updated"
          }
        }
        output = mgmt_client.authorization_server.update(RESOURCE_GROUP, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        BODY = {}
        output = mgmt_client.authorization_server.delete(RESOURCE_GROUP, SERVICE_NAME, AUTHORIZATION_SERVER_NAME, BODY)
        BODY = {}
        output = mgmt_client.backend.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.backend.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
        BODY = {}
        output = mgmt_client.backend.get(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
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
        output = mgmt_client.backend.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
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
        output = mgmt_client.backend.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
        BODY = {
          "properties": {
            "description": "description5308",
            "tls": {
              "validate_certificate_chain": False,
              "validate_certificate_name": True
            }
          }
        }
        output = mgmt_client.backend.update(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
        BODY = {}
        output = mgmt_client.backend.delete(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, BODY)
        BODY = {
          "properties": {
            "after": "PT3S"
          }
        }
        output = mgmt_client.backend.reconnect(RESOURCE_GROUP, SERVICE_NAME, BACKEND_NAME, , BODY)
        BODY = {}
        output = mgmt_client.cache.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.cache.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, CACHE_NAME, BODY)
        BODY = {}
        output = mgmt_client.cache.get(RESOURCE_GROUP, SERVICE_NAME, CACHE_NAME, BODY)
        BODY = {
          "properties": {
            "connection_string": "contoso5.redis.cache.windows.net,ssl=true,password=...",
            "description": "Redis cache instances in West India",
            "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Cache/Redis/" + REDIS_NAME + ""
          }
        }
        output = mgmt_client.cache.create_or_update(RESOURCE_GROUP, SERVICE_NAME, CACHE_NAME, BODY)
        BODY = {
          "properties": {
            "description": "Update Cache in west India"
          }
        }
        output = mgmt_client.cache.update(RESOURCE_GROUP, SERVICE_NAME, CACHE_NAME, BODY)
        BODY = {}
        output = mgmt_client.cache.delete(RESOURCE_GROUP, SERVICE_NAME, CACHE_NAME, BODY)
        BODY = {}
        output = mgmt_client.certificate.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.certificate.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.certificate.get(RESOURCE_GROUP, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        BODY = {
          "properties": {
            "data": "****************Base 64 Encoded Certificate *******************************",
            "password": "****Certificate Password******"
          }
        }
        output = mgmt_client.certificate.create_or_update(RESOURCE_GROUP, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.certificate.delete(RESOURCE_GROUP, SERVICE_NAME, CERTIFICATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_management_operations.list(, BODY)
        BODY = {}
        output = mgmt_client.api_management_service_skus.list_available_service_skus(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_management_service_skus.list_available_service_skus(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "storage_account": "teststorageaccount",
          "access_key": "**************************************************",
          "container_name": "backupContainer",
          "backup_name": "apimService1backup_2017_03_19"
        }
        output = mgmt_client.api_management_service.restore(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "storage_account": "teststorageaccount",
          "access_key": "**************************************************",
          "container_name": "backupContainer",
          "backup_name": "apimService1backup_2017_03_19"
        }
        output = mgmt_client.api_management_service.backup(RESOURCE_GROUP, SERVICE_NAME, , BODY)
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
        output = mgmt_client.api_management_service.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
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
        output = mgmt_client.api_management_service.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
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
        output = mgmt_client.api_management_service.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
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
        output = mgmt_client.api_management_service.create_or_update(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {
          "properties": {
            "custom_properties": {
              "microsoft.windows_azure.api_management.gateway.security.protocols.tls10": "false"
            }
          }
        }
        output = mgmt_client.api_management_service.update(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {
          "properties": {
            "publisher_email": "foobar@live.com",
            "publisher_name": "Contoso Vnext"
          }
        }
        output = mgmt_client.api_management_service.update(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_management_service.get(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_management_service.get(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_management_service.get(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_management_service.delete(RESOURCE_GROUP, SERVICE_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_management_service.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.api_management_service.list(, BODY)
        BODY = {}
        output = mgmt_client.api_management_service.get_sso_token(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "name": "apimService1"
        }
        output = mgmt_client.api_management_service.check_name_availability(, BODY)
        BODY = {
          "location": "west us"
        }
        output = mgmt_client.api_management_service.apply_network_configuration_updates(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.diagnostic.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.diagnostic.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.diagnostic.get(RESOURCE_GROUP, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
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
        output = mgmt_client.diagnostic.create_or_update(RESOURCE_GROUP, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
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
        output = mgmt_client.diagnostic.update(RESOURCE_GROUP, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.diagnostic.delete(RESOURCE_GROUP, SERVICE_NAME, DIAGNOSTIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.email_template.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.email_template.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, TEMPLATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.email_template.get(RESOURCE_GROUP, SERVICE_NAME, TEMPLATE_NAME, BODY)
        BODY = {
          "properties": {
            "subject": "Your request for $IssueName was successfully received."
          }
        }
        output = mgmt_client.email_template.create_or_update(RESOURCE_GROUP, SERVICE_NAME, TEMPLATE_NAME, BODY)
        BODY = {
          "properties": {
            "subject": "Your application $AppName is published in the gallery",
            "body": "<!DOCTYPE html >\r\n<html>\r\n  <head />\r\n  <body>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Dear $DevFirstName $DevLastName,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">\r\n          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href=\"http://$DevPortalUrl/Applications/Details/$AppId\">here</a>.\r\n        </p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Best,</p>\r\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">The $OrganizationName API Team</p>\r\n  </body>\r\n</html>"
          }
        }
        output = mgmt_client.email_template.update(RESOURCE_GROUP, SERVICE_NAME, TEMPLATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.email_template.delete(RESOURCE_GROUP, SERVICE_NAME, TEMPLATE_NAME, BODY)
        BODY = {}
        output = mgmt_client.group.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.group.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, BODY)
        BODY = {}
        output = mgmt_client.group.get(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "temp group"
          }
        }
        output = mgmt_client.group.create_or_update(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "NewGroup (samiraad.onmicrosoft.com)",
            "description": "new group to test",
            "type": "external",
            "external_id": "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"
          }
        }
        output = mgmt_client.group.create_or_update(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "temp group"
          }
        }
        output = mgmt_client.group.update(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, BODY)
        BODY = {}
        output = mgmt_client.group.delete(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, BODY)
        BODY = {}
        output = mgmt_client.group_user.list(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, , BODY)
        BODY = {}
        output = mgmt_client.group_user.check_entity_exists(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.group_user.create(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.group_user.delete(RESOURCE_GROUP, SERVICE_NAME, GROUP_NAME, USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.identity_provider.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.identity_provider.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        BODY = {}
        output = mgmt_client.identity_provider.get(RESOURCE_GROUP, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        BODY = {
          "properties": {
            "client_id": "facebookid",
            "client_secret": "facebookapplicationsecret"
          }
        }
        output = mgmt_client.identity_provider.create_or_update(RESOURCE_GROUP, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        BODY = {
          "properties": {
            "client_id": "updatedfacebookid",
            "client_secret": "updatedfacebooksecret"
          }
        }
        output = mgmt_client.identity_provider.update(RESOURCE_GROUP, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        BODY = {}
        output = mgmt_client.identity_provider.delete(RESOURCE_GROUP, SERVICE_NAME, IDENTITY_PROVIDER_NAME, BODY)
        BODY = {}
        output = mgmt_client.issue.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.issue.get(RESOURCE_GROUP, SERVICE_NAME, ISSUE_NAME, BODY)
        BODY = {}
        output = mgmt_client.logger.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.logger.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, LOGGER_NAME, BODY)
        BODY = {}
        output = mgmt_client.logger.get(RESOURCE_GROUP, SERVICE_NAME, LOGGER_NAME, BODY)
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
        output = mgmt_client.logger.create_or_update(RESOURCE_GROUP, SERVICE_NAME, LOGGER_NAME, BODY)
        BODY = {
          "properties": {
            "logger_type": "applicationInsights",
            "description": "adding a new logger",
            "credentials": {
              "instrumentation_key": "11................a1"
            }
          }
        }
        output = mgmt_client.logger.create_or_update(RESOURCE_GROUP, SERVICE_NAME, LOGGER_NAME, BODY)
        BODY = {
          "properties": {
            "credentials": {
              "name": "hydraeventhub",
              "connection_string": "Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********="
            }
          }
        }
        output = mgmt_client.logger.update(RESOURCE_GROUP, SERVICE_NAME, LOGGER_NAME, BODY)
        BODY = {}
        output = mgmt_client.logger.delete(RESOURCE_GROUP, SERVICE_NAME, LOGGER_NAME, BODY)
        BODY = {}
        output = mgmt_client.network_status.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.network_status.list_by_location(RESOURCE_GROUP, SERVICE_NAME, LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.notification.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.notification.get(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification.create_or_update(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_user.list_by_notification(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_user.check_entity_exists(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_user.create_or_update(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_user.delete(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_email.list_by_notification(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_email.check_entity_exists(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_EMAIL_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_email.create_or_update(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_EMAIL_NAME, BODY)
        BODY = {}
        output = mgmt_client.notification_recipient_email.delete(RESOURCE_GROUP, SERVICE_NAME, NOTIFICATION_NAME, RECIPIENT_EMAIL_NAME, BODY)
        BODY = {}
        output = mgmt_client.open_id_connect_provider.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.open_id_connect_provider.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        BODY = {}
        output = mgmt_client.open_id_connect_provider.get(RESOURCE_GROUP, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "templateoidprovider3",
            "metadata_endpoint": "https://oidprovider-template3.net",
            "client_id": "oidprovidertemplate3"
          }
        }
        output = mgmt_client.open_id_connect_provider.create_or_update(RESOURCE_GROUP, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        BODY = {
          "properties": {
            "client_secret": "updatedsecret"
          }
        }
        output = mgmt_client.open_id_connect_provider.update(RESOURCE_GROUP, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        BODY = {}
        output = mgmt_client.open_id_connect_provider.delete(RESOURCE_GROUP, SERVICE_NAME, OPENID_CONNECT_PROVIDER_NAME, BODY)
        BODY = {}
        output = mgmt_client.policy.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.policy.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.policy.get(RESOURCE_GROUP, SERVICE_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.policy.get(RESOURCE_GROUP, SERVICE_NAME, POLICY_NAME, BODY)
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
          }
        }
        output = mgmt_client.policy.create_or_update(RESOURCE_GROUP, SERVICE_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.policy.delete(RESOURCE_GROUP, SERVICE_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.policy_snippet.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.sign_in_settings.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.sign_in_settings.get(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "properties": {
            "enabled": True
          }
        }
        output = mgmt_client.sign_in_settings.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "properties": {
            "enabled": True
          }
        }
        output = mgmt_client.sign_in_settings.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.sign_up_settings.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.sign_up_settings.get(RESOURCE_GROUP, SERVICE_NAME, , BODY)
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
        output = mgmt_client.sign_up_settings.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
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
        output = mgmt_client.sign_up_settings.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.delegation_settings.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.delegation_settings.get(RESOURCE_GROUP, SERVICE_NAME, , BODY)
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
        output = mgmt_client.delegation_settings.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
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
        output = mgmt_client.delegation_settings.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, BODY)
        BODY = {}
        output = mgmt_client.product.get(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "Test Template ProductName 4"
          }
        }
        output = mgmt_client.product.create_or_update(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, BODY)
        BODY = {
          "properties": {
            "display_name": "Test Template ProductName 4"
          }
        }
        output = mgmt_client.product.update(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, BODY)
        BODY = {}
        output = mgmt_client.product.delete(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, BODY)
        BODY = {}
        output = mgmt_client.product.list_by_tags(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product_api.list_by_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product_api.check_entity_exists(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_api.create_or_update(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_api.delete(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_group.list_by_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product_group.check_entity_exists(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, GROUP_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_group.create_or_update(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, GROUP_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_group.delete(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, GROUP_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_subscriptions.list(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product_policy.list_by_product(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.product_policy.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_policy.get(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        BODY = {
          "properties": {
            "format": "xml",
            "value": "<policies>\r\n  <inbound>\r\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\r\n    <log-to-eventhub logger-id=\"16\">\r\n                      @( string.Join(\",\", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) \r\n                  </log-to-eventhub>\r\n    <quota-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(context.Request.Method == &quot;POST&quot; ? 1:2)\" />\r\n    <base />\r\n  </inbound>\r\n  <backend>\r\n    <base />\r\n  </backend>\r\n  <outbound>\r\n    <base />\r\n  </outbound>\r\n</policies>"
          }
        }
        output = mgmt_client.product_policy.create_or_update(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.product_policy.delete(RESOURCE_GROUP, SERVICE_NAME, PRODUCT_NAME, POLICY_NAME, BODY)
        BODY = {}
        output = mgmt_client.property.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.property.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, PROPERTY_NAME, BODY)
        BODY = {}
        output = mgmt_client.property.get(RESOURCE_GROUP, SERVICE_NAME, PROPERTY_NAME, BODY)
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
        output = mgmt_client.property.create_or_update(RESOURCE_GROUP, SERVICE_NAME, PROPERTY_NAME, BODY)
        BODY = {
          "properties": {
            "tags": [
              "foo",
              "bar2"
            ],
            "secret": True
          }
        }
        output = mgmt_client.property.update(RESOURCE_GROUP, SERVICE_NAME, PROPERTY_NAME, BODY)
        BODY = {}
        output = mgmt_client.property.delete(RESOURCE_GROUP, SERVICE_NAME, PROPERTY_NAME, BODY)
        BODY = {}
        output = mgmt_client.quota_by_counter_keys.list_by_service(RESOURCE_GROUP, SERVICE_NAME, QUOTA_NAME, BODY)
        BODY = {
          "calls_count": "0",
          "kb_transferred": "2.5630078125"
        }
        output = mgmt_client.quota_by_counter_keys.update(RESOURCE_GROUP, SERVICE_NAME, QUOTA_NAME, BODY)
        BODY = {}
        output = mgmt_client.quota_by_period_keys.get(RESOURCE_GROUP, SERVICE_NAME, QUOTA_NAME, PERIOD_NAME, BODY)
        BODY = {
          "calls_count": "0",
          "kb_transferred": "0"
        }
        output = mgmt_client.quota_by_period_keys.update(RESOURCE_GROUP, SERVICE_NAME, QUOTA_NAME, PERIOD_NAME, BODY)
        BODY = {}
        output = mgmt_client.region.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_api(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_user(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_operation(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_product(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_geo(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_subscription(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_time(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.reports.list_by_request(RESOURCE_GROUP, SERVICE_NAME, REPORT_NAME, BODY)
        BODY = {}
        output = mgmt_client.subscription.list(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.subscription.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.subscription.get(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "properties": {
            "owner_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + "",
            "scope": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/products/" + PRODUCT_NAME + "",
            "display_name": "testsub"
          }
        }
        output = mgmt_client.subscription.create_or_update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {
          "properties": {
            "display_name": "testsub"
          }
        }
        output = mgmt_client.subscription.update(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.subscription.delete(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.subscription.regenerate_primary_key(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.subscription.regenerate_secondary_key(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tag_resource.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tenant_access.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, BODY)
        BODY = {}
        output = mgmt_client.tenant_access.get(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, BODY)
        BODY = {
          "enabled": True
        }
        output = mgmt_client.tenant_access.update(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, BODY)
        BODY = {}
        output = mgmt_client.tenant_access.regenerate_primary_key(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tenant_access.regenerate_primary_key(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tenant_access.get(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, BODY)
        BODY = {}
        output = mgmt_client.tenant_access.regenerate_primary_key(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tenant_access.regenerate_primary_key(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {
          "properties": {
            "branch": "master"
          }
        }
        output = mgmt_client.tenant_configuration.deploy(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {
          "properties": {
            "branch": "master"
          }
        }
        output = mgmt_client.tenant_configuration.save(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {
          "properties": {
            "branch": "master"
          }
        }
        output = mgmt_client.tenant_configuration.validate(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.tenant_configuration.get_sync_state(RESOURCE_GROUP, SERVICE_NAME, TENANT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.user.list_by_service(RESOURCE_GROUP, SERVICE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.user.get_entity_tag(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.user.get(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, BODY)
        BODY = {
          "properties": {
            "first_name": "foo",
            "last_name": "bar",
            "email": "foobar@outlook.com",
            "confirmation": "signup"
          }
        }
        output = mgmt_client.user.create_or_update(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, BODY)
        BODY = {
          "properties": {
            "first_name": "foo",
            "last_name": "bar",
            "email": "foobar@outlook.com"
          }
        }
        output = mgmt_client.user.update(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.user.delete(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, BODY)
        BODY = {}
        output = mgmt_client.user.generate_sso_url(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, , BODY)
        BODY = {
          "properties": {
            "key_type": "primary",
            "expiry": "2019-04-21T00:44:24.2845269Z"
          }
        }
        output = mgmt_client.user.get_shared_access_token(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, , BODY)
        BODY = {}
        output = mgmt_client.user_group.list(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, , BODY)
        BODY = {}
        output = mgmt_client.user_subscription.list(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, , BODY)
        BODY = {}
        output = mgmt_client.user_identities.list(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, , BODY)
        BODY = {}
        output = mgmt_client.user_confirmation_password.send(RESOURCE_GROUP, SERVICE_NAME, USER_NAME, CONFIRMATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.api_export.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)
        BODY = {}
        output = mgmt_client.api_export.get(RESOURCE_GROUP, SERVICE_NAME, API_NAME, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()