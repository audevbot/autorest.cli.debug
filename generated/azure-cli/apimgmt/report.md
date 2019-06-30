# Azure CLI Module Creation Report

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

**Example: ApiManagementCreateService**

```
apimgmt create s--resource_group rg1
        --name apimService1
        --publisher_email apim@autorestsdk.com
        --publisher_name autorestsdk
        --sku_name Developer
        --sku_capacity 1
        --location "Central US"
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apimgmt create s--resource_group rg1
        --name apimService1
        --virtual_network_type External
        --publisher_email admin@live.com
        --publisher_name contoso
        --sku_name Premium
        --sku_capacity 1
        --location "Central US"
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apimgmt create s--resource_group rg1
        --name apimService1
        --publisher_email apim@autorestsdk.com
        --publisher_name autorestsdk
        --sku_name Consumption
        --location "West US"
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apimgmt create s--resource_group rg1
        --name apimService1
        --publisher_email apim@autorestsdk.com
        --publisher_name autorestsdk
        --sku_name Basic
        --sku_capacity 1
        --location "Central US"
```

**Example: ApiManagementUpdateServiceDisableTls10**

```
apimgmt create s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apimgmt create s--resource_group rg1
        --name apimService1
        --publisher_email foobar@live.com
        --publisher_name "Contoso Vnext"
```

**Example: ApiManagementServiceDeleteService**

```
apimgmt create s--resource_group rg1
        --name apimService1
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

**Example: ApiManagementCreateService**

```
apimgmt update s--resource_group rg1
        --name apimService1
        --publisher_email apim@autorestsdk.com
        --publisher_name autorestsdk
        --sku_name Developer
        --sku_capacity 1
        --location "Central US"
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apimgmt update s--resource_group rg1
        --name apimService1
        --virtual_network_type External
        --publisher_email admin@live.com
        --publisher_name contoso
        --sku_name Premium
        --sku_capacity 1
        --location "Central US"
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apimgmt update s--resource_group rg1
        --name apimService1
        --publisher_email apim@autorestsdk.com
        --publisher_name autorestsdk
        --sku_name Consumption
        --location "West US"
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apimgmt update s--resource_group rg1
        --name apimService1
        --publisher_email apim@autorestsdk.com
        --publisher_name autorestsdk
        --sku_name Basic
        --sku_capacity 1
        --location "Central US"
```

**Example: ApiManagementUpdateServiceDisableTls10**

```
apimgmt update s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apimgmt update s--resource_group rg1
        --name apimService1
        --publisher_email foobar@live.com
        --publisher_name "Contoso Vnext"
```

**Example: ApiManagementServiceDeleteService**

```
apimgmt update s--resource_group rg1
        --name apimService1
```
### apimgmt delete

delete a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateService**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServiceDisableTls10**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementServiceDeleteService**

```
apimgmt delete s--resource_group rg1
        --name apimService1
```
### apimgmt list

list a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|

**Example: ApiManagementCreateService**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementUpdateServiceDisableTls10**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementServiceDeleteService**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateService**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementUpdateServiceDisableTls10**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apimgmt list s--resource_group rg1
```

**Example: ApiManagementServiceDeleteService**

```
apimgmt list s--resource_group rg1
```
### apimgmt show

show a apimgmt.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateService**

```
apimgmt show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementCreateMultiRegionServiceWithCustomHostname**

```
apimgmt show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementCreateServiceHavingMsi**

```
apimgmt show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementCreateServiceWithSystemCertificates**

```
apimgmt show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServiceDisableTls10**

```
apimgmt show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementUpdateServicePublisherDetails**

```
apimgmt show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementServiceDeleteService**

```
apimgmt show s--resource_group rg1
        --name apimService1
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

**Example: ApiManagementCreateApiUsingOai3Import**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id petstore
        --path petstore
        --value https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml
        --format openapi-link
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id petstore
        --path petstore
        --value http://petstore.swagger.io/v2/swagger.json
        --format swagger-link-json
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id petstore
        --path collector
        --value https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl
        --format wadl-link-json
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
        --path currency
        --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL
        --format wsdl-link
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
        --path currency
        --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL
        --format wsdl-link
        --api_type soap
```

**Example: ApiManagementCreateApi**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
        --description apidescription5200
        --display_name apiname1463
        --service_url http://newechoapi.cloudapp.net/api
        --path newapiPath
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id echo-api;rev=3
        --api_revision_description "Creating a Revision of an existing API"
        --source_api_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --service_url http://echoapi.cloudapp.net/apiv3
        --path echo
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id echoapiv3
        --description "Create Echo API into a new Version using Existing Version Set and Copy all Operations."
        --api_version v4
        --is_current true
        --api_version_set_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }}"
        --subscription_required true
        --source_api_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --display_name "Echo API2"
        --service_url http://echoapi.cloudapp.net/api
        --path echo2
```

**Example: ApiManagementCreateApiClone**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id echo-api2
        --description "Copy of Existing Echo Api including Operations."
        --is_current true
        --subscription_required true
        --source_api_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --display_name "Echo API2"
        --service_url http://echoapi.cloudapp.net/api
        --path echo2
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
        --description "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters."
        --display_name "Swagger Petstore"
        --service_url http://petstore.swagger.io/v2
        --path petstore
```

**Example: ApiManagementUpdateApi**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
        --display_name "Echo API New"
        --service_url http://echoapi.cloudapp.net/api2
        --path newecho
```

**Example: ApiManagementDeleteApi**

```
apimgmt api create s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
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

**Example: ApiManagementCreateApiUsingOai3Import**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id petstore
        --path petstore
        --value https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml
        --format openapi-link
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id petstore
        --path petstore
        --value http://petstore.swagger.io/v2/swagger.json
        --format swagger-link-json
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id petstore
        --path collector
        --value https://developer.cisco.com/media/wae-release-6-2-api-reference/wae-collector-rest-api/application.wadl
        --format wadl-link-json
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
        --path currency
        --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL
        --format wsdl-link
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
        --path currency
        --value http://www.webservicex.net/CurrencyConvertor.asmx?WSDL
        --format wsdl-link
        --api_type soap
```

**Example: ApiManagementCreateApi**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
        --description apidescription5200
        --display_name apiname1463
        --service_url http://newechoapi.cloudapp.net/api
        --path newapiPath
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id echo-api;rev=3
        --api_revision_description "Creating a Revision of an existing API"
        --source_api_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --service_url http://echoapi.cloudapp.net/apiv3
        --path echo
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id echoapiv3
        --description "Create Echo API into a new Version using Existing Version Set and Copy all Operations."
        --api_version v4
        --is_current true
        --api_version_set_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apiVersionSets/{{ api_version_set_name }}"
        --subscription_required true
        --source_api_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --display_name "Echo API2"
        --service_url http://echoapi.cloudapp.net/api
        --path echo2
```

**Example: ApiManagementCreateApiClone**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id echo-api2
        --description "Copy of Existing Echo Api including Operations."
        --is_current true
        --subscription_required true
        --source_api_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/apis/{{ api_name }}"
        --display_name "Echo API2"
        --service_url http://echoapi.cloudapp.net/api
        --path echo2
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
        --description "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters."
        --display_name "Swagger Petstore"
        --service_url http://petstore.swagger.io/v2
        --path petstore
```

**Example: ApiManagementUpdateApi**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
        --display_name "Echo API New"
        --service_url http://echoapi.cloudapp.net/api2
        --path newecho
```

**Example: ApiManagementDeleteApi**

```
apimgmt api update s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
```
### apimgmt api delete

delete a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateApiUsingOai3Import**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id petstore
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id petstore
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id petstore
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
```

**Example: ApiManagementCreateApi**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id echo-api;rev=3
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id echoapiv3
```

**Example: ApiManagementCreateApiClone**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id echo-api2
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
```

**Example: ApiManagementUpdateApi**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
```

**Example: ApiManagementDeleteApi**

```
apimgmt api delete s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
```
### apimgmt api list

list a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateApiUsingOai3Import**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiClone**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiUsingOai3Import**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiClone**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteApi**

```
apimgmt api list s--resource_group rg1
        --service_name apimService1
```
### apimgmt api show

show a apimgmt api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateApiUsingOai3Import**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id petstore
```

**Example: ApiManagementCreateApiUsingSwaggerImport**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id petstore
```

**Example: ApiManagementCreateApiUsingWadlImport**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id petstore
```

**Example: ApiManagementCreateSoapToRestApiUsingWsdlImport**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
```

**Example: ApiManagementCreateSoapPassThroughApiUsingWsdlImport**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id soapApi
```

**Example: ApiManagementCreateApi**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
```

**Example: ApiManagementCreateApiRevisionFromExistingApi**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id echo-api;rev=3
```

**Example: ApiManagementCreateApiNewVersionUsingExistingApi**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id echoapiv3
```

**Example: ApiManagementCreateApiClone**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id echo-api2
```

**Example: ApiManagementCreateApiWithOpenIdConnect**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id tempgroup
```

**Example: ApiManagementUpdateApi**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
```

**Example: ApiManagementDeleteApi**

```
apimgmt api show s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
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

**Example: ApiManagementCreateApiDiagnostic**

```
apimgmt api diagnostic create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/applicationinsights
```

