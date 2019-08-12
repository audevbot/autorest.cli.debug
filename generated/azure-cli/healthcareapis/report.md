# Azure CLI Module Creation Report

## healthcareapis

### healthcareapis create

create a healthcareapis.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group that contains the service instance.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the service instance.|resource_name|resourceName|
|**--kind**|str|The kind of the service. Valid values are: fhir, fhir-Stu3 and fhir-R4.|/kind|/kind|
|**--location**|str|The resource location.|/location|/location|
|**--access-policies-object-id**|str|An object ID that is allowed access to the FHIR service.|/access_policies/object_id|/properties/accessPolicies/objectId|
|--tags|dictionary|The resource tags.|/tags|/tags|
|--etag|str|An etag associated with the resource, used for optimistic concurrency when editing it.|/etag|/etag|
|--cosmos-db-offer-throughput|number|The provisioned throughput for the backing database.|/cosmos_db_configuration/offer_throughput|/properties/cosmosDbConfiguration/offerThroughput|
|--authentication-authority|str|The authority url for the service|/authentication_configuration/authority|/properties/authenticationConfiguration/authority|
|--authentication-audience|str|The audience url for the service|/authentication_configuration/audience|/properties/authenticationConfiguration/audience|
|--authentication-smart-proxy-enabled|boolean|If the SMART on FHIR proxy is enabled|/authentication_configuration/smart_proxy_enabled|/properties/authenticationConfiguration/smartProxyEnabled|
|--cors-origins|list|The origins to be allowed via CORS.|/cors_configuration/origins|/properties/corsConfiguration/origins|
|--cors-headers|list|The headers to be allowed via CORS.|/cors_configuration/headers|/properties/corsConfiguration/headers|
|--cors-methods|list|The methods to be allowed via CORS.|/cors_configuration/methods|/properties/corsConfiguration/methods|
|--cors-max-age|number|The max age to be allowed via CORS.|/cors_configuration/max_age|/properties/corsConfiguration/maxAge|
|--cors-allow-credentials|boolean|If credentials are allowed via CORS.|/cors_configuration/allow_credentials|/properties/corsConfiguration/allowCredentials|

**Example: ServicePut**

```
healthcareapis create --resource-group rg1
        --name service1
        --kind fhir
        --location westus
        --cosmos-db-offer-throughput 1000
        --authentication-authority https://login.microsoftonline.com/common
        --authentication-audience https://azurehealthcareapis.com
        --authentication-smart-proxy-enabled true
        --cors-max-age 1440
        --cors-allow-credentials false
```
### healthcareapis update

update a healthcareapis.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group that contains the service instance.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the service instance.|resource_name|resourceName|
|**--kind**|str|The kind of the service. Valid values are: fhir, fhir-Stu3 and fhir-R4.|/kind|/kind|
|**--location**|str|The resource location.|/location|/location|
|**--access-policies-object-id**|str|An object ID that is allowed access to the FHIR service.|/access_policies/object_id|/properties/accessPolicies/objectId|
|--tags|dictionary|The resource tags.|/tags|/tags|
|--etag|str|An etag associated with the resource, used for optimistic concurrency when editing it.|/etag|/etag|
|--cosmos-db-offer-throughput|number|The provisioned throughput for the backing database.|/cosmos_db_configuration/offer_throughput|/properties/cosmosDbConfiguration/offerThroughput|
|--authentication-authority|str|The authority url for the service|/authentication_configuration/authority|/properties/authenticationConfiguration/authority|
|--authentication-audience|str|The audience url for the service|/authentication_configuration/audience|/properties/authenticationConfiguration/audience|
|--authentication-smart-proxy-enabled|boolean|If the SMART on FHIR proxy is enabled|/authentication_configuration/smart_proxy_enabled|/properties/authenticationConfiguration/smartProxyEnabled|
|--cors-origins|list|The origins to be allowed via CORS.|/cors_configuration/origins|/properties/corsConfiguration/origins|
|--cors-headers|list|The headers to be allowed via CORS.|/cors_configuration/headers|/properties/corsConfiguration/headers|
|--cors-methods|list|The methods to be allowed via CORS.|/cors_configuration/methods|/properties/corsConfiguration/methods|
|--cors-max-age|number|The max age to be allowed via CORS.|/cors_configuration/max_age|/properties/corsConfiguration/maxAge|
|--cors-allow-credentials|boolean|If credentials are allowed via CORS.|/cors_configuration/allow_credentials|/properties/corsConfiguration/allowCredentials|

**Example: ServicePatch**

```
healthcareapis update --resource-group rg1
        --name service1
```
### healthcareapis delete

delete a healthcareapis.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group that contains the service instance.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the service instance.|resource_name|resourceName|

**Example: ServiceDelete**

```
healthcareapis delete --resource-group rg1
        --name service1
```
### healthcareapis list

list a healthcareapis.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group that contains the service instance.|resource_group_name|resourceGroupName|
### healthcareapis show

show a healthcareapis.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group that contains the service instance.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the service instance.|resource_name|resourceName|