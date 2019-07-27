# Azure CLI Module Creation Report

## apim

### apim create

create a apim.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|**--publisher-email**|str|Publisher email.|/publisher_email|/properties/publisherEmail|
|**--publisher-name**|str|Publisher name.|/publisher_name|/properties/publisherName|
|**--sku-name**|str|Name of the Sku.|/sku/name|/sku/name|
|**--location**|str|Resource location.|/location|/location|
|--tags|dictionary|Resource tags.|/tags|/tags|
|--notification-sender-email|str|Email address from which the notification will be sent.|/notification_sender_email|/properties/notificationSenderEmail|
|--hostname-configurations|list|Custom hostname configuration of the API Management service.|/hostname_configurations|/properties/hostnameConfigurations|
|--virtual-network-configuration|dict|Virtual network configuration of the API Management service.|/virtual_network_configuration|/properties/virtualNetworkConfiguration|
|--additional-locations|list|Additional datacenter locations of the API Management service.|/additional_locations|/properties/additionalLocations|
|--custom-properties|dictionary|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.</br></br>You can disable any of next ciphers by using settings `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]`: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256`:`false`. The default value is `true` for them.|/custom_properties|/properties/customProperties|
|--certificates|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/certificates|/properties/certificates|
|--enable-client-certificate|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/enable_client_certificate|/properties/enableClientCertificate|
|--virtual-network-type|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/virtual_network_type|/properties/virtualNetworkType|
|--sku-capacity|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|/sku/capacity|
|--identity|dict|Managed service identity of the Api Management service.|/identity|/identity|

**Example: ApiManagementCreateService**

```
apim create --resource-group rg1
        --name apimService1
        --publisher-email apim@autorestsdk.com
        --publisher-name autorestsdk
        --sku-name Developer
        --sku-capacity 1
        --location "Central US"
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apim create --resource-group rg1
        --name apimService1
        --virtual-network-type External
        --publisher-email admin@live.com
        --publisher-name contoso
        --sku-name Premium
        --sku-capacity 1
        --location "Central US"
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apim create --resource-group rg1
        --name apimService1
        --publisher-email apim@autorestsdk.com
        --publisher-name autorestsdk
        --sku-name Consumption
        --location "West US"
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apim create --resource-group rg1
        --name apimService1
        --publisher-email apim@autorestsdk.com
        --publisher-name autorestsdk
        --sku-name Basic
        --sku-capacity 1
        --location "Central US"
```
### apim update

update a apim.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|**--publisher-email**|str|Publisher email.|/publisher_email|/properties/publisherEmail|
|**--publisher-name**|str|Publisher name.|/publisher_name|/properties/publisherName|
|**--sku-name**|str|Name of the Sku.|/sku/name|/sku/name|
|**--location**|str|Resource location.|/location|/location|
|--tags|dictionary|Resource tags.|/tags|/tags|
|--notification-sender-email|str|Email address from which the notification will be sent.|/notification_sender_email|/properties/notificationSenderEmail|
|--hostname-configurations|list|Custom hostname configuration of the API Management service.|/hostname_configurations|/properties/hostnameConfigurations|
|--virtual-network-configuration|dict|Virtual network configuration of the API Management service.|/virtual_network_configuration|/properties/virtualNetworkConfiguration|
|--additional-locations|list|Additional datacenter locations of the API Management service.|/additional_locations|/properties/additionalLocations|
|--custom-properties|dictionary|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.</br></br>You can disable any of next ciphers by using settings `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]`: TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA. For example, `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256`:`false`. The default value is `true` for them.|/custom_properties|/properties/customProperties|
|--certificates|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/certificates|/properties/certificates|
|--enable-client-certificate|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/enable_client_certificate|/properties/enableClientCertificate|
|--virtual-network-type|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/virtual_network_type|/properties/virtualNetworkType|
|--sku-capacity|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|/sku/capacity|
|--identity|dict|Managed service identity of the Api Management service.|/identity|/identity|

**Example: ApiManagementUpdateServiceDisableTls10**

```
apim update --resource-group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apim update --resource-group rg1
        --name apimService1
        --publisher-email foobar@live.com
        --publisher-name "Contoso Vnext"
```
### apim delete

delete a apim.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementServiceDeleteService**

```
apim delete --resource-group rg1
        --name apimService1
```
### apim list

list a apim.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
### apim show

show a apim.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
## apim api

### apim api create

create a apim api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication-settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription-key-parameter-names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api-revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api-version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is-current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--api-revision-description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api-version-description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api-version-set-id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription-required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source-api-id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display-name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service-url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api-version-set|dict|Version set details|/api_version_set|/properties/apiVersionSet|
|--value|str|Content value when Importing an API.|/value|/properties/value|
|--format|str|Format of the Content in which the API is getting imported.|/format|/properties/format|
|--wsdl-selector|dict|Criteria to limit import of WSDL to a subset of the document.|/wsdl_selector|/properties/wsdlSelector|
|--api-type|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/api_type|/properties/apiType|

**Example: ApiManagementCreateApiUsingOai3Import**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id petstore
        --path petstore
        --value https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml
        --format openapi-link
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id petstore
        --path petstore
        --value http://petstore.swagger.io/v2/swagger.json
        --format swagger-link-json
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id petstore
        --path collector
        --value https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl
        --format wadl-link-json
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id soapApi
        --path currency
        --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL
        --format wsdl-link
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id soapApi
        --path currency
        --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL
        --format wsdl-link
        --api-type soap
```

**Example: ApiManagementCreateApi**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id tempgroup
        --description apidescription5200
        --display-name apiname1463
        --service-url http://newechoapi.cloudapp.net/api
        --path newapiPath
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id echo-api;rev=3
        --api-revision-description "Creating a Revision of an existing API"
        --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --service-url http://echoapi.cloudapp.net/apiv3
        --path echo
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id echoapiv3
        --description "Create Echo API into a new Version using Existing Version Set and Copy all Operations."
        --api-version v4
        --is-current true
        --api-version-set-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }}"
        --subscription-required true
        --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --display-name "Echo API2"
        --service-url http://echoapi.cloudapp.net/api
        --path echo2
```

**Example: ApiManagementCreateApiClone**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id echo-api2
        --description "Copy of Existing Echo Api including Operations."
        --is-current true
        --subscription-required true
        --source-api-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --display-name "Echo API2"
        --service-url http://echoapi.cloudapp.net/api
        --path echo2
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apim api create --resource-group rg1
        --service-name apimService1
        --api-id tempgroup
        --description "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters."
        --display-name "Swagger Petstore"
        --service-url http://petstore.swagger.io/v2
        --path petstore
```
### apim api update

update a apim api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication-settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription-key-parameter-names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api-revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api-version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is-current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--api-revision-description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api-version-description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api-version-set-id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription-required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source-api-id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display-name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service-url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api-version-set|dict|Version set details|/api_version_set|/properties/apiVersionSet|
|--value|str|Content value when Importing an API.|/value|/properties/value|
|--format|str|Format of the Content in which the API is getting imported.|/format|/properties/format|
|--wsdl-selector|dict|Criteria to limit import of WSDL to a subset of the document.|/wsdl_selector|/properties/wsdlSelector|
|--api-type|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/api_type|/properties/apiType|

**Example: ApiManagementUpdateApi**

```
apim api update --resource-group rg1
        --service-name apimService1
        --api-id echo-api
        --display-name "Echo API New"
        --service-url http://echoapi.cloudapp.net/api2
        --path newecho
```
### apim api delete