**Example: ApiManagementUpdateApiDiagnostic**

```
apimgmt api diagnostic create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/applicationinsights
```

**Example: ApiManagementDeleteApiDiagnostic**

```
apimgmt api diagnostic create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
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

**Example: ApiManagementCreateApiDiagnostic**

```
apimgmt api diagnostic update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/applicationinsights
```

**Example: ApiManagementUpdateApiDiagnostic**

```
apimgmt api diagnostic update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/applicationinsights
```

**Example: ApiManagementDeleteApiDiagnostic**

```
apimgmt api diagnostic update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
```
### apimgmt api diagnostic delete

delete a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

**Example: ApiManagementCreateApiDiagnostic**

```
apimgmt api diagnostic delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
```

**Example: ApiManagementUpdateApiDiagnostic**

```
apimgmt api diagnostic delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
```

**Example: ApiManagementDeleteApiDiagnostic**

```
apimgmt api diagnostic delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
```
### apimgmt api diagnostic list

list a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|

**Example: ApiManagementCreateApiDiagnostic**

```
apimgmt api diagnostic list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
```

**Example: ApiManagementUpdateApiDiagnostic**

```
apimgmt api diagnostic list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
```

**Example: ApiManagementDeleteApiDiagnostic**

```
apimgmt api diagnostic list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
```
### apimgmt api diagnostic show

show a apimgmt api diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

**Example: ApiManagementCreateApiDiagnostic**

```
apimgmt api diagnostic show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
```

**Example: ApiManagementUpdateApiDiagnostic**

```
apimgmt api diagnostic show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
```

**Example: ApiManagementDeleteApiDiagnostic**

```
apimgmt api diagnostic show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --diagnostic_id applicationinsights
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

**Example: ApiManagementCreateApiIssue**

```
apimgmt api issue create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --created_date 2018-02-01T22:21:20.467Z
        --state open
        --title "New API issue"
        --description "New API issue description"
        --user_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
```

**Example: ApiManagementUpdateApiIssue**

```
apimgmt api issue create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --state closed
```

**Example: ApiManagementDeleteApiIssue**

```
apimgmt api issue create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
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

**Example: ApiManagementCreateApiIssue**

```
apimgmt api issue update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --created_date 2018-02-01T22:21:20.467Z
        --state open
        --title "New API issue"
        --description "New API issue description"
        --user_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
```

**Example: ApiManagementUpdateApiIssue**

```
apimgmt api issue update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --state closed
```

**Example: ApiManagementDeleteApiIssue**

```
apimgmt api issue update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```
### apimgmt api issue delete

delete a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

**Example: ApiManagementCreateApiIssue**

```
apimgmt api issue delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```

**Example: ApiManagementUpdateApiIssue**

```
apimgmt api issue delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```

**Example: ApiManagementDeleteApiIssue**

```
apimgmt api issue delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```
### apimgmt api issue list

list a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|

**Example: ApiManagementCreateApiIssue**

```
apimgmt api issue list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
```

**Example: ApiManagementUpdateApiIssue**

```
apimgmt api issue list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
```

**Example: ApiManagementDeleteApiIssue**

```
apimgmt api issue list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
```
### apimgmt api issue show

show a apimgmt api issue.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

**Example: ApiManagementCreateApiIssue**

```
apimgmt api issue show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```

**Example: ApiManagementUpdateApiIssue**

```
apimgmt api issue show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```

**Example: ApiManagementDeleteApiIssue**

```
apimgmt api issue show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
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

**Example: ApiManagementCreateApiIssueAttachment**

```
apimgmt api issue attachment create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
        --title "Issue attachment."
        --content_format image/jpeg
        --content IEJhc2U2NA==
```

**Example: ApiManagementDeleteApiIssueAttachment**

```
apimgmt api issue attachment create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
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

**Example: ApiManagementCreateApiIssueAttachment**

```
apimgmt api issue attachment update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
        --title "Issue attachment."
        --content_format image/jpeg
        --content IEJhc2U2NA==
```

**Example: ApiManagementDeleteApiIssueAttachment**

```
apimgmt api issue attachment update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
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

**Example: ApiManagementCreateApiIssueAttachment**

```
apimgmt api issue attachment delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
```

**Example: ApiManagementDeleteApiIssueAttachment**

```
apimgmt api issue attachment delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
```
### apimgmt api issue attachment list

list a apimgmt api issue attachment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

**Example: ApiManagementCreateApiIssueAttachment**

```
apimgmt api issue attachment list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```

**Example: ApiManagementDeleteApiIssueAttachment**

```
apimgmt api issue attachment list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
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

**Example: ApiManagementCreateApiIssueAttachment**

```
apimgmt api issue attachment show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
```

**Example: ApiManagementDeleteApiIssueAttachment**

```
apimgmt api issue attachment show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --attachment_id 57d2ef278aa04f0888cba3f3
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

**Example: ApiManagementCreateApiIssueComment**

```
apimgmt api issue comment create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
        --text "Issue comment."
        --created_date 2018-02-01T22:21:20.467Z
        --user_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
```

**Example: ApiManagementDeleteApiIssueComment**

```
apimgmt api issue comment create s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
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

**Example: ApiManagementCreateApiIssueComment**

```
apimgmt api issue comment update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
        --text "Issue comment."
        --created_date 2018-02-01T22:21:20.467Z
        --user_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
```

**Example: ApiManagementDeleteApiIssueComment**

```
apimgmt api issue comment update s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
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

**Example: ApiManagementCreateApiIssueComment**

```
apimgmt api issue comment delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
```

**Example: ApiManagementDeleteApiIssueComment**

```
apimgmt api issue comment delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
```
### apimgmt api issue comment list

list a apimgmt api issue comment.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--issue_id**|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|

**Example: ApiManagementCreateApiIssueComment**

```
apimgmt api issue comment list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
```

**Example: ApiManagementDeleteApiIssueComment**

```
apimgmt api issue comment list s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
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

**Example: ApiManagementCreateApiIssueComment**

```
apimgmt api issue comment show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
```

**Example: ApiManagementDeleteApiIssueComment**

```
apimgmt api issue comment show s--resource_group rg1
        --service_name apimService1
        --api_id 57d1f7558aa04f15146d9d8a
        --issue_id 57d2ef278aa04f0ad01d6cdc
        --comment_id 599e29ab193c3c0bd0b3e2fb
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

**Example: ApiManagementCreateApiOperation**

```
apimgmt api operation create s--resource_group rg1
        --service_name apimService1
        --api_id PetStoreTemplate2
        --operation_id newoperations
        --description "This can only be done by the logged in user."
        --display_name createUser2
        --method POST
        --url_template /user1
```

**Example: ApiManagementUpdateApiOperation**

```
apimgmt api operation create s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
        --operation_id operationId
        --display_name "Retrieve resource"
        --method GET
        --url_template /resource
```

**Example: ApiManagementDeleteApiOperation**

```
apimgmt api operation create s--resource_group rg1
        --service_name apimService1
        --api_id 57d2ef278aa04f0888cba3f3
        --operation_id 57d2ef278aa04f0ad01d6cdc
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

**Example: ApiManagementCreateApiOperation**

```
apimgmt api operation update s--resource_group rg1
        --service_name apimService1
        --api_id PetStoreTemplate2
        --operation_id newoperations
        --description "This can only be done by the logged in user."
        --display_name createUser2
        --method POST
        --url_template /user1
```

**Example: ApiManagementUpdateApiOperation**

```
apimgmt api operation update s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
        --operation_id operationId
        --display_name "Retrieve resource"
        --method GET
        --url_template /resource
```

**Example: ApiManagementDeleteApiOperation**

```
apimgmt api operation update s--resource_group rg1
        --service_name apimService1
        --api_id 57d2ef278aa04f0888cba3f3
        --operation_id 57d2ef278aa04f0ad01d6cdc
```
### apimgmt api operation delete

delete a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

**Example: ApiManagementCreateApiOperation**

```
apimgmt api operation delete s--resource_group rg1
        --service_name apimService1
        --api_id PetStoreTemplate2
        --operation_id newoperations
```

**Example: ApiManagementUpdateApiOperation**

```
apimgmt api operation delete s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
        --operation_id operationId
```

**Example: ApiManagementDeleteApiOperation**

```
apimgmt api operation delete s--resource_group rg1
        --service_name apimService1
        --api_id 57d2ef278aa04f0888cba3f3
        --operation_id 57d2ef278aa04f0ad01d6cdc
```
### apimgmt api operation list

list a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateApiOperation**

```
apimgmt api operation list s--resource_group rg1
        --service_name apimService1
        --api_id PetStoreTemplate2
```

**Example: ApiManagementUpdateApiOperation**

```
apimgmt api operation list s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
```

**Example: ApiManagementDeleteApiOperation**

```
apimgmt api operation list s--resource_group rg1
        --service_name apimService1
        --api_id 57d2ef278aa04f0888cba3f3
```
### apimgmt api operation show

show a apimgmt api operation.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

**Example: ApiManagementCreateApiOperation**

```
apimgmt api operation show s--resource_group rg1
        --service_name apimService1
        --api_id PetStoreTemplate2
        --operation_id newoperations
