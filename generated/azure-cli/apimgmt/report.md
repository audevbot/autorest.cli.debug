# Azure CLI Module Creation Report

# ApiManagementCreateApiUsingOai3Import
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id petstore --path petstore --value https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml --format openapi-link
# ApiManagementCreateApiUsingSwaggerImport
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id petstore --path petstore --value http://petstore.swagger.io/v2/swagger.json --format swagger-link-json
# ApiManagementCreateApiUsingWadlImport
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id petstore --path collector --value https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl --format wadl-link-json
# ApiManagementCreateSoapToRestApiUsingWsdlImport
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id soapApi --path currency --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL --format wsdl-link
# ApiManagementCreateSoapPassThroughApiUsingWsdlImport
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id soapApi --path currency --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL --format wsdl-link --api_type soap
# ApiManagementCreateApi
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id tempgroup --description apidescription5200 --display_name apiname1463 --service_url http://newechoapi.cloudapp.net/api --path newapiPath
# ApiManagementCreateApiRevisionFromExistingApi
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id echo-api;rev=3 --api_revision_description Creating a Revision of an existing API --source_api_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }} --service_url http://echoapi.cloudapp.net/apiv3 --path echo
# ApiManagementCreateApiNewVersionUsingExistingApi
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id echoapiv3 --description Create Echo API into a new Version using Existing Version Set and Copy all Operations. --api_version v4 --is_current true --api_version_set_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }} --subscription_required true --source_api_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }} --display_name Echo API2 --service_url http://echoapi.cloudapp.net/api --path echo2
# ApiManagementCreateApiClone
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id echo-api2 --description Copy of Existing Echo Api including Operations. --is_current true --subscription_required true --source_api_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }} --display_name Echo API2 --service_url http://echoapi.cloudapp.net/api --path echo2
# ApiManagementCreateApiWithOpenIdConnect
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id tempgroup --description This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters. --display_name Swagger Petstore --service_url http://petstore.swagger.io/v2 --path petstore
# ApiManagementUpdateApi
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id echo-api --display_name Echo API New --service_url http://echoapi.cloudapp.net/api2 --path newecho
# ApiManagementDeleteApi
apimgmt api create  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementCreateApiUsingOai3Import
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id petstore --path petstore --value https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml --format openapi-link
# ApiManagementCreateApiUsingSwaggerImport
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id petstore --path petstore --value http://petstore.swagger.io/v2/swagger.json --format swagger-link-json
# ApiManagementCreateApiUsingWadlImport
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id petstore --path collector --value https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl --format wadl-link-json
# ApiManagementCreateSoapToRestApiUsingWsdlImport
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id soapApi --path currency --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL --format wsdl-link
# ApiManagementCreateSoapPassThroughApiUsingWsdlImport
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id soapApi --path currency --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL --format wsdl-link --api_type soap
# ApiManagementCreateApi
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id tempgroup --description apidescription5200 --display_name apiname1463 --service_url http://newechoapi.cloudapp.net/api --path newapiPath
# ApiManagementCreateApiRevisionFromExistingApi
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id echo-api;rev=3 --api_revision_description Creating a Revision of an existing API --source_api_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }} --service_url http://echoapi.cloudapp.net/apiv3 --path echo
# ApiManagementCreateApiNewVersionUsingExistingApi
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id echoapiv3 --description Create Echo API into a new Version using Existing Version Set and Copy all Operations. --api_version v4 --is_current true --api_version_set_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }} --subscription_required true --source_api_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }} --display_name Echo API2 --service_url http://echoapi.cloudapp.net/api --path echo2
# ApiManagementCreateApiClone
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id echo-api2 --description Copy of Existing Echo Api including Operations. --is_current true --subscription_required true --source_api_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }} --display_name Echo API2 --service_url http://echoapi.cloudapp.net/api --path echo2
# ApiManagementCreateApiWithOpenIdConnect
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id tempgroup --description This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters. --display_name Swagger Petstore --service_url http://petstore.swagger.io/v2 --path petstore
# ApiManagementUpdateApi
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id echo-api --display_name Echo API New --service_url http://echoapi.cloudapp.net/api2 --path newecho
# ApiManagementDeleteApi
apimgmt api update  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementCreateApiUsingOai3Import
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id petstore
# ApiManagementCreateApiUsingSwaggerImport
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id petstore
# ApiManagementCreateApiUsingWadlImport
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id petstore
# ApiManagementCreateSoapToRestApiUsingWsdlImport
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id soapApi
# ApiManagementCreateSoapPassThroughApiUsingWsdlImport
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id soapApi
# ApiManagementCreateApi
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id tempgroup
# ApiManagementCreateApiRevisionFromExistingApi
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id echo-api;rev=3
# ApiManagementCreateApiNewVersionUsingExistingApi
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id echoapiv3
# ApiManagementCreateApiClone
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id echo-api2
# ApiManagementCreateApiWithOpenIdConnect
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id tempgroup
# ApiManagementUpdateApi
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementDeleteApi
apimgmt api delete  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementCreateApiUsingOai3Import
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiUsingSwaggerImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiUsingWadlImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateSoapToRestApiUsingWsdlImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateSoapPassThroughApiUsingWsdlImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiRevisionFromExistingApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiNewVersionUsingExistingApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiClone
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiWithOpenIdConnect
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiUsingOai3Import
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiUsingSwaggerImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiUsingWadlImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateSoapToRestApiUsingWsdlImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateSoapPassThroughApiUsingWsdlImport
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiRevisionFromExistingApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiNewVersionUsingExistingApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiClone
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiWithOpenIdConnect
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteApi
apimgmt api list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiUsingOai3Import
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id petstore
# ApiManagementCreateApiUsingSwaggerImport
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id petstore
# ApiManagementCreateApiUsingWadlImport
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id petstore
# ApiManagementCreateSoapToRestApiUsingWsdlImport
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id soapApi
# ApiManagementCreateSoapPassThroughApiUsingWsdlImport
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id soapApi
# ApiManagementCreateApi
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id tempgroup
# ApiManagementCreateApiRevisionFromExistingApi
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id echo-api;rev=3
# ApiManagementCreateApiNewVersionUsingExistingApi
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id echoapiv3
# ApiManagementCreateApiClone
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id echo-api2
# ApiManagementCreateApiWithOpenIdConnect
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id tempgroup
# ApiManagementUpdateApi
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementDeleteApi
apimgmt api show  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementCreateApiRelease
apimgmt api release create  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev --notes yahooagain
# ApiManagementUpdateApiRelease
apimgmt api release create  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev --notes yahooagain
# ApiManagementDeleteApiRelease
apimgmt api release create  --resource_group rg1 --service_name apimService1 --api_id 5a5fcc09124a7fa9b89f2f1d --release_id testrev
# ApiManagementCreateApiRelease
apimgmt api release update  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev --notes yahooagain
# ApiManagementUpdateApiRelease
apimgmt api release update  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev --notes yahooagain
# ApiManagementDeleteApiRelease
apimgmt api release update  --resource_group rg1 --service_name apimService1 --api_id 5a5fcc09124a7fa9b89f2f1d --release_id testrev
# ApiManagementCreateApiRelease
apimgmt api release delete  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev
# ApiManagementUpdateApiRelease
apimgmt api release delete  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev
# ApiManagementDeleteApiRelease
apimgmt api release delete  --resource_group rg1 --service_name apimService1 --api_id 5a5fcc09124a7fa9b89f2f1d --release_id testrev
# ApiManagementCreateApiRelease
apimgmt api release list  --resource_group rg1 --service_name apimService1 --api_id a1
# ApiManagementUpdateApiRelease
apimgmt api release list  --resource_group rg1 --service_name apimService1 --api_id a1
# ApiManagementDeleteApiRelease
apimgmt api release list  --resource_group rg1 --service_name apimService1 --api_id 5a5fcc09124a7fa9b89f2f1d
# ApiManagementCreateApiRelease
apimgmt api release show  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev
# ApiManagementUpdateApiRelease
apimgmt api release show  --resource_group rg1 --service_name apimService1 --api_id a1 --release_id testrev
# ApiManagementDeleteApiRelease
apimgmt api release show  --resource_group rg1 --service_name apimService1 --api_id 5a5fcc09124a7fa9b89f2f1d --release_id testrev
# ApiManagementCreateApiOperation
apimgmt api operation create  --resource_group rg1 --service_name apimService1 --api_id PetStoreTemplate2 --operation_id newoperations --description This can only be done by the logged in user. --display_name createUser2 --method POST --url_template /user1
# ApiManagementUpdateApiOperation
apimgmt api operation create  --resource_group rg1 --service_name apimService1 --api_id echo-api --operation_id operationId --display_name Retrieve resource --method GET --url_template /resource
# ApiManagementDeleteApiOperation
apimgmt api operation create  --resource_group rg1 --service_name apimService1 --api_id 57d2ef278aa04f0888cba3f3 --operation_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiOperation
apimgmt api operation update  --resource_group rg1 --service_name apimService1 --api_id PetStoreTemplate2 --operation_id newoperations --description This can only be done by the logged in user. --display_name createUser2 --method POST --url_template /user1
# ApiManagementUpdateApiOperation
apimgmt api operation update  --resource_group rg1 --service_name apimService1 --api_id echo-api --operation_id operationId --display_name Retrieve resource --method GET --url_template /resource
# ApiManagementDeleteApiOperation
apimgmt api operation update  --resource_group rg1 --service_name apimService1 --api_id 57d2ef278aa04f0888cba3f3 --operation_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiOperation
apimgmt api operation delete  --resource_group rg1 --service_name apimService1 --api_id PetStoreTemplate2 --operation_id newoperations
# ApiManagementUpdateApiOperation
apimgmt api operation delete  --resource_group rg1 --service_name apimService1 --api_id echo-api --operation_id operationId
# ApiManagementDeleteApiOperation
apimgmt api operation delete  --resource_group rg1 --service_name apimService1 --api_id 57d2ef278aa04f0888cba3f3 --operation_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiOperation
apimgmt api operation list  --resource_group rg1 --service_name apimService1 --api_id PetStoreTemplate2
# ApiManagementUpdateApiOperation
apimgmt api operation list  --resource_group rg1 --service_name apimService1 --api_id echo-api
# ApiManagementDeleteApiOperation
apimgmt api operation list  --resource_group rg1 --service_name apimService1 --api_id 57d2ef278aa04f0888cba3f3
# ApiManagementCreateApiOperation
apimgmt api operation show  --resource_group rg1 --service_name apimService1 --api_id PetStoreTemplate2 --operation_id newoperations
# ApiManagementUpdateApiOperation
apimgmt api operation show  --resource_group rg1 --service_name apimService1 --api_id echo-api --operation_id operationId
# ApiManagementDeleteApiOperation
apimgmt api operation show  --resource_group rg1 --service_name apimService1 --api_id 57d2ef278aa04f0888cba3f3 --operation_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiOperationPolicy
apimgmt api operation policy create  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --operation_id 5600b57e7e8880006a080001 --policy_id policy --value <policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies> --format xml
# ApiManagementDeleteApiOperationPolicy
apimgmt api operation policy create  --resource_group rg1 --service_name apimService1 --api_id testapi --operation_id testoperation --policy_id policy
# ApiManagementCreateApiOperationPolicy
apimgmt api operation policy update  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --operation_id 5600b57e7e8880006a080001 --policy_id policy --value <policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies> --format xml
# ApiManagementDeleteApiOperationPolicy
apimgmt api operation policy update  --resource_group rg1 --service_name apimService1 --api_id testapi --operation_id testoperation --policy_id policy
# ApiManagementCreateApiOperationPolicy
apimgmt api operation policy delete  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --operation_id 5600b57e7e8880006a080001 --policy_id policy
# ApiManagementDeleteApiOperationPolicy
apimgmt api operation policy delete  --resource_group rg1 --service_name apimService1 --api_id testapi --operation_id testoperation --policy_id policy
# ApiManagementCreateApiOperationPolicy
apimgmt api operation policy list  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --operation_id 5600b57e7e8880006a080001
# ApiManagementDeleteApiOperationPolicy
apimgmt api operation policy list  --resource_group rg1 --service_name apimService1 --api_id testapi --operation_id testoperation
# ApiManagementCreateApiOperationPolicy
apimgmt api operation policy show  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --operation_id 5600b57e7e8880006a080001 --format xml --policy_id policy
# ApiManagementDeleteApiOperationPolicy
apimgmt api operation policy show  --resource_group rg1 --service_name apimService1 --api_id testapi --operation_id testoperation --policy_id policy
# ApiManagementCreateTag
apimgmt tag create  --resource_group rg1 --service_name apimService1 --tag_id tagId1 --display_name tag1
# ApiManagementUpdateTag
apimgmt tag create  --resource_group rg1 --service_name apimService1 --tag_id temptag --display_name temp tag
# ApiManagementDeleteTag
apimgmt tag create  --resource_group rg1 --service_name apimService1 --tag_id tagId1
# ApiManagementCreateTag
apimgmt tag update  --resource_group rg1 --service_name apimService1 --tag_id tagId1 --display_name tag1
# ApiManagementUpdateTag
apimgmt tag update  --resource_group rg1 --service_name apimService1 --tag_id temptag --display_name temp tag
# ApiManagementDeleteTag
apimgmt tag update  --resource_group rg1 --service_name apimService1 --tag_id tagId1
# ApiManagementCreateTag
apimgmt tag delete  --resource_group rg1 --service_name apimService1 --tag_id tagId1
# ApiManagementUpdateTag
apimgmt tag delete  --resource_group rg1 --service_name apimService1 --tag_id temptag
# ApiManagementDeleteTag
apimgmt tag delete  --resource_group rg1 --service_name apimService1 --tag_id tagId1
# ApiManagementCreateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteTag
apimgmt tag list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateTag
apimgmt tag show  --resource_group rg1 --service_name apimService1 --tag_id tagId1
# ApiManagementUpdateTag
apimgmt tag show  --resource_group rg1 --service_name apimService1 --tag_id temptag
# ApiManagementDeleteTag
apimgmt tag show  --resource_group rg1 --service_name apimService1 --tag_id tagId1
# ApiManagementCreateApiPolicy
apimgmt api policy create  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy --value <policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies> --format xml
# ApiManagementCreateApiPolicyNonXmlEncoded
apimgmt api policy create  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy --value <policies>
     <inbound>
     <base />
  <set-header name="newvalue" exists-action="override">
   <value>"@(context.Request.Headers.FirstOrDefault(h => h.Ke=="Via"))" </value>
    </set-header>
  </inbound>
      </policies> --format rawxml
