# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['apimgmt api'] = """
    type: group
    short-summary: Commands to manage Api.
"""

helps['apimgmt api create'] = """
    type: command
    short-summary: create a apimgmt api.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiUsingOai3Import
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "petstore" --path "petstore" --value "https://raw.githubusercontent.com/OAI/OpenAPI-Specif
               ication/master/examples/v3.0/petstore.yaml" --format "openapi-link"
# create
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "petstore" --path "petstore" --value "http://petstore.swagger.io/v2/swagger.json" \\
               --format "swagger-link-json"
# create
      - name: ApiManagementCreateApiUsingWadlImport
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "petstore" --path "collector" --value "https://developer.cisco.com/media/wae-release-6-2-a
               pi-reference/wae-collector-rest-api/application.wadl" --format "wadl-link-json"
# create
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "soapApi" --path "currency" --value \\
               "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL" --format "wsdl-link"
# create
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "soapApi" --path "currency" --value \\
               "http://www.webservicex.net/CurrencyConvertor.asmx?WSDL" --format "wsdl-link" --api-type \\
               "soap"
# create
      - name: ApiManagementCreateApi
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "tempgroup" --description "apidescription5200" --display-name "apiname1463" --service-url \\
               "http://newechoapi.cloudapp.net/api" --path "newapiPath"
# create
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "echo-api;rev=3" --api-revision-description "Creating a Revision of an existing API" \\
               --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/
               providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" \\
               --service-url "http://echoapi.cloudapp.net/apiv3" --path "echo"
# create
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "echoapiv3" --description \\
               "Create Echo API into a new Version using Existing Version Set and Copy all Operations." \\
               --api-version "v4" --is-current true --api-version-set-id "/subscriptions/{{ subscription_
               id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ ser
               vice_name }}/apiVersionSets/{{ api_version_set_name }}" --subscription-required true \\
               --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/
               providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}" \\
               --display-name "Echo API2" --service-url "http://echoapi.cloudapp.net/api" --path "echo2"
# create
      - name: ApiManagementCreateApiClone
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "echo-api2" --description "Copy of Existing Echo Api including Operations." --is-current \\
               true --subscription-required true --source-api-id "/subscriptions/{{ subscription_id }}/re
               sourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_nam
               e }}/apis/{{ api_name }}" --display-name "Echo API2" --service-url \\
               "http://echoapi.cloudapp.net/api" --path "echo2"