```

**Example: ApiManagementUpdateApiOperation**

```
apimgmt api operation show s--resource_group rg1
        --service_name apimService1
        --api_id echo-api
        --operation_id operationId
```

**Example: ApiManagementDeleteApiOperation**

```
apimgmt api operation show s--resource_group rg1
        --service_name apimService1
        --api_id 57d2ef278aa04f0888cba3f3
        --operation_id 57d2ef278aa04f0ad01d6cdc
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

**Example: ApiManagementCreateApiOperationPolicy**

```
apimgmt api operation policy create s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --operation_id 5600b57e7e8880006a080001
        --policy_id policy
        --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
        --format xml
```

**Example: ApiManagementDeleteApiOperationPolicy**

```
apimgmt api operation policy create s--resource_group rg1
        --service_name apimService1
        --api_id testapi
        --operation_id testoperation
        --policy_id policy
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

**Example: ApiManagementCreateApiOperationPolicy**

```
apimgmt api operation policy update s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --operation_id 5600b57e7e8880006a080001
        --policy_id policy
        --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
        --format xml
```

**Example: ApiManagementDeleteApiOperationPolicy**

```
apimgmt api operation policy update s--resource_group rg1
        --service_name apimService1
        --api_id testapi
        --operation_id testoperation
        --policy_id policy
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

**Example: ApiManagementCreateApiOperationPolicy**

```
apimgmt api operation policy delete s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --operation_id 5600b57e7e8880006a080001
        --policy_id policy
```

**Example: ApiManagementDeleteApiOperationPolicy**

```
apimgmt api operation policy delete s--resource_group rg1
        --service_name apimService1
        --api_id testapi
        --operation_id testoperation
        --policy_id policy
```
### apimgmt api operation policy list

list a apimgmt api operation policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--operation_id**|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|

**Example: ApiManagementCreateApiOperationPolicy**

```
apimgmt api operation policy list s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --operation_id 5600b57e7e8880006a080001
```

**Example: ApiManagementDeleteApiOperationPolicy**

```
apimgmt api operation policy list s--resource_group rg1
        --service_name apimService1
        --api_id testapi
        --operation_id testoperation
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

**Example: ApiManagementCreateApiOperationPolicy**

```
apimgmt api operation policy show s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --operation_id 5600b57e7e8880006a080001
        --format xml
        --policy_id policy
```

**Example: ApiManagementDeleteApiOperationPolicy**

```
apimgmt api operation policy show s--resource_group rg1
        --service_name apimService1
        --api_id testapi
        --operation_id testoperation
        --policy_id policy
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

**Example: ApiManagementCreateApiPolicy**

```
apimgmt api policy create s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
        --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
        --format xml
```

**Example: ApiManagementCreateApiPolicyNonXmlEncoded**

```
apimgmt api policy create s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
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

**Example: ApiManagementDeleteApiPolicy**

```
apimgmt api policy create s--resource_group rg1
        --service_name apimService1
        --api_id loggerId
        --policy_id policy
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

**Example: ApiManagementCreateApiPolicy**

```
apimgmt api policy update s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
        --value "<policies> <inbound /> <backend>    <forward-request />  </backend>  <outbound /></policies>"
        --format xml
```

**Example: ApiManagementCreateApiPolicyNonXmlEncoded**

```
apimgmt api policy update s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
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

**Example: ApiManagementDeleteApiPolicy**

```
apimgmt api policy update s--resource_group rg1
        --service_name apimService1
        --api_id loggerId
        --policy_id policy
```
### apimgmt api policy delete

delete a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementCreateApiPolicy**

```
apimgmt api policy delete s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
```

**Example: ApiManagementCreateApiPolicyNonXmlEncoded**

```
apimgmt api policy delete s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
```

**Example: ApiManagementDeleteApiPolicy**

```
apimgmt api policy delete s--resource_group rg1
        --service_name apimService1
        --api_id loggerId
        --policy_id policy
```
### apimgmt api policy list

list a apimgmt api policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateApiPolicy**

```
apimgmt api policy list s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
```

**Example: ApiManagementCreateApiPolicyNonXmlEncoded**

```
apimgmt api policy list s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
```

**Example: ApiManagementDeleteApiPolicy**

```
apimgmt api policy list s--resource_group rg1
        --service_name apimService1
        --api_id loggerId
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

**Example: ApiManagementCreateApiPolicy**

```
apimgmt api policy show s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
        --format xml
```

**Example: ApiManagementCreateApiPolicyNonXmlEncoded**

```
apimgmt api policy show s--resource_group rg1
        --service_name apimService1
        --api_id 5600b57e7e8880006a040001
        --policy_id policy
        --format rawxml
```

**Example: ApiManagementDeleteApiPolicy**

```
apimgmt api policy show s--resource_group rg1
        --service_name apimService1
        --api_id loggerId
        --policy_id policy
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

**Example: ApiManagementCreateApiRelease**

```
apimgmt api release create s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
        --notes yahooagain
```

**Example: ApiManagementUpdateApiRelease**

```
apimgmt api release create s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
        --notes yahooagain
```

**Example: ApiManagementDeleteApiRelease**

```
apimgmt api release create s--resource_group rg1
        --service_name apimService1
        --api_id 5a5fcc09124a7fa9b89f2f1d
        --release_id testrev
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

**Example: ApiManagementCreateApiRelease**

```
apimgmt api release update s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
        --notes yahooagain
```

**Example: ApiManagementUpdateApiRelease**

```
apimgmt api release update s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
        --notes yahooagain
```

**Example: ApiManagementDeleteApiRelease**

```
apimgmt api release update s--resource_group rg1
        --service_name apimService1
        --api_id 5a5fcc09124a7fa9b89f2f1d
        --release_id testrev
```
### apimgmt api release delete

delete a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release_id**|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|

**Example: ApiManagementCreateApiRelease**

```
apimgmt api release delete s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
```

**Example: ApiManagementUpdateApiRelease**

```
apimgmt api release delete s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
```

**Example: ApiManagementDeleteApiRelease**

```
apimgmt api release delete s--resource_group rg1
        --service_name apimService1
        --api_id 5a5fcc09124a7fa9b89f2f1d
        --release_id testrev
```
### apimgmt api release list

list a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|

**Example: ApiManagementCreateApiRelease**

```
apimgmt api release list s--resource_group rg1
        --service_name apimService1
        --api_id a1
```

**Example: ApiManagementUpdateApiRelease**

```
apimgmt api release list s--resource_group rg1
        --service_name apimService1
        --api_id a1
```

**Example: ApiManagementDeleteApiRelease**

```
apimgmt api release list s--resource_group rg1
        --service_name apimService1
        --api_id 5a5fcc09124a7fa9b89f2f1d
```
### apimgmt api release show

show a apimgmt api release.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|**--release_id**|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|

**Example: ApiManagementCreateApiRelease**

```
apimgmt api release show s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
```

**Example: ApiManagementUpdateApiRelease**

```
apimgmt api release show s--resource_group rg1
        --service_name apimService1
        --api_id a1
        --release_id testrev
```

**Example: ApiManagementDeleteApiRelease**

```
apimgmt api release show s--resource_group rg1
        --service_name apimService1
        --api_id 5a5fcc09124a7fa9b89f2f1d
        --release_id testrev
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

**Example: ApiManagementCreateApiSchema**

```
apimgmt api schema create s--resource_group rg1
        --service_name apimService1
        --api_id 59d6bb8f1f7fab13dc67ec9b
        --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
        --content_type application/vnd.ms-azure-apim.xsd+xml
```

**Example: ApiManagementDeleteApiSchema**

```
apimgmt api schema create s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --schema_id 59d5b28e1f7fab116402044e
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

**Example: ApiManagementCreateApiSchema**

```
apimgmt api schema update s--resource_group rg1
        --service_name apimService1
        --api_id 59d6bb8f1f7fab13dc67ec9b
        --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
        --content_type application/vnd.ms-azure-apim.xsd+xml
```

**Example: ApiManagementDeleteApiSchema**

```
apimgmt api schema update s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --schema_id 59d5b28e1f7fab116402044e
```
### apimgmt api schema delete

delete a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema_id**|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|

**Example: ApiManagementCreateApiSchema**

```
apimgmt api schema delete s--resource_group rg1
        --service_name apimService1
        --api_id 59d6bb8f1f7fab13dc67ec9b
        --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
```

**Example: ApiManagementDeleteApiSchema**

```
apimgmt api schema delete s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --schema_id 59d5b28e1f7fab116402044e
```
### apimgmt api schema list

list a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateApiSchema**

```
apimgmt api schema list s--resource_group rg1
        --service_name apimService1
        --api_id 59d6bb8f1f7fab13dc67ec9b
```

**Example: ApiManagementDeleteApiSchema**

```
apimgmt api schema list s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
```
### apimgmt api schema show

show a apimgmt api schema.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--schema_id**|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|

**Example: ApiManagementCreateApiSchema**

```
apimgmt api schema show s--resource_group rg1
        --service_name apimService1
        --api_id 59d6bb8f1f7fab13dc67ec9b
        --schema_id ec12520d-9d48-4e7b-8f39-698ca2ac63f1
```

**Example: ApiManagementDeleteApiSchema**