# ApiManagementDeleteApiPolicy
apimgmt api policy create  --resource_group rg1 --service_name apimService1 --api_id loggerId --policy_id policy
# ApiManagementCreateApiPolicy
apimgmt api policy update  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy --value <policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies> --format xml
# ApiManagementCreateApiPolicyNonXmlEncoded
apimgmt api policy update  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy --value <policies>
     <inbound>
     <base />
  <set-header name="newvalue" exists-action="override">
   <value>"@(context.Request.Headers.FirstOrDefault(h => h.Ke=="Via"))" </value>
    </set-header>
  </inbound>
      </policies> --format rawxml
# ApiManagementDeleteApiPolicy
apimgmt api policy update  --resource_group rg1 --service_name apimService1 --api_id loggerId --policy_id policy
# ApiManagementCreateApiPolicy
apimgmt api policy delete  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy
# ApiManagementCreateApiPolicyNonXmlEncoded
apimgmt api policy delete  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy
# ApiManagementDeleteApiPolicy
apimgmt api policy delete  --resource_group rg1 --service_name apimService1 --api_id loggerId --policy_id policy
# ApiManagementCreateApiPolicy
apimgmt api policy list  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001
# ApiManagementCreateApiPolicyNonXmlEncoded
apimgmt api policy list  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001
# ApiManagementDeleteApiPolicy
apimgmt api policy list  --resource_group rg1 --service_name apimService1 --api_id loggerId
# ApiManagementCreateApiPolicy
apimgmt api policy show  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy --format xml
# ApiManagementCreateApiPolicyNonXmlEncoded
apimgmt api policy show  --resource_group rg1 --service_name apimService1 --api_id 5600b57e7e8880006a040001 --policy_id policy --format rawxml
# ApiManagementDeleteApiPolicy
apimgmt api policy show  --resource_group rg1 --service_name apimService1 --api_id loggerId --policy_id policy
# ApiManagementCreateApiSchema
apimgmt api schema create  --resource_group rg1 --service_name apimService1 --api_id 59d6bb8f1f7fab13dc67ec9b --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1 --content_type application/vnd.ms-azure-apim.xsd+xml
# ApiManagementDeleteApiSchema
apimgmt api schema create  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --schema_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiSchema
apimgmt api schema update  --resource_group rg1 --service_name apimService1 --api_id 59d6bb8f1f7fab13dc67ec9b --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1 --content_type application/vnd.ms-azure-apim.xsd+xml
# ApiManagementDeleteApiSchema
apimgmt api schema update  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --schema_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiSchema
apimgmt api schema delete  --resource_group rg1 --service_name apimService1 --api_id 59d6bb8f1f7fab13dc67ec9b --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
# ApiManagementDeleteApiSchema
apimgmt api schema delete  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --schema_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiSchema
apimgmt api schema list  --resource_group rg1 --service_name apimService1 --api_id 59d6bb8f1f7fab13dc67ec9b
# ApiManagementDeleteApiSchema
apimgmt api schema list  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650
# ApiManagementCreateApiSchema
apimgmt api schema show  --resource_group rg1 --service_name apimService1 --api_id 59d6bb8f1f7fab13dc67ec9b --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
# ApiManagementDeleteApiSchema
apimgmt api schema show  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --schema_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiDiagnostic
apimgmt api diagnostic create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/applicationinsights
# ApiManagementUpdateApiDiagnostic
apimgmt api diagnostic create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/applicationinsights
# ApiManagementDeleteApiDiagnostic
apimgmt api diagnostic create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementCreateApiDiagnostic
apimgmt api diagnostic update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/applicationinsights
# ApiManagementUpdateApiDiagnostic
apimgmt api diagnostic update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/applicationinsights
# ApiManagementDeleteApiDiagnostic
apimgmt api diagnostic update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementCreateApiDiagnostic
apimgmt api diagnostic delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementUpdateApiDiagnostic
apimgmt api diagnostic delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementDeleteApiDiagnostic
apimgmt api diagnostic delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementCreateApiDiagnostic
apimgmt api diagnostic list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a
# ApiManagementUpdateApiDiagnostic
apimgmt api diagnostic list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a
# ApiManagementDeleteApiDiagnostic
apimgmt api diagnostic list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a
# ApiManagementCreateApiDiagnostic
apimgmt api diagnostic show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementUpdateApiDiagnostic
apimgmt api diagnostic show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementDeleteApiDiagnostic
apimgmt api diagnostic show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --diagnostic_id applicationinsights
# ApiManagementCreateApiIssue
apimgmt api issue create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --created_date 2018-02-01T22:21:20.467Z --state open --title New API issue --description New API issue description --user_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}
# ApiManagementUpdateApiIssue
apimgmt api issue create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --state closed
# ApiManagementDeleteApiIssue
apimgmt api issue create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiIssue
apimgmt api issue update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --created_date 2018-02-01T22:21:20.467Z --state open --title New API issue --description New API issue description --user_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}
# ApiManagementUpdateApiIssue
apimgmt api issue update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --state closed
# ApiManagementDeleteApiIssue
apimgmt api issue update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiIssue
apimgmt api issue delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementUpdateApiIssue
apimgmt api issue delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementDeleteApiIssue
apimgmt api issue delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiIssue
apimgmt api issue list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a
# ApiManagementUpdateApiIssue
apimgmt api issue list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a
# ApiManagementDeleteApiIssue
apimgmt api issue list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a
# ApiManagementCreateApiIssue
apimgmt api issue show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementUpdateApiIssue
apimgmt api issue show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementDeleteApiIssue
apimgmt api issue show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiIssueComment
apimgmt api issue comment create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb --text Issue comment. --created_date 2018-02-01T22:21:20.467Z --user_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}
# ApiManagementDeleteApiIssueComment
apimgmt api issue comment create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb
# ApiManagementCreateApiIssueComment
apimgmt api issue comment update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb --text Issue comment. --created_date 2018-02-01T22:21:20.467Z --user_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}
# ApiManagementDeleteApiIssueComment
apimgmt api issue comment update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb
# ApiManagementCreateApiIssueComment
apimgmt api issue comment delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb
# ApiManagementDeleteApiIssueComment
apimgmt api issue comment delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb
# ApiManagementCreateApiIssueComment
apimgmt api issue comment list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementDeleteApiIssueComment
apimgmt api issue comment list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiIssueComment
apimgmt api issue comment show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb
# ApiManagementDeleteApiIssueComment
apimgmt api issue comment show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --comment_id 599e29ab193c3c0bd0b3e2fb
# ApiManagementCreateApiIssueAttachment
apimgmt api issue attachment create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3 --title Issue attachment. --content_format image/jpeg --content IEJhc2U2NA==
# ApiManagementDeleteApiIssueAttachment
apimgmt api issue attachment create  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3
# ApiManagementCreateApiIssueAttachment
apimgmt api issue attachment update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3 --title Issue attachment. --content_format image/jpeg --content IEJhc2U2NA==
# ApiManagementDeleteApiIssueAttachment
apimgmt api issue attachment update  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3
# ApiManagementCreateApiIssueAttachment
apimgmt api issue attachment delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3
# ApiManagementDeleteApiIssueAttachment
apimgmt api issue attachment delete  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3
# ApiManagementCreateApiIssueAttachment
apimgmt api issue attachment list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementDeleteApiIssueAttachment
apimgmt api issue attachment list  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc
# ApiManagementCreateApiIssueAttachment
apimgmt api issue attachment show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3
# ApiManagementDeleteApiIssueAttachment
apimgmt api issue attachment show  --resource_group rg1 --service_name apimService1 --api_id 57d1f7558aa04f15146d9d8a --issue_id 57d2ef278aa04f0ad01d6cdc --attachment_id 57d2ef278aa04f0888cba3f3
# ApiManagementCreateApiTagDescription
apimgmt api tagdescription create  --resource_group rg1 --service_name apimService1 --api_id 5931a75ae4bbd512a88c680b --tag_id tagId1 --description Some description that will be displayed for operation's tag if the tag is assigned to operation of the API --external_docs_url http://some.url/additionaldoc --external_docs_description Description of the external docs resource
# ApiManagementDeleteApiTagDescription
apimgmt api tagdescription create  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --tag_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiTagDescription
apimgmt api tagdescription update  --resource_group rg1 --service_name apimService1 --api_id 5931a75ae4bbd512a88c680b --tag_id tagId1 --description Some description that will be displayed for operation's tag if the tag is assigned to operation of the API --external_docs_url http://some.url/additionaldoc --external_docs_description Description of the external docs resource
# ApiManagementDeleteApiTagDescription
apimgmt api tagdescription update  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --tag_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiTagDescription
apimgmt api tagdescription delete  --resource_group rg1 --service_name apimService1 --api_id 5931a75ae4bbd512a88c680b --tag_id tagId1
# ApiManagementDeleteApiTagDescription
apimgmt api tagdescription delete  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --tag_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiTagDescription
apimgmt api tagdescription list  --resource_group rg1 --service_name apimService1 --api_id 5931a75ae4bbd512a88c680b
# ApiManagementDeleteApiTagDescription
apimgmt api tagdescription list  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650
# ApiManagementCreateApiTagDescription
apimgmt api tagdescription show  --resource_group rg1 --service_name apimService1 --api_id 5931a75ae4bbd512a88c680b --tag_id tagId1
# ApiManagementDeleteApiTagDescription
apimgmt api tagdescription show  --resource_group rg1 --service_name apimService1 --api_id 59d5b28d1f7fab116c282650 --tag_id 59d5b28e1f7fab116402044e
# ApiManagementCreateApiVersionSet
apimgmt apiversionset create  --resource_group rg1 --service_name apimService1 --version_set_id api1 --description Version configuration --display_name api set 1 --versioning_scheme Segment
# ApiManagementUpdateApiVersionSet
apimgmt apiversionset create  --resource_group rg1 --service_name apimService1 --version_set_id api1 --description Version configuration --display_name api set 1 --versioning_scheme Segment
# ApiManagementDeleteApiVersionSet
apimgmt apiversionset create  --resource_group rg1 --service_name apimService1 --version_set_id a1
# ApiManagementCreateApiVersionSet
apimgmt apiversionset update  --resource_group rg1 --service_name apimService1 --version_set_id api1 --description Version configuration --display_name api set 1 --versioning_scheme Segment
# ApiManagementUpdateApiVersionSet
apimgmt apiversionset update  --resource_group rg1 --service_name apimService1 --version_set_id api1 --description Version configuration --display_name api set 1 --versioning_scheme Segment
# ApiManagementDeleteApiVersionSet
apimgmt apiversionset update  --resource_group rg1 --service_name apimService1 --version_set_id a1
# ApiManagementCreateApiVersionSet
apimgmt apiversionset delete  --resource_group rg1 --service_name apimService1 --version_set_id api1
# ApiManagementUpdateApiVersionSet
apimgmt apiversionset delete  --resource_group rg1 --service_name apimService1 --version_set_id api1
# ApiManagementDeleteApiVersionSet
apimgmt apiversionset delete  --resource_group rg1 --service_name apimService1 --version_set_id a1
# ApiManagementCreateApiVersionSet
apimgmt apiversionset list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateApiVersionSet
apimgmt apiversionset list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteApiVersionSet
apimgmt apiversionset list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateApiVersionSet
apimgmt apiversionset show  --resource_group rg1 --service_name apimService1 --version_set_id api1
# ApiManagementUpdateApiVersionSet
apimgmt apiversionset show  --resource_group rg1 --service_name apimService1 --version_set_id api1
# ApiManagementDeleteApiVersionSet
apimgmt apiversionset show  --resource_group rg1 --service_name apimService1 --version_set_id a1
# ApiManagementCreateAuthorizationServer
apimgmt authorizationserver create  --resource_group rg1 --service_name apimService1 --authsid newauthServer --description test server --token_endpoint https://www.contoso.com/oauth2/token --support_state true --default_scope read write --client_secret 2 --resource_owner_username un --resource_owner_password pwd --display_name test2 --client_registration_endpoint https://www.contoso.com/apps --authorization_endpoint https://www.contoso.com/oauth2/auth --client_id 1
# ApiManagementUpdateAuthorizationServer
apimgmt authorizationserver create  --resource_group rg1 --service_name apimService1 --authsid newauthServer --client_secret updated --client_id update
# ApiManagementDeleteAuthorizationServer
apimgmt authorizationserver create  --resource_group rg1 --service_name apimService1 --authsid newauthServer2
# ApiManagementCreateAuthorizationServer
apimgmt authorizationserver update  --resource_group rg1 --service_name apimService1 --authsid newauthServer --description test server --token_endpoint https://www.contoso.com/oauth2/token --support_state true --default_scope read write --client_secret 2 --resource_owner_username un --resource_owner_password pwd --display_name test2 --client_registration_endpoint https://www.contoso.com/apps --authorization_endpoint https://www.contoso.com/oauth2/auth --client_id 1
# ApiManagementUpdateAuthorizationServer
apimgmt authorizationserver update  --resource_group rg1 --service_name apimService1 --authsid newauthServer --client_secret updated --client_id update
# ApiManagementDeleteAuthorizationServer
apimgmt authorizationserver update  --resource_group rg1 --service_name apimService1 --authsid newauthServer2
# ApiManagementCreateAuthorizationServer
apimgmt authorizationserver delete  --resource_group rg1 --service_name apimService1 --authsid newauthServer
# ApiManagementUpdateAuthorizationServer
apimgmt authorizationserver delete  --resource_group rg1 --service_name apimService1 --authsid newauthServer
# ApiManagementDeleteAuthorizationServer
apimgmt authorizationserver delete  --resource_group rg1 --service_name apimService1 --authsid newauthServer2
# ApiManagementCreateAuthorizationServer
apimgmt authorizationserver list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateAuthorizationServer
apimgmt authorizationserver list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteAuthorizationServer
apimgmt authorizationserver list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateAuthorizationServer
apimgmt authorizationserver show  --resource_group rg1 --service_name apimService1 --authsid newauthServer
# ApiManagementUpdateAuthorizationServer
apimgmt authorizationserver show  --resource_group rg1 --service_name apimService1 --authsid newauthServer
# ApiManagementDeleteAuthorizationServer
apimgmt authorizationserver show  --resource_group rg1 --service_name apimService1 --authsid newauthServer2
# ApiManagementCreateBackendServiceFabric
apimgmt backend create  --resource_group rg1 --service_name apimService1 --backend_id sfbackend --description Service Fabric Test App 1 --url fabric:/mytestapp/mytestservice --protocol http
# ApiManagementCreateBackendProxyBackend
apimgmt backend create  --resource_group rg1 --service_name apimService1 --backend_id proxybackend --description description5308 --url https://backendname2644/ --protocol http
# ApiManagementUpdateBackend
apimgmt backend create  --resource_group rg1 --service_name apimService1 --backend_id proxybackend --description description5308
# ApiManagementDeleteBackend
apimgmt backend create  --resource_group rg1 --service_name apimService1 --backend_id sfbackend
# ApiManagementCreateBackendServiceFabric
apimgmt backend update  --resource_group rg1 --service_name apimService1 --backend_id sfbackend --description Service Fabric Test App 1 --url fabric:/mytestapp/mytestservice --protocol http
# ApiManagementCreateBackendProxyBackend
apimgmt backend update  --resource_group rg1 --service_name apimService1 --backend_id proxybackend --description description5308 --url https://backendname2644/ --protocol http
# ApiManagementUpdateBackend
apimgmt backend update  --resource_group rg1 --service_name apimService1 --backend_id proxybackend --description description5308
# ApiManagementDeleteBackend
apimgmt backend update  --resource_group rg1 --service_name apimService1 --backend_id sfbackend
# ApiManagementCreateBackendServiceFabric
apimgmt backend delete  --resource_group rg1 --service_name apimService1 --backend_id sfbackend
# ApiManagementCreateBackendProxyBackend
apimgmt backend delete  --resource_group rg1 --service_name apimService1 --backend_id proxybackend
# ApiManagementUpdateBackend
apimgmt backend delete  --resource_group rg1 --service_name apimService1 --backend_id proxybackend
# ApiManagementDeleteBackend
apimgmt backend delete  --resource_group rg1 --service_name apimService1 --backend_id sfbackend
# ApiManagementCreateBackendServiceFabric
apimgmt backend list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateBackendProxyBackend
apimgmt backend list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateBackend
apimgmt backend list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteBackend
apimgmt backend list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateBackendServiceFabric
apimgmt backend show  --resource_group rg1 --service_name apimService1 --backend_id sfbackend
# ApiManagementCreateBackendProxyBackend
apimgmt backend show  --resource_group rg1 --service_name apimService1 --backend_id proxybackend
# ApiManagementUpdateBackend
apimgmt backend show  --resource_group rg1 --service_name apimService1 --backend_id proxybackend
# ApiManagementDeleteBackend
apimgmt backend show  --resource_group rg1 --service_name apimService1 --backend_id sfbackend
# ApiManagementCreateCache
apimgmt cache create  --resource_group rg1 --service_name apimService1 --cache_id westindia --description Redis cache instances in West India --connection_string contoso5.redis.cache.windows.net,ssl=true,password=... --resource_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}
# ApiManagementUpdateCache
apimgmt cache create  --resource_group rg1 --service_name apimService1 --cache_id westindia --description Update Cache in west India
# ApiManagementDeleteCache
apimgmt cache create  --resource_group rg1 --service_name apimService1 --cache_id southindia
# ApiManagementCreateCache
apimgmt cache update  --resource_group rg1 --service_name apimService1 --cache_id westindia --description Redis cache instances in West India --connection_string contoso5.redis.cache.windows.net,ssl=true,password=... --resource_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}
# ApiManagementUpdateCache
apimgmt cache update  --resource_group rg1 --service_name apimService1 --cache_id westindia --description Update Cache in west India
# ApiManagementDeleteCache
apimgmt cache update  --resource_group rg1 --service_name apimService1 --cache_id southindia
# ApiManagementCreateCache
apimgmt cache delete  --resource_group rg1 --service_name apimService1 --cache_id westindia
# ApiManagementUpdateCache
apimgmt cache delete  --resource_group rg1 --service_name apimService1 --cache_id westindia
# ApiManagementDeleteCache
apimgmt cache delete  --resource_group rg1 --service_name apimService1 --cache_id southindia
# ApiManagementCreateCache
apimgmt cache list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateCache
apimgmt cache list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteCache
apimgmt cache list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateCache
apimgmt cache show  --resource_group rg1 --service_name apimService1 --cache_id westindia
# ApiManagementUpdateCache
apimgmt cache show  --resource_group rg1 --service_name apimService1 --cache_id westindia
# ApiManagementDeleteCache
apimgmt cache show  --resource_group rg1 --service_name apimService1 --cache_id southindia
# ApiManagementCreateCertificate
apimgmt certificate create  --resource_group rg1 --service_name apimService1 --certificate_id tempcert --data ****************Base 64 Encoded Certificate ******************************* --password ****Certificate Password******
# ApiManagementDeleteCertificate
apimgmt certificate create  --resource_group rg1 --service_name apimService1 --certificate_id tempcert
# ApiManagementCreateCertificate
apimgmt certificate update  --resource_group rg1 --service_name apimService1 --certificate_id tempcert --data ****************Base 64 Encoded Certificate ******************************* --password ****Certificate Password******
# ApiManagementDeleteCertificate
apimgmt certificate update  --resource_group rg1 --service_name apimService1 --certificate_id tempcert
# ApiManagementCreateCertificate
apimgmt certificate delete  --resource_group rg1 --service_name apimService1 --certificate_id tempcert
# ApiManagementDeleteCertificate
apimgmt certificate delete  --resource_group rg1 --service_name apimService1 --certificate_id tempcert
# ApiManagementCreateCertificate
apimgmt certificate list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteCertificate
apimgmt certificate list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateCertificate
apimgmt certificate show  --resource_group rg1 --service_name apimService1 --certificate_id tempcert
# ApiManagementDeleteCertificate
apimgmt certificate show  --resource_group rg1 --service_name apimService1 --certificate_id tempcert
# ApiManagementCreateService
apimgmt create  --resource_group rg1 --name apimService1 --publisher_email apim@autorestsdk.com --publisher_name autorestsdk --sku_name Developer --sku_capacity 1 --location Central US
# ApiManagementCreateMultiRegionServiceWithCustomHostname
apimgmt create  --resource_group rg1 --name apimService1 --virtual_network_type External --publisher_email admin@live.com --publisher_name contoso --sku_name Premium --sku_capacity 1 --location Central US
# ApiManagementCreateServiceHavingMsi
apimgmt create  --resource_group rg1 --name apimService1 --publisher_email apim@autorestsdk.com --publisher_name autorestsdk --sku_name Consumption --location West US
# ApiManagementCreateServiceWithSystemCertificates
apimgmt create  --resource_group rg1 --name apimService1 --publisher_email apim@autorestsdk.com --publisher_name autorestsdk --sku_name Basic --sku_capacity 1 --location Central US
# ApiManagementUpdateServiceDisableTls10
apimgmt create  --resource_group rg1 --name apimService1
# ApiManagementUpdateServicePublisherDetails
apimgmt create  --resource_group rg1 --name apimService1 --publisher_email foobar@live.com --publisher_name Contoso Vnext
# ApiManagementServiceDeleteService
apimgmt create  --resource_group rg1 --name apimService1
# ApiManagementCreateService
apimgmt update  --resource_group rg1 --name apimService1 --publisher_email apim@autorestsdk.com --publisher_name autorestsdk --sku_name Developer --sku_capacity 1 --location Central US
# ApiManagementCreateMultiRegionServiceWithCustomHostname
apimgmt update  --resource_group rg1 --name apimService1 --virtual_network_type External --publisher_email admin@live.com --publisher_name contoso --sku_name Premium --sku_capacity 1 --location Central US
# ApiManagementCreateServiceHavingMsi
apimgmt update  --resource_group rg1 --name apimService1 --publisher_email apim@autorestsdk.com --publisher_name autorestsdk --sku_name Consumption --location West US
# ApiManagementCreateServiceWithSystemCertificates
apimgmt update  --resource_group rg1 --name apimService1 --publisher_email apim@autorestsdk.com --publisher_name autorestsdk --sku_name Basic --sku_capacity 1 --location Central US
# ApiManagementUpdateServiceDisableTls10
apimgmt update  --resource_group rg1 --name apimService1
# ApiManagementUpdateServicePublisherDetails
apimgmt update  --resource_group rg1 --name apimService1 --publisher_email foobar@live.com --publisher_name Contoso Vnext
# ApiManagementServiceDeleteService
apimgmt update  --resource_group rg1 --name apimService1
# ApiManagementCreateService
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementCreateMultiRegionServiceWithCustomHostname
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementCreateServiceHavingMsi
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementCreateServiceWithSystemCertificates
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementUpdateServiceDisableTls10
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementUpdateServicePublisherDetails
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementServiceDeleteService
apimgmt delete  --resource_group rg1 --name apimService1
# ApiManagementCreateService
apimgmt list  --resource_group rg1
# ApiManagementCreateMultiRegionServiceWithCustomHostname
apimgmt list  --resource_group rg1
# ApiManagementCreateServiceHavingMsi
apimgmt list  --resource_group rg1
# ApiManagementCreateServiceWithSystemCertificates
apimgmt list  --resource_group rg1
# ApiManagementUpdateServiceDisableTls10
apimgmt list  --resource_group rg1
# ApiManagementUpdateServicePublisherDetails
apimgmt list  --resource_group rg1
# ApiManagementServiceDeleteService
apimgmt list  --resource_group rg1
# ApiManagementCreateService
apimgmt list  --resource_group rg1
# ApiManagementCreateMultiRegionServiceWithCustomHostname
apimgmt list  --resource_group rg1
# ApiManagementCreateServiceHavingMsi
apimgmt list  --resource_group rg1
# ApiManagementCreateServiceWithSystemCertificates
apimgmt list  --resource_group rg1
# ApiManagementUpdateServiceDisableTls10
apimgmt list  --resource_group rg1
# ApiManagementUpdateServicePublisherDetails
apimgmt list  --resource_group rg1
# ApiManagementServiceDeleteService
apimgmt list  --resource_group rg1
# ApiManagementCreateService
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementCreateMultiRegionServiceWithCustomHostname
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementCreateServiceHavingMsi
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementCreateServiceWithSystemCertificates
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementUpdateServiceDisableTls10
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementUpdateServicePublisherDetails
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementServiceDeleteService
apimgmt show  --resource_group rg1 --name apimService1
# ApiManagementCreateDiagnostic
apimgmt diagnostic create  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/azuremonitor
# ApiManagementUpdateDiagnostic
apimgmt diagnostic create  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/applicationinsights
# ApiManagementDeleteDiagnostic
apimgmt diagnostic create  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementCreateDiagnostic
apimgmt diagnostic update  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/azuremonitor
# ApiManagementUpdateDiagnostic
apimgmt diagnostic update  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights --always_log allErrors --logger_id /loggers/applicationinsights
# ApiManagementDeleteDiagnostic
apimgmt diagnostic update  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementCreateDiagnostic
apimgmt diagnostic delete  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementUpdateDiagnostic
apimgmt diagnostic delete  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementDeleteDiagnostic
apimgmt diagnostic delete  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementCreateDiagnostic
apimgmt diagnostic list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateDiagnostic
apimgmt diagnostic list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteDiagnostic
apimgmt diagnostic list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateDiagnostic
apimgmt diagnostic show  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementUpdateDiagnostic
apimgmt diagnostic show  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementDeleteDiagnostic
apimgmt diagnostic show  --resource_group rg1 --service_name apimService1 --diagnostic_id applicationinsights
# ApiManagementCreateEmailTemplate
apimgmt template create  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage --subject Your request for $IssueName was successfully received.
# ApiManagementUpdateEmailTemplate
apimgmt template create  --resource_group rg1 --service_name apimService1 --name applicationApprovedNotificationMessage --subject Your application $AppName is published in the gallery --body <!DOCTYPE html >
<html>
  <head />
  <body>
    <p style="font-size:12pt;font-family:'Segoe UI'">Dear $DevFirstName $DevLastName,</p>
    <p style="font-size:12pt;font-family:'Segoe UI'">
          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href="http://$DevPortalUrl/Applications/Details/$AppId">here</a>.
        </p>
    <p style="font-size:12pt;font-family:'Segoe UI'">Best,</p>
    <p style="font-size:12pt;font-family:'Segoe UI'">The $OrganizationName API Team</p>
  </body>