# create
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: |-
               az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "tempgroup" --description "This is a sample server Petstore server.  You can find out more
                about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger
               ](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test
                the authorization filters." --display-name "Swagger Petstore" --service-url \\
               "http://petstore.swagger.io/v2" --path "petstore"
"""

helps['apimgmt api update'] = """
    type: command
    short-summary: update a apimgmt api.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateApi
        text: |-
               az apimgmt api update --resource-group "rg1" --service-name "apimService1" --api-id \\
               "echo-api" --display-name "Echo API New" --service-url "http://echoapi.cloudapp.net/api2" \\
               --path "newecho"
"""

helps['apimgmt api delete'] = """
    type: command
    short-summary: delete a apimgmt api.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApi
        text: |-
               az apimgmt api delete --resource-group "rg1" --service-name "apimService1" --api-id \\
               "echo-api"
"""

helps['apimgmt api list'] = """
    type: command
    short-summary: list a apimgmt api.
# list_by_tags -- list
# list_by_service -- list
"""

helps['apimgmt api show'] = """
    type: command
    short-summary: show a apimgmt api.
# get -- show
"""

helps['apimgmt api release'] = """
    type: group
    short-summary: Commands to manage ApiRelease.
"""

helps['apimgmt api release create'] = """
    type: command
    short-summary: create a apimgmt api release.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiRelease
        text: |-
               az apimgmt api release create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "a1" --release-id "testrev" --notes "yahooagain"
"""

helps['apimgmt api release update'] = """
    type: command
    short-summary: update a apimgmt api release.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateApiRelease
        text: |-
               az apimgmt api release update --resource-group "rg1" --service-name "apimService1" \\
               --api-id "a1" --release-id "testrev" --notes "yahooagain"
"""

helps['apimgmt api release delete'] = """
    type: command
    short-summary: delete a apimgmt api release.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiRelease
        text: |-
               az apimgmt api release delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "5a5fcc09124a7fa9b89f2f1d" --release-id "testrev"
"""

helps['apimgmt api release list'] = """
    type: command
    short-summary: list a apimgmt api release.
# list_by_service -- list
"""

helps['apimgmt api release show'] = """
    type: command
    short-summary: show a apimgmt api release.
# get -- show
"""

helps['apimgmt api operation'] = """
    type: group
    short-summary: Commands to manage ApiOperation.
"""

helps['apimgmt api operation create'] = """
    type: command
    short-summary: create a apimgmt api operation.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiOperation
        text: |-
               az apimgmt api operation create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "PetStoreTemplate2" --operation-id "newoperations" --description \\
               "This can only be done by the logged in user." --display-name "createUser2" --method \\
               "POST" --url-template "/user1"
"""

helps['apimgmt api operation update'] = """
    type: command
    short-summary: update a apimgmt api operation.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateApiOperation
        text: |-
               az apimgmt api operation update --resource-group "rg1" --service-name "apimService1" \\
               --api-id "echo-api" --operation-id "operationId" --display-name "Retrieve resource" \\
               --method "GET" --url-template "/resource"
"""

helps['apimgmt api operation delete'] = """
    type: command
    short-summary: delete a apimgmt api operation.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiOperation
        text: |-
               az apimgmt api operation delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "57d2ef278aa04f0888cba3f3" --operation-id "57d2ef278aa04f0ad01d6cdc"
"""

helps['apimgmt api operation list'] = """
    type: command
    short-summary: list a apimgmt api operation.
# list_by_api -- list
"""

helps['apimgmt api operation show'] = """
    type: command
    short-summary: show a apimgmt api operation.
# get -- show
"""

helps['apimgmt api operation policy'] = """
    type: group
    short-summary: Commands to manage ApiOperationPolicy.
"""

helps['apimgmt api operation policy create'] = """
    type: command
    short-summary: create a apimgmt api operation policy.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiOperationPolicy
        text: |-
               az apimgmt api operation policy create --resource-group "rg1" --service-name \\
               "apimService1" --api-id "5600b57e7e8880006a040001" --operation-id \\
               "5600b57e7e8880006a080001" --policy-id "policy" --value "<policies> <inbound /> <backend> 
                  <forward-request />  </backend>  <outbound /></policies>" --format "xml"
"""

helps['apimgmt api operation policy update'] = """
    type: command
    short-summary: update a apimgmt api operation policy.
# create_or_update -- update
"""

helps['apimgmt api operation policy delete'] = """
    type: command
    short-summary: delete a apimgmt api operation policy.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiOperationPolicy
        text: |-
               az apimgmt api operation policy delete --resource-group "rg1" --service-name \\
               "apimService1" --api-id "testapi" --operation-id "testoperation" --policy-id "policy"
"""

helps['apimgmt api operation policy list'] = """
    type: command
    short-summary: list a apimgmt api operation policy.
# list_by_operation -- list
"""

helps['apimgmt api operation policy show'] = """
    type: command
    short-summary: show a apimgmt api operation policy.
# get -- show
"""

helps['apimgmt tag'] = """
    type: group
    short-summary: Commands to manage Tag.
"""

helps['apimgmt tag create'] = """
    type: command
    short-summary: create a apimgmt tag.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateTag
        text: |-
               az apimgmt tag create --resource-group "rg1" --service-name "apimService1" --tag-id \\
               "tagId1" --display-name "tag1"
"""

helps['apimgmt tag update'] = """
    type: command
    short-summary: update a apimgmt tag.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateTag
        text: |-
               az apimgmt tag update --resource-group "rg1" --service-name "apimService1" --tag-id \\
               "temptag" --display-name "temp tag"
"""

helps['apimgmt tag delete'] = """
    type: command
    short-summary: delete a apimgmt tag.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteTag
        text: |-
               az apimgmt tag delete --resource-group "rg1" --service-name "apimService1" --tag-id \\
               "tagId1"
"""

helps['apimgmt tag list'] = """
    type: command
    short-summary: list a apimgmt tag.
# list_by_operation -- list
# list_by_product -- list
# list_by_api -- list
# list_by_service -- list
"""

helps['apimgmt tag show'] = """
    type: command
    short-summary: show a apimgmt tag.
# get -- show
"""

helps['apimgmt api policy'] = """
    type: group
    short-summary: Commands to manage ApiPolicy.
"""

helps['apimgmt api policy create'] = """
    type: command
    short-summary: create a apimgmt api policy.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiPolicy
        text: |-
               az apimgmt api policy create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "5600b57e7e8880006a040001" --policy-id "policy" --value "<policies> <inbound /> <
               backend>    <forward-request />  </backend>  <outbound /></policies>" --format "xml"
# create
      - name: ApiManagementCreateApiPolicyNonXmlEncoded
        text: |-
               az apimgmt api policy create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "5600b57e7e8880006a040001" --policy-id "policy" --value "<policies>\\r\\n     <in
               bound>\\r\\n     <base />\\r\\n  <set-header name=\"newvalue\" exists-action=\"override\">
               \\r\\n   <value>\"@(context.Request.Headers.FirstOrDefault(h => h.Ke==\"Via\"))\" </value>
               \\r\\n    </set-header>\\r\\n  </inbound>\\r\\n      </policies>" --format "rawxml"
"""

helps['apimgmt api policy update'] = """
    type: command
    short-summary: update a apimgmt api policy.
# create_or_update -- update
"""

helps['apimgmt api policy delete'] = """
    type: command
    short-summary: delete a apimgmt api policy.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiPolicy
        text: |-
               az apimgmt api policy delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "loggerId" --policy-id "policy"
"""

helps['apimgmt api policy list'] = """
    type: command
    short-summary: list a apimgmt api policy.
# list_by_api -- list
"""

helps['apimgmt api policy show'] = """
    type: command
    short-summary: show a apimgmt api policy.
# get -- show
"""

helps['apimgmt api schema'] = """
    type: group
    short-summary: Commands to manage ApiSchema.
"""

helps['apimgmt api schema create'] = """
    type: command
    short-summary: create a apimgmt api schema.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiSchema
        text: |-
               az apimgmt api schema create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "59d6bb8f1f7fab13dc67ec9b" --schema-id "ec12520d-9d48-4e7b-8f39-698ca2ac63f1" \\
               --content-type "application/vnd.ms-azure-apim.xsd+xml"
"""

helps['apimgmt api schema update'] = """
    type: command
    short-summary: update a apimgmt api schema.
# create_or_update -- update
"""

helps['apimgmt api schema delete'] = """
    type: command
    short-summary: delete a apimgmt api schema.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiSchema
        text: |-
               az apimgmt api schema delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "59d5b28d1f7fab116c282650" --schema-id "59d5b28e1f7fab116402044e"
"""

helps['apimgmt api schema list'] = """
    type: command
    short-summary: list a apimgmt api schema.
# list_by_api -- list
"""

helps['apimgmt api schema show'] = """
    type: command
    short-summary: show a apimgmt api schema.
# get -- show
"""

helps['apimgmt api diagnostic'] = """
    type: group
    short-summary: Commands to manage ApiDiagnostic.
"""

helps['apimgmt api diagnostic create'] = """
    type: command
    short-summary: create a apimgmt api diagnostic.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiDiagnostic
        text: |-
               az apimgmt api diagnostic create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights" --always-log \\
               "allErrors" --logger-id "/loggers/applicationinsights"
"""

helps['apimgmt api diagnostic update'] = """
    type: command
    short-summary: update a apimgmt api diagnostic.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateApiDiagnostic
        text: |-
               az apimgmt api diagnostic update --resource-group "rg1" --service-name "apimService1" \\
               --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights" --always-log \\
               "allErrors" --logger-id "/loggers/applicationinsights"
"""

helps['apimgmt api diagnostic delete'] = """
    type: command
    short-summary: delete a apimgmt api diagnostic.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiDiagnostic
        text: |-
               az apimgmt api diagnostic delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "57d1f7558aa04f15146d9d8a" --diagnostic-id "applicationinsights"
"""

helps['apimgmt api diagnostic list'] = """
    type: command
    short-summary: list a apimgmt api diagnostic.
# list_by_service -- list
"""

helps['apimgmt api diagnostic show'] = """
    type: command
    short-summary: show a apimgmt api diagnostic.
# get -- show
"""

helps['apimgmt api issue'] = """
    type: group
    short-summary: Commands to manage ApiIssue.
"""

helps['apimgmt api issue create'] = """
    type: command
    short-summary: create a apimgmt api issue.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiIssue
        text: |-
               az apimgmt api issue create --resource-group "rg1" --service-name "apimService1" --api-id \\
               "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --created-date \\
               "2018-02-01T22:21:20.467Z" --state "open" --title "New API issue" --description \\
               "New API issue description" --user-id "/subscriptions/{{ subscription_id }}/resourceGroups
               /{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{
               { user_name }}"
"""

helps['apimgmt api issue update'] = """
    type: command
    short-summary: update a apimgmt api issue.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateApiIssue
        text: |-
               az apimgmt api issue update --resource-group "rg1" --service-name "apimService1" --api-id \\
               "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --state "closed"
"""

helps['apimgmt api issue delete'] = """
    type: command
    short-summary: delete a apimgmt api issue.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiIssue
        text: |-
               az apimgmt api issue delete --resource-group "rg1" --service-name "apimService1" --api-id \\
               "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc"
"""

helps['apimgmt api issue list'] = """
    type: command
    short-summary: list a apimgmt api issue.
# list_by_service -- list
"""

helps['apimgmt api issue show'] = """
    type: command
    short-summary: show a apimgmt api issue.
# get -- show
"""

helps['apimgmt api issue comment'] = """
    type: group
    short-summary: Commands to manage ApiIssueComment.
"""

helps['apimgmt api issue comment create'] = """
    type: command
    short-summary: create a apimgmt api issue comment.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiIssueComment
        text: |-
               az apimgmt api issue comment create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id \\
               "599e29ab193c3c0bd0b3e2fb" --text "Issue comment." --created-date \\
               "2018-02-01T22:21:20.467Z" --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/
               {{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{
                user_name }}"
"""

helps['apimgmt api issue comment update'] = """
    type: command
    short-summary: update a apimgmt api issue comment.
# create_or_update -- update
"""

helps['apimgmt api issue comment delete'] = """
    type: command
    short-summary: delete a apimgmt api issue comment.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiIssueComment
        text: |-
               az apimgmt api issue comment delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" --comment-id \\
               "599e29ab193c3c0bd0b3e2fb"
"""

helps['apimgmt api issue comment list'] = """
    type: command
    short-summary: list a apimgmt api issue comment.
# list_by_service -- list
"""

helps['apimgmt api issue comment show'] = """
    type: command
    short-summary: show a apimgmt api issue comment.
# get -- show
"""

helps['apimgmt api issue attachment'] = """
    type: group
    short-summary: Commands to manage ApiIssueAttachment.
"""

helps['apimgmt api issue attachment create'] = """
    type: command
    short-summary: create a apimgmt api issue attachment.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiIssueAttachment
        text: |-
               az apimgmt api issue attachment create --resource-group "rg1" --service-name \\
               "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" \\
               --attachment-id "57d2ef278aa04f0888cba3f3" --title "Issue attachment." --content-format \\
               "image/jpeg" --content "IEJhc2U2NA=="
"""

helps['apimgmt api issue attachment update'] = """
    type: command
    short-summary: update a apimgmt api issue attachment.
# create_or_update -- update
"""

helps['apimgmt api issue attachment delete'] = """
    type: command
    short-summary: delete a apimgmt api issue attachment.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiIssueAttachment
        text: |-
               az apimgmt api issue attachment delete --resource-group "rg1" --service-name \\
               "apimService1" --api-id "57d1f7558aa04f15146d9d8a" --issue-id "57d2ef278aa04f0ad01d6cdc" \\
               --attachment-id "57d2ef278aa04f0888cba3f3"
"""

helps['apimgmt api issue attachment list'] = """
    type: command
    short-summary: list a apimgmt api issue attachment.
# list_by_service -- list
"""

helps['apimgmt api issue attachment show'] = """
    type: command
    short-summary: show a apimgmt api issue attachment.
# get -- show
"""

helps['apimgmt api tagdescription'] = """
    type: group
    short-summary: Commands to manage ApiTagDescription.
"""

helps['apimgmt api tagdescription create'] = """
    type: command
    short-summary: create a apimgmt api tagdescription.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiTagDescription
        text: |-
               az apimgmt api tagdescription create --resource-group "rg1" --service-name "apimService1" \\
               --api-id "5931a75ae4bbd512a88c680b" --tag-id "tagId1" --description "Some description that
                will be displayed for operation's tag if the tag is assigned to operation of the API" \\
               --external-docs-url "http://some.url/additionaldoc" --external-docs-description \\
               "Description of the external docs resource"
"""

helps['apimgmt api tagdescription update'] = """
    type: command
    short-summary: update a apimgmt api tagdescription.
# create_or_update -- update
"""

helps['apimgmt api tagdescription delete'] = """
    type: command
    short-summary: delete a apimgmt api tagdescription.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiTagDescription
        text: |-
               az apimgmt api tagdescription delete --resource-group "rg1" --service-name "apimService1" \\
               --api-id "59d5b28d1f7fab116c282650" --tag-id "59d5b28e1f7fab116402044e"
"""

helps['apimgmt api tagdescription list'] = """
    type: command
    short-summary: list a apimgmt api tagdescription.
# list_by_service -- list
"""

helps['apimgmt api tagdescription show'] = """
    type: command
    short-summary: show a apimgmt api tagdescription.
# get -- show
"""

helps['apimgmt apiversionset'] = """
    type: group
    short-summary: Commands to manage ApiVersionSet.
"""

helps['apimgmt apiversionset create'] = """
    type: command
    short-summary: create a apimgmt apiversionset.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateApiVersionSet
        text: |-
               az apimgmt apiversionset create --resource-group "rg1" --service-name "apimService1" \\
               --version-set-id "api1" --description "Version configuration" --display-name "api set 1" \\
               --versioning-scheme "Segment"
"""

helps['apimgmt apiversionset update'] = """
    type: command
    short-summary: update a apimgmt apiversionset.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateApiVersionSet
        text: |-
               az apimgmt apiversionset update --resource-group "rg1" --service-name "apimService1" \\
               --version-set-id "api1" --description "Version configuration" --display-name "api set 1" \\
               --versioning-scheme "Segment"
"""

helps['apimgmt apiversionset delete'] = """
    type: command
    short-summary: delete a apimgmt apiversionset.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteApiVersionSet
        text: |-
               az apimgmt apiversionset delete --resource-group "rg1" --service-name "apimService1" \\
               --version-set-id "a1"
"""

helps['apimgmt apiversionset list'] = """
    type: command
    short-summary: list a apimgmt apiversionset.
# list_by_service -- list
"""

helps['apimgmt apiversionset show'] = """
    type: command
    short-summary: show a apimgmt apiversionset.
# get -- show
"""

helps['apimgmt authorizationserver'] = """
    type: group
    short-summary: Commands to manage AuthorizationServer.
"""

helps['apimgmt authorizationserver create'] = """
    type: command
    short-summary: create a apimgmt authorizationserver.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateAuthorizationServer
        text: |-
               az apimgmt authorizationserver create --resource-group "rg1" --service-name \\
               "apimService1" --authsid "newauthServer" --description "test server" --token-endpoint \\
               "https://www.contoso.com/oauth2/token" --support-state true --default-scope "read write" \\
               --client-secret "2" --resource-owner-username "un" --resource-owner-password "pwd" \\
               --display-name "test2" --client-registration-endpoint "https://www.contoso.com/apps" \\
               --authorization-endpoint "https://www.contoso.com/oauth2/auth" --client-id "1"
"""

helps['apimgmt authorizationserver update'] = """
    type: command
    short-summary: update a apimgmt authorizationserver.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateAuthorizationServer
        text: |-
               az apimgmt authorizationserver update --resource-group "rg1" --service-name \\
               "apimService1" --authsid "newauthServer" --client-secret "updated" --client-id "update"
"""

helps['apimgmt authorizationserver delete'] = """
    type: command
    short-summary: delete a apimgmt authorizationserver.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteAuthorizationServer
        text: |-
               az apimgmt authorizationserver delete --resource-group "rg1" --service-name \\
               "apimService1" --authsid "newauthServer2"
"""

helps['apimgmt authorizationserver list'] = """
    type: command
    short-summary: list a apimgmt authorizationserver.
# list_by_service -- list
"""

helps['apimgmt authorizationserver show'] = """
    type: command
    short-summary: show a apimgmt authorizationserver.
# get -- show
"""

helps['apimgmt backend'] = """
    type: group
    short-summary: Commands to manage Backend.
"""

helps['apimgmt backend create'] = """
    type: command
    short-summary: create a apimgmt backend.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateBackendServiceFabric
        text: |-
               az apimgmt backend create --resource-group "rg1" --service-name "apimService1" \\
               --backend-id "sfbackend" --description "Service Fabric Test App 1" --url \\
               "fabric:/mytestapp/mytestservice" --protocol "http"
# create
      - name: ApiManagementCreateBackendProxyBackend
        text: |-
               az apimgmt backend create --resource-group "rg1" --service-name "apimService1" \\
               --backend-id "proxybackend" --description "description5308" --url \\
               "https://backendname2644/" --protocol "http"
"""

helps['apimgmt backend update'] = """
    type: command
    short-summary: update a apimgmt backend.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateBackend
        text: |-
               az apimgmt backend update --resource-group "rg1" --service-name "apimService1" \\
               --backend-id "proxybackend" --description "description5308"
"""

helps['apimgmt backend delete'] = """
    type: command
    short-summary: delete a apimgmt backend.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteBackend
        text: |-
               az apimgmt backend delete --resource-group "rg1" --service-name "apimService1" \\
               --backend-id "sfbackend"
"""

helps['apimgmt backend list'] = """
    type: command
    short-summary: list a apimgmt backend.
# list_by_service -- list
"""

helps['apimgmt backend show'] = """
    type: command
    short-summary: show a apimgmt backend.
# get -- show
"""

helps['apimgmt cache'] = """
    type: group
    short-summary: Commands to manage Cache.
"""

helps['apimgmt cache create'] = """
    type: command
    short-summary: create a apimgmt cache.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateCache
        text: |-
               az apimgmt cache create --resource-group "rg1" --service-name "apimService1" --cache-id \\
               "westindia" --description "Redis cache instances in West India" --connection-string \\
               "contoso5.redis.cache.windows.net,ssl=true,password=..." --resource-id "/subscriptions/{{ 
               subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ 
               redis_name }}"
"""

helps['apimgmt cache update'] = """
    type: command
    short-summary: update a apimgmt cache.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateCache
        text: |-
               az apimgmt cache update --resource-group "rg1" --service-name "apimService1" --cache-id \\
               "westindia" --description "Update Cache in west India"
"""

helps['apimgmt cache delete'] = """
    type: command
    short-summary: delete a apimgmt cache.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteCache
        text: |-
               az apimgmt cache delete --resource-group "rg1" --service-name "apimService1" --cache-id \\
               "southindia"
"""

helps['apimgmt cache list'] = """
    type: command
    short-summary: list a apimgmt cache.
# list_by_service -- list
"""

helps['apimgmt cache show'] = """
    type: command
    short-summary: show a apimgmt cache.
# get -- show
"""

helps['apimgmt certificate'] = """
    type: group
    short-summary: Commands to manage Certificate.
"""

helps['apimgmt certificate create'] = """
    type: command
    short-summary: create a apimgmt certificate.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateCertificate
        text: |-
               az apimgmt certificate create --resource-group "rg1" --service-name "apimService1" \\
               --certificate-id "tempcert" --data \\
               "****************Base 64 Encoded Certificate *******************************" --password \\
               "****Certificate Password******"
"""

helps['apimgmt certificate update'] = """
    type: command
    short-summary: update a apimgmt certificate.
# create_or_update -- update
"""

helps['apimgmt certificate delete'] = """
    type: command
    short-summary: delete a apimgmt certificate.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteCertificate
        text: |-
               az apimgmt certificate delete --resource-group "rg1" --service-name "apimService1" \\
               --certificate-id "tempcert"
"""

helps['apimgmt certificate list'] = """
    type: command
    short-summary: list a apimgmt certificate.
# list_by_service -- list
"""

helps['apimgmt certificate show'] = """
    type: command
    short-summary: show a apimgmt certificate.
# get -- show
"""

helps['apimgmt'] = """
    type: group
    short-summary: Commands to manage ApiManagementService.
"""

helps['apimgmt create'] = """
    type: command
    short-summary: create a apimgmt.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateService
        text: |-
               az apimgmt create --resource-group "rg1" --name "apimService1" --publisher-email \\
               "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Developer" \\
               --sku-capacity "1" --location "Central US"
# create
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: |-
               az apimgmt create --resource-group "rg1" --name "apimService1" --virtual-network-type \\
               "External" --publisher-email "admin@live.com" --publisher-name "contoso" --sku-name \\
               "Premium" --sku-capacity "1" --location "Central US"
# create
      - name: ApiManagementCreateServiceHavingMsi
        text: |-
               az apimgmt create --resource-group "rg1" --name "apimService1" --publisher-email \\
               "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Consumption" --location \\
               "West US"
# create
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: |-
               az apimgmt create --resource-group "rg1" --name "apimService1" --publisher-email \\
               "apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Basic" --sku-capacity \\
               "1" --location "Central US"
"""

helps['apimgmt update'] = """
    type: command
    short-summary: update a apimgmt.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateServiceDisableTls10
        text: |-
               az apimgmt update --resource-group "rg1" --name "apimService1"
# update
      - name: ApiManagementUpdateServicePublisherDetails
        text: |-
               az apimgmt update --resource-group "rg1" --name "apimService1" --publisher-email \\
               "foobar@live.com" --publisher-name "Contoso Vnext"
"""

helps['apimgmt delete'] = """
    type: command
    short-summary: delete a apimgmt.
# delete -- delete
    examples:
# delete
      - name: ApiManagementServiceDeleteService
        text: |-
               az apimgmt delete --resource-group "rg1" --name "apimService1"
"""

helps['apimgmt list'] = """
    type: command
    short-summary: list a apimgmt.
# list_by_resource_group -- list
# list -- list
"""

helps['apimgmt show'] = """
    type: command
    short-summary: show a apimgmt.
# get -- show
"""

helps['apimgmt diagnostic'] = """
    type: group
    short-summary: Commands to manage Diagnostic.
"""

helps['apimgmt diagnostic create'] = """
    type: command
    short-summary: create a apimgmt diagnostic.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateDiagnostic
        text: |-
               az apimgmt diagnostic create --resource-group "rg1" --service-name "apimService1" \\
               --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id \\
               "/loggers/azuremonitor"
"""

helps['apimgmt diagnostic update'] = """
    type: command
    short-summary: update a apimgmt diagnostic.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateDiagnostic
        text: |-
               az apimgmt diagnostic update --resource-group "rg1" --service-name "apimService1" \\
               --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id \\
               "/loggers/applicationinsights"
"""

helps['apimgmt diagnostic delete'] = """
    type: command
    short-summary: delete a apimgmt diagnostic.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteDiagnostic
        text: |-
               az apimgmt diagnostic delete --resource-group "rg1" --service-name "apimService1" \\
               --diagnostic-id "applicationinsights"
"""

helps['apimgmt diagnostic list'] = """
    type: command
    short-summary: list a apimgmt diagnostic.
# list_by_service -- list
"""

helps['apimgmt diagnostic show'] = """
    type: command
    short-summary: show a apimgmt diagnostic.
# get -- show
"""

helps['apimgmt template'] = """
    type: group
    short-summary: Commands to manage EmailTemplate.
"""

helps['apimgmt template create'] = """
    type: command
    short-summary: create a apimgmt template.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateEmailTemplate
        text: |-
               az apimgmt template create --resource-group "rg1" --service-name "apimService1" --name \\
               "newIssueNotificationMessage" --subject \\
               "Your request for $IssueName was successfully received."
"""

helps['apimgmt template update'] = """
    type: command
    short-summary: update a apimgmt template.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateEmailTemplate
        text: |-
               az apimgmt template update --resource-group "rg1" --service-name "apimService1" --name \\
               "applicationApprovedNotificationMessage" --subject \\
               "Your application $AppName is published in the gallery" --body "<!DOCTYPE html >\\r\\n<htm
               l>\\r\\n  <head />\\r\\n  <body>\\r\\n    <p style=\"font-size:12pt;font-family:'Segoe UI'
               \">Dear $DevFirstName $DevLastName,</p>\\r\\n    <p style=\"font-size:12pt;font-family:'Se
               goe UI'\">\\r\\n          We are happy to let you know that your request to publish the $A
               ppName application in the gallery has been approved. Your application has been published a
               nd can be viewed <a href=\"http://$DevPortalUrl/Applications/Details/$AppId\">here</a>.\\r
               \\n        </p>\\r\\n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">Best,</p>\\r\\
               n    <p style=\"font-size:12pt;font-family:'Segoe UI'\">The $OrganizationName API Team</p>
               \\r\\n  </body>\\r\\n</html>"
"""

helps['apimgmt template delete'] = """
    type: command
    short-summary: delete a apimgmt template.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteEmailTemplate
        text: |-
               az apimgmt template delete --resource-group "rg1" --service-name "apimService1" --name \\
               "newIssueNotificationMessage"
"""

helps['apimgmt template list'] = """
    type: command
    short-summary: list a apimgmt template.
# list_by_service -- list
"""

helps['apimgmt template show'] = """
    type: command
    short-summary: show a apimgmt template.
# get -- show
"""

helps['apimgmt group'] = """
    type: group
    short-summary: Commands to manage Group.
"""

helps['apimgmt group create'] = """
    type: command
    short-summary: create a apimgmt group.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateGroup
        text: |-
               az apimgmt group create --resource-group "rg1" --service-name "apimService1" --group-id \\
               "tempgroup" --display-name "temp group"
# create
      - name: ApiManagementCreateGroupExternal
        text: |-
               az apimgmt group create --resource-group "rg1" --service-name "apimService1" --group-id \\
               "aadGroup" --display-name "NewGroup (samiraad.onmicrosoft.com)" --description \\
               "new group to test" --type "external" --external-id \\
               "aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"
"""

helps['apimgmt group update'] = """
    type: command
    short-summary: update a apimgmt group.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateGroup
        text: |-
               az apimgmt group update --resource-group "rg1" --service-name "apimService1" --group-id \\
               "tempgroup" --display-name "temp group"
"""

helps['apimgmt group delete'] = """
    type: command
    short-summary: delete a apimgmt group.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteGroup
        text: |-
               az apimgmt group delete --resource-group "rg1" --service-name "apimService1" --group-id \\
               "aadGroup"
"""

helps['apimgmt group list'] = """
    type: command
    short-summary: list a apimgmt group.
# list_by_service -- list
"""

helps['apimgmt group show'] = """
    type: command
    short-summary: show a apimgmt group.
# get -- show
"""

helps['apimgmt group user'] = """
    type: group
    short-summary: Commands to manage GroupUser.
"""

helps['apimgmt group user create'] = """
    type: command
    short-summary: create a apimgmt group user.
# create -- create
    examples:
# create
      - name: ApiManagementCreateGroupUser
        text: |-
               az apimgmt group user create --resource-group "rg1" --service-name "apimService1" \\
               --group-id "tempgroup" --user-id "59307d350af58404d8a26300"
"""

helps['apimgmt group user delete'] = """
    type: command
    short-summary: delete a apimgmt group user.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteGroupUser
        text: |-
               az apimgmt group user delete --resource-group "rg1" --service-name "apimService1" \\
               --group-id "templategroup" --user-id "59307d350af58404d8a26300"
"""

helps['apimgmt group user list'] = """
    type: command
    short-summary: list a apimgmt group user.
# list -- list
"""

helps['apimgmt identityprovider'] = """
    type: group
    short-summary: Commands to manage IdentityProvider.
"""

helps['apimgmt identityprovider create'] = """
    type: command
    short-summary: create a apimgmt identityprovider.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateIdentityProvider
        text: |-
               az apimgmt identityprovider create --resource-group "rg1" --service-name "apimService1" \\
               --name "facebook" --client-id "facebookid" --client-secret "facebookapplicationsecret"
"""

helps['apimgmt identityprovider update'] = """
    type: command
    short-summary: update a apimgmt identityprovider.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateIdentityProvider
        text: |-
               az apimgmt identityprovider update --resource-group "rg1" --service-name "apimService1" \\
               --name "facebook" --client-id "updatedfacebookid" --client-secret "updatedfacebooksecret"
"""

helps['apimgmt identityprovider delete'] = """
    type: command
    short-summary: delete a apimgmt identityprovider.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteIdentityProvider
        text: |-
               az apimgmt identityprovider delete --resource-group "rg1" --service-name "apimService1" \\
               --name "aad"
"""

helps['apimgmt identityprovider list'] = """
    type: command
    short-summary: list a apimgmt identityprovider.
# list_by_service -- list
"""

helps['apimgmt identityprovider show'] = """
    type: command
    short-summary: show a apimgmt identityprovider.
# get -- show
"""

helps['apimgmt logger'] = """
    type: group
    short-summary: Commands to manage Logger.
"""

helps['apimgmt logger create'] = """
    type: command
    short-summary: create a apimgmt logger.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateEHLogger
        text: |-
               az apimgmt logger create --resource-group "rg1" --service-name "apimService1" --logger-id \\
               "loggerId" --logger-type "azureEventHub" --description "adding a new logger"
# create
      - name: ApiManagementCreateAILogger
        text: |-
               az apimgmt logger create --resource-group "rg1" --service-name "apimService1" --logger-id \\
               "loggerId" --logger-type "applicationInsights" --description "adding a new logger"
"""

helps['apimgmt logger update'] = """
    type: command
    short-summary: update a apimgmt logger.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateLogger
        text: |-
               az apimgmt logger update --resource-group "rg1" --service-name "apimService1" --logger-id \\
               "loggerId"
"""

helps['apimgmt logger delete'] = """
    type: command
    short-summary: delete a apimgmt logger.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteLogger
        text: |-
               az apimgmt logger delete --resource-group "rg1" --service-name "apimService1" --logger-id \\
               "loggerId"
"""

helps['apimgmt logger list'] = """
    type: command
    short-summary: list a apimgmt logger.
# list_by_service -- list
"""

helps['apimgmt logger show'] = """
    type: command
    short-summary: show a apimgmt logger.
# get -- show
"""

helps['apimgmt notification'] = """
    type: group
    short-summary: Commands to manage Notification.
"""

helps['apimgmt notification create'] = """
    type: command
    short-summary: create a apimgmt notification.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateNotification
        text: |-
               az apimgmt notification create --resource-group "rg1" --service-name "apimService1" \\
               --name "RequestPublisherNotificationMessage"
"""

helps['apimgmt notification update'] = """
    type: command
    short-summary: update a apimgmt notification.
# create_or_update -- update
"""

helps['apimgmt notification list'] = """
    type: command
    short-summary: list a apimgmt notification.
# list_by_service -- list
"""

helps['apimgmt notification show'] = """
    type: command
    short-summary: show a apimgmt notification.
# get -- show
"""

helps['apimgmt notification recipientuser'] = """
    type: group
    short-summary: Commands to manage NotificationRecipientUser.
"""

helps['apimgmt notification recipientuser create'] = """
    type: command
    short-summary: create a apimgmt notification recipientuser.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateNotificationRecipientUser
        text: |-
               az apimgmt notification recipientuser create --resource-group "rg1" --service-name \\
               "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id \\
               "576823d0a40f7e74ec07d642"
"""

helps['apimgmt notification recipientuser update'] = """
    type: command
    short-summary: update a apimgmt notification recipientuser.
# create_or_update -- update
"""

helps['apimgmt notification recipientuser delete'] = """
    type: command
    short-summary: delete a apimgmt notification recipientuser.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteNotificationRecipientUser
        text: |-
               az apimgmt notification recipientuser delete --resource-group "rg1" --service-name \\
               "apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id \\
               "576823d0a40f7e74ec07d642"
"""

helps['apimgmt notification recipientuser list'] = """
    type: command
    short-summary: list a apimgmt notification recipientuser.
# list_by_notification -- list
"""

helps['apimgmt notification recipientemail'] = """
    type: group
    short-summary: Commands to manage NotificationRecipientEmail.
"""

helps['apimgmt notification recipientemail create'] = """
    type: command
    short-summary: create a apimgmt notification recipientemail.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateNotificationRecipientEmail
        text: |-
               az apimgmt notification recipientemail create --resource-group "rg1" --service-name \\
               "apimService1" --notification-name "RequestPublisherNotificationMessage" --email \\
               "foobar@live.com"
"""

helps['apimgmt notification recipientemail update'] = """
    type: command
    short-summary: update a apimgmt notification recipientemail.
# create_or_update -- update
"""

helps['apimgmt notification recipientemail delete'] = """
    type: command
    short-summary: delete a apimgmt notification recipientemail.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteNotificationRecipientEmail
        text: |-
               az apimgmt notification recipientemail delete --resource-group "rg1" --service-name \\
               "apimService1" --notification-name "RequestPublisherNotificationMessage" --email \\
               "contoso@live.com"
"""

helps['apimgmt notification recipientemail list'] = """
    type: command
    short-summary: list a apimgmt notification recipientemail.
# list_by_notification -- list
"""

helps['apimgmt openidconnectprovider'] = """
    type: group
    short-summary: Commands to manage OpenIdConnectProvider.
"""

helps['apimgmt openidconnectprovider create'] = """
    type: command
    short-summary: create a apimgmt openidconnectprovider.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateOpenIdConnectProvider
        text: |-
               az apimgmt openidconnectprovider create --resource-group "rg1" --service-name \\
               "apimService1" --opid "templateOpenIdConnect3" --display-name "templateoidprovider3" \\
               --metadata-endpoint "https://oidprovider-template3.net" --client-id \\
               "oidprovidertemplate3"
"""

helps['apimgmt openidconnectprovider update'] = """
    type: command
    short-summary: update a apimgmt openidconnectprovider.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateOpenIdConnectProvider
        text: |-
               az apimgmt openidconnectprovider update --resource-group "rg1" --service-name \\
               "apimService1" --opid "templateOpenIdConnect2" --client-secret "updatedsecret"
"""

helps['apimgmt openidconnectprovider delete'] = """
    type: command
    short-summary: delete a apimgmt openidconnectprovider.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteOpenIdConnectProvider
        text: |-
               az apimgmt openidconnectprovider delete --resource-group "rg1" --service-name \\
               "apimService1" --opid "templateOpenIdConnect3"
"""

helps['apimgmt openidconnectprovider list'] = """
    type: command
    short-summary: list a apimgmt openidconnectprovider.
# list_by_service -- list
"""

helps['apimgmt openidconnectprovider show'] = """
    type: command
    short-summary: show a apimgmt openidconnectprovider.
# get -- show
"""

helps['apimgmt policy'] = """
    type: group
    short-summary: Commands to manage Policy.
"""

helps['apimgmt policy create'] = """
    type: command
    short-summary: create a apimgmt policy.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreatePolicy
        text: |-
               az apimgmt policy create --resource-group "rg1" --service-name "apimService1" --policy-id \\
               "policy" --value "<policies>\\r\\n  <inbound />\\r\\n  <backend>\\r\\n    <forward-request
                />\\r\\n  </backend>\\r\\n  <outbound />\\r\\n</policies>" --format "xml"
"""

helps['apimgmt policy update'] = """
    type: command
    short-summary: update a apimgmt policy.
# create_or_update -- update
"""

helps['apimgmt policy delete'] = """
    type: command
    short-summary: delete a apimgmt policy.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeletePolicy
        text: |-
               az apimgmt policy delete --resource-group "rg1" --service-name "apimService1" --policy-id \\
               "policy"
"""

helps['apimgmt policy list'] = """
    type: command
    short-summary: list a apimgmt policy.
# list_by_service -- list
"""

helps['apimgmt policy show'] = """
    type: command
    short-summary: show a apimgmt policy.
# get -- show
"""

helps['apimgmt portalsetting signin'] = """
    type: group
    short-summary: Commands to manage SignInSetting.
"""

helps['apimgmt portalsetting signin create'] = """
    type: command
    short-summary: create a apimgmt portalsetting signin.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: |-
               az apimgmt portalsetting signin create --resource-group "rg1" --name "apimService1" \\
               --enabled true
"""

helps['apimgmt portalsetting signin update'] = """
    type: command
    short-summary: update a apimgmt portalsetting signin.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: |-
               az apimgmt portalsetting signin update --resource-group "rg1" --name "apimService1" \\
               --enabled true
"""

helps['apimgmt portalsetting signin show'] = """
    type: command
    short-summary: show a apimgmt portalsetting signin.
# get -- show
"""

helps['apimgmt portalsetting signup'] = """
    type: group
    short-summary: Commands to manage SignUpSetting.
"""

helps['apimgmt portalsetting signup create'] = """
    type: command
    short-summary: create a apimgmt portalsetting signup.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: |-
               az apimgmt portalsetting signup create --resource-group "rg1" --name "apimService1" \\
               --enabled true
"""

helps['apimgmt portalsetting signup update'] = """
    type: command
    short-summary: update a apimgmt portalsetting signup.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: |-
               az apimgmt portalsetting signup update --resource-group "rg1" --name "apimService1" \\
               --enabled true
"""

helps['apimgmt portalsetting signup show'] = """
    type: command
    short-summary: show a apimgmt portalsetting signup.
# get -- show
"""

helps['apimgmt portalsetting delegation'] = """
    type: group
    short-summary: Commands to manage DelegationSetting.
"""

helps['apimgmt portalsetting delegation create'] = """
    type: command
    short-summary: create a apimgmt portalsetting delegation.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: |-
               az apimgmt portalsetting delegation create --resource-group "rg1" --name "apimService1" \\
               --url "http://contoso.com/delegation" --validation-key "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7
               o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q=="
"""

helps['apimgmt portalsetting delegation update'] = """
    type: command
    short-summary: update a apimgmt portalsetting delegation.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: |-
               az apimgmt portalsetting delegation update --resource-group "rg1" --name "apimService1" \\
               --url "http://contoso.com/delegation" --validation-key "nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7
               o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q=="
"""

helps['apimgmt portalsetting delegation show'] = """
    type: command
    short-summary: show a apimgmt portalsetting delegation.
# get -- show
"""

helps['apimgmt product'] = """
    type: group
    short-summary: Commands to manage Product.
"""

helps['apimgmt product create'] = """
    type: command
    short-summary: create a apimgmt product.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateProduct
        text: |-
               az apimgmt product create --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --display-name "Test Template ProductName 4"
"""

helps['apimgmt product update'] = """
    type: command
    short-summary: update a apimgmt product.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateProduct
        text: |-
               az apimgmt product update --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --display-name "Test Template ProductName 4"
"""

helps['apimgmt product delete'] = """
    type: command
    short-summary: delete a apimgmt product.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteProduct
        text: |-
               az apimgmt product delete --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct"
"""

helps['apimgmt product list'] = """
    type: command
    short-summary: list a apimgmt product.
# list_by_tags -- list
# list_by_service -- list
"""

helps['apimgmt product show'] = """
    type: command
    short-summary: show a apimgmt product.
# get -- show
"""

helps['apimgmt product api'] = """
    type: group
    short-summary: Commands to manage ProductApi.
"""

helps['apimgmt product api create'] = """
    type: command
    short-summary: create a apimgmt product api.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateProductApi
        text: |-
               az apimgmt product api create --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --api-id "echo-api"
"""

helps['apimgmt product api update'] = """
    type: command
    short-summary: update a apimgmt product api.
# create_or_update -- update
"""

helps['apimgmt product api delete'] = """
    type: command
    short-summary: delete a apimgmt product api.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteProductApi
        text: |-
               az apimgmt product api delete --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --api-id "echo-api"
"""

helps['apimgmt product api list'] = """
    type: command
    short-summary: list a apimgmt product api.
# list_by_product -- list
"""

helps['apimgmt product group'] = """
    type: group
    short-summary: Commands to manage ProductGroup.
"""

helps['apimgmt product group create'] = """
    type: command
    short-summary: create a apimgmt product group.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateProductGroup
        text: |-
               az apimgmt product group create --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --group-id "templateGroup"
"""

helps['apimgmt product group update'] = """
    type: command
    short-summary: update a apimgmt product group.
# create_or_update -- update
"""

helps['apimgmt product group delete'] = """
    type: command
    short-summary: delete a apimgmt product group.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteProductGroup
        text: |-
               az apimgmt product group delete --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --group-id "templateGroup"
"""

helps['apimgmt product group list'] = """
    type: command
    short-summary: list a apimgmt product group.
# list_by_product -- list
"""

helps['apimgmt product policy'] = """
    type: group
    short-summary: Commands to manage ProductPolicy.
"""

helps['apimgmt product policy create'] = """
    type: command
    short-summary: create a apimgmt product policy.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateProductPolicy
        text: |-
               az apimgmt product policy create --resource-group "rg1" --service-name "apimService1" \\
               --product-id "5702e97e5157a50f48dce801" --policy-id "policy" --value "<policies>\\r\\n  <i
               nbound>\\r\\n    <rate-limit calls=\"{{call-count}}\" renewal-period=\"15\"></rate-limit>\
               \r\\n    <log-to-eventhub logger-id=\"16\">\\r\\n                      @( string.Join(\",\
               ", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpA
               ddress, context.Operation.Name) ) \\r\\n                  </log-to-eventhub>\\r\\n    <quo
               ta-by-key calls=\"40\" counter-key=\"cc\" renewal-period=\"3600\" increment-count=\"@(cont
               ext.Request.Method == &quot;POST&quot; ? 1:2)\" />\\r\\n    <base />\\r\\n  </inbound>\\r\
               \n  <backend>\\r\\n    <base />\\r\\n  </backend>\\r\\n  <outbound>\\r\\n    <base />\\r\\
               n  </outbound>\\r\\n</policies>" --format "xml"
