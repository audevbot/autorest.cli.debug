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
|**--access-policies**|list|The access policies of the service instance.|/access_policies|/properties/accessPolicies|
|--tags|dictionary|The resource tags.|/tags|/tags|
|--etag|str|An etag associated with the resource, used for optimistic concurrency when editing it.|/etag|/etag|
|--cosmos-db-configuration|dict|The settings for the Cosmos DB database backing the service.|/cosmos_db_configuration|/properties/cosmosDbConfiguration|
|--authentication-configuration|dict|The authentication configuration for the service instance.|/authentication_configuration|/properties/authenticationConfiguration|
|--cors-configuration|dict|The settings for the CORS configuration of the service instance.|/cors_configuration|/properties/corsConfiguration|

**Example: ServicePut**

```
healthcareapis create --resource-group rg1
        --name service1
        --kind fhir
        --location westus
```
### healthcareapis update

update a healthcareapis.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group that contains the service instance.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the service instance.|resource_name|resourceName|
|**--kind**|str|The kind of the service. Valid values are: fhir, fhir-Stu3 and fhir-R4.|/kind|/kind|
|**--location**|str|The resource location.|/location|/location|
|**--access-policies**|list|The access policies of the service instance.|/access_policies|/properties/accessPolicies|
|--tags|dictionary|The resource tags.|/tags|/tags|
|--etag|str|An etag associated with the resource, used for optimistic concurrency when editing it.|/etag|/etag|
|--cosmos-db-configuration|dict|The settings for the Cosmos DB database backing the service.|/cosmos_db_configuration|/properties/cosmosDbConfiguration|
|--authentication-configuration|dict|The authentication configuration for the service instance.|/authentication_configuration|/properties/authenticationConfiguration|
|--cors-configuration|dict|The settings for the CORS configuration of the service instance.|/cors_configuration|/properties/corsConfiguration|

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