</html>
# ApiManagementDeleteEmailTemplate
apimgmt template create  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage
# ApiManagementCreateEmailTemplate
apimgmt template update  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage --subject Your request for $IssueName was successfully received.
# ApiManagementUpdateEmailTemplate
apimgmt template update  --resource_group rg1 --service_name apimService1 --name applicationApprovedNotificationMessage --subject Your application $AppName is published in the gallery --body <!DOCTYPE html >
<html>
  <head />
  <body>
    <p style="font-size:12pt;font-family:'Segoe UI'">Dear $DevFirstName $DevLastName,</p>
    <p style="font-size:12pt;font-family:'Segoe UI'">
          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href="http://$DevPortalUrl/Applications/Details/$AppId">here</a>.
        </p>
    <p style="font-size:12pt;font-family:'Segoe UI'">Best,</p>
    <p style="font-size:12pt;font-family:'Segoe UI'">The $OrganizationName API Team</p>
  </body>
</html>
# ApiManagementDeleteEmailTemplate
apimgmt template update  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage
# ApiManagementCreateEmailTemplate
apimgmt template delete  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage
# ApiManagementUpdateEmailTemplate
apimgmt template delete  --resource_group rg1 --service_name apimService1 --name applicationApprovedNotificationMessage
# ApiManagementDeleteEmailTemplate
apimgmt template delete  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage
# ApiManagementCreateEmailTemplate
apimgmt template list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateEmailTemplate
apimgmt template list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteEmailTemplate
apimgmt template list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateEmailTemplate
apimgmt template show  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage
# ApiManagementUpdateEmailTemplate
apimgmt template show  --resource_group rg1 --service_name apimService1 --name applicationApprovedNotificationMessage
# ApiManagementDeleteEmailTemplate
apimgmt template show  --resource_group rg1 --service_name apimService1 --name newIssueNotificationMessage
# ApiManagementCreateGroup
apimgmt group create  --resource_group rg1 --service_name apimService1 --group_id tempgroup --display_name temp group
# ApiManagementCreateGroupExternal
apimgmt group create  --resource_group rg1 --service_name apimService1 --group_id aadGroup --display_name NewGroup (samiraad.onmicrosoft.com) --description new group to test --type external --external_id aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d
# ApiManagementUpdateGroup
apimgmt group create  --resource_group rg1 --service_name apimService1 --group_id tempgroup --display_name temp group
# ApiManagementDeleteGroup
apimgmt group create  --resource_group rg1 --service_name apimService1 --group_id aadGroup
# ApiManagementCreateGroup
apimgmt group update  --resource_group rg1 --service_name apimService1 --group_id tempgroup --display_name temp group
# ApiManagementCreateGroupExternal
apimgmt group update  --resource_group rg1 --service_name apimService1 --group_id aadGroup --display_name NewGroup (samiraad.onmicrosoft.com) --description new group to test --type external --external_id aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d
# ApiManagementUpdateGroup
apimgmt group update  --resource_group rg1 --service_name apimService1 --group_id tempgroup --display_name temp group
# ApiManagementDeleteGroup
apimgmt group update  --resource_group rg1 --service_name apimService1 --group_id aadGroup
# ApiManagementCreateGroup
apimgmt group delete  --resource_group rg1 --service_name apimService1 --group_id tempgroup
# ApiManagementCreateGroupExternal
apimgmt group delete  --resource_group rg1 --service_name apimService1 --group_id aadGroup
# ApiManagementUpdateGroup
apimgmt group delete  --resource_group rg1 --service_name apimService1 --group_id tempgroup
# ApiManagementDeleteGroup
apimgmt group delete  --resource_group rg1 --service_name apimService1 --group_id aadGroup
# ApiManagementCreateGroup
apimgmt group list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateGroupExternal
apimgmt group list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateGroup
apimgmt group list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteGroup
apimgmt group list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateGroup
apimgmt group show  --resource_group rg1 --service_name apimService1 --group_id tempgroup
# ApiManagementCreateGroupExternal
apimgmt group show  --resource_group rg1 --service_name apimService1 --group_id aadGroup
# ApiManagementUpdateGroup
apimgmt group show  --resource_group rg1 --service_name apimService1 --group_id tempgroup
# ApiManagementDeleteGroup
apimgmt group show  --resource_group rg1 --service_name apimService1 --group_id aadGroup
# ApiManagementCreateGroupUser
apimgmt group user create  --resource_group rg1 --service_name apimService1 --group_id tempgroup --user_id 59307d350af58404d8a26300
# ApiManagementDeleteGroupUser
apimgmt group user create  --resource_group rg1 --service_name apimService1 --group_id templategroup --user_id 59307d350af58404d8a26300
# ApiManagementCreateGroupUser
apimgmt group user delete  --resource_group rg1 --service_name apimService1 --group_id tempgroup --user_id 59307d350af58404d8a26300
# ApiManagementDeleteGroupUser
apimgmt group user delete  --resource_group rg1 --service_name apimService1 --group_id templategroup --user_id 59307d350af58404d8a26300
# ApiManagementCreateGroupUser
apimgmt group user list  --resource_group rg1 --service_name apimService1 --group_id tempgroup
# ApiManagementDeleteGroupUser
apimgmt group user list  --resource_group rg1 --service_name apimService1 --group_id templategroup
# ApiManagementCreateIdentityProvider
apimgmt identityprovider create  --resource_group rg1 --service_name apimService1 --name facebook --client_id facebookid --client_secret facebookapplicationsecret
# ApiManagementUpdateIdentityProvider
apimgmt identityprovider create  --resource_group rg1 --service_name apimService1 --name facebook --client_id updatedfacebookid --client_secret updatedfacebooksecret
# ApiManagementDeleteIdentityProvider
apimgmt identityprovider create  --resource_group rg1 --service_name apimService1 --name aad
# ApiManagementCreateIdentityProvider
apimgmt identityprovider update  --resource_group rg1 --service_name apimService1 --name facebook --client_id facebookid --client_secret facebookapplicationsecret
# ApiManagementUpdateIdentityProvider
apimgmt identityprovider update  --resource_group rg1 --service_name apimService1 --name facebook --client_id updatedfacebookid --client_secret updatedfacebooksecret
# ApiManagementDeleteIdentityProvider
apimgmt identityprovider update  --resource_group rg1 --service_name apimService1 --name aad
# ApiManagementCreateIdentityProvider
apimgmt identityprovider delete  --resource_group rg1 --service_name apimService1 --name facebook
# ApiManagementUpdateIdentityProvider
apimgmt identityprovider delete  --resource_group rg1 --service_name apimService1 --name facebook
# ApiManagementDeleteIdentityProvider
apimgmt identityprovider delete  --resource_group rg1 --service_name apimService1 --name aad
# ApiManagementCreateIdentityProvider
apimgmt identityprovider list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateIdentityProvider
apimgmt identityprovider list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteIdentityProvider
apimgmt identityprovider list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateIdentityProvider
apimgmt identityprovider show  --resource_group rg1 --service_name apimService1 --name facebook
# ApiManagementUpdateIdentityProvider
apimgmt identityprovider show  --resource_group rg1 --service_name apimService1 --name facebook
# ApiManagementDeleteIdentityProvider
apimgmt identityprovider show  --resource_group rg1 --service_name apimService1 --name aad
# ApiManagementCreateEHLogger
apimgmt logger create  --resource_group rg1 --service_name apimService1 --logger_id loggerId --logger_type azureEventHub --description adding a new logger
# ApiManagementCreateAILogger
apimgmt logger create  --resource_group rg1 --service_name apimService1 --logger_id loggerId --logger_type applicationInsights --description adding a new logger
# ApiManagementUpdateLogger
apimgmt logger create  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementDeleteLogger
apimgmt logger create  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementCreateEHLogger
apimgmt logger update  --resource_group rg1 --service_name apimService1 --logger_id loggerId --logger_type azureEventHub --description adding a new logger
# ApiManagementCreateAILogger
apimgmt logger update  --resource_group rg1 --service_name apimService1 --logger_id loggerId --logger_type applicationInsights --description adding a new logger
# ApiManagementUpdateLogger
apimgmt logger update  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementDeleteLogger
apimgmt logger update  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementCreateEHLogger
apimgmt logger delete  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementCreateAILogger
apimgmt logger delete  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementUpdateLogger
apimgmt logger delete  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementDeleteLogger
apimgmt logger delete  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementCreateEHLogger
apimgmt logger list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateAILogger
apimgmt logger list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateLogger
apimgmt logger list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteLogger
apimgmt logger list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateEHLogger
apimgmt logger show  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementCreateAILogger
apimgmt logger show  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementUpdateLogger
apimgmt logger show  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementDeleteLogger
apimgmt logger show  --resource_group rg1 --service_name apimService1 --logger_id loggerId
# ApiManagementCreateNotification
apimgmt notification create  --resource_group rg1 --service_name apimService1 --name RequestPublisherNotificationMessage
# ApiManagementCreateNotification
apimgmt notification update  --resource_group rg1 --service_name apimService1 --name RequestPublisherNotificationMessage
# ApiManagementCreateNotification
apimgmt notification list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateNotification
apimgmt notification show  --resource_group rg1 --service_name apimService1 --name RequestPublisherNotificationMessage
# ApiManagementCreateNotificationRecipientUser
apimgmt notification recipientuser create  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --user_id 576823d0a40f7e74ec07d642
# ApiManagementDeleteNotificationRecipientUser
apimgmt notification recipientuser create  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --user_id 576823d0a40f7e74ec07d642
# ApiManagementCreateNotificationRecipientUser
apimgmt notification recipientuser update  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --user_id 576823d0a40f7e74ec07d642
# ApiManagementDeleteNotificationRecipientUser
apimgmt notification recipientuser update  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --user_id 576823d0a40f7e74ec07d642
# ApiManagementCreateNotificationRecipientUser
apimgmt notification recipientuser delete  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --user_id 576823d0a40f7e74ec07d642
# ApiManagementDeleteNotificationRecipientUser
apimgmt notification recipientuser delete  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --user_id 576823d0a40f7e74ec07d642
# ApiManagementCreateNotificationRecipientUser
apimgmt notification recipientuser list  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage
# ApiManagementDeleteNotificationRecipientUser
apimgmt notification recipientuser list  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage
# ApiManagementCreateNotificationRecipientEmail
apimgmt notification recipientemail create  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --email foobar@live.com
# ApiManagementDeleteNotificationRecipientEmail
apimgmt notification recipientemail create  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --email contoso@live.com
# ApiManagementCreateNotificationRecipientEmail
apimgmt notification recipientemail update  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --email foobar@live.com
# ApiManagementDeleteNotificationRecipientEmail
apimgmt notification recipientemail update  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --email contoso@live.com
# ApiManagementCreateNotificationRecipientEmail
apimgmt notification recipientemail delete  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --email foobar@live.com
# ApiManagementDeleteNotificationRecipientEmail
apimgmt notification recipientemail delete  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage --email contoso@live.com
# ApiManagementCreateNotificationRecipientEmail
apimgmt notification recipientemail list  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage
# ApiManagementDeleteNotificationRecipientEmail
apimgmt notification recipientemail list  --resource_group rg1 --service_name apimService1 --notification_name RequestPublisherNotificationMessage
# ApiManagementCreateOpenIdConnectProvider
apimgmt openidconnectprovider create  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3 --display_name templateoidprovider3 --metadata_endpoint https://oidprovider-template3.net --client_id oidprovidertemplate3
# ApiManagementUpdateOpenIdConnectProvider
apimgmt openidconnectprovider create  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect2 --client_secret updatedsecret
# ApiManagementDeleteOpenIdConnectProvider
apimgmt openidconnectprovider create  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3
# ApiManagementCreateOpenIdConnectProvider
apimgmt openidconnectprovider update  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3 --display_name templateoidprovider3 --metadata_endpoint https://oidprovider-template3.net --client_id oidprovidertemplate3
# ApiManagementUpdateOpenIdConnectProvider
apimgmt openidconnectprovider update  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect2 --client_secret updatedsecret
# ApiManagementDeleteOpenIdConnectProvider
apimgmt openidconnectprovider update  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3
# ApiManagementCreateOpenIdConnectProvider
apimgmt openidconnectprovider delete  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3
# ApiManagementUpdateOpenIdConnectProvider
apimgmt openidconnectprovider delete  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect2
# ApiManagementDeleteOpenIdConnectProvider
apimgmt openidconnectprovider delete  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3
# ApiManagementCreateOpenIdConnectProvider
apimgmt openidconnectprovider list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateOpenIdConnectProvider
apimgmt openidconnectprovider list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteOpenIdConnectProvider
apimgmt openidconnectprovider list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateOpenIdConnectProvider
apimgmt openidconnectprovider show  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3
# ApiManagementUpdateOpenIdConnectProvider
apimgmt openidconnectprovider show  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect2
# ApiManagementDeleteOpenIdConnectProvider
apimgmt openidconnectprovider show  --resource_group rg1 --service_name apimService1 --opid templateOpenIdConnect3
# ApiManagementCreatePolicy
apimgmt policy create  --resource_group rg1 --service_name apimService1 --policy_id policy --value <policies>
  <inbound />
  <backend>
    <forward-request />
  </backend>
  <outbound />