"""

helps['apimgmt product policy update'] = """
    type: command
    short-summary: update a apimgmt product policy.
# create_or_update -- update
"""

helps['apimgmt product policy delete'] = """
    type: command
    short-summary: delete a apimgmt product policy.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteProductPolicy
        text: |-
               az apimgmt product policy delete --resource-group "rg1" --service-name "apimService1" \\
               --product-id "testproduct" --policy-id "policy"
"""

helps['apimgmt product policy list'] = """
    type: command
    short-summary: list a apimgmt product policy.
# list_by_product -- list
"""

helps['apimgmt product policy show'] = """
    type: command
    short-summary: show a apimgmt product policy.
# get -- show
"""

helps['apimgmt property'] = """
    type: group
    short-summary: Commands to manage Property.
"""

helps['apimgmt property create'] = """
    type: command
    short-summary: create a apimgmt property.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateProperty
        text: |-
               az apimgmt property create --resource-group "rg1" --service-name "apimService1" --prop-id \\
               "testprop2" --secret true --display-name "prop3name" --value "propValue"
"""

helps['apimgmt property update'] = """
    type: command
    short-summary: update a apimgmt property.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateProperty
        text: |-
               az apimgmt property update --resource-group "rg1" --service-name "apimService1" --prop-id \\
               "testprop2" --secret true