delete a apim api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementDeleteApi**

```
apim api delete --resource-group rg1
        --service-name apimService1
        --api-id echo-api
```
### apim api list

list a apim api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim api show

show a apim api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
## apim api diagnostic

### apim api diagnostic create

create a apim api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger-id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always-log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable-http-correlation-headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

**Example: ApiManagementCreateApiDiagnostic**

```
apim api diagnostic create --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --diagnostic-id applicationinsights
        --always-log allErrors
        --logger-id /loggers/applicationinsights
```
### apim api diagnostic update

update a apim api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger-id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always-log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable-http-correlation-headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

**Example: ApiManagementUpdateApiDiagnostic**

```
apim api diagnostic update --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --diagnostic-id applicationinsights
        --always-log allErrors
        --logger-id /loggers/applicationinsights
```
### apim api diagnostic delete

delete a apim api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

**Example: ApiManagementDeleteApiDiagnostic**

```
apim api diagnostic delete --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --diagnostic-id applicationinsights
```
### apim api diagnostic list

list a apim api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
### apim api diagnostic show

show a apim api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
## apim api issue

### apim api issue create

create a apim api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--title**|str|The issue title.|/title|/properties/title|
|**--description**|str|Text describing the issue.|/description|/properties/description|
|**--user-id**|str|A resource identifier for the user created the issue.|/user_id|/properties/userId|
|--created-date|datetime|Date and time when the issue was created.|/created_date|/properties/createdDate|
|--state|str|Status of the issue.|/state|/properties/state|

**Example: ApiManagementCreateApiIssue**

```
apim api issue create --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
        --created-date 2018-02-01T22:21:20.467Z
        --state open
        --title "New API issue"
        --description "New API issue description"
        --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
```
### apim api issue update

update a apim api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--title**|str|The issue title.|/title|/properties/title|
|**--description**|str|Text describing the issue.|/description|/properties/description|
|**--user-id**|str|A resource identifier for the user created the issue.|/user_id|/properties/userId|
|--created-date|datetime|Date and time when the issue was created.|/created_date|/properties/createdDate|
|--state|str|Status of the issue.|/state|/properties/state|

**Example: ApiManagementUpdateApiIssue**

```
apim api issue update --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
        --state closed
```
### apim api issue delete

delete a apim api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

**Example: ApiManagementDeleteApiIssue**

```
apim api issue delete --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
```
### apim api issue list

list a apim api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
### apim api issue show

show a apim api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
## apim api issue attachment

### apim api issue attachment create

create a apim api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment-id**|str|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
|**--title**|str|Filename by which the binary data will be saved.|/title|/properties/title|
|**--content-format**|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/content_format|/properties/contentFormat|
|**--content**|str|An HTTP link or Base64-encoded binary data.|/content|/properties/content|

**Example: ApiManagementCreateApiIssueAttachment**

```
apim api issue attachment create --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
        --attachment-id 57d2ef278aa04f0888cba3f3
        --title "Issue attachment."
        --content-format image/jpeg
        --content IEJhc2U2NA==
```
### apim api issue attachment update

update a apim api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment-id**|str|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
|**--title**|str|Filename by which the binary data will be saved.|/title|/properties/title|
|**--content-format**|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/content_format|/properties/contentFormat|
|**--content**|str|An HTTP link or Base64-encoded binary data.|/content|/properties/content|
### apim api issue attachment delete

delete a apim api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment-id**|str|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|

**Example: ApiManagementDeleteApiIssueAttachment**

```
apim api issue attachment delete --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
        --attachment-id 57d2ef278aa04f0888cba3f3
```
### apim api issue attachment list

list a apim api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
### apim api issue attachment show

show a apim api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--attachment-id**|str|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
## apim api issue comment

### apim api issue comment create

create a apim api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment-id**|str|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
|**--text**|str|Comment text.|/text|/properties/text|
|**--user-id**|str|A resource identifier for the user who left the comment.|/user_id|/properties/userId|
|--created-date|datetime|Date and time when the comment was created.|/created_date|/properties/createdDate|

**Example: ApiManagementCreateApiIssueComment**

```
apim api issue comment create --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
        --comment-id 599e29ab193c3c0bd0b3e2fb
        --text "Issue comment."
        --created-date 2018-02-01T22:21:20.467Z
        --user-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
```
### apim api issue comment update

update a apim api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment-id**|str|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
|**--text**|str|Comment text.|/text|/properties/text|
|**--user-id**|str|A resource identifier for the user who left the comment.|/user_id|/properties/userId|
|--created-date|datetime|Date and time when the comment was created.|/created_date|/properties/createdDate|
### apim api issue comment delete

delete a apim api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment-id**|str|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|

**Example: ApiManagementDeleteApiIssueComment**

```
apim api issue comment delete --resource-group rg1
        --service-name apimService1
        --api-id 57d1f7558aa04f15146d9d8a
        --issue-id 57d2ef278aa04f0ad01d6cdc
        --comment-id 599e29ab193c3c0bd0b3e2fb
```
### apim api issue comment list

list a apim api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
### apim api issue comment show

show a apim api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue-id**|str|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|**--comment-id**|str|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
## apim api operation

### apim api operation create

create a apim api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--display-name**|str|Operation Name.|/display_name|/properties/displayName|
|**--method**|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/method|/properties/method|
|**--url-template**|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/url_template|/properties/urlTemplate|
|--template-parameters|list|Collection of URL template parameters.|/template_parameters|/properties/templateParameters|
|--description|str|Description of the operation. May include HTML formatting tags.|/description|/properties/description|
|--request|dict|An entity containing request details.|/request|/properties/request|
|--responses|list|Array of Operation responses.|/responses|/properties/responses|
|--policies|str|Operation Policies|/policies|/properties/policies|

**Example: ApiManagementCreateApiOperation**

```
apim api operation create --resource-group rg1
        --service-name apimService1
        --api-id PetStoreTemplate2
        --operation-id newoperations
        --description "This can only be done by the logged in user."
        --display-name createUser2
        --method POST
        --url-template /user1
```
### apim api operation update

update a apim api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--display-name**|str|Operation Name.|/display_name|/properties/displayName|
|**--method**|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/method|/properties/method|
|**--url-template**|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/url_template|/properties/urlTemplate|
|--template-parameters|list|Collection of URL template parameters.|/template_parameters|/properties/templateParameters|
|--description|str|Description of the operation. May include HTML formatting tags.|/description|/properties/description|
|--request|dict|An entity containing request details.|/request|/properties/request|
|--responses|list|Array of Operation responses.|/responses|/properties/responses|
|--policies|str|Operation Policies|/policies|/properties/policies|

**Example: ApiManagementUpdateApiOperation**

```
apim api operation update --resource-group rg1
        --service-name apimService1
        --api-id echo-api
        --operation-id operationId
        --display-name "Retrieve resource"
        --method GET
        --url-template /resource
```
### apim api operation delete

delete a apim api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

**Example: ApiManagementDeleteApiOperation**

```
apim api operation delete --resource-group rg1
        --service-name apimService1
        --api-id 57d2ef278aa04f0888cba3f3
        --operation-id 57d2ef278aa04f0ad01d6cdc
```
### apim api operation list

list a apim api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apim api operation show

show a apim api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
## apim api operation policy

### apim api operation policy create

create a apim api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

**Example: ApiManagementCreateApiOperationPolicy**

```
apim api operation policy create --resource-group rg1
        --service-name apimService1
        --api-id 5600b57e7e8880006a040001
        --operation-id 5600b57e7e8880006a080001
        --policy-id policy
        --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
        --format xml
```
### apim api operation policy update