```
apimgmt api schema show s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --schema_id 59d5b28e1f7fab116402044e
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

**Example: ApiManagementCreateApiTagDescription**

```
apimgmt api tagdescription create s--resource_group rg1
        --service_name apimService1
        --api_id 5931a75ae4bbd512a88c680b
        --tag_id tagId1
        --description "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API"
        --external_docs_url http://some.url/additionaldoc
        --external_docs_description "Description of the external docs resource"
```

**Example: ApiManagementDeleteApiTagDescription**

```
apimgmt api tagdescription create s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --tag_id 59d5b28e1f7fab116402044e
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

**Example: ApiManagementCreateApiTagDescription**

```
apimgmt api tagdescription update s--resource_group rg1
        --service_name apimService1
        --api_id 5931a75ae4bbd512a88c680b
        --tag_id tagId1
        --description "Some description that will be displayed for operation's tag if the tag is assigned to operation of the API"
        --external_docs_url http://some.url/additionaldoc
        --external_docs_description "Description of the external docs resource"
```

**Example: ApiManagementDeleteApiTagDescription**

```
apimgmt api tagdescription update s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --tag_id 59d5b28e1f7fab116402044e
```
### apimgmt api tagdescription delete

delete a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

**Example: ApiManagementCreateApiTagDescription**

```
apimgmt api tagdescription delete s--resource_group rg1
        --service_name apimService1
        --api_id 5931a75ae4bbd512a88c680b
        --tag_id tagId1
```

**Example: ApiManagementDeleteApiTagDescription**

```
apimgmt api tagdescription delete s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --tag_id 59d5b28e1f7fab116402044e
```
### apimgmt api tagdescription list

list a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateApiTagDescription**

```
apimgmt api tagdescription list s--resource_group rg1
        --service_name apimService1
        --api_id 5931a75ae4bbd512a88c680b
```

**Example: ApiManagementDeleteApiTagDescription**

```
apimgmt api tagdescription list s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
```
### apimgmt api tagdescription show

show a apimgmt api tagdescription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

**Example: ApiManagementCreateApiTagDescription**

```
apimgmt api tagdescription show s--resource_group rg1
        --service_name apimService1
        --api_id 5931a75ae4bbd512a88c680b
        --tag_id tagId1
```

**Example: ApiManagementDeleteApiTagDescription**

```
apimgmt api tagdescription show s--resource_group rg1
        --service_name apimService1
        --api_id 59d5b28d1f7fab116c282650
        --tag_id 59d5b28e1f7fab116402044e
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

**Example: ApiManagementCreateApiVersionSet**

```
apimgmt apiversionset create s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
        --description "Version configuration"
        --display_name "api set 1"
        --versioning_scheme Segment
```

**Example: ApiManagementUpdateApiVersionSet**

```
apimgmt apiversionset create s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
        --description "Version configuration"
        --display_name "api set 1"
        --versioning_scheme Segment
```

**Example: ApiManagementDeleteApiVersionSet**

```
apimgmt apiversionset create s--resource_group rg1
        --service_name apimService1
        --version_set_id a1
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

**Example: ApiManagementCreateApiVersionSet**

```
apimgmt apiversionset update s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
        --description "Version configuration"
        --display_name "api set 1"
        --versioning_scheme Segment
```

**Example: ApiManagementUpdateApiVersionSet**

```
apimgmt apiversionset update s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
        --description "Version configuration"
        --display_name "api set 1"
        --versioning_scheme Segment
```

**Example: ApiManagementDeleteApiVersionSet**

```
apimgmt apiversionset update s--resource_group rg1
        --service_name apimService1
        --version_set_id a1
```
### apimgmt apiversionset delete

delete a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--version_set_id**|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|

**Example: ApiManagementCreateApiVersionSet**

```
apimgmt apiversionset delete s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
```

**Example: ApiManagementUpdateApiVersionSet**

```
apimgmt apiversionset delete s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
```

**Example: ApiManagementDeleteApiVersionSet**

```
apimgmt apiversionset delete s--resource_group rg1
        --service_name apimService1
        --version_set_id a1
```
### apimgmt apiversionset list

list a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateApiVersionSet**

```
apimgmt apiversionset list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateApiVersionSet**

```
apimgmt apiversionset list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteApiVersionSet**

```
apimgmt apiversionset list s--resource_group rg1
        --service_name apimService1
```
### apimgmt apiversionset show

show a apimgmt apiversionset.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--version_set_id**|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|

**Example: ApiManagementCreateApiVersionSet**

```
apimgmt apiversionset show s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
```

**Example: ApiManagementUpdateApiVersionSet**

```
apimgmt apiversionset show s--resource_group rg1
        --service_name apimService1
        --version_set_id api1
```

**Example: ApiManagementDeleteApiVersionSet**

```
apimgmt apiversionset show s--resource_group rg1
        --service_name apimService1
        --version_set_id a1
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

**Example: ApiManagementCreateAuthorizationServer**

```
apimgmt authorizationserver create s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
        --description "test server"
        --token_endpoint https://www.contoso.com/oauth2/token
        --support_state true
        --default_scope "read write"
        --client_secret 2
        --resource_owner_username un
        --resource_owner_password pwd
        --display_name test2
        --client_registration_endpoint https://www.contoso.com/apps
        --authorization_endpoint https://www.contoso.com/oauth2/auth
        --client_id 1
```

**Example: ApiManagementUpdateAuthorizationServer**

```
apimgmt authorizationserver create s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
        --client_secret updated
        --client_id update
```

**Example: ApiManagementDeleteAuthorizationServer**

```
apimgmt authorizationserver create s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer2
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

**Example: ApiManagementCreateAuthorizationServer**

```
apimgmt authorizationserver update s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
        --description "test server"
        --token_endpoint https://www.contoso.com/oauth2/token
        --support_state true
        --default_scope "read write"
        --client_secret 2
        --resource_owner_username un
        --resource_owner_password pwd
        --display_name test2
        --client_registration_endpoint https://www.contoso.com/apps
        --authorization_endpoint https://www.contoso.com/oauth2/auth
        --client_id 1
```

**Example: ApiManagementUpdateAuthorizationServer**

```
apimgmt authorizationserver update s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
        --client_secret updated
        --client_id update
```

**Example: ApiManagementDeleteAuthorizationServer**

```
apimgmt authorizationserver update s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer2
```
### apimgmt authorizationserver delete

delete a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--authsid**|default|Identifier of the authorization server.|authsid|authsid|

**Example: ApiManagementCreateAuthorizationServer**

```
apimgmt authorizationserver delete s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
```

**Example: ApiManagementUpdateAuthorizationServer**

```
apimgmt authorizationserver delete s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
```

**Example: ApiManagementDeleteAuthorizationServer**

```
apimgmt authorizationserver delete s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer2
```
### apimgmt authorizationserver list

list a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateAuthorizationServer**

```
apimgmt authorizationserver list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateAuthorizationServer**

```
apimgmt authorizationserver list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteAuthorizationServer**

```
apimgmt authorizationserver list s--resource_group rg1
        --service_name apimService1
```
### apimgmt authorizationserver show

show a apimgmt authorizationserver.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--authsid**|default|Identifier of the authorization server.|authsid|authsid|

**Example: ApiManagementCreateAuthorizationServer**

```
apimgmt authorizationserver show s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
```

**Example: ApiManagementUpdateAuthorizationServer**

```
apimgmt authorizationserver show s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer
```

**Example: ApiManagementDeleteAuthorizationServer**

```
apimgmt authorizationserver show s--resource_group rg1
        --service_name apimService1
        --authsid newauthServer2
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

**Example: ApiManagementCreateBackendServiceFabric**

```
apimgmt backend create s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
        --description "Service Fabric Test App 1"
        --url fabric:/mytestapp/mytestservice
        --protocol http
```

**Example: ApiManagementCreateBackendProxyBackend**

```
apimgmt backend create s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
        --description description5308
        --url https://backendname2644/
        --protocol http
```

**Example: ApiManagementUpdateBackend**

```
apimgmt backend create s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
        --description description5308
```

**Example: ApiManagementDeleteBackend**

```
apimgmt backend create s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
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

**Example: ApiManagementCreateBackendServiceFabric**

```
apimgmt backend update s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
        --description "Service Fabric Test App 1"
        --url fabric:/mytestapp/mytestservice
        --protocol http
```

**Example: ApiManagementCreateBackendProxyBackend**

```
apimgmt backend update s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
        --description description5308
        --url https://backendname2644/
        --protocol http
```

**Example: ApiManagementUpdateBackend**

```
apimgmt backend update s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
        --description description5308
```

**Example: ApiManagementDeleteBackend**

```
apimgmt backend update s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
```
### apimgmt backend delete

delete a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--backend_id**|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|

**Example: ApiManagementCreateBackendServiceFabric**

```
apimgmt backend delete s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
```

**Example: ApiManagementCreateBackendProxyBackend**

```
apimgmt backend delete s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
```

**Example: ApiManagementUpdateBackend**

```
apimgmt backend delete s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
```

**Example: ApiManagementDeleteBackend**

```
apimgmt backend delete s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
```
### apimgmt backend list

list a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateBackendServiceFabric**

```
apimgmt backend list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateBackendProxyBackend**

```
apimgmt backend list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateBackend**