</policies> --format xml
# ApiManagementDeletePolicy
apimgmt policy create  --resource_group rg1 --service_name apimService1 --policy_id policy
# ApiManagementCreatePolicy
apimgmt policy update  --resource_group rg1 --service_name apimService1 --policy_id policy --value <policies>
  <inbound />
  <backend>
    <forward-request />
  </backend>
  <outbound />
</policies> --format xml
# ApiManagementDeletePolicy
apimgmt policy update  --resource_group rg1 --service_name apimService1 --policy_id policy
# ApiManagementCreatePolicy
apimgmt policy delete  --resource_group rg1 --service_name apimService1 --policy_id policy
# ApiManagementDeletePolicy
apimgmt policy delete  --resource_group rg1 --service_name apimService1 --policy_id policy
# ApiManagementCreatePolicy
apimgmt policy list  --resource_group rg1 --service_name apimService1
# ApiManagementDeletePolicy
apimgmt policy list  --resource_group rg1 --service_name apimService1
# ApiManagementCreatePolicy
apimgmt policy show  --resource_group rg1 --service_name apimService1 --policy_id policy --format xml
# ApiManagementDeletePolicy
apimgmt policy show  --resource_group rg1 --service_name apimService1 --policy_id policy
# ApiManagementPortalSettingsUpdateSignIn
apimgmt portalsetting create  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignIn
apimgmt portalsetting create  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignIn
apimgmt portalsetting update  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignIn
apimgmt portalsetting update  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignIn
apimgmt portalsetting show  --resource_group rg1 --name apimService1
# ApiManagementPortalSettingsUpdateSignIn
apimgmt portalsetting show  --resource_group rg1 --name apimService1
# ApiManagementPortalSettingsUpdateSignUp
apimgmt portalsetting create  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignUp
apimgmt portalsetting create  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignUp
apimgmt portalsetting update  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignUp
apimgmt portalsetting update  --resource_group rg1 --name apimService1 --enabled true
# ApiManagementPortalSettingsUpdateSignUp
apimgmt portalsetting show  --resource_group rg1 --name apimService1
# ApiManagementPortalSettingsUpdateSignUp
apimgmt portalsetting show  --resource_group rg1 --name apimService1
# ApiManagementPortalSettingsUpdateDelegation
apimgmt portalsetting create  --resource_group rg1 --name apimService1 --url http://contoso.com/delegation --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
# ApiManagementPortalSettingsUpdateDelegation
apimgmt portalsetting create  --resource_group rg1 --name apimService1 --url http://contoso.com/delegation --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
# ApiManagementPortalSettingsUpdateDelegation
apimgmt portalsetting update  --resource_group rg1 --name apimService1 --url http://contoso.com/delegation --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
# ApiManagementPortalSettingsUpdateDelegation
apimgmt portalsetting update  --resource_group rg1 --name apimService1 --url http://contoso.com/delegation --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
# ApiManagementPortalSettingsUpdateDelegation
apimgmt portalsetting show  --resource_group rg1 --name apimService1
# ApiManagementPortalSettingsUpdateDelegation
apimgmt portalsetting show  --resource_group rg1 --name apimService1
# ApiManagementCreateProduct
apimgmt product create  --resource_group rg1 --service_name apimService1 --product_id testproduct --display_name Test Template ProductName 4
# ApiManagementUpdateProduct
apimgmt product create  --resource_group rg1 --service_name apimService1 --product_id testproduct --display_name Test Template ProductName 4
# ApiManagementDeleteProduct
apimgmt product create  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProduct
apimgmt product update  --resource_group rg1 --service_name apimService1 --product_id testproduct --display_name Test Template ProductName 4
# ApiManagementUpdateProduct
apimgmt product update  --resource_group rg1 --service_name apimService1 --product_id testproduct --display_name Test Template ProductName 4
# ApiManagementDeleteProduct
apimgmt product update  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProduct
apimgmt product delete  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementUpdateProduct
apimgmt product delete  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementDeleteProduct
apimgmt product delete  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProduct
apimgmt product list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateProduct
apimgmt product list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteProduct
apimgmt product list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateProduct
apimgmt product list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateProduct
apimgmt product list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteProduct
apimgmt product list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateProduct
apimgmt product show  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementUpdateProduct
apimgmt product show  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementDeleteProduct
apimgmt product show  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProductApi
apimgmt product api create  --resource_group rg1 --service_name apimService1 --product_id testproduct --api_id echo-api
# ApiManagementDeleteProductApi
apimgmt product api create  --resource_group rg1 --service_name apimService1 --product_id testproduct --api_id echo-api
# ApiManagementCreateProductApi
apimgmt product api update  --resource_group rg1 --service_name apimService1 --product_id testproduct --api_id echo-api
# ApiManagementDeleteProductApi
apimgmt product api update  --resource_group rg1 --service_name apimService1 --product_id testproduct --api_id echo-api
# ApiManagementCreateProductApi
apimgmt product api delete  --resource_group rg1 --service_name apimService1 --product_id testproduct --api_id echo-api
# ApiManagementDeleteProductApi
apimgmt product api delete  --resource_group rg1 --service_name apimService1 --product_id testproduct --api_id echo-api
# ApiManagementCreateProductApi
apimgmt product api list  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementDeleteProductApi
apimgmt product api list  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProductGroup
apimgmt product group create  --resource_group rg1 --service_name apimService1 --product_id testproduct --group_id templateGroup
# ApiManagementDeleteProductGroup
apimgmt product group create  --resource_group rg1 --service_name apimService1 --product_id testproduct --group_id templateGroup
# ApiManagementCreateProductGroup
apimgmt product group update  --resource_group rg1 --service_name apimService1 --product_id testproduct --group_id templateGroup
# ApiManagementDeleteProductGroup
apimgmt product group update  --resource_group rg1 --service_name apimService1 --product_id testproduct --group_id templateGroup
# ApiManagementCreateProductGroup
apimgmt product group delete  --resource_group rg1 --service_name apimService1 --product_id testproduct --group_id templateGroup
# ApiManagementDeleteProductGroup
apimgmt product group delete  --resource_group rg1 --service_name apimService1 --product_id testproduct --group_id templateGroup
# ApiManagementCreateProductGroup
apimgmt product group list  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementDeleteProductGroup
apimgmt product group list  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProductPolicy
apimgmt product policy create  --resource_group rg1 --service_name apimService1 --product_id 5702e97e5157a50f48dce801 --policy_id policy --value <policies>
  <inbound>
    <rate-limit calls="{{call-count}}" renewal-period="15"></rate-limit>
    <log-to-eventhub logger-id="16">
                      @( string.Join(",", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) 
                  </log-to-eventhub>
    <quota-by-key calls="40" counter-key="cc" renewal-period="3600" increment-count="@(context.Request.Method == &quot;POST&quot; ? 1:2)" />
    <base />
  </inbound>
  <backend>
    <base />
  </backend>
  <outbound>
    <base />
  </outbound>
</policies> --format xml
# ApiManagementDeleteProductPolicy
apimgmt product policy create  --resource_group rg1 --service_name apimService1 --product_id testproduct --policy_id policy
# ApiManagementCreateProductPolicy
apimgmt product policy update  --resource_group rg1 --service_name apimService1 --product_id 5702e97e5157a50f48dce801 --policy_id policy --value <policies>
  <inbound>
    <rate-limit calls="{{call-count}}" renewal-period="15"></rate-limit>
    <log-to-eventhub logger-id="16">
                      @( string.Join(",", DateTime.UtcNow, context.Deployment.ServiceName, context.RequestId, context.Request.IpAddress, context.Operation.Name) ) 
                  </log-to-eventhub>
    <quota-by-key calls="40" counter-key="cc" renewal-period="3600" increment-count="@(context.Request.Method == &quot;POST&quot; ? 1:2)" />
    <base />
  </inbound>
  <backend>
    <base />
  </backend>
  <outbound>
    <base />
  </outbound>
</policies> --format xml
# ApiManagementDeleteProductPolicy
apimgmt product policy update  --resource_group rg1 --service_name apimService1 --product_id testproduct --policy_id policy
# ApiManagementCreateProductPolicy
apimgmt product policy delete  --resource_group rg1 --service_name apimService1 --product_id 5702e97e5157a50f48dce801 --policy_id policy
# ApiManagementDeleteProductPolicy
apimgmt product policy delete  --resource_group rg1 --service_name apimService1 --product_id testproduct --policy_id policy
# ApiManagementCreateProductPolicy
apimgmt product policy list  --resource_group rg1 --service_name apimService1 --product_id 5702e97e5157a50f48dce801
# ApiManagementDeleteProductPolicy
apimgmt product policy list  --resource_group rg1 --service_name apimService1 --product_id testproduct
# ApiManagementCreateProductPolicy
apimgmt product policy show  --resource_group rg1 --service_name apimService1 --product_id 5702e97e5157a50f48dce801 --policy_id policy --format xml
# ApiManagementDeleteProductPolicy
apimgmt product policy show  --resource_group rg1 --service_name apimService1 --product_id testproduct --policy_id policy
# ApiManagementCreateProperty
apimgmt property create  --resource_group rg1 --service_name apimService1 --prop_id testprop2 --secret true --display_name prop3name --value propValue
# ApiManagementUpdateProperty
apimgmt property create  --resource_group rg1 --service_name apimService1 --prop_id testprop2 --secret true
# ApiManagementDeleteProperty
apimgmt property create  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementCreateProperty
apimgmt property update  --resource_group rg1 --service_name apimService1 --prop_id testprop2 --secret true --display_name prop3name --value propValue
# ApiManagementUpdateProperty
apimgmt property update  --resource_group rg1 --service_name apimService1 --prop_id testprop2 --secret true
# ApiManagementDeleteProperty
apimgmt property update  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementCreateProperty
apimgmt property delete  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementUpdateProperty
apimgmt property delete  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementDeleteProperty
apimgmt property delete  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementCreateProperty
apimgmt property list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateProperty
apimgmt property list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteProperty
apimgmt property list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateProperty
apimgmt property show  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementUpdateProperty
apimgmt property show  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementDeleteProperty
apimgmt property show  --resource_group rg1 --service_name apimService1 --prop_id testprop2
# ApiManagementCreateSubscription
apimgmt subscription create  --resource_group rg1 --service_name apimService1 --sid testsub --owner_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }} --scope /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }} --display_name testsub
# ApiManagementUpdateSubscription
apimgmt subscription create  --resource_group rg1 --service_name apimService1 --sid testsub --display_name testsub
# ApiManagementDeleteSubscription
apimgmt subscription create  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementCreateSubscription
apimgmt subscription update  --resource_group rg1 --service_name apimService1 --sid testsub --owner_id /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }} --scope /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }} --display_name testsub
# ApiManagementUpdateSubscription
apimgmt subscription update  --resource_group rg1 --service_name apimService1 --sid testsub --display_name testsub
# ApiManagementDeleteSubscription
apimgmt subscription update  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementCreateSubscription
apimgmt subscription delete  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementUpdateSubscription
apimgmt subscription delete  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementDeleteSubscription
apimgmt subscription delete  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementCreateSubscription
apimgmt subscription list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateSubscription
apimgmt subscription list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteSubscription
apimgmt subscription list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateSubscription
apimgmt subscription show  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementUpdateSubscription
apimgmt subscription show  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementDeleteSubscription
apimgmt subscription show  --resource_group rg1 --service_name apimService1 --sid testsub
# ApiManagementCreateUser
apimgmt user create  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b --email foobar@outlook.com --first_name foo --last_name bar --confirmation signup
# ApiManagementUpdateUser
apimgmt user create  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b --email foobar@outlook.com --first_name foo --last_name bar
# ApiManagementDeleteUser
apimgmt user create  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementCreateUser
apimgmt user update  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b --email foobar@outlook.com --first_name foo --last_name bar --confirmation signup
# ApiManagementUpdateUser
apimgmt user update  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b --email foobar@outlook.com --first_name foo --last_name bar
# ApiManagementDeleteUser
apimgmt user update  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementCreateUser
apimgmt user delete  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementUpdateUser
apimgmt user delete  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementDeleteUser
apimgmt user delete  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementCreateUser
apimgmt user list  --resource_group rg1 --service_name apimService1
# ApiManagementUpdateUser
apimgmt user list  --resource_group rg1 --service_name apimService1
# ApiManagementDeleteUser
apimgmt user list  --resource_group rg1 --service_name apimService1
# ApiManagementCreateUser
apimgmt user show  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementUpdateUser
apimgmt user show  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
# ApiManagementDeleteUser
apimgmt user show  --resource_group rg1 --service_name apimService1 --user_id 5931a75ae4bbd512288c680b
## apimgmt