update a apim api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|
### apim api operation policy delete

delete a apim api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementDeleteApiOperationPolicy**

```
apim api operation policy delete --resource-group rg1
        --service-name apimService1
        --api-id testapi
        --operation-id testoperation
        --policy-id policy
```
### apim api operation policy list

list a apim api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
### apim api operation policy show

show a apim api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation-id**|str|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|--format|str|Format of the policyContent.|/format|/properties/format|
## apim api policy

### apim api policy create

create a apim api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

**Example: ApiManagementCreateApiPolicy**

```
apim api policy create --resource-group rg1
        --service-name apimService1
        --api-id 5600b57e7e8880006a040001
        --policy-id policy
        --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
        --format xml
```

**Example: ApiManagementCreateApiPolicyNonXmlEncoded**

```
apim api policy create --resource-group rg1
        --service-name apimService1
        --api-id 5600b57e7e8880006a040001
        --policy-id policy
        --value "<policies>
     <inbound>
     <base />
  <set-header name=\"newvalue" exists-action="override">
   <value>"@(context.Request.Headers.FirstOrDefault(h => h.Ke=="Via"))" </value>
    </set-header>
  </inbound>
      </policies>"
        --format rawxml
```
### apim api policy update

update a apim api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|
### apim api policy delete

delete a apim api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementDeleteApiPolicy**

```
apim api policy delete --resource-group rg1
        --service-name apimService1
        --api-id loggerId
        --policy-id policy
```
### apim api policy list

list a apim api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apim api policy show

show a apim api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|--format|str|Format of the policyContent.|/format|/properties/format|
## apim api release

### apim api release create

create a apim api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release-id**|str|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
|--notes|str|Release Notes|/notes|/properties/notes|

**Example: ApiManagementCreateApiRelease**

```
apim api release create --resource-group rg1
        --service-name apimService1
        --api-id a1
        --release-id testrev
        --notes yahooagain
```
### apim api release update

update a apim api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release-id**|str|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
|--notes|str|Release Notes|/notes|/properties/notes|

**Example: ApiManagementUpdateApiRelease**

```
apim api release update --resource-group rg1
        --service-name apimService1
        --api-id a1
        --release-id testrev
        --notes yahooagain
```
### apim api release delete

delete a apim api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release-id**|str|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|

**Example: ApiManagementDeleteApiRelease**

```
apim api release delete --resource-group rg1
        --service-name apimService1
        --api-id 5a5fcc09124a7fa9b89f2f1d
        --release-id testrev
```
### apim api release list

list a apim api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
### apim api release show

show a apim api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release-id**|str|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
## apim api schema

### apim api schema create

create a apim api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema-id**|str|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
|**--content-type**|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/content_type|/properties/contentType|
|--document|dict|Create or update Properties of the Schema Document.|/document|/properties/document|

**Example: ApiManagementCreateApiSchema**

```
apim api schema create --resource-group rg1
        --service-name apimService1
        --api-id 59d6bb8f1f7fab13dc67ec9b
        --schema-id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
        --content-type application/vnd.ms-azure-apim.xsd+xml
```
### apim api schema update

update a apim api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema-id**|str|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
|**--content-type**|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/content_type|/properties/contentType|
|--document|dict|Create or update Properties of the Schema Document.|/document|/properties/document|
### apim api schema delete

delete a apim api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema-id**|str|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|

**Example: ApiManagementDeleteApiSchema**

```
apim api schema delete --resource-group rg1
        --service-name apimService1
        --api-id 59d5b28d1f7fab116c282650
        --schema-id 59d5b28e1f7fab116402044e
```
### apim api schema list

list a apim api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apim api schema show

show a apim api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema-id**|str|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
## apim api tag-description

### apim api tag-description create

create a apim api tag-description.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--description|str|Description of the Tag.|/description|/properties/description|
|--external-docs-url|str|Absolute URL of external resources describing the tag.|/external_docs_url|/properties/externalDocsUrl|
|--external-docs-description|str|Description of the external resources describing the tag.|/external_docs_description|/properties/externalDocsDescription|

**Example: ApiManagementCreateApiTagDescription**

```
apim api tag-description create --resource-group rg1
        --service-name apimService1
        --api-id 5931a75ae4bbd512a88c680b
        --tag-id tagId1
        --description "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API"
        --external-docs-url http://some.url/additionaldoc
        --external-docs-description "Description of the external docs resource"
```
### apim api tag-description update

update a apim api tag-description.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--description|str|Description of the Tag.|/description|/properties/description|
|--external-docs-url|str|Absolute URL of external resources describing the tag.|/external_docs_url|/properties/externalDocsUrl|
|--external-docs-description|str|Description of the external resources describing the tag.|/external_docs_description|/properties/externalDocsDescription|
### apim api tag-description delete

delete a apim api tag-description.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

**Example: ApiManagementDeleteApiTagDescription**

```
apim api tag-description delete --resource-group rg1
        --service-name apimService1
        --api-id 59d5b28d1f7fab116c282650
        --tag-id 59d5b28e1f7fab116402044e
```
### apim api tag-description list

list a apim api tag-description.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apim api tag-description show

show a apim api tag-description.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
## apim api-version-set

### apim api-version-set create

create a apim api-version-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--version-set-id**|str|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
|**--display-name**|str|Name of API Version Set|/display_name|/properties/displayName|
|**--versioning-scheme**|str|An value that determines where the API Version identifer will be located in a HTTP request.|/versioning_scheme|/properties/versioningScheme|
|--description|str|Description of API Version Set.|/description|/properties/description|
|--version-query-name|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/version_query_name|/properties/versionQueryName|
|--version-header-name|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/version_header_name|/properties/versionHeaderName|

**Example: ApiManagementCreateApiVersionSet**

```
apim api-version-set create --resource-group rg1
        --service-name apimService1
        --version-set-id api1
        --description "Version configuration"
        --display-name "api set 1"
        --versioning-scheme Segment
```
### apim api-version-set update

update a apim api-version-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--version-set-id**|str|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
|**--display-name**|str|Name of API Version Set|/display_name|/properties/displayName|
|**--versioning-scheme**|str|An value that determines where the API Version identifer will be located in a HTTP request.|/versioning_scheme|/properties/versioningScheme|
|--description|str|Description of API Version Set.|/description|/properties/description|
|--version-query-name|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/version_query_name|/properties/versionQueryName|
|--version-header-name|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/version_header_name|/properties/versionHeaderName|

**Example: ApiManagementUpdateApiVersionSet**

```
apim api-version-set update --resource-group rg1
        --service-name apimService1
        --version-set-id api1
        --description "Version configuration"
        --display-name "api set 1"
        --versioning-scheme Segment
```
### apim api-version-set delete

delete a apim api-version-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--version-set-id**|str|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|

**Example: ApiManagementDeleteApiVersionSet**

```
apim api-version-set delete --resource-group rg1
        --service-name apimService1
        --version-set-id a1
```
### apim api-version-set list

list a apim api-version-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim api-version-set show

show a apim api-version-set.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--version-set-id**|str|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
## apim authorization-server

### apim authorization-server create