```
apimgmt backend list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteBackend**

```
apimgmt backend list s--resource_group rg1
        --service_name apimService1
```
### apimgmt backend show

show a apimgmt backend.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--backend_id**|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|

**Example: ApiManagementCreateBackendServiceFabric**

```
apimgmt backend show s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
```

**Example: ApiManagementCreateBackendProxyBackend**

```
apimgmt backend show s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
```

**Example: ApiManagementUpdateBackend**

```
apimgmt backend show s--resource_group rg1
        --service_name apimService1
        --backend_id proxybackend
```

**Example: ApiManagementDeleteBackend**

```
apimgmt backend show s--resource_group rg1
        --service_name apimService1
        --backend_id sfbackend
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

**Example: ApiManagementCreateCache**

```
apimgmt cache create s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
        --description "Redis cache instances in West India"
        --connection_string contoso5.redis.cache.windows.net,ssl=true,password=...
        --resource_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}"
```

**Example: ApiManagementUpdateCache**

```
apimgmt cache create s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
        --description "Update Cache in west India"
```

**Example: ApiManagementDeleteCache**

```
apimgmt cache create s--resource_group rg1
        --service_name apimService1
        --cache_id southindia
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

**Example: ApiManagementCreateCache**

```
apimgmt cache update s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
        --description "Redis cache instances in West India"
        --connection_string contoso5.redis.cache.windows.net,ssl=true,password=...
        --resource_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.Cache/Redis/{{ redis_name }}"
```

**Example: ApiManagementUpdateCache**

```
apimgmt cache update s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
        --description "Update Cache in west India"
```

**Example: ApiManagementDeleteCache**

```
apimgmt cache update s--resource_group rg1
        --service_name apimService1
        --cache_id southindia
```
### apimgmt cache delete

delete a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--cache_id**|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|

**Example: ApiManagementCreateCache**

```
apimgmt cache delete s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
```

**Example: ApiManagementUpdateCache**

```
apimgmt cache delete s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
```

**Example: ApiManagementDeleteCache**

```
apimgmt cache delete s--resource_group rg1
        --service_name apimService1
        --cache_id southindia
```
### apimgmt cache list

list a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateCache**

```
apimgmt cache list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateCache**

```
apimgmt cache list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteCache**

```
apimgmt cache list s--resource_group rg1
        --service_name apimService1
```
### apimgmt cache show

show a apimgmt cache.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--cache_id**|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|

**Example: ApiManagementCreateCache**

```
apimgmt cache show s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
```

**Example: ApiManagementUpdateCache**

```
apimgmt cache show s--resource_group rg1
        --service_name apimService1
        --cache_id westindia
```

**Example: ApiManagementDeleteCache**

```
apimgmt cache show s--resource_group rg1
        --service_name apimService1
        --cache_id southindia
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

**Example: ApiManagementCreateCertificate**

```
apimgmt certificate create s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
        --data "****************Base 64 Encoded Certificate *******************************"
        --password "****Certificate Password******"
```

**Example: ApiManagementDeleteCertificate**

```
apimgmt certificate create s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
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

**Example: ApiManagementCreateCertificate**

```
apimgmt certificate update s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
        --data "****************Base 64 Encoded Certificate *******************************"
        --password "****Certificate Password******"
```

**Example: ApiManagementDeleteCertificate**

```
apimgmt certificate update s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
```
### apimgmt certificate delete

delete a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--certificate_id**|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|

**Example: ApiManagementCreateCertificate**

```
apimgmt certificate delete s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
```

**Example: ApiManagementDeleteCertificate**

```
apimgmt certificate delete s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
```
### apimgmt certificate list

list a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateCertificate**

```
apimgmt certificate list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteCertificate**

```
apimgmt certificate list s--resource_group rg1
        --service_name apimService1
```
### apimgmt certificate show

show a apimgmt certificate.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--certificate_id**|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|

**Example: ApiManagementCreateCertificate**

```
apimgmt certificate show s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
```

**Example: ApiManagementDeleteCertificate**

```
apimgmt certificate show s--resource_group rg1
        --service_name apimService1
        --certificate_id tempcert
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

**Example: ApiManagementCreateDiagnostic**

```
apimgmt diagnostic create s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/azuremonitor
```

**Example: ApiManagementUpdateDiagnostic**

```
apimgmt diagnostic create s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/applicationinsights
```

**Example: ApiManagementDeleteDiagnostic**

```
apimgmt diagnostic create s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
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

**Example: ApiManagementCreateDiagnostic**

```
apimgmt diagnostic update s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/azuremonitor
```

**Example: ApiManagementUpdateDiagnostic**

```
apimgmt diagnostic update s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
        --always_log allErrors
        --logger_id /loggers/applicationinsights
```

**Example: ApiManagementDeleteDiagnostic**

```
apimgmt diagnostic update s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
```
### apimgmt diagnostic delete

delete a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

**Example: ApiManagementCreateDiagnostic**

```
apimgmt diagnostic delete s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
```

**Example: ApiManagementUpdateDiagnostic**

```
apimgmt diagnostic delete s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
```

**Example: ApiManagementDeleteDiagnostic**

```
apimgmt diagnostic delete s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
```
### apimgmt diagnostic list

list a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateDiagnostic**

```
apimgmt diagnostic list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateDiagnostic**

```
apimgmt diagnostic list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteDiagnostic**

```
apimgmt diagnostic list s--resource_group rg1
        --service_name apimService1
```
### apimgmt diagnostic show

show a apimgmt diagnostic.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--diagnostic_id**|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|

**Example: ApiManagementCreateDiagnostic**

```
apimgmt diagnostic show s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
```

**Example: ApiManagementUpdateDiagnostic**

```
apimgmt diagnostic show s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
```

**Example: ApiManagementDeleteDiagnostic**

```
apimgmt diagnostic show s--resource_group rg1
        --service_name apimService1
        --diagnostic_id applicationinsights
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

**Example: ApiManagementCreateGroup**

```
apimgmt group create s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
        --display_name "temp group"
```

**Example: ApiManagementCreateGroupExternal**

```
apimgmt group create s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
        --display_name "NewGroup (samiraad.onmicrosoft.com)"
        --description "new group to test"
        --type external
        --external_id aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d
```

**Example: ApiManagementUpdateGroup**

```
apimgmt group create s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
        --display_name "temp group"
```

**Example: ApiManagementDeleteGroup**

```
apimgmt group create s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
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

**Example: ApiManagementCreateGroup**

```
apimgmt group update s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
        --display_name "temp group"
```

**Example: ApiManagementCreateGroupExternal**

```
apimgmt group update s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
        --display_name "NewGroup (samiraad.onmicrosoft.com)"
        --description "new group to test"
        --type external
        --external_id aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d
```

**Example: ApiManagementUpdateGroup**

```
apimgmt group update s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
        --display_name "temp group"
```

**Example: ApiManagementDeleteGroup**

```
apimgmt group update s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
```
### apimgmt group delete

delete a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

**Example: ApiManagementCreateGroup**

```
apimgmt group delete s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
```

**Example: ApiManagementCreateGroupExternal**

```
apimgmt group delete s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
```

**Example: ApiManagementUpdateGroup**

```
apimgmt group delete s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
```

**Example: ApiManagementDeleteGroup**

```
apimgmt group delete s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
```
### apimgmt group list

list a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateGroup**

```
apimgmt group list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateGroupExternal**

```
apimgmt group list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateGroup**

```
apimgmt group list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteGroup**

```
apimgmt group list s--resource_group rg1
        --service_name apimService1
```
### apimgmt group show

show a apimgmt group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

**Example: ApiManagementCreateGroup**

```
apimgmt group show s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
```

**Example: ApiManagementCreateGroupExternal**

```
apimgmt group show s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
```

**Example: ApiManagementUpdateGroup**

```
apimgmt group show s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
```

**Example: ApiManagementDeleteGroup**

```
apimgmt group show s--resource_group rg1
        --service_name apimService1
        --group_id aadGroup
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

**Example: ApiManagementCreateGroupUser**

```
apimgmt group user create s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
        --user_id 59307d350af58404d8a26300
```

**Example: ApiManagementDeleteGroupUser**

```
apimgmt group user create s--resource_group rg1
        --service_name apimService1
        --group_id templategroup
        --user_id 59307d350af58404d8a26300
```
### apimgmt group user delete

delete a apimgmt group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementCreateGroupUser**

```
apimgmt group user delete s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
        --user_id 59307d350af58404d8a26300
```

**Example: ApiManagementDeleteGroupUser**

```
apimgmt group user delete s--resource_group rg1
        --service_name apimService1
        --group_id templategroup
        --user_id 59307d350af58404d8a26300
```
### apimgmt group user list

list a apimgmt group user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

**Example: ApiManagementCreateGroupUser**

```
apimgmt group user list s--resource_group rg1
        --service_name apimService1
        --group_id tempgroup
```

**Example: ApiManagementDeleteGroupUser**

```
apimgmt group user list s--resource_group rg1
        --service_name apimService1
        --group_id templategroup
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

**Example: ApiManagementCreateIdentityProvider**

```
apimgmt identityprovider create s--resource_group rg1
        --service_name apimService1
        --name facebook
        --client_id facebookid
        --client_secret facebookapplicationsecret