"""

helps['apimgmt property delete'] = """
    type: command
    short-summary: delete a apimgmt property.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteProperty
        text: |-
               az apimgmt property delete --resource-group "rg1" --service-name "apimService1" --prop-id \\
               "testprop2"
"""

helps['apimgmt property list'] = """
    type: command
    short-summary: list a apimgmt property.
# list_by_service -- list
"""

helps['apimgmt property show'] = """
    type: command
    short-summary: show a apimgmt property.
# get -- show
"""

helps['apimgmt subscription'] = """
    type: group
    short-summary: Commands to manage Subscription.
"""

helps['apimgmt subscription create'] = """
    type: command
    short-summary: create a apimgmt subscription.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateSubscription
        text: |-
               az apimgmt subscription create --resource-group "rg1" --service-name "apimService1" --sid \\
               "testsub" --owner-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_grou
               p }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}" \\
               --scope "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/provider
               s/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }}" \\
               --display-name "testsub"
"""

helps['apimgmt subscription update'] = """
    type: command
    short-summary: update a apimgmt subscription.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateSubscription
        text: |-
               az apimgmt subscription update --resource-group "rg1" --service-name "apimService1" --sid \\
               "testsub" --display-name "testsub"
"""

helps['apimgmt subscription delete'] = """
    type: command
    short-summary: delete a apimgmt subscription.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteSubscription
        text: |-
               az apimgmt subscription delete --resource-group "rg1" --service-name "apimService1" --sid \\
               "testsub"