create a apim authorization-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--authsid**|str|Identifier of the authorization server.|authsid|authsid|
|**--display-name**|str|User-friendly authorization server name.|/display_name|/properties/displayName|
|**--client-registration-endpoint**|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/client_registration_endpoint|/properties/clientRegistrationEndpoint|
|**--authorization-endpoint**|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/authorization_endpoint|/properties/authorizationEndpoint|
|**--grant-types**|list|Form of an authorization grant, which the client uses to request the access token.|/grant_types|/properties/grantTypes|
|**--client-id**|str|Client or app id registered with this authorization server.|/client_id|/properties/clientId|
|--description|str|Description of the authorization server. Can contain HTML formatting tags.|/description|/properties/description|
|--authorization-methods|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/authorization_methods|/properties/authorizationMethods|
|--client-authentication-method|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/client_authentication_method|/properties/clientAuthenticationMethod|
|--token-body-parameters|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/token_body_parameters|/properties/tokenBodyParameters|
|--token-endpoint|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/token_endpoint|/properties/tokenEndpoint|
|--support-state|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/support_state|/properties/supportState|
|--default-scope|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/default_scope|/properties/defaultScope|
|--bearer-token-sending-methods|list|Specifies the mechanism by which access token is passed to the API. |/bearer_token_sending_methods|/properties/bearerTokenSendingMethods|
|--client-secret|str|Client or app secret registered with this authorization server.|/client_secret|/properties/clientSecret|
|--resource-owner-username|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/resource_owner_username|/properties/resourceOwnerUsername|
|--resource-owner-password|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/resource_owner_password|/properties/resourceOwnerPassword|

**Example: ApiManagementCreateAuthorizationServer**

```
apim authorization-server create --resource-group rg1
        --service-name apimService1
        --authsid newauthServer
        --description "test server"
        --token-endpoint https://www.contoso.com/oauth2/token
        --support-state true
        --default-scope "read write"
        --client-secret 2
        --resource-owner-username un
        --resource-owner-password pwd
        --display-name test2
        --client-registration-endpoint https://www.contoso.com/apps
        --authorization-endpoint https://www.contoso.com/oauth2/auth
        --client-id 1
```
### apim authorization-server update

update a apim authorization-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--authsid**|str|Identifier of the authorization server.|authsid|authsid|
|**--display-name**|str|User-friendly authorization server name.|/display_name|/properties/displayName|
|**--client-registration-endpoint**|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/client_registration_endpoint|/properties/clientRegistrationEndpoint|
|**--authorization-endpoint**|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/authorization_endpoint|/properties/authorizationEndpoint|
|**--grant-types**|list|Form of an authorization grant, which the client uses to request the access token.|/grant_types|/properties/grantTypes|
|**--client-id**|str|Client or app id registered with this authorization server.|/client_id|/properties/clientId|
|--description|str|Description of the authorization server. Can contain HTML formatting tags.|/description|/properties/description|
|--authorization-methods|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/authorization_methods|/properties/authorizationMethods|
|--client-authentication-method|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/client_authentication_method|/properties/clientAuthenticationMethod|
|--token-body-parameters|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/token_body_parameters|/properties/tokenBodyParameters|
|--token-endpoint|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/token_endpoint|/properties/tokenEndpoint|
|--support-state|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/support_state|/properties/supportState|
|--default-scope|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/default_scope|/properties/defaultScope|
|--bearer-token-sending-methods|list|Specifies the mechanism by which access token is passed to the API. |/bearer_token_sending_methods|/properties/bearerTokenSendingMethods|
|--client-secret|str|Client or app secret registered with this authorization server.|/client_secret|/properties/clientSecret|
|--resource-owner-username|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/resource_owner_username|/properties/resourceOwnerUsername|
|--resource-owner-password|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/resource_owner_password|/properties/resourceOwnerPassword|

**Example: ApiManagementUpdateAuthorizationServer**

```
apim authorization-server update --resource-group rg1
        --service-name apimService1
        --authsid newauthServer
        --client-secret updated
        --client-id update
```
### apim authorization-server delete

delete a apim authorization-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--authsid**|str|Identifier of the authorization server.|authsid|authsid|

**Example: ApiManagementDeleteAuthorizationServer**

```
apim authorization-server delete --resource-group rg1
        --service-name apimService1
        --authsid newauthServer2
```
### apim authorization-server list

list a apim authorization-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim authorization-server show

show a apim authorization-server.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--authsid**|str|Identifier of the authorization server.|authsid|authsid|
## apim backend

### apim backend create

create a apim backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--backend-id**|str|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
|**--url**|str|Runtime Url of the Backend.|/url|/properties/url|
|**--protocol**|str|Backend communication protocol.|/protocol|/properties/protocol|
|--title|str|Backend Title.|/title|/properties/title|
|--description|str|Backend Description.|/description|/properties/description|
|--resource-id|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/resource_id|/properties/resourceId|
|--service-fabric-cluster|dict|Backend Service Fabric Cluster Properties|/service_fabric_cluster|/properties/properties/serviceFabricCluster|
|--credentials|dict|Backend Credentials Contract Properties|/credentials|/properties/credentials|
|--proxy|dict|Backend Proxy Contract Properties|/proxy|/properties/proxy|
|--tls|dict|Backend TLS Properties|/tls|/properties/tls|

**Example: ApiManagementCreateBackendServiceFabric**

```
apim backend create --resource-group rg1
        --service-name apimService1
        --backend-id sfbackend
        --description "Service Fabric Test App 1"
        --url fabric:/mytestapp/mytestservice
        --protocol http
```

**Example: ApiManagementCreateBackendProxyBackend**

```
apim backend create --resource-group rg1
        --service-name apimService1
        --backend-id proxybackend
        --description description5308
        --url https://backendname2644/
        --protocol http
```
### apim backend update

update a apim backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--backend-id**|str|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
|**--url**|str|Runtime Url of the Backend.|/url|/properties/url|
|**--protocol**|str|Backend communication protocol.|/protocol|/properties/protocol|
|--title|str|Backend Title.|/title|/properties/title|
|--description|str|Backend Description.|/description|/properties/description|
|--resource-id|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/resource_id|/properties/resourceId|
|--service-fabric-cluster|dict|Backend Service Fabric Cluster Properties|/service_fabric_cluster|/properties/properties/serviceFabricCluster|
|--credentials|dict|Backend Credentials Contract Properties|/credentials|/properties/credentials|
|--proxy|dict|Backend Proxy Contract Properties|/proxy|/properties/proxy|
|--tls|dict|Backend TLS Properties|/tls|/properties/tls|

**Example: ApiManagementUpdateBackend**

```
apim backend update --resource-group rg1
        --service-name apimService1
        --backend-id proxybackend
        --description description5308
```
### apim backend delete

delete a apim backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--backend-id**|str|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|

**Example: ApiManagementDeleteBackend**

```
apim backend delete --resource-group rg1
        --service-name apimService1
        --backend-id sfbackend
```
### apim backend list

list a apim backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim backend show

show a apim backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--backend-id**|str|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
## apim cache

### apim cache create

create a apim cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--cache-id**|str|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
|**--connection-string**|str|Runtime connection string to cache|/connection_string|/properties/connectionString|
|--description|str|Cache description|/description|/properties/description|
|--resource-id|str|Original uri of entity in external system cache points to|/resource_id|/properties/resourceId|

**Example: ApiManagementCreateCache**

```
apim cache create --resource-group rg1
        --service-name apimService1
        --cache-id westindia
        --description "Redis cache instances in West India"
        --connection-string contoso5.redis.cache.windows.net,ssl=true,password=...
        --resource-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}"
```
### apim cache update

update a apim cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--cache-id**|str|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
|**--connection-string**|str|Runtime connection string to cache|/connection_string|/properties/connectionString|
|--description|str|Cache description|/description|/properties/description|
|--resource-id|str|Original uri of entity in external system cache points to|/resource_id|/properties/resourceId|