### apimgmt create

create a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|
|**--publisher_email**|str|Publisher email.|/publisher_email|/properties/publisherEmail|
|**--publisher_name**|str|Publisher name.|/publisher_name|/properties/publisherName|
|**--sku_name**|str|Name of the Sku.|/sku/name|/sku/name|
|**--location**|str|Resource location.|/location|/location|
|--tags|unknown[DictionaryType {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]|Resource tags.|/tags|/tags|
|--notification_sender_email|str|Email address from which the notification will be sent.|/notification_sender_email|/properties/notificationSenderEmail|
|--hostname_configurations|list|Custom hostname configuration of the API Management service.|/hostname_configurations|/properties/hostnameConfigurations|
|--virtual_network_configuration|dict|Virtual network configuration of the API Management service.|/virtual_network_configuration|/properties/virtualNetworkConfiguration|
|--additional_locations|list|Additional datacenter locations of the API Management service.|/additional_locations|/properties/additionalLocations|
|--custom_properties|unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.|/custom_properties|/properties/customProperties|
|--certificates|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/certificates|/properties/certificates|
|--enable_client_certificate|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/enable_client_certificate|/properties/enableClientCertificate|
|--virtual_network_type|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/virtual_network_type|/properties/virtualNetworkType|
|--sku_capacity|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|/sku/capacity|
|--identity|dict|Managed service identity of the Api Management service.|/identity|/identity|

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt update

update a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|
|**--publisher_email**|str|Publisher email.|/publisher_email|/properties/publisherEmail|
|**--publisher_name**|str|Publisher name.|/publisher_name|/properties/publisherName|
|**--sku_name**|str|Name of the Sku.|/sku/name|/sku/name|
|**--location**|str|Resource location.|/location|/location|
|--tags|unknown[DictionaryType {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]|Resource tags.|/tags|/tags|
|--notification_sender_email|str|Email address from which the notification will be sent.|/notification_sender_email|/properties/notificationSenderEmail|
|--hostname_configurations|list|Custom hostname configuration of the API Management service.|/hostname_configurations|/properties/hostnameConfigurations|
|--virtual_network_configuration|dict|Virtual network configuration of the API Management service.|/virtual_network_configuration|/properties/virtualNetworkConfiguration|
|--additional_locations|list|Additional datacenter locations of the API Management service.|/additional_locations|/properties/additionalLocations|
|--custom_properties|unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.|/custom_properties|/properties/customProperties|
|--certificates|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/certificates|/properties/certificates|
|--enable_client_certificate|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/enable_client_certificate|/properties/enableClientCertificate|
|--virtual_network_type|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/virtual_network_type|/properties/virtualNetworkType|
|--sku_capacity|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|/sku/capacity|
|--identity|dict|Managed service identity of the Api Management service.|/identity|/identity|

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt delete

delete a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt list

list a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt show

show a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```

```
```

```
```

```
```
## apimgmt api

### apimgmt api create

create a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api_revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--api_revision_description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|dict|Version set details|/api_version_set|/properties/apiVersionSet|
|--value|str|Content value when Importing an API.|/value|/properties/value|
|--format|str|Format of the Content in which the API is getting imported.|/format|/properties/format|
|--wsdl_selector|dict|Criteria to limit import of WSDL to a subset of the document.|/wsdl_selector|/properties/wsdlSelector|
|--api_type|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/api_type|/properties/apiType|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt api update

update a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api_revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--api_revision_description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|dict|Version set details|/api_version_set|/properties/apiVersionSet|
|--value|str|Content value when Importing an API.|/value|/properties/value|
|--format|str|Format of the Content in which the API is getting imported.|/format|/properties/format|
|--wsdl_selector|dict|Criteria to limit import of WSDL to a subset of the document.|/wsdl_selector|/properties/wsdlSelector|
|--api_type|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/api_type|/properties/apiType|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt api delete

delete a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt api list

list a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt api show

show a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
## apimgmt api diagnostic

### apimgmt api diagnostic create

create a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger_id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

```
```

```
```

```
```
### apimgmt api diagnostic update

update a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger_id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

```
```

```
```

```
```
### apimgmt api diagnostic delete

delete a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

```
```

```
```

```
```
### apimgmt api diagnostic list

list a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|

```
```

```
```

```
```
### apimgmt api diagnostic show

show a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

```
```

```
```

```
```
## apimgmt api issue

### apimgmt api issue create

create a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--title**|str|The issue title.|/title|/properties/title|
|**--description**|str|Text describing the issue.|/description|/properties/description|
|**--user_id**|str|A resource identifier for the user created the issue.|/user_id|/properties/userId|
|--created_date|datetime|Date and time when the issue was created.|/created_date|/properties/createdDate|
|--state|str|Status of the issue.|/state|/properties/state|

```
```

```
```

```
```
### apimgmt api issue update

update a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--title**|str|The issue title.|/title|/properties/title|
|**--description**|str|Text describing the issue.|/description|/properties/description|
|**--user_id**|str|A resource identifier for the user created the issue.|/user_id|/properties/userId|
|--created_date|datetime|Date and time when the issue was created.|/created_date|/properties/createdDate|
|--state|str|Status of the issue.|/state|/properties/state|

```
```

```
```

```
```
### apimgmt api issue delete

delete a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

```
```

```
```

```
```
### apimgmt api issue list

list a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|

```
```

```
```

```
```
### apimgmt api issue show

show a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

```
```

```
```

```
```
## apimgmt api issue attachment

### apimgmt api issue attachment create

create a apimgmt api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment_id**|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
|**--title**|str|Filename by which the binary data will be saved.|/title|/properties/title|
|**--content_format**|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/content_format|/properties/contentFormat|
|**--content**|str|An HTTP link or Base64-encoded binary data.|/content|/properties/content|

```
```

```
```
### apimgmt api issue attachment update

update a apimgmt api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment_id**|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
|**--title**|str|Filename by which the binary data will be saved.|/title|/properties/title|
|**--content_format**|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/content_format|/properties/contentFormat|
|**--content**|str|An HTTP link or Base64-encoded binary data.|/content|/properties/content|

```
```

```
```
### apimgmt api issue attachment delete

delete a apimgmt api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment_id**|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|

```
```

```
```
### apimgmt api issue attachment list

list a apimgmt api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

```
```

```
```
### apimgmt api issue attachment show

show a apimgmt api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment_id**|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|

```
```

```
```
## apimgmt api issue comment

### apimgmt api issue comment create

create a apimgmt api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment_id**|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
|**--text**|str|Comment text.|/text|/properties/text|
|**--user_id**|str|A resource identifier for the user who left the comment.|/user_id|/properties/userId|
|--created_date|datetime|Date and time when the comment was created.|/created_date|/properties/createdDate|

```
```

```
```
### apimgmt api issue comment update

update a apimgmt api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment_id**|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
|**--text**|str|Comment text.|/text|/properties/text|
|**--user_id**|str|A resource identifier for the user who left the comment.|/user_id|/properties/userId|
|--created_date|datetime|Date and time when the comment was created.|/created_date|/properties/createdDate|

```
```

```
```
### apimgmt api issue comment delete

delete a apimgmt api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment_id**|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|

```
```

```
```
### apimgmt api issue comment list

list a apimgmt api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

```
```

```
```
### apimgmt api issue comment show

show a apimgmt api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment_id**|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|

```
```

```
```
## apimgmt api operation

### apimgmt api operation create

create a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--display_name**|str|Operation Name.|/display_name|/properties/displayName|
|**--method**|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/method|/properties/method|
|**--url_template**|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/url_template|/properties/urlTemplate|
|--template_parameters|list|Collection of URL template parameters.|/template_parameters|/properties/templateParameters|
|--description|str|Description of the operation. May include HTML formatting tags.|/description|/properties/description|
|--request|dict|An entity containing request details.|/request|/properties/request|
|--responses|list|Array of Operation responses.|/responses|/properties/responses|
|--policies|str|Operation Policies|/policies|/properties/policies|

```
```

```
```

```
```
### apimgmt api operation update

update a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--display_name**|str|Operation Name.|/display_name|/properties/displayName|
|**--method**|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/method|/properties/method|
|**--url_template**|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/url_template|/properties/urlTemplate|
|--template_parameters|list|Collection of URL template parameters.|/template_parameters|/properties/templateParameters|
|--description|str|Description of the operation. May include HTML formatting tags.|/description|/properties/description|
|--request|dict|An entity containing request details.|/request|/properties/request|
|--responses|list|Array of Operation responses.|/responses|/properties/responses|
|--policies|str|Operation Policies|/policies|/properties/policies|

```
```

```
```

```
```
### apimgmt api operation delete

delete a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

```
```

```
```

```
```
### apimgmt api operation list

list a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```

```
```
### apimgmt api operation show

show a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

```
```

```
```

```
```
## apimgmt api operation policy

### apimgmt api operation policy create

create a apimgmt api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```
### apimgmt api operation policy update

update a apimgmt api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```
### apimgmt api operation policy delete

delete a apimgmt api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

```
```

```
```
### apimgmt api operation policy list

list a apimgmt api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

```
```

```
```
### apimgmt api operation policy show

show a apimgmt api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|--format|default|Format of the policyContent.|/format|/properties/format|

```
```

```
```
## apimgmt api policy

### apimgmt api policy create

create a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```

```
```
### apimgmt api policy update

update a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```

```
```
### apimgmt api policy delete

delete a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

```
```

```
```

```
```
### apimgmt api policy list

list a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```

```
```
### apimgmt api policy show

show a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|--format|default|Format of the policyContent.|/format|/properties/format|

```
```

```
```

```
```
## apimgmt api release

### apimgmt api release create

create a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release_id**|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
|--notes|str|Release Notes|/notes|/properties/notes|

```
```

```
```

```
```
### apimgmt api release update

update a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release_id**|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
|--notes|str|Release Notes|/notes|/properties/notes|

```
```

```
```

```
```
### apimgmt api release delete

delete a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release_id**|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|

```
```

```
```

```
```
### apimgmt api release list

list a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|

```
```

```
```

```
```
### apimgmt api release show

show a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release_id**|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|

```
```

```
```

```
```
## apimgmt api schema

### apimgmt api schema create

create a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema_id**|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
|**--content_type**|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/content_type|/properties/contentType|
|--document|dict|Create or update Properties of the Schema Document.|/document|/properties/document|

```
```

```
```
### apimgmt api schema update

update a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema_id**|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
|**--content_type**|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/content_type|/properties/contentType|
|--document|dict|Create or update Properties of the Schema Document.|/document|/properties/document|

```
```

```
```
### apimgmt api schema delete

delete a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema_id**|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|

```
```

```
```
### apimgmt api schema list

list a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```
### apimgmt api schema show

show a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema_id**|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|

```
```

```
```
## apimgmt api tagdescription

### apimgmt api tagdescription create

create a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--description|str|Description of the Tag.|/description|/properties/description|
|--external_docs_url|str|Absolute URL of external resources describing the tag.|/external_docs_url|/properties/externalDocsUrl|
|--external_docs_description|str|Description of the external resources describing the tag.|/external_docs_description|/properties/externalDocsDescription|

```
```

```
```
### apimgmt api tagdescription update

update a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--description|str|Description of the Tag.|/description|/properties/description|
|--external_docs_url|str|Absolute URL of external resources describing the tag.|/external_docs_url|/properties/externalDocsUrl|
|--external_docs_description|str|Description of the external resources describing the tag.|/external_docs_description|/properties/externalDocsDescription|

```
```

```
```
### apimgmt api tagdescription delete

delete a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

```
```

```
```
### apimgmt api tagdescription list

list a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```
### apimgmt api tagdescription show

show a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

```
```

```
```
## apimgmt apiversionset

### apimgmt apiversionset create

create a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--version_set_id**|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
|**--display_name**|str|Name of API Version Set|/display_name|/properties/displayName|
|**--versioning_scheme**|str|An value that determines where the API Version identifer will be located in a HTTP request.|/versioning_scheme|/properties/versioningScheme|
|--description|str|Description of API Version Set.|/description|/properties/description|
|--version_query_name|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/version_query_name|/properties/versionQueryName|
|--version_header_name|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/version_header_name|/properties/versionHeaderName|

```
```

```
```

```
```
### apimgmt apiversionset update

update a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--version_set_id**|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
|**--display_name**|str|Name of API Version Set|/display_name|/properties/displayName|
|**--versioning_scheme**|str|An value that determines where the API Version identifer will be located in a HTTP request.|/versioning_scheme|/properties/versioningScheme|
|--description|str|Description of API Version Set.|/description|/properties/description|
|--version_query_name|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/version_query_name|/properties/versionQueryName|
|--version_header_name|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/version_header_name|/properties/versionHeaderName|

```
```

```
```

```
```
### apimgmt apiversionset delete

delete a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--version_set_id**|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|

```
```

```
```

```
```
### apimgmt apiversionset list

list a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt apiversionset show

show a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--version_set_id**|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|

```
```

```
```

```
```
## apimgmt authorizationserver

### apimgmt authorizationserver create

create a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--authsid**|default|Identifier of the authorization server.|authsid|authsid|
|**--display_name**|str|User-friendly authorization server name.|/display_name|/properties/displayName|
|**--client_registration_endpoint**|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/client_registration_endpoint|/properties/clientRegistrationEndpoint|
|**--authorization_endpoint**|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/authorization_endpoint|/properties/authorizationEndpoint|
|**--grant_types**|list|Form of an authorization grant, which the client uses to request the access token.|/grant_types|/properties/grantTypes|
|**--client_id**|str|Client or app id registered with this authorization server.|/client_id|/properties/clientId|
|--description|str|Description of the authorization server. Can contain HTML formatting tags.|/description|/properties/description|
|--authorization_methods|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/authorization_methods|/properties/authorizationMethods|
|--client_authentication_method|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/client_authentication_method|/properties/clientAuthenticationMethod|
|--token_body_parameters|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/token_body_parameters|/properties/tokenBodyParameters|
|--token_endpoint|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/token_endpoint|/properties/tokenEndpoint|
|--support_state|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/support_state|/properties/supportState|
|--default_scope|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/default_scope|/properties/defaultScope|
|--bearer_token_sending_methods|list|Specifies the mechanism by which access token is passed to the API. |/bearer_token_sending_methods|/properties/bearerTokenSendingMethods|
|--client_secret|str|Client or app secret registered with this authorization server.|/client_secret|/properties/clientSecret|
|--resource_owner_username|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/resource_owner_username|/properties/resourceOwnerUsername|
|--resource_owner_password|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/resource_owner_password|/properties/resourceOwnerPassword|

```
```

```
```

```
```
### apimgmt authorizationserver update

update a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--authsid**|default|Identifier of the authorization server.|authsid|authsid|
|**--display_name**|str|User-friendly authorization server name.|/display_name|/properties/displayName|
|**--client_registration_endpoint**|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/client_registration_endpoint|/properties/clientRegistrationEndpoint|
|**--authorization_endpoint**|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/authorization_endpoint|/properties/authorizationEndpoint|
|**--grant_types**|list|Form of an authorization grant, which the client uses to request the access token.|/grant_types|/properties/grantTypes|
|**--client_id**|str|Client or app id registered with this authorization server.|/client_id|/properties/clientId|
|--description|str|Description of the authorization server. Can contain HTML formatting tags.|/description|/properties/description|
|--authorization_methods|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/authorization_methods|/properties/authorizationMethods|
|--client_authentication_method|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/client_authentication_method|/properties/clientAuthenticationMethod|
|--token_body_parameters|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/token_body_parameters|/properties/tokenBodyParameters|
|--token_endpoint|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/token_endpoint|/properties/tokenEndpoint|
|--support_state|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/support_state|/properties/supportState|
|--default_scope|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/default_scope|/properties/defaultScope|
|--bearer_token_sending_methods|list|Specifies the mechanism by which access token is passed to the API. |/bearer_token_sending_methods|/properties/bearerTokenSendingMethods|
|--client_secret|str|Client or app secret registered with this authorization server.|/client_secret|/properties/clientSecret|
|--resource_owner_username|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/resource_owner_username|/properties/resourceOwnerUsername|
|--resource_owner_password|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/resource_owner_password|/properties/resourceOwnerPassword|

```
```

```
```

```
```
### apimgmt authorizationserver delete

delete a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--authsid**|default|Identifier of the authorization server.|authsid|authsid|

```
```

```
```

```
```
### apimgmt authorizationserver list

list a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt authorizationserver show

show a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--authsid**|default|Identifier of the authorization server.|authsid|authsid|

```
```

```
```

```
```
## apimgmt backend

### apimgmt backend create

create a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--backend_id**|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
|**--url**|str|Runtime Url of the Backend.|/url|/properties/url|
|**--protocol**|str|Backend communication protocol.|/protocol|/properties/protocol|
|--title|str|Backend Title.|/title|/properties/title|
|--description|str|Backend Description.|/description|/properties/description|
|--resource_id|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/resource_id|/properties/resourceId|
|--service_fabric_cluster|dict|Backend Service Fabric Cluster Properties|/service_fabric_cluster|/properties/properties/serviceFabricCluster|
|--credentials|dict|Backend Credentials Contract Properties|/credentials|/properties/credentials|
|--proxy|dict|Backend Proxy Contract Properties|/proxy|/properties/proxy|
|--tls|dict|Backend TLS Properties|/tls|/properties/tls|

```
```

```
```

```
```

```
```
### apimgmt backend update

update a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--backend_id**|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
|**--url**|str|Runtime Url of the Backend.|/url|/properties/url|
|**--protocol**|str|Backend communication protocol.|/protocol|/properties/protocol|
|--title|str|Backend Title.|/title|/properties/title|
|--description|str|Backend Description.|/description|/properties/description|
|--resource_id|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/resource_id|/properties/resourceId|
|--service_fabric_cluster|dict|Backend Service Fabric Cluster Properties|/service_fabric_cluster|/properties/properties/serviceFabricCluster|
|--credentials|dict|Backend Credentials Contract Properties|/credentials|/properties/credentials|
|--proxy|dict|Backend Proxy Contract Properties|/proxy|/properties/proxy|
|--tls|dict|Backend TLS Properties|/tls|/properties/tls|

```
```

```
```

```
```

```
```
### apimgmt backend delete

delete a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--backend_id**|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|

```
```

```
```

```
```

```
```
### apimgmt backend list

list a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```
### apimgmt backend show

show a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--backend_id**|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|

```
```

```
```

```
```

```
```
## apimgmt cache

### apimgmt cache create

create a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--cache_id**|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
|**--connection_string**|str|Runtime connection string to cache|/connection_string|/properties/connectionString|
|--description|str|Cache description|/description|/properties/description|
|--resource_id|str|Original uri of entity in external system cache points to|/resource_id|/properties/resourceId|

```
```

```
```

```
```
### apimgmt cache update

update a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--cache_id**|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
|**--connection_string**|str|Runtime connection string to cache|/connection_string|/properties/connectionString|
|--description|str|Cache description|/description|/properties/description|
|--resource_id|str|Original uri of entity in external system cache points to|/resource_id|/properties/resourceId|

```
```

```
```

```
```
### apimgmt cache delete

delete a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--cache_id**|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|

```
```

```
```

```
```
### apimgmt cache list

list a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt cache show

show a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--cache_id**|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|

```
```

```
```

```
```
## apimgmt certificate

### apimgmt certificate create

create a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--certificate_id**|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
|**--data**|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/data|/properties/data|
|**--password**|str|Password for the Certificate|/password|/properties/password|

```
```

```
```
### apimgmt certificate update

update a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--certificate_id**|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
|**--data**|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/data|/properties/data|
|**--password**|str|Password for the Certificate|/password|/properties/password|

```
```

```
```
### apimgmt certificate delete

delete a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--certificate_id**|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|

```
```

```
```
### apimgmt certificate list

list a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```
### apimgmt certificate show

show a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--certificate_id**|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|

```
```

```
```
## apimgmt diagnostic

### apimgmt diagnostic create

create a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger_id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

```
```

```
```

```
```
### apimgmt diagnostic update

update a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger_id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

```
```

```
```

```
```
### apimgmt diagnostic delete

delete a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

```
```

```
```

```
```
### apimgmt diagnostic list

list a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt diagnostic show

show a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

```
```

```
```

```
```
## apimgmt group

### apimgmt group create

create a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display_name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description.|/description|/properties/description|
|--type|str|Group type.|/type|/properties/type|
|--external_id|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

```
```

```
```

```
```

```
```
### apimgmt group update

update a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display_name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description.|/description|/properties/description|
|--type|str|Group type.|/type|/properties/type|
|--external_id|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

```
```

```
```

```
```

```
```
### apimgmt group delete

delete a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

```
```

```
```

```
```

```
```
### apimgmt group list

list a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```
### apimgmt group show

show a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

```
```

```
```

```
```

```
```
## apimgmt group user

### apimgmt group user create

create a apimgmt group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|--state|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|list|Collection of user identities.|/identities|/properties/identities|
|--first_name|str|First name.|/first_name|/properties/firstName|
|--last_name|str|Last name.|/last_name|/properties/lastName|
|--email|str|Email address.|/email|/properties/email|
|--registration_date|datetime|Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>|/registration_date|/properties/registrationDate|
|--groups|list|Collection of groups user is part of.|/groups|/properties/groups|

```
```

```
```
### apimgmt group user delete

delete a apimgmt group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

```
```

```
```
### apimgmt group user list

list a apimgmt group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

```
```

```
```
## apimgmt identityprovider

### apimgmt identityprovider create

create a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
|**--client_id**|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/client_id|/properties/clientId|
|**--client_secret**|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/client_secret|/properties/clientSecret|
|--type|str|Identity Provider Type identifier.|/type|/properties/type|
|--allowed_tenants|list|List of Allowed Tenants when configuring Azure Active Directory login.|/allowed_tenants|/properties/allowedTenants|
|--authority|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/authority|/properties/authority|
|--signup_policy_name|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/signup_policy_name|/properties/signupPolicyName|
|--signin_policy_name|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/signin_policy_name|/properties/signinPolicyName|
|--profile_editing_policy_name|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/profile_editing_policy_name|/properties/profileEditingPolicyName|
|--password_reset_policy_name|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/password_reset_policy_name|/properties/passwordResetPolicyName|

```
```

```
```

```
```
### apimgmt identityprovider update

update a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
|**--client_id**|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/client_id|/properties/clientId|
|**--client_secret**|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/client_secret|/properties/clientSecret|
|--type|str|Identity Provider Type identifier.|/type|/properties/type|
|--allowed_tenants|list|List of Allowed Tenants when configuring Azure Active Directory login.|/allowed_tenants|/properties/allowedTenants|
|--authority|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/authority|/properties/authority|
|--signup_policy_name|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/signup_policy_name|/properties/signupPolicyName|
|--signin_policy_name|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/signin_policy_name|/properties/signinPolicyName|
|--profile_editing_policy_name|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/profile_editing_policy_name|/properties/profileEditingPolicyName|
|--password_reset_policy_name|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/password_reset_policy_name|/properties/passwordResetPolicyName|

```
```

```
```

```
```
### apimgmt identityprovider delete

delete a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|

```
```

```
```

```
```
### apimgmt identityprovider list

list a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt identityprovider show

show a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|

```
```

```
```

```
```
## apimgmt logger

### apimgmt logger create

create a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--logger_id**|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
|**--logger_type**|str|Logger type.|/logger_type|/properties/loggerType|
|**--credentials**|unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/credentials|/properties/credentials|
|--description|str|Logger description.|/description|/properties/description|
|--is_buffered|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/is_buffered|/properties/isBuffered|
|--resource_id|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/resource_id|/properties/resourceId|

```
```

```
```

```
```

```
```
### apimgmt logger update

update a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--logger_id**|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
|**--logger_type**|str|Logger type.|/logger_type|/properties/loggerType|
|**--credentials**|unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/credentials|/properties/credentials|
|--description|str|Logger description.|/description|/properties/description|
|--is_buffered|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/is_buffered|/properties/isBuffered|
|--resource_id|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/resource_id|/properties/resourceId|

```
```

```
```

```
```

```
```
### apimgmt logger delete

delete a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--logger_id**|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|

```
```

```
```

```
```

```
```
### apimgmt logger list

list a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```
### apimgmt logger show

show a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--logger_id**|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|

```
```

```
```

```
```

```
```
## apimgmt notification

### apimgmt notification create

create a apimgmt notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--title**|str|Title of the Notification.|/title|/properties/title|
|--description|str|Description of the Notification.|/description|/properties/description|
|--recipients|dict|Recipient Parameter values.|/recipients|/properties/recipients|

```
```
### apimgmt notification update

update a apimgmt notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--title**|str|Title of the Notification.|/title|/properties/title|
|--description|str|Description of the Notification.|/description|/properties/description|
|--recipients|dict|Recipient Parameter values.|/recipients|/properties/recipients|

```
```
### apimgmt notification list

list a apimgmt notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```
### apimgmt notification show

show a apimgmt notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Notification Name Identifier.|notification_name|notificationName|

```
```
## apimgmt notification recipientemail

### apimgmt notification recipientemail create

create a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--email**|default|Email identifier.|email|email|

```
```

```
```
### apimgmt notification recipientemail update

update a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--email**|default|Email identifier.|email|email|

```
```

```
```
### apimgmt notification recipientemail delete

delete a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--email**|default|Email identifier.|email|email|

```
```

```
```
### apimgmt notification recipientemail list

list a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|

```
```

```
```
## apimgmt notification recipientuser

### apimgmt notification recipientuser create

create a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

```
```

```
```
### apimgmt notification recipientuser update

update a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

```
```

```
```
### apimgmt notification recipientuser delete

delete a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

```
```

```
```
### apimgmt notification recipientuser list

list a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|

```
```

```
```
## apimgmt openidconnectprovider

### apimgmt openidconnectprovider create

create a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--opid**|default|Identifier of the OpenID Connect Provider.|opid|opid|
|**--display_name**|str|User-friendly OpenID Connect Provider name.|/display_name|/properties/displayName|
|**--metadata_endpoint**|str|Metadata endpoint URI.|/metadata_endpoint|/properties/metadataEndpoint|
|**--client_id**|str|Client ID of developer console which is the client application.|/client_id|/properties/clientId|
|--description|str|User-friendly description of OpenID Connect Provider.|/description|/properties/description|
|--client_secret|str|Client Secret of developer console which is the client application.|/client_secret|/properties/clientSecret|

```
```

```
```

```
```
### apimgmt openidconnectprovider update

update a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--opid**|default|Identifier of the OpenID Connect Provider.|opid|opid|
|**--display_name**|str|User-friendly OpenID Connect Provider name.|/display_name|/properties/displayName|
|**--metadata_endpoint**|str|Metadata endpoint URI.|/metadata_endpoint|/properties/metadataEndpoint|
|**--client_id**|str|Client ID of developer console which is the client application.|/client_id|/properties/clientId|
|--description|str|User-friendly description of OpenID Connect Provider.|/description|/properties/description|
|--client_secret|str|Client Secret of developer console which is the client application.|/client_secret|/properties/clientSecret|

```
```

```
```

```
```
### apimgmt openidconnectprovider delete

delete a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--opid**|default|Identifier of the OpenID Connect Provider.|opid|opid|

```
```

```
```

```
```
### apimgmt openidconnectprovider list

list a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt openidconnectprovider show

show a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--opid**|default|Identifier of the OpenID Connect Provider.|opid|opid|

```
```

```
```

```
```
## apimgmt policy

### apimgmt policy create

create a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```
### apimgmt policy update

update a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```
### apimgmt policy delete

delete a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

```
```

```
```
### apimgmt policy list

list a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```
### apimgmt policy show

show a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|--format|default|Format of the policyContent.|/format|/properties/format|

```
```

```
```
## apimgmt portalsetting

### apimgmt portalsetting create

create a apimgmt portalsetting.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|
|--url|str|A delegation Url.|/url|/properties/url|
|--validation_key|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/validation_key|/properties/validationKey|
|--subscriptions|dict|Subscriptions delegation settings.|/subscriptions|/properties/subscriptions|
|--user_registration|dict|User registration delegation settings.|/user_registration|/properties/userRegistration|

```
```

```
```
### apimgmt portalsetting update

update a apimgmt portalsetting.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|
|--url|str|A delegation Url.|/url|/properties/url|
|--validation_key|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/validation_key|/properties/validationKey|
|--subscriptions|dict|Subscriptions delegation settings.|/subscriptions|/properties/subscriptions|
|--user_registration|dict|User registration delegation settings.|/user_registration|/properties/userRegistration|

```
```

```
```
### apimgmt portalsetting show

show a apimgmt portalsetting.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```
## apimgmt product

### apimgmt product create

create a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--display_name**|str|Product name.|/display_name|/properties/displayName|
|--description|str|Product description. May include HTML formatting tags.|/description|/properties/description|
|--terms|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/terms|/properties/terms|
|--subscription_required|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/subscription_required|/properties/subscriptionRequired|
|--approval_required|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/approval_required|/properties/approvalRequired|
|--subscriptions_limit|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/subscriptions_limit|/properties/subscriptionsLimit|
|--state|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/state|/properties/state|

```
```

```
```

```
```
### apimgmt product update

update a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--display_name**|str|Product name.|/display_name|/properties/displayName|
|--description|str|Product description. May include HTML formatting tags.|/description|/properties/description|
|--terms|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/terms|/properties/terms|
|--subscription_required|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/subscription_required|/properties/subscriptionRequired|
|--approval_required|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/approval_required|/properties/approvalRequired|
|--subscriptions_limit|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/subscriptions_limit|/properties/subscriptionsLimit|
|--state|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/state|/properties/state|

```
```

```
```

```
```
### apimgmt product delete

delete a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

```
```

```
```

```
```
### apimgmt product list

list a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt product show

show a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

```
```

```
```

```
```
## apimgmt product api

### apimgmt product api create

create a apimgmt product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api_revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--is_online|boolean|Indicates if API revision is accessible via the gateway.|/is_online|/properties/isOnline|
|--api_revision_description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|dict|Version set details|/api_version_set|/properties/apiVersionSet|

```
```

```
```
### apimgmt product api update

update a apimgmt product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api_revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--is_online|boolean|Indicates if API revision is accessible via the gateway.|/is_online|/properties/isOnline|
|--api_revision_description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|dict|Version set details|/api_version_set|/properties/apiVersionSet|

```
```

```
```
### apimgmt product api delete

delete a apimgmt product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

```
```

```
```
### apimgmt product api list

list a apimgmt product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

```
```

```
```
## apimgmt product group

### apimgmt product group create

create a apimgmt product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display_name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description. Can contain HTML formatting tags.|/description|/properties/description|
|--built_in|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/built_in|/properties/builtIn|
|--type|str|Group type.|/type|/properties/type|
|--external_id|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

```
```

```
```
### apimgmt product group update

update a apimgmt product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display_name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description. Can contain HTML formatting tags.|/description|/properties/description|
|--built_in|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/built_in|/properties/builtIn|
|--type|str|Group type.|/type|/properties/type|
|--external_id|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

```
```

```
```
### apimgmt product group delete

delete a apimgmt product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

```
```

```
```
### apimgmt product group list

list a apimgmt product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

```
```

```
```
## apimgmt product policy

### apimgmt product policy create

create a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```
### apimgmt product policy update

update a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

```
```

```
```
### apimgmt product policy delete

delete a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

```
```

```
```
### apimgmt product policy list

list a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

```
```

```
```
### apimgmt product policy show

show a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|--format|default|Format of the policyContent.|/format|/properties/format|

```
```

```
```
## apimgmt property

### apimgmt property create

create a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--prop_id**|default|Identifier of the property.|prop_id|propId|
|**--display_name**|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/display_name|/properties/displayName|
|**--value**|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/value|/properties/value|
|--tags|list|Optional tags that when provided can be used to filter the property list.|/tags|/properties/tags|
|--secret|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/secret|/properties/secret|

```
```

```
```

```
```
### apimgmt property update

update a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--prop_id**|default|Identifier of the property.|prop_id|propId|
|**--display_name**|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/display_name|/properties/displayName|
|**--value**|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/value|/properties/value|
|--tags|list|Optional tags that when provided can be used to filter the property list.|/tags|/properties/tags|
|--secret|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/secret|/properties/secret|

```
```

```
```

```
```
### apimgmt property delete

delete a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--prop_id**|default|Identifier of the property.|prop_id|propId|

```
```

```
```

```
```
### apimgmt property list

list a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt property show

show a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--prop_id**|default|Identifier of the property.|prop_id|propId|

```
```

```
```

```
```
## apimgmt subscription

### apimgmt subscription create

create a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--sid**|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
|**--scope**|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/scope|/properties/scope|
|**--display_name**|str|Subscription name.|/display_name|/properties/displayName|
|--notify|default|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |notify|notify|
|--owner_id|str|User (user id path) for whom subscription is being created in form /users/{userId}|/owner_id|/properties/ownerId|
|--primary_key|str|Primary subscription key. If not specified during request key will be generated automatically.|/primary_key|/properties/primaryKey|
|--secondary_key|str|Secondary subscription key. If not specified during request key will be generated automatically.|/secondary_key|/properties/secondaryKey|
|--state|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/state|/properties/state|
|--allow_tracing|boolean|Determines whether tracing can be enabled|/allow_tracing|/properties/allowTracing|

```
```

```
```

```
```
### apimgmt subscription update

update a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--sid**|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
|**--scope**|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/scope|/properties/scope|
|**--display_name**|str|Subscription name.|/display_name|/properties/displayName|
|--notify|default|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |notify|notify|
|--owner_id|str|User (user id path) for whom subscription is being created in form /users/{userId}|/owner_id|/properties/ownerId|
|--primary_key|str|Primary subscription key. If not specified during request key will be generated automatically.|/primary_key|/properties/primaryKey|
|--secondary_key|str|Secondary subscription key. If not specified during request key will be generated automatically.|/secondary_key|/properties/secondaryKey|
|--state|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/state|/properties/state|
|--allow_tracing|boolean|Determines whether tracing can be enabled|/allow_tracing|/properties/allowTracing|

```
```

```
```

```
```
### apimgmt subscription delete

delete a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--sid**|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|

```
```

```
```

```
```
### apimgmt subscription list

list a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt subscription show

show a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--sid**|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|

```
```

```
```

```
```
## apimgmt tag

### apimgmt tag create

create a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|**--display_name**|str|Tag name.|/display_name|/properties/displayName|

```
```

```
```

```
```
### apimgmt tag update

update a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|**--display_name**|str|Tag name.|/display_name|/properties/displayName|

```
```

```
```

```
```
### apimgmt tag delete

delete a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

```
```

```
```

```
```
### apimgmt tag list

list a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```
### apimgmt tag show

show a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

```
```

```
```

```
```
## apimgmt template

### apimgmt template create

create a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Email Template Name Identifier.|template_name|templateName|
|--subject|str|Subject of the Template.|/subject|/properties/subject|
|--title|str|Title of the Template.|/title|/properties/title|
|--description|str|Description of the Email Template.|/description|/properties/description|
|--body|str|Email Template Body. This should be a valid XDocument|/body|/properties/body|

```
```

```
```

```
```
### apimgmt template update

update a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Email Template Name Identifier.|template_name|templateName|
|--subject|str|Subject of the Template.|/subject|/properties/subject|
|--title|str|Title of the Template.|/title|/properties/title|
|--description|str|Description of the Email Template.|/description|/properties/description|
|--body|str|Email Template Body. This should be a valid XDocument|/body|/properties/body|

```
```

```
```

```
```
### apimgmt template delete

delete a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Email Template Name Identifier.|template_name|templateName|

```
```

```
```

```
```
### apimgmt template list

list a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt template show

show a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Email Template Name Identifier.|template_name|templateName|

```
```

```
```

```
```
## apimgmt user

### apimgmt user create

create a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|**--email**|str|Email address. Must not be empty and must be unique within the service instance.|/email|/properties/email|
|**--first_name**|str|First name.|/first_name|/properties/firstName|
|**--last_name**|str|Last name.|/last_name|/properties/lastName|
|--state|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|list|Collection of user identities.|/identities|/properties/identities|
|--password|str|User Password. If no value is provided, a default password is generated.|/password|/properties/password|
|--confirmation|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/confirmation|/properties/confirmation|

```
```

```
```

```
```
### apimgmt user update

update a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|**--email**|str|Email address. Must not be empty and must be unique within the service instance.|/email|/properties/email|
|**--first_name**|str|First name.|/first_name|/properties/firstName|
|**--last_name**|str|Last name.|/last_name|/properties/lastName|
|--state|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|list|Collection of user identities.|/identities|/properties/identities|
|--password|str|User Password. If no value is provided, a default password is generated.|/password|/properties/password|
|--confirmation|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/confirmation|/properties/confirmation|

```
```

```
```

```
```
### apimgmt user delete

delete a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

```
```

```
```

```
```
### apimgmt user list

list a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

```
```

```
```

```
```
### apimgmt user show

show a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

```
```

```
```

```
```