```

**Example: ApiManagementUpdateIdentityProvider**

```
apimgmt identityprovider create s--resource_group rg1
        --service_name apimService1
        --name facebook
        --client_id updatedfacebookid
        --client_secret updatedfacebooksecret
```

**Example: ApiManagementDeleteIdentityProvider**

```
apimgmt identityprovider create s--resource_group rg1
        --service_name apimService1
        --name aad
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

**Example: ApiManagementCreateIdentityProvider**

```
apimgmt identityprovider update s--resource_group rg1
        --service_name apimService1
        --name facebook
        --client_id facebookid
        --client_secret facebookapplicationsecret
```

**Example: ApiManagementUpdateIdentityProvider**

```
apimgmt identityprovider update s--resource_group rg1
        --service_name apimService1
        --name facebook
        --client_id updatedfacebookid
        --client_secret updatedfacebooksecret
```

**Example: ApiManagementDeleteIdentityProvider**

```
apimgmt identityprovider update s--resource_group rg1
        --service_name apimService1
        --name aad
```
### apimgmt identityprovider delete

delete a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|

**Example: ApiManagementCreateIdentityProvider**

```
apimgmt identityprovider delete s--resource_group rg1
        --service_name apimService1
        --name facebook
```

**Example: ApiManagementUpdateIdentityProvider**

```
apimgmt identityprovider delete s--resource_group rg1
        --service_name apimService1
        --name facebook
```

**Example: ApiManagementDeleteIdentityProvider**

```
apimgmt identityprovider delete s--resource_group rg1
        --service_name apimService1
        --name aad
```
### apimgmt identityprovider list

list a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateIdentityProvider**

```
apimgmt identityprovider list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateIdentityProvider**

```
apimgmt identityprovider list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteIdentityProvider**

```
apimgmt identityprovider list s--resource_group rg1
        --service_name apimService1
```
### apimgmt identityprovider show

show a apimgmt identityprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|

**Example: ApiManagementCreateIdentityProvider**

```
apimgmt identityprovider show s--resource_group rg1
        --service_name apimService1
        --name facebook
```

**Example: ApiManagementUpdateIdentityProvider**

```
apimgmt identityprovider show s--resource_group rg1
        --service_name apimService1
        --name facebook
```

**Example: ApiManagementDeleteIdentityProvider**

```
apimgmt identityprovider show s--resource_group rg1
        --service_name apimService1
        --name aad
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

**Example: ApiManagementCreateEHLogger**

```
apimgmt logger create s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
        --logger_type azureEventHub
        --description "adding a new logger"
```

**Example: ApiManagementCreateAILogger**

```
apimgmt logger create s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
        --logger_type applicationInsights
        --description "adding a new logger"
```

**Example: ApiManagementUpdateLogger**

```
apimgmt logger create s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementDeleteLogger**

```
apimgmt logger create s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
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

**Example: ApiManagementCreateEHLogger**

```
apimgmt logger update s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
        --logger_type azureEventHub
        --description "adding a new logger"
```

**Example: ApiManagementCreateAILogger**

```
apimgmt logger update s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
        --logger_type applicationInsights
        --description "adding a new logger"
```

**Example: ApiManagementUpdateLogger**

```
apimgmt logger update s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementDeleteLogger**

```
apimgmt logger update s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```
### apimgmt logger delete

delete a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--logger_id**|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|

**Example: ApiManagementCreateEHLogger**

```
apimgmt logger delete s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementCreateAILogger**

```
apimgmt logger delete s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementUpdateLogger**

```
apimgmt logger delete s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementDeleteLogger**

```
apimgmt logger delete s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```
### apimgmt logger list

list a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateEHLogger**

```
apimgmt logger list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateAILogger**

```
apimgmt logger list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateLogger**

```
apimgmt logger list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteLogger**

```
apimgmt logger list s--resource_group rg1
        --service_name apimService1
```
### apimgmt logger show

show a apimgmt logger.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--logger_id**|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|

**Example: ApiManagementCreateEHLogger**

```
apimgmt logger show s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementCreateAILogger**

```
apimgmt logger show s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementUpdateLogger**

```
apimgmt logger show s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
```

**Example: ApiManagementDeleteLogger**

```
apimgmt logger show s--resource_group rg1
        --service_name apimService1
        --logger_id loggerId
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

**Example: ApiManagementCreateNotification**

```
apimgmt notification create s--resource_group rg1
        --service_name apimService1
        --name RequestPublisherNotificationMessage
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

**Example: ApiManagementCreateNotification**

```
apimgmt notification update s--resource_group rg1
        --service_name apimService1
        --name RequestPublisherNotificationMessage
```
### apimgmt notification list

list a apimgmt notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateNotification**

```
apimgmt notification list s--resource_group rg1
        --service_name apimService1
```
### apimgmt notification show

show a apimgmt notification.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Notification Name Identifier.|notification_name|notificationName|

**Example: ApiManagementCreateNotification**

```
apimgmt notification show s--resource_group rg1
        --service_name apimService1
        --name RequestPublisherNotificationMessage
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

**Example: ApiManagementCreateNotificationRecipientEmail**

```
apimgmt notification recipientemail create s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --email foobar@live.com
```

**Example: ApiManagementDeleteNotificationRecipientEmail**

```
apimgmt notification recipientemail create s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --email contoso@live.com
```
### apimgmt notification recipientemail update

update a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--email**|default|Email identifier.|email|email|

**Example: ApiManagementCreateNotificationRecipientEmail**

```
apimgmt notification recipientemail update s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --email foobar@live.com
```

**Example: ApiManagementDeleteNotificationRecipientEmail**

```
apimgmt notification recipientemail update s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --email contoso@live.com
```
### apimgmt notification recipientemail delete

delete a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--email**|default|Email identifier.|email|email|

**Example: ApiManagementCreateNotificationRecipientEmail**

```
apimgmt notification recipientemail delete s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --email foobar@live.com
```

**Example: ApiManagementDeleteNotificationRecipientEmail**

```
apimgmt notification recipientemail delete s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --email contoso@live.com
```
### apimgmt notification recipientemail list

list a apimgmt notification recipientemail.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|

**Example: ApiManagementCreateNotificationRecipientEmail**

```
apimgmt notification recipientemail list s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
```

**Example: ApiManagementDeleteNotificationRecipientEmail**

```
apimgmt notification recipientemail list s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
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

**Example: ApiManagementCreateNotificationRecipientUser**

```
apimgmt notification recipientuser create s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --user_id 576823d0a40f7e74ec07d642
```

**Example: ApiManagementDeleteNotificationRecipientUser**

```
apimgmt notification recipientuser create s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --user_id 576823d0a40f7e74ec07d642
```
### apimgmt notification recipientuser update

update a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementCreateNotificationRecipientUser**

```
apimgmt notification recipientuser update s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --user_id 576823d0a40f7e74ec07d642
```

**Example: ApiManagementDeleteNotificationRecipientUser**

```
apimgmt notification recipientuser update s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --user_id 576823d0a40f7e74ec07d642
```
### apimgmt notification recipientuser delete

delete a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementCreateNotificationRecipientUser**

```
apimgmt notification recipientuser delete s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --user_id 576823d0a40f7e74ec07d642
```

**Example: ApiManagementDeleteNotificationRecipientUser**

```
apimgmt notification recipientuser delete s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
        --user_id 576823d0a40f7e74ec07d642
```
### apimgmt notification recipientuser list

list a apimgmt notification recipientuser.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--notification_name**|default|Notification Name Identifier.|notification_name|notificationName|

**Example: ApiManagementCreateNotificationRecipientUser**

```
apimgmt notification recipientuser list s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
```

**Example: ApiManagementDeleteNotificationRecipientUser**

```
apimgmt notification recipientuser list s--resource_group rg1
        --service_name apimService1
        --notification_name RequestPublisherNotificationMessage
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

**Example: ApiManagementCreateOpenIdConnectProvider**

```
apimgmt openidconnectprovider create s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
        --display_name templateoidprovider3
        --metadata_endpoint https://oidprovider-template3.net
        --client_id oidprovidertemplate3
```

**Example: ApiManagementUpdateOpenIdConnectProvider**

```
apimgmt openidconnectprovider create s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect2
        --client_secret updatedsecret
```

**Example: ApiManagementDeleteOpenIdConnectProvider**

```
apimgmt openidconnectprovider create s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
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

**Example: ApiManagementCreateOpenIdConnectProvider**

```
apimgmt openidconnectprovider update s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
        --display_name templateoidprovider3
        --metadata_endpoint https://oidprovider-template3.net
        --client_id oidprovidertemplate3
```

**Example: ApiManagementUpdateOpenIdConnectProvider**

```
apimgmt openidconnectprovider update s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect2
        --client_secret updatedsecret
```

**Example: ApiManagementDeleteOpenIdConnectProvider**

```
apimgmt openidconnectprovider update s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
```
### apimgmt openidconnectprovider delete

delete a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--opid**|default|Identifier of the OpenID Connect Provider.|opid|opid|

**Example: ApiManagementCreateOpenIdConnectProvider**

```
apimgmt openidconnectprovider delete s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
```