**Example: ApiManagementUpdateCache**

```
apim cache update --resource-group rg1
        --service-name apimService1
        --cache-id westindia
        --description "Update Cache in west India"
```
### apim cache delete

delete a apim cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--cache-id**|str|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|

**Example: ApiManagementDeleteCache**

```
apim cache delete --resource-group rg1
        --service-name apimService1
        --cache-id southindia
```
### apim cache list

list a apim cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim cache show

show a apim cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--cache-id**|str|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
## apim certificate

### apim certificate create

create a apim certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--certificate-id**|str|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
|**--data**|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/data|/properties/data|
|**--password**|str|Password for the Certificate|/password|/properties/password|

**Example: ApiManagementCreateCertificate**

```
apim certificate create --resource-group rg1
        --service-name apimService1
        --certificate-id tempcert
        --data "****************Base 64 Encoded Certificate *******************************"
        --password "****Certificate Password******"
```
### apim certificate update

update a apim certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--certificate-id**|str|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
|**--data**|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/data|/properties/data|
|**--password**|str|Password for the Certificate|/password|/properties/password|
### apim certificate delete

delete a apim certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--certificate-id**|str|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|

**Example: ApiManagementDeleteCertificate**

```
apim certificate delete --resource-group rg1
        --service-name apimService1
        --certificate-id tempcert
```
### apim certificate list

list a apim certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim certificate show

show a apim certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--certificate-id**|str|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
## apim diagnostic

### apim diagnostic create

create a apim diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger-id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always-log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable-http-correlation-headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

**Example: ApiManagementCreateDiagnostic**

```
apim diagnostic create --resource-group rg1
        --service-name apimService1
        --diagnostic-id applicationinsights
        --always-log allErrors
        --logger-id /loggers/azuremonitor
```
### apim diagnostic update

update a apim diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|**--logger-id**|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always-log|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable-http-correlation-headers|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|

**Example: ApiManagementUpdateDiagnostic**

```
apim diagnostic update --resource-group rg1
        --service-name apimService1
        --diagnostic-id applicationinsights
        --always-log allErrors
        --logger-id /loggers/applicationinsights
```
### apim diagnostic delete

delete a apim diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

**Example: ApiManagementDeleteDiagnostic**

```
apim diagnostic delete --resource-group rg1
        --service-name apimService1
        --diagnostic-id applicationinsights
```
### apim diagnostic list

list a apim diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim diagnostic show

show a apim diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--diagnostic-id**|str|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
## apim group

### apim group create

create a apim group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display-name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description.|/description|/properties/description|
|--type|str|Group type.|/type|/properties/type|
|--external-id|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

**Example: ApiManagementCreateGroup**

```
apim group create --resource-group rg1
        --service-name apimService1
        --group-id tempgroup
        --display-name "temp group"
```

**Example: ApiManagementCreateGroupExternal**

```
apim group create --resource-group rg1
        --service-name apimService1
        --group-id aadGroup
        --display-name "NewGroup (samiraad.onmicrosoft.com)"
        --description "new group to test"
        --type external
        --external-id aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d
```
### apim group update

update a apim group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display-name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description.|/description|/properties/description|
|--type|str|Group type.|/type|/properties/type|
|--external-id|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

**Example: ApiManagementUpdateGroup**

```
apim group update --resource-group rg1
        --service-name apimService1
        --group-id tempgroup
        --display-name "temp group"
```
### apim group delete

delete a apim group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

**Example: ApiManagementDeleteGroup**

```
apim group delete --resource-group rg1
        --service-name apimService1
        --group-id aadGroup
```
### apim group list

list a apim group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim group show

show a apim group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
## apim group user

### apim group user create

create a apim group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|--state|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|list|Collection of user identities.|/identities|/properties/identities|
|--first-name|str|First name.|/first_name|/properties/firstName|
|--last-name|str|Last name.|/last_name|/properties/lastName|
|--email|str|Email address.|/email|/properties/email|
|--registration-date|datetime|Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>|/registration_date|/properties/registrationDate|
|--groups|list|Collection of groups user is part of.|/groups|/properties/groups|

**Example: ApiManagementCreateGroupUser**

```
apim group user create --resource-group rg1
        --service-name apimService1
        --group-id tempgroup
        --user-id 59307d350af58404d8a26300
```
### apim group user delete

delete a apim group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementDeleteGroupUser**

```
apim group user delete --resource-group rg1
        --service-name apimService1
        --group-id templategroup
        --user-id 59307d350af58404d8a26300
```
### apim group user list

list a apim group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
## apim identity-provider

### apim identity-provider create

create a apim identity-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
|**--client-id**|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/client_id|/properties/clientId|
|**--client-secret**|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/client_secret|/properties/clientSecret|
|--type|str|Identity Provider Type identifier.|/type|/properties/type|
|--allowed-tenants|list|List of Allowed Tenants when configuring Azure Active Directory login.|/allowed_tenants|/properties/allowedTenants|
|--authority|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/authority|/properties/authority|
|--signup-policy-name|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/signup_policy_name|/properties/signupPolicyName|
|--signin-policy-name|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/signin_policy_name|/properties/signinPolicyName|
|--profile-editing-policy-name|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/profile_editing_policy_name|/properties/profileEditingPolicyName|
|--password-reset-policy-name|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/password_reset_policy_name|/properties/passwordResetPolicyName|

**Example: ApiManagementCreateIdentityProvider**

```
apim identity-provider create --resource-group rg1
        --service-name apimService1
        --name facebook
        --client-id facebookid
        --client-secret facebookapplicationsecret
```
### apim identity-provider update

update a apim identity-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
|**--client-id**|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/client_id|/properties/clientId|
|**--client-secret**|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/client_secret|/properties/clientSecret|
|--type|str|Identity Provider Type identifier.|/type|/properties/type|
|--allowed-tenants|list|List of Allowed Tenants when configuring Azure Active Directory login.|/allowed_tenants|/properties/allowedTenants|
|--authority|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/authority|/properties/authority|
|--signup-policy-name|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/signup_policy_name|/properties/signupPolicyName|
|--signin-policy-name|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/signin_policy_name|/properties/signinPolicyName|
|--profile-editing-policy-name|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/profile_editing_policy_name|/properties/profileEditingPolicyName|
|--password-reset-policy-name|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/password_reset_policy_name|/properties/passwordResetPolicyName|

**Example: ApiManagementUpdateIdentityProvider**

```
apim identity-provider update --resource-group rg1
        --service-name apimService1
        --name facebook
        --client-id updatedfacebookid
        --client-secret updatedfacebooksecret
```
### apim identity-provider delete

delete a apim identity-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Identity Provider Type identifier.|identity_provider_name|identityProviderName|

**Example: ApiManagementDeleteIdentityProvider**

```
apim identity-provider delete --resource-group rg1
        --service-name apimService1
        --name aad
```
### apim identity-provider list

list a apim identity-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim identity-provider show

show a apim identity-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
## apim logger

### apim logger create

create a apim logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--logger-id**|str|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
|**--logger-type**|str|Logger type.|/logger_type|/properties/loggerType|
|**--credentials**|dictionary|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/credentials|/properties/credentials|
|--description|str|Logger description.|/description|/properties/description|
|--is-buffered|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/is_buffered|/properties/isBuffered|
|--resource-id|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/resource_id|/properties/resourceId|

**Example: ApiManagementCreateEHLogger**