"""

helps['apimgmt subscription list'] = """
    type: command
    short-summary: list a apimgmt subscription.
# list -- list
"""

helps['apimgmt subscription show'] = """
    type: command
    short-summary: show a apimgmt subscription.
# get -- show
"""

helps['apimgmt user'] = """
    type: group
    short-summary: Commands to manage User.
"""

helps['apimgmt user create'] = """
    type: command
    short-summary: create a apimgmt user.
# create_or_update -- create
    examples:
# create
      - name: ApiManagementCreateUser
        text: |-
               az apimgmt user create --resource-group "rg1" --service-name "apimService1" --user-id \\
               "5931a75ae4bbd512288c680b" --email "foobar@outlook.com" --first-name "foo" --last-name \\
               "bar" --confirmation "signup"
"""

helps['apimgmt user update'] = """
    type: command
    short-summary: update a apimgmt user.
# create_or_update -- update
    examples:
# update
      - name: ApiManagementUpdateUser
        text: |-
               az apimgmt user update --resource-group "rg1" --service-name "apimService1" --user-id \\
               "5931a75ae4bbd512288c680b" --email "foobar@outlook.com" --first-name "foo" --last-name \\
               "bar"
"""

helps['apimgmt user delete'] = """
    type: command
    short-summary: delete a apimgmt user.
# delete -- delete
    examples:
# delete
      - name: ApiManagementDeleteUser
        text: |-
               az apimgmt user delete --resource-group "rg1" --service-name "apimService1" --user-id \\
               "5931a75ae4bbd512288c680b"
"""

helps['apimgmt user list'] = """
    type: command
    short-summary: list a apimgmt user.
# list_by_service -- list
"""

helps['apimgmt user show'] = """
    type: command
    short-summary: show a apimgmt user.
# get -- show
"""