**Example: ApiManagementUpdateOpenIdConnectProvider**

```
apimgmt openidconnectprovider delete s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect2
```

**Example: ApiManagementDeleteOpenIdConnectProvider**

```
apimgmt openidconnectprovider delete s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
```
### apimgmt openidconnectprovider list

list a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateOpenIdConnectProvider**

```
apimgmt openidconnectprovider list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateOpenIdConnectProvider**

```
apimgmt openidconnectprovider list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteOpenIdConnectProvider**

```
apimgmt openidconnectprovider list s--resource_group rg1
        --service_name apimService1
```
### apimgmt openidconnectprovider show

show a apimgmt openidconnectprovider.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--opid**|default|Identifier of the OpenID Connect Provider.|opid|opid|

**Example: ApiManagementCreateOpenIdConnectProvider**

```
apimgmt openidconnectprovider show s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
```

**Example: ApiManagementUpdateOpenIdConnectProvider**

```
apimgmt openidconnectprovider show s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect2
```

**Example: ApiManagementDeleteOpenIdConnectProvider**

```
apimgmt openidconnectprovider show s--resource_group rg1
        --service_name apimService1
        --opid templateOpenIdConnect3
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

**Example: ApiManagementCreatePolicy**

```
apimgmt policy create s--resource_group rg1
        --service_name apimService1
        --policy_id policy
        --value "<policies>
  <inbound />
  <backend>
    <forward-request />
  </backend>
  <outbound />
</policies>"
        --format xml
```

**Example: ApiManagementDeletePolicy**

```
apimgmt policy create s--resource_group rg1
        --service_name apimService1
        --policy_id policy
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

**Example: ApiManagementCreatePolicy**

```
apimgmt policy update s--resource_group rg1
        --service_name apimService1
        --policy_id policy
        --value "<policies>
  <inbound />
  <backend>
    <forward-request />
  </backend>
  <outbound />
</policies>"
        --format xml
```

**Example: ApiManagementDeletePolicy**

```
apimgmt policy update s--resource_group rg1
        --service_name apimService1
        --policy_id policy
```
### apimgmt policy delete

delete a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementCreatePolicy**

```
apimgmt policy delete s--resource_group rg1
        --service_name apimService1
        --policy_id policy
```

**Example: ApiManagementDeletePolicy**

```
apimgmt policy delete s--resource_group rg1
        --service_name apimService1
        --policy_id policy
```
### apimgmt policy list

list a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreatePolicy**

```
apimgmt policy list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeletePolicy**

```
apimgmt policy list s--resource_group rg1
        --service_name apimService1
```
### apimgmt policy show

show a apimgmt policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|
|--format|default|Format of the policyContent.|/format|/properties/format|

**Example: ApiManagementCreatePolicy**

```
apimgmt policy show s--resource_group rg1
        --service_name apimService1
        --policy_id policy
        --format xml
```

**Example: ApiManagementDeletePolicy**

```
apimgmt policy show s--resource_group rg1
        --service_name apimService1
        --policy_id policy
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

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apimgmt portalsetting create s--resource_group rg1
        --name apimService1
        --url http://contoso.com/delegation
        --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
```

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apimgmt portalsetting create s--resource_group rg1
        --name apimService1
        --url http://contoso.com/delegation
        --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
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

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apimgmt portalsetting update s--resource_group rg1
        --name apimService1
        --url http://contoso.com/delegation
        --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
```

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apimgmt portalsetting update s--resource_group rg1
        --name apimService1
        --url http://contoso.com/delegation
        --validation_key nVF7aKIvr9mV/RM5lOD0sYoi8ThXTRHQP7o66hvUmjCDkPKR3qxPu/otJcNciz2aQdqPuzJH3ECG4TU2yZjQ7Q==
```
### apimgmt portalsetting show

show a apimgmt portalsetting.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apimgmt portalsetting show s--resource_group rg1
        --name apimService1
```

**Example: ApiManagementPortalSettingsUpdateDelegation**

```
apimgmt portalsetting show s--resource_group rg1
        --name apimService1
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

**Example: ApiManagementCreateProduct**

```
apimgmt product create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --display_name "Test Template ProductName 4"
```

**Example: ApiManagementUpdateProduct**

```
apimgmt product create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --display_name "Test Template ProductName 4"
```

**Example: ApiManagementDeleteProduct**

```
apimgmt product create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
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

**Example: ApiManagementCreateProduct**

```
apimgmt product update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --display_name "Test Template ProductName 4"
```

**Example: ApiManagementUpdateProduct**

```
apimgmt product update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --display_name "Test Template ProductName 4"
```

**Example: ApiManagementDeleteProduct**

```
apimgmt product update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```
### apimgmt product delete

delete a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

**Example: ApiManagementCreateProduct**

```
apimgmt product delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```

**Example: ApiManagementUpdateProduct**

```
apimgmt product delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```

**Example: ApiManagementDeleteProduct**

```
apimgmt product delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```
### apimgmt product list

list a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateProduct**

```
apimgmt product list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateProduct**

```
apimgmt product list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteProduct**

```
apimgmt product list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateProduct**

```
apimgmt product list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateProduct**

```
apimgmt product list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteProduct**

```
apimgmt product list s--resource_group rg1
        --service_name apimService1
```
### apimgmt product show

show a apimgmt product.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

**Example: ApiManagementCreateProduct**

```
apimgmt product show s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```

**Example: ApiManagementUpdateProduct**

```
apimgmt product show s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```

**Example: ApiManagementDeleteProduct**

```
apimgmt product show s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
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

**Example: ApiManagementCreateProductApi**

```
apimgmt product api create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --api_id echo-api
```

**Example: ApiManagementDeleteProductApi**

```
apimgmt product api create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --api_id echo-api
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

**Example: ApiManagementCreateProductApi**

```
apimgmt product api update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --api_id echo-api
```

**Example: ApiManagementDeleteProductApi**

```
apimgmt product api update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --api_id echo-api
```
### apimgmt product api delete

delete a apimgmt product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--api_id**|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|

**Example: ApiManagementCreateProductApi**

```
apimgmt product api delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --api_id echo-api
```

**Example: ApiManagementDeleteProductApi**

```
apimgmt product api delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --api_id echo-api
```
### apimgmt product api list

list a apimgmt product api.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

**Example: ApiManagementCreateProductApi**

```
apimgmt product api list s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```

**Example: ApiManagementDeleteProductApi**

```
apimgmt product api list s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
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

**Example: ApiManagementCreateProductGroup**

```
apimgmt product group create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --group_id templateGroup
```

**Example: ApiManagementDeleteProductGroup**

```
apimgmt product group create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --group_id templateGroup
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

**Example: ApiManagementCreateProductGroup**

```
apimgmt product group update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --group_id templateGroup
```

**Example: ApiManagementDeleteProductGroup**

```
apimgmt product group update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --group_id templateGroup
```
### apimgmt product group delete

delete a apimgmt product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--group_id**|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|

**Example: ApiManagementCreateProductGroup**

```
apimgmt product group delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --group_id templateGroup
```

**Example: ApiManagementDeleteProductGroup**

```
apimgmt product group delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --group_id templateGroup
```
### apimgmt product group list

list a apimgmt product group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

**Example: ApiManagementCreateProductGroup**

```
apimgmt product group list s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
```

**Example: ApiManagementDeleteProductGroup**

```
apimgmt product group list s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
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

**Example: ApiManagementCreateProductPolicy**

```
apimgmt product policy create s--resource_group rg1
        --service_name apimService1
        --product_id 5702e97e5157a50f48dce801
        --policy_id policy
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

**Example: ApiManagementDeleteProductPolicy**

```
apimgmt product policy create s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --policy_id policy
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

**Example: ApiManagementCreateProductPolicy**

```
apimgmt product policy update s--resource_group rg1
        --service_name apimService1
        --product_id 5702e97e5157a50f48dce801
        --policy_id policy
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

**Example: ApiManagementDeleteProductPolicy**

```
apimgmt product policy update s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --policy_id policy
```
### apimgmt product policy delete

delete a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|**--policy_id**|default|The identifier of the Policy.|policy_id|policyId|

**Example: ApiManagementCreateProductPolicy**

```
apimgmt product policy delete s--resource_group rg1
        --service_name apimService1
        --product_id 5702e97e5157a50f48dce801
        --policy_id policy
```

**Example: ApiManagementDeleteProductPolicy**

```
apimgmt product policy delete s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --policy_id policy
```
### apimgmt product policy list

list a apimgmt product policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--product_id**|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|

**Example: ApiManagementCreateProductPolicy**

```
apimgmt product policy list s--resource_group rg1
        --service_name apimService1
        --product_id 5702e97e5157a50f48dce801
```

**Example: ApiManagementDeleteProductPolicy**

```
apimgmt product policy list s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
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

**Example: ApiManagementCreateProductPolicy**

```
apimgmt product policy show s--resource_group rg1
        --service_name apimService1
        --product_id 5702e97e5157a50f48dce801
        --policy_id policy
        --format xml
```

**Example: ApiManagementDeleteProductPolicy**

```
apimgmt product policy show s--resource_group rg1
        --service_name apimService1
        --product_id testproduct
        --policy_id policy
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

**Example: ApiManagementCreateProperty**

```
apimgmt property create s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
        --secret true
        --display_name prop3name
        --value propValue