```
apim logger create --resource-group rg1
        --service-name apimService1
        --logger-id loggerId
        --logger-type azureEventHub
        --description "adding a new logger"
```

**Example: ApiManagementCreateAILogger**

```
apim logger create --resource-group rg1
        --service-name apimService1
        --logger-id loggerId
        --logger-type applicationInsights
        --description "adding a new logger"
```
### apim logger update

update a apim logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--logger-id**|str|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
|**--logger-type**|str|Logger type.|/logger_type|/properties/loggerType|
|**--credentials**|dictionary|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/credentials|/properties/credentials|
|--description|str|Logger description.|/description|/properties/description|
|--is-buffered|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/is_buffered|/properties/isBuffered|
|--resource-id|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/resource_id|/properties/resourceId|

**Example: ApiManagementUpdateLogger**

```
apim logger update --resource-group rg1
        --service-name apimService1
        --logger-id loggerId
```
### apim logger delete

delete a apim logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--logger-id**|str|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|

**Example: ApiManagementDeleteLogger**

```
apim logger delete --resource-group rg1
        --service-name apimService1
        --logger-id loggerId
```
### apim logger list

list a apim logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim logger show

show a apim logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--logger-id**|str|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
## apim notification

### apim notification create

create a apim notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--title**|str|Title of the Notification.|/title|/properties/title|
|--description|str|Description of the Notification.|/description|/properties/description|
|--recipients|dict|Recipient Parameter values.|/recipients|/properties/recipients|

**Example: ApiManagementCreateNotification**

```
apim notification create --resource-group rg1
        --service-name apimService1
        --name RequestPublisherNotificationMessage
```
### apim notification update

update a apim notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--title**|str|Title of the Notification.|/title|/properties/title|
|--description|str|Description of the Notification.|/description|/properties/description|
|--recipients|dict|Recipient Parameter values.|/recipients|/properties/recipients|
### apim notification list

list a apim notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim notification show

show a apim notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Notification Name Identifier.|notification_name|notificationName|
## apim notification recipient-email

### apim notification recipient-email create

create a apim notification recipient-email.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--email**|str|Email identifier.|email|email|

**Example: ApiManagementCreateNotificationRecipientEmail**

```
apim notification recipient-email create --resource-group rg1
        --service-name apimService1
        --notification-name RequestPublisherNotificationMessage
        --email foobar@live.com
```
### apim notification recipient-email update

update a apim notification recipient-email.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--email**|str|Email identifier.|email|email|
### apim notification recipient-email delete

delete a apim notification recipient-email.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--email**|str|Email identifier.|email|email|

**Example: ApiManagementDeleteNotificationRecipientEmail**

```
apim notification recipient-email delete --resource-group rg1
        --service-name apimService1
        --notification-name RequestPublisherNotificationMessage
        --email contoso@live.com
```
### apim notification recipient-email list

list a apim notification recipient-email.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
## apim notification recipient-user

### apim notification recipient-user create

create a apim notification recipient-user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementCreateNotificationRecipientUser**

```
apim notification recipient-user create --resource-group rg1
        --service-name apimService1
        --notification-name RequestPublisherNotificationMessage
        --user-id 576823d0a40f7e74ec07d642
```
### apim notification recipient-user update

update a apim notification recipient-user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
### apim notification recipient-user delete

delete a apim notification recipient-user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementDeleteNotificationRecipientUser**

```
apim notification recipient-user delete --resource-group rg1
        --service-name apimService1
        --notification-name RequestPublisherNotificationMessage
        --user-id 576823d0a40f7e74ec07d642
```
### apim notification recipient-user list

list a apim notification recipient-user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--notification-name**|str|Notification Name Identifier.|notification_name|notificationName|
## apim openid-connect-provider

### apim openid-connect-provider create

create a apim openid-connect-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--opid**|str|Identifier of the OpenID Connect Provider.|opid|opid|
|**--display-name**|str|User-friendly OpenID Connect Provider name.|/display_name|/properties/displayName|
|**--metadata-endpoint**|str|Metadata endpoint URI.|/metadata_endpoint|/properties/metadataEndpoint|
|**--client-id**|str|Client ID of developer console which is the client application.|/client_id|/properties/clientId|
|--description|str|User-friendly description of OpenID Connect Provider.|/description|/properties/description|
|--client-secret|str|Client Secret of developer console which is the client application.|/client_secret|/properties/clientSecret|

**Example: ApiManagementCreateOpenIdConnectProvider**

```
apim openid-connect-provider create --resource-group rg1
        --service-name apimService1
        --opid templateOpenIdConnect3
        --display-name templateoidprovider3
        --metadata-endpoint https://oidprovider-template3.net
        --client-id oidprovidertemplate3
```
### apim openid-connect-provider update

update a apim openid-connect-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--opid**|str|Identifier of the OpenID Connect Provider.|opid|opid|
|**--display-name**|str|User-friendly OpenID Connect Provider name.|/display_name|/properties/displayName|
|**--metadata-endpoint**|str|Metadata endpoint URI.|/metadata_endpoint|/properties/metadataEndpoint|
|**--client-id**|str|Client ID of developer console which is the client application.|/client_id|/properties/clientId|
|--description|str|User-friendly description of OpenID Connect Provider.|/description|/properties/description|
|--client-secret|str|Client Secret of developer console which is the client application.|/client_secret|/properties/clientSecret|

**Example: ApiManagementUpdateOpenIdConnectProvider**

```
apim openid-connect-provider update --resource-group rg1
        --service-name apimService1
        --opid templateOpenIdConnect2
        --client-secret updatedsecret
```
### apim openid-connect-provider delete

delete a apim openid-connect-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--opid**|str|Identifier of the OpenID Connect Provider.|opid|opid|

**Example: ApiManagementDeleteOpenIdConnectProvider**

```
apim openid-connect-provider delete --resource-group rg1
        --service-name apimService1
        --opid templateOpenIdConnect3
```
### apim openid-connect-provider list

list a apim openid-connect-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim openid-connect-provider show

show a apim openid-connect-provider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--opid**|str|Identifier of the OpenID Connect Provider.|opid|opid|
## apim policy

### apim policy create

create a apim policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

**Example: ApiManagementCreatePolicy**

```
apim policy create --resource-group rg1
        --service-name apimService1
        --policy-id policy
        --value "<policies>
  <inbound />
  <backend>
    <forward-request />
  </backend>
  <outbound />
</policies>"
        --format xml
```
### apim policy update

update a apim policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|
### apim policy delete

delete a apim policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementDeletePolicy**

```
apim policy delete --resource-group rg1
        --service-name apimService1
        --policy-id policy
```
### apim policy list

list a apim policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim policy show

show a apim policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|--format|str|Format of the policyContent.|/format|/properties/format|
## apim portalsetting delegation

### apim portalsetting delegation create

create a apim portalsetting delegation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|--url|str|A delegation Url.|/url|/properties/url|
|--validation-key|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/validation_key|/properties/validationKey|
|--subscriptions|dict|Subscriptions delegation settings.|/subscriptions|/properties/subscriptions|
|--user-registration|dict|User registration delegation settings.|/user_registration|/properties/userRegistration|

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apim portalsetting delegation create --resource-group rg1
        --name apimService1
        --url http://contoso.com/delegation
        --validation-key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
```
### apim portalsetting delegation update

update a apim portalsetting delegation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|--url|str|A delegation Url.|/url|/properties/url|
|--validation-key|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/validation_key|/properties/validationKey|
|--subscriptions|dict|Subscriptions delegation settings.|/subscriptions|/properties/subscriptions|
|--user-registration|dict|User registration delegation settings.|/user_registration|/properties/userRegistration|

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apim portalsetting delegation update --resource-group rg1
        --name apimService1
        --url http://contoso.com/delegation
        --validation-key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
```
### apim portalsetting delegation show

show a apim portalsetting delegation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
## apim portalsetting signin

### apim portalsetting signin create

create a apim portalsetting signin.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|--enabled|boolean|Redirect Anonymous users to the Sign-In page.|/enabled|/properties/enabled|

**Example: ApiManagementPortalSettingsUpdateSignIn**

```
apim portalsetting signin create --resource-group rg1
        --name apimService1
        --enabled true
```
### apim portalsetting signin update

update a apim portalsetting signin.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|--enabled|boolean|Redirect Anonymous users to the Sign-In page.|/enabled|/properties/enabled|

**Example: ApiManagementPortalSettingsUpdateSignIn**

```
apim portalsetting signin update --resource-group rg1
        --name apimService1
        --enabled true
```
### apim portalsetting signin show

show a apim portalsetting signin.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
## apim portalsetting signup

### apim portalsetting signup create

create a apim portalsetting signup.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|--enabled|boolean|Allow users to sign up on a developer portal.|/enabled|/properties/enabled|
|--terms-of-service|dict|Terms of service contract properties.|/terms_of_service|/properties/termsOfService|

**Example: ApiManagementPortalSettingsUpdateSignUp**

```
apim portalsetting signup create --resource-group rg1
        --name apimService1
        --enabled true
```
### apim portalsetting signup update

update a apim portalsetting signup.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
|--enabled|boolean|Allow users to sign up on a developer portal.|/enabled|/properties/enabled|
|--terms-of-service|dict|Terms of service contract properties.|/terms_of_service|/properties/termsOfService|

**Example: ApiManagementPortalSettingsUpdateSignUp**

```
apim portalsetting signup update --resource-group rg1
        --name apimService1
        --enabled true
```
### apim portalsetting signup show

show a apim portalsetting signup.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the API Management service.|service_name|serviceName|
## apim product

### apim product create

create a apim product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--display-name**|str|Product name.|/display_name|/properties/displayName|
|--description|str|Product description. May include HTML formatting tags.|/description|/properties/description|
|--terms|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/terms|/properties/terms|
|--subscription-required|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/subscription_required|/properties/subscriptionRequired|
|--approval-required|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/approval_required|/properties/approvalRequired|
|--subscriptions-limit|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/subscriptions_limit|/properties/subscriptionsLimit|
|--state|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/state|/properties/state|

**Example: ApiManagementCreateProduct**

```
apim product create --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --display-name "Test Template ProductName 4"
```
### apim product update

update a apim product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--display-name**|str|Product name.|/display_name|/properties/displayName|
|--description|str|Product description. May include HTML formatting tags.|/description|/properties/description|
|--terms|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/terms|/properties/terms|
|--subscription-required|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/subscription_required|/properties/subscriptionRequired|
|--approval-required|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/approval_required|/properties/approvalRequired|
|--subscriptions-limit|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/subscriptions_limit|/properties/subscriptionsLimit|
|--state|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/state|/properties/state|

**Example: ApiManagementUpdateProduct**

```
apim product update --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --display-name "Test Template ProductName 4"
```
### apim product delete

delete a apim product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

**Example: ApiManagementDeleteProduct**

```
apim product delete --resource-group rg1
        --service-name apimService1
        --product-id testproduct
```
### apim product list

list a apim product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim product show

show a apim product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
## apim product api

### apim product api create

create a apim product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication-settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription-key-parameter-names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api-revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api-version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is-current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--is-online|boolean|Indicates if API revision is accessible via the gateway.|/is_online|/properties/isOnline|
|--api-revision-description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api-version-description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api-version-set-id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription-required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source-api-id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display-name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service-url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api-version-set|dict|Version set details|/api_version_set|/properties/apiVersionSet|

**Example: ApiManagementCreateProductApi**

```
apim product api create --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --api-id echo-api
```
### apim product api update

update a apim product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--path**|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication-settings|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription-key-parameter-names|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|str|Type of API.|/type|/properties/type|
|--api-revision|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api-version|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is-current|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--is-online|boolean|Indicates if API revision is accessible via the gateway.|/is_online|/properties/isOnline|
|--api-revision-description|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api-version-description|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api-version-set-id|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription-required|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source-api-id|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display-name|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service-url|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api-version-set|dict|Version set details|/api_version_set|/properties/apiVersionSet|
### apim product api delete

delete a apim product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api-id**|str|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementDeleteProductApi**

```
apim product api delete --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --api-id echo-api
```
### apim product api list

list a apim product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
## apim product group

### apim product group create

create a apim product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display-name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description. Can contain HTML formatting tags.|/description|/properties/description|
|--built-in|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/built_in|/properties/builtIn|
|--type|str|Group type.|/type|/properties/type|
|--external-id|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|

**Example: ApiManagementCreateProductGroup**

```
apim product group create --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --group-id templateGroup
```
### apim product group update

update a apim product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--display-name**|str|Group name.|/display_name|/properties/displayName|
|--description|str|Group description. Can contain HTML formatting tags.|/description|/properties/description|
|--built-in|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/built_in|/properties/builtIn|
|--type|str|Group type.|/type|/properties/type|
|--external-id|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|
### apim product group delete

delete a apim product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group-id**|str|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

**Example: ApiManagementDeleteProductGroup**

```
apim product group delete --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --group-id templateGroup
```
### apim product group list

list a apim product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
## apim product policy

### apim product policy create

create a apim product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|

**Example: ApiManagementCreateProductPolicy**

```
apim product policy create --resource-group rg1
        --service-name apimService1
        --product-id 5702e97e5157a50f48dce801
        --policy-id policy
        --value "<policies>
  <inbound>
    <rate-limit calls=\"{{call-count}}" renewal-period="15"></rate-limit>
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
</policies>"
        --format xml
```
### apim product policy update

update a apim product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|**--value**|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|str|Format of the policyContent.|/format|/properties/format|
### apim product policy delete

delete a apim product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementDeleteProductPolicy**

```
apim product policy delete --resource-group rg1
        --service-name apimService1
        --product-id testproduct
        --policy-id policy
```
### apim product policy list

list a apim product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
### apim product policy show

show a apim product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--product-id**|str|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy-id**|str|The identifier of the Policy.|policy_id|policyId|
|--format|str|Format of the policyContent.|/format|/properties/format|
## apim property

### apim property create

create a apim property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--prop-id**|str|Identifier of the property.|prop_id|propId|
|**--display-name**|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/display_name|/properties/displayName|
|**--value**|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/value|/properties/value|
|--tags|list|Optional tags that when provided can be used to filter the property list.|/tags|/properties/tags|
|--secret|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/secret|/properties/secret|

**Example: ApiManagementCreateProperty**

```
apim property create --resource-group rg1
        --service-name apimService1
        --prop-id testprop2
        --secret true
        --display-name prop3name
        --value propValue
```
### apim property update

update a apim property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--prop-id**|str|Identifier of the property.|prop_id|propId|
|**--display-name**|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/display_name|/properties/displayName|
|**--value**|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/value|/properties/value|
|--tags|list|Optional tags that when provided can be used to filter the property list.|/tags|/properties/tags|
|--secret|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/secret|/properties/secret|

**Example: ApiManagementUpdateProperty**

```
apim property update --resource-group rg1
        --service-name apimService1
        --prop-id testprop2
        --secret true
```
### apim property delete