```

**Example: ApiManagementUpdateProperty**

```
apimgmt property create s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
        --secret true
```

**Example: ApiManagementDeleteProperty**

```
apimgmt property create s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
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

**Example: ApiManagementCreateProperty**

```
apimgmt property update s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
        --secret true
        --display_name prop3name
        --value propValue
```

**Example: ApiManagementUpdateProperty**

```
apimgmt property update s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
        --secret true
```

**Example: ApiManagementDeleteProperty**

```
apimgmt property update s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
```
### apimgmt property delete

delete a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--prop_id**|default|Identifier of the property.|prop_id|propId|

**Example: ApiManagementCreateProperty**

```
apimgmt property delete s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
```

**Example: ApiManagementUpdateProperty**

```
apimgmt property delete s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
```

**Example: ApiManagementDeleteProperty**

```
apimgmt property delete s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
```
### apimgmt property list

list a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateProperty**

```
apimgmt property list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateProperty**

```
apimgmt property list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteProperty**

```
apimgmt property list s--resource_group rg1
        --service_name apimService1
```
### apimgmt property show

show a apimgmt property.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--prop_id**|default|Identifier of the property.|prop_id|propId|

**Example: ApiManagementCreateProperty**

```
apimgmt property show s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
```

**Example: ApiManagementUpdateProperty**

```
apimgmt property show s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
```

**Example: ApiManagementDeleteProperty**

```
apimgmt property show s--resource_group rg1
        --service_name apimService1
        --prop_id testprop2
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

**Example: ApiManagementCreateSubscription**

```
apimgmt subscription create s--resource_group rg1
        --service_name apimService1
        --sid testsub
        --owner_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
        --scope "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }}"
        --display_name testsub
```

**Example: ApiManagementUpdateSubscription**

```
apimgmt subscription create s--resource_group rg1
        --service_name apimService1
        --sid testsub
        --display_name testsub
```

**Example: ApiManagementDeleteSubscription**

```
apimgmt subscription create s--resource_group rg1
        --service_name apimService1
        --sid testsub
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

**Example: ApiManagementCreateSubscription**

```
apimgmt subscription update s--resource_group rg1
        --service_name apimService1
        --sid testsub
        --owner_id "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{ user_name }}"
        --scope "/subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/products/{{ product_name }}"
        --display_name testsub
```

**Example: ApiManagementUpdateSubscription**

```
apimgmt subscription update s--resource_group rg1
        --service_name apimService1
        --sid testsub
        --display_name testsub
```

**Example: ApiManagementDeleteSubscription**

```
apimgmt subscription update s--resource_group rg1
        --service_name apimService1
        --sid testsub
```
### apimgmt subscription delete

delete a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--sid**|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|

**Example: ApiManagementCreateSubscription**

```
apimgmt subscription delete s--resource_group rg1
        --service_name apimService1
        --sid testsub
```

**Example: ApiManagementUpdateSubscription**

```
apimgmt subscription delete s--resource_group rg1
        --service_name apimService1
        --sid testsub
```

**Example: ApiManagementDeleteSubscription**

```
apimgmt subscription delete s--resource_group rg1
        --service_name apimService1
        --sid testsub
```
### apimgmt subscription list

list a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateSubscription**

```
apimgmt subscription list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateSubscription**

```
apimgmt subscription list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteSubscription**

```
apimgmt subscription list s--resource_group rg1
        --service_name apimService1
```
### apimgmt subscription show

show a apimgmt subscription.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--sid**|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|

**Example: ApiManagementCreateSubscription**

```
apimgmt subscription show s--resource_group rg1
        --service_name apimService1
        --sid testsub
```

**Example: ApiManagementUpdateSubscription**

```
apimgmt subscription show s--resource_group rg1
        --service_name apimService1
        --sid testsub
```

**Example: ApiManagementDeleteSubscription**

```
apimgmt subscription show s--resource_group rg1
        --service_name apimService1
        --sid testsub
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

**Example: ApiManagementCreateTag**

```
apimgmt tag create s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
        --display_name tag1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag create s--resource_group rg1
        --service_name apimService1
        --tag_id temptag
        --display_name "temp tag"
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag create s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
```
### apimgmt tag update

update a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|**--display_name**|str|Tag name.|/display_name|/properties/displayName|

**Example: ApiManagementCreateTag**

```
apimgmt tag update s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
        --display_name tag1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag update s--resource_group rg1
        --service_name apimService1
        --tag_id temptag
        --display_name "temp tag"
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag update s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
```
### apimgmt tag delete

delete a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

**Example: ApiManagementCreateTag**

```
apimgmt tag delete s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag delete s--resource_group rg1
        --service_name apimService1
        --tag_id temptag
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag delete s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
```
### apimgmt tag list

list a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementCreateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag list s--resource_group rg1
        --service_name apimService1
```
### apimgmt tag show

show a apimgmt tag.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--tag_id**|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|

**Example: ApiManagementCreateTag**

```
apimgmt tag show s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
```

**Example: ApiManagementUpdateTag**

```
apimgmt tag show s--resource_group rg1
        --service_name apimService1
        --tag_id temptag
```

**Example: ApiManagementDeleteTag**

```
apimgmt tag show s--resource_group rg1
        --service_name apimService1
        --tag_id tagId1
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

**Example: ApiManagementCreateEmailTemplate**

```
apimgmt template create s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
        --subject "Your request for $IssueName was successfully received."
```

**Example: ApiManagementUpdateEmailTemplate**

```
apimgmt template create s--resource_group rg1
        --service_name apimService1
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

**Example: ApiManagementDeleteEmailTemplate**

```
apimgmt template create s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
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

**Example: ApiManagementCreateEmailTemplate**

```
apimgmt template update s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
        --subject "Your request for $IssueName was successfully received."
```

**Example: ApiManagementUpdateEmailTemplate**

```
apimgmt template update s--resource_group rg1
        --service_name apimService1
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

**Example: ApiManagementDeleteEmailTemplate**

```
apimgmt template update s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
```
### apimgmt template delete

delete a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Email Template Name Identifier.|template_name|templateName|

**Example: ApiManagementCreateEmailTemplate**

```
apimgmt template delete s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
```

**Example: ApiManagementUpdateEmailTemplate**

```
apimgmt template delete s--resource_group rg1
        --service_name apimService1
        --name applicationApprovedNotificationMessage
```

**Example: ApiManagementDeleteEmailTemplate**

```
apimgmt template delete s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
```
### apimgmt template list

list a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateEmailTemplate**

```
apimgmt template list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateEmailTemplate**

```
apimgmt template list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteEmailTemplate**

```
apimgmt template list s--resource_group rg1
        --service_name apimService1
```
### apimgmt template show

show a apimgmt template.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--name**|default|Email Template Name Identifier.|template_name|templateName|

**Example: ApiManagementCreateEmailTemplate**

```
apimgmt template show s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
```

**Example: ApiManagementUpdateEmailTemplate**

```
apimgmt template show s--resource_group rg1
        --service_name apimService1
        --name applicationApprovedNotificationMessage
```

**Example: ApiManagementDeleteEmailTemplate**

```
apimgmt template show s--resource_group rg1
        --service_name apimService1
        --name newIssueNotificationMessage
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

**Example: ApiManagementCreateUser**

```
apimgmt user create s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
        --email foobar@outlook.com
        --first_name foo
        --last_name bar
        --confirmation signup
```

**Example: ApiManagementUpdateUser**

```
apimgmt user create s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
        --email foobar@outlook.com
        --first_name foo
        --last_name bar
```

**Example: ApiManagementDeleteUser**

```
apimgmt user create s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
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

**Example: ApiManagementCreateUser**

```
apimgmt user update s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
        --email foobar@outlook.com
        --first_name foo
        --last_name bar
        --confirmation signup
```

**Example: ApiManagementUpdateUser**

```
apimgmt user update s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
        --email foobar@outlook.com
        --first_name foo
        --last_name bar
```

**Example: ApiManagementDeleteUser**

```
apimgmt user update s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```
### apimgmt user delete

delete a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementCreateUser**

```
apimgmt user delete s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```

**Example: ApiManagementUpdateUser**

```
apimgmt user delete s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```

**Example: ApiManagementDeleteUser**

```
apimgmt user delete s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```
### apimgmt user list

list a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|

**Example: ApiManagementCreateUser**

```
apimgmt user list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementUpdateUser**

```
apimgmt user list s--resource_group rg1
        --service_name apimService1
```

**Example: ApiManagementDeleteUser**

```
apimgmt user list s--resource_group rg1
        --service_name apimService1
```
### apimgmt user show

show a apimgmt user.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource_group**|default|The name of the resource group.|resource_group_name|resourceGroupName|
|**--service_name**|default|The name of the API Management service.|service_name|serviceName|
|**--user_id**|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|

**Example: ApiManagementCreateUser**

```
apimgmt user show s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```

**Example: ApiManagementUpdateUser**

```
apimgmt user show s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```

**Example: ApiManagementDeleteUser**

```
apimgmt user show s--resource_group rg1
        --service_name apimService1
        --user_id 5931a75ae4bbd512288c680b
```