delete a apim property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--prop-id**|str|Identifier of the property.|prop_id|propId|

**Example: ApiManagementDeleteProperty**

```
apim property delete --resource-group rg1
        --service-name apimService1
        --prop-id testprop2
```
### apim property list

list a apim property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim property show

show a apim property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--prop-id**|str|Identifier of the property.|prop_id|propId|
## apim subscription

### apim subscription create

create a apim subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--sid**|str|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
|**--scope**|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/scope|/properties/scope|
|**--display-name**|str|Subscription name.|/display_name|/properties/displayName|
|--notify|boolean|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |notify|notify|
|--owner-id|str|User (user id path) for whom subscription is being created in form /users/{userId}|/owner_id|/properties/ownerId|
|--primary-key|str|Primary subscription key. If not specified during request key will be generated automatically.|/primary_key|/properties/primaryKey|
|--secondary-key|str|Secondary subscription key. If not specified during request key will be generated automatically.|/secondary_key|/properties/secondaryKey|
|--state|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/state|/properties/state|
|--allow-tracing|boolean|Determines whether tracing can be enabled|/allow_tracing|/properties/allowTracing|

**Example: ApiManagementCreateSubscription**

```
apim subscription create --resource-group rg1
        --service-name apimService1
        --sid testsub
        --owner-id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
        --scope "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }}"
        --display-name testsub
```
### apim subscription update

update a apim subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--sid**|str|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
|**--scope**|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/scope|/properties/scope|
|**--display-name**|str|Subscription name.|/display_name|/properties/displayName|
|--notify|boolean|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |notify|notify|
|--owner-id|str|User (user id path) for whom subscription is being created in form /users/{userId}|/owner_id|/properties/ownerId|
|--primary-key|str|Primary subscription key. If not specified during request key will be generated automatically.|/primary_key|/properties/primaryKey|
|--secondary-key|str|Secondary subscription key. If not specified during request key will be generated automatically.|/secondary_key|/properties/secondaryKey|
|--state|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/state|/properties/state|
|--allow-tracing|boolean|Determines whether tracing can be enabled|/allow_tracing|/properties/allowTracing|

**Example: ApiManagementUpdateSubscription**

```
apim subscription update --resource-group rg1
        --service-name apimService1
        --sid testsub
        --display-name testsub
```
### apim subscription delete

delete a apim subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--sid**|str|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|

**Example: ApiManagementDeleteSubscription**

```
apim subscription delete --resource-group rg1
        --service-name apimService1
        --sid testsub
```
### apim subscription list

list a apim subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim subscription show

show a apim subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--sid**|str|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
## apim tag

### apim tag create

create a apim tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|**--display-name**|str|Tag name.|/display_name|/properties/displayName|

**Example: ApiManagementCreateTag**

```
apim tag create --resource-group rg1
        --service-name apimService1
        --tag-id tagId1
        --display-name tag1
```
### apim tag update

update a apim tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|**--display-name**|str|Tag name.|/display_name|/properties/displayName|

**Example: ApiManagementUpdateTag**

```
apim tag update --resource-group rg1
        --service-name apimService1
        --tag-id temptag
        --display-name "temp tag"
```
### apim tag delete

delete a apim tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

**Example: ApiManagementDeleteTag**

```
apim tag delete --resource-group rg1
        --service-name apimService1
        --tag-id tagId1
```
### apim tag list

list a apim tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim tag show

show a apim tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--tag-id**|str|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
## apim template

### apim template create

create a apim template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Email Template Name Identifier.|template_name|templateName|
|--subject|str|Subject of the Template.|/subject|/properties/subject|
|--title|str|Title of the Template.|/title|/properties/title|
|--description|str|Description of the Email Template.|/description|/properties/description|
|--body|str|Email Template Body. This should be a valid XDocument|/body|/properties/body|

**Example: ApiManagementCreateEmailTemplate**

```
apim template create --resource-group rg1
        --service-name apimService1
        --name newIssueNotificationMessage
        --subject "Your request for $IssueName was successfully received."
```
### apim template update

update a apim template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Email Template Name Identifier.|template_name|templateName|
|--subject|str|Subject of the Template.|/subject|/properties/subject|
|--title|str|Title of the Template.|/title|/properties/title|
|--description|str|Description of the Email Template.|/description|/properties/description|
|--body|str|Email Template Body. This should be a valid XDocument|/body|/properties/body|

**Example: ApiManagementUpdateEmailTemplate**

```
apim template update --resource-group rg1
        --service-name apimService1
        --name applicationApprovedNotificationMessage
        --subject "Your application $AppName is published in the gallery"
        --body "<!DOCTYPE html >
<html>
  <head />
  <body>
    <p style=\"font-size:12pt;font-family:'Segoe UI'">Dear $DevFirstName $DevLastName,</p>
    <p style="font-size:12pt;font-family:'Segoe UI'">
          We are happy to let you know that your request to publish the $AppName application in the gallery has been approved. Your application has been published and can be viewed <a href="http://$DevPortalUrl/Applications/Details/$AppId">here</a>.
        </p>
    <p style="font-size:12pt;font-family:'Segoe UI'">Best,</p>
    <p style="font-size:12pt;font-family:'Segoe UI'">The $OrganizationName API Team</p>
  </body>
</html>"
```
### apim template delete

delete a apim template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Email Template Name Identifier.|template_name|templateName|

**Example: ApiManagementDeleteEmailTemplate**

```
apim template delete --resource-group rg1
        --service-name apimService1
        --name newIssueNotificationMessage
```
### apim template list

list a apim template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim template show

show a apim template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--name**|str|Email Template Name Identifier.|template_name|templateName|
## apim user

### apim user create

create a apim user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|**--email**|str|Email address. Must not be empty and must be unique within the service instance.|/email|/properties/email|
|**--first-name**|str|First name.|/first_name|/properties/firstName|
|**--last-name**|str|Last name.|/last_name|/properties/lastName|
|--state|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|list|Collection of user identities.|/identities|/properties/identities|
|--password|str|User Password. If no value is provided, a default password is generated.|/password|/properties/password|
|--confirmation|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/confirmation|/properties/confirmation|

**Example: ApiManagementCreateUser**

```
apim user create --resource-group rg1
        --service-name apimService1
        --user-id 5931a75ae4bbd512288c680b
        --email foobar@outlook.com
        --first-name foo
        --last-name bar
        --confirmation signup
```
### apim user update

update a apim user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|**--email**|str|Email address. Must not be empty and must be unique within the service instance.|/email|/properties/email|
|**--first-name**|str|First name.|/first_name|/properties/firstName|
|**--last-name**|str|Last name.|/last_name|/properties/lastName|
|--state|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|list|Collection of user identities.|/identities|/properties/identities|
|--password|str|User Password. If no value is provided, a default password is generated.|/password|/properties/password|
|--confirmation|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/confirmation|/properties/confirmation|

**Example: ApiManagementUpdateUser**

```
apim user update --resource-group rg1
        --service-name apimService1
        --user-id 5931a75ae4bbd512288c680b
        --email foobar@outlook.com
        --first-name foo
        --last-name bar
```
### apim user delete

delete a apim user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementDeleteUser**

```
apim user delete --resource-group rg1
        --service-name apimService1
        --user-id 5931a75ae4bbd512288c680b
```
### apim user list

list a apim user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
### apim user show

show a apim user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service-name**|str|The name of the API Management service.|service_name|serviceName|
|**--user-id**|str|User identifier. Must be unique in the current API Management service instance.|user_id|userId|