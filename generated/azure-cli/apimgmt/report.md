# Azure CLI Module Creation Report

## apimgmt api

### apimgmt api create

create a apimgmt api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/*|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/*|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/*|
|--type|NO|str|Type of API.|/*|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/*|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/*|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/*|
|--api_revision_description|NO|str|Description of the Api Revision.|/*|
|--api_version_description|NO|str|Description of the Api Version.|/*|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/*|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/*|
|--source_api_id|NO|str|API identifier of the source API.|/*|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/*|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/*|
|--path|NO|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/*|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/*|
|--api_version_set|NO|dict|Version set details|/*|
|--value|NO|str|Content value when Importing an API.|/*|
|--format|NO|str|Format of the Content in which the API is getting imported.|/*|
|--wsdl_selector|NO|dict|Criteria to limit import of WSDL to a subset of the document.|/*|
|--api_type|NO|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/*|
### apimgmt api update

update a apimgmt api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/*|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/*|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/*|
|--type|NO|str|Type of API.|/*|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/*|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/*|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/*|
|--api_revision_description|NO|str|Description of the Api Revision.|/*|
|--api_version_description|NO|str|Description of the Api Version.|/*|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/*|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/*|
|--source_api_id|NO|str|API identifier of the source API.|/*|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/*|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/*|
|--path|NO|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/*|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/*|
|--api_version_set|NO|dict|Version set details|/*|
|--value|NO|str|Content value when Importing an API.|/*|
|--format|NO|str|Format of the Content in which the API is getting imported.|/*|
|--wsdl_selector|NO|dict|Criteria to limit import of WSDL to a subset of the document.|/*|
|--api_type|NO|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/*|
### apimgmt api delete

delete a apimgmt api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
### apimgmt api list

list a apimgmt api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt api show

show a apimgmt api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
## apimgmt api release

### apimgmt api release create

create a apimgmt api release.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|*|
|--notes|NO|str|Release Notes|/*|
### apimgmt api release update

update a apimgmt api release.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|*|
|--notes|NO|str|Release Notes|/*|
### apimgmt api release delete

delete a apimgmt api release.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|*|
### apimgmt api release list

list a apimgmt api release.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api release show

show a apimgmt api release.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|*|
## apimgmt api operation

### apimgmt api operation create

create a apimgmt api operation.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
|--template_parameters|NO|list|Collection of URL template parameters.|/*|
|--description|NO|str|Description of the operation. May include HTML formatting tags.|/*|
|--request|NO|dict|An entity containing request details.|/*|
|--responses|NO|list|Array of Operation responses.|/*|
|--policies|NO|str|Operation Policies|/*|
|--display_name|NO|str|Operation Name.|/*|
|--method|NO|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/*|
|--url_template|NO|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/*|
### apimgmt api operation update

update a apimgmt api operation.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
|--template_parameters|NO|list|Collection of URL template parameters.|/*|
|--description|NO|str|Description of the operation. May include HTML formatting tags.|/*|
|--request|NO|dict|An entity containing request details.|/*|
|--responses|NO|list|Array of Operation responses.|/*|
|--policies|NO|str|Operation Policies|/*|
|--display_name|NO|str|Operation Name.|/*|
|--method|NO|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/*|
|--url_template|NO|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/*|
### apimgmt api operation delete

delete a apimgmt api operation.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
### apimgmt api operation list

list a apimgmt api operation.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
### apimgmt api operation show

show a apimgmt api operation.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
## apimgmt api operation policy

### apimgmt api operation policy create

create a apimgmt api operation policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt api operation policy update

update a apimgmt api operation policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt api operation policy delete

delete a apimgmt api operation policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
### apimgmt api operation policy list

list a apimgmt api operation policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
### apimgmt api operation policy show

show a apimgmt api operation policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--format|NO|default|Format of the policyContent.|/*|
## apimgmt tag

### apimgmt tag create

create a apimgmt tag.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
|--display_name|NO|str|Tag name.|/*|
### apimgmt tag update

update a apimgmt tag.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
|--display_name|NO|str|Tag name.|/*|
### apimgmt tag delete

delete a apimgmt tag.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
### apimgmt tag list

list a apimgmt tag.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt tag show

show a apimgmt tag.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
## apimgmt api policy

### apimgmt api policy create

create a apimgmt api policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt api policy update

update a apimgmt api policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt api policy delete

delete a apimgmt api policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
### apimgmt api policy list

list a apimgmt api policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
### apimgmt api policy show

show a apimgmt api policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--format|NO|default|Format of the policyContent.|/*|
## apimgmt api schema

### apimgmt api schema create

create a apimgmt api schema.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|*|
|--content_type|NO|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/*|
|--document|NO|dict|Create or update Properties of the Schema Document.|/*|
### apimgmt api schema update

update a apimgmt api schema.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|*|
|--content_type|NO|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/*|
|--document|NO|dict|Create or update Properties of the Schema Document.|/*|
### apimgmt api schema delete

delete a apimgmt api schema.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|*|
### apimgmt api schema list

list a apimgmt api schema.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
### apimgmt api schema show

show a apimgmt api schema.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|*|
## apimgmt api diagnostic

### apimgmt api diagnostic create

create a apimgmt api diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/*|
|--logger_id|NO|str|Resource Id of a target logger.|/*|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/*|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/*|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/*|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/*|
### apimgmt api diagnostic update

update a apimgmt api diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/*|
|--logger_id|NO|str|Resource Id of a target logger.|/*|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/*|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/*|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/*|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/*|
### apimgmt api diagnostic delete

delete a apimgmt api diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api diagnostic list

list a apimgmt api diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api diagnostic show

show a apimgmt api diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
## apimgmt api issue

### apimgmt api issue create

create a apimgmt api issue.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--created_date|NO|datetime|Date and time when the issue was created.|/*|
|--state|NO|str|Status of the issue.|/*|
|--title|NO|str|The issue title.|/*|
|--description|NO|str|Text describing the issue.|/*|
|--user_id|NO|str|A resource identifier for the user created the issue.|/*|
### apimgmt api issue update

update a apimgmt api issue.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--created_date|NO|datetime|Date and time when the issue was created.|/*|
|--state|NO|str|Status of the issue.|/*|
|--title|NO|str|The issue title.|/*|
|--description|NO|str|Text describing the issue.|/*|
|--user_id|NO|str|A resource identifier for the user created the issue.|/*|
### apimgmt api issue delete

delete a apimgmt api issue.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api issue list

list a apimgmt api issue.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api issue show

show a apimgmt api issue.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
## apimgmt api issue comment

### apimgmt api issue comment create

create a apimgmt api issue comment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|*|
|--text|NO|str|Comment text.|/*|
|--created_date|NO|datetime|Date and time when the comment was created.|/*|
|--user_id|NO|str|A resource identifier for the user who left the comment.|/*|
### apimgmt api issue comment update

update a apimgmt api issue comment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|*|
|--text|NO|str|Comment text.|/*|
|--created_date|NO|datetime|Date and time when the comment was created.|/*|
|--user_id|NO|str|A resource identifier for the user who left the comment.|/*|
### apimgmt api issue comment delete

delete a apimgmt api issue comment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|*|
### apimgmt api issue comment list

list a apimgmt api issue comment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api issue comment show

show a apimgmt api issue comment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|*|
## apimgmt api issue attachment

### apimgmt api issue attachment create

create a apimgmt api issue attachment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|*|
|--title|NO|str|Filename by which the binary data will be saved.|/*|
|--content_format|NO|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/*|
|--content|NO|str|An HTTP link or Base64-encoded binary data.|/*|
### apimgmt api issue attachment update

update a apimgmt api issue attachment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|*|
|--title|NO|str|Filename by which the binary data will be saved.|/*|
|--content_format|NO|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/*|
|--content|NO|str|An HTTP link or Base64-encoded binary data.|/*|
### apimgmt api issue attachment delete

delete a apimgmt api issue attachment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|*|
### apimgmt api issue attachment list

list a apimgmt api issue attachment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api issue attachment show

show a apimgmt api issue attachment.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|*|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|*|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|*|
## apimgmt api tagdescription

### apimgmt api tagdescription create

create a apimgmt api tagdescription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
|--description|NO|str|Description of the Tag.|/*|
|--external_docs_url|NO|str|Absolute URL of external resources describing the tag.|/*|
|--external_docs_description|NO|str|Description of the external resources describing the tag.|/*|
### apimgmt api tagdescription update

update a apimgmt api tagdescription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
|--description|NO|str|Description of the Tag.|/*|
|--external_docs_url|NO|str|Absolute URL of external resources describing the tag.|/*|
|--external_docs_description|NO|str|Description of the external resources describing the tag.|/*|
### apimgmt api tagdescription delete

delete a apimgmt api tagdescription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
### apimgmt api tagdescription list

list a apimgmt api tagdescription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
### apimgmt api tagdescription show

show a apimgmt api tagdescription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|*|
## apimgmt apiversionset

### apimgmt apiversionset create

create a apimgmt apiversionset.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|*|
|--description|NO|str|Description of API Version Set.|/*|
|--version_query_name|NO|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/*|
|--version_header_name|NO|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/*|
|--display_name|NO|str|Name of API Version Set|/*|
|--versioning_scheme|NO|str|An value that determines where the API Version identifer will be located in a HTTP request.|/*|
### apimgmt apiversionset update

update a apimgmt apiversionset.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|*|
|--description|NO|str|Description of API Version Set.|/*|
|--version_query_name|NO|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/*|
|--version_header_name|NO|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/*|
|--display_name|NO|str|Name of API Version Set|/*|
|--versioning_scheme|NO|str|An value that determines where the API Version identifer will be located in a HTTP request.|/*|
### apimgmt apiversionset delete

delete a apimgmt apiversionset.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|*|
### apimgmt apiversionset list

list a apimgmt apiversionset.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt apiversionset show

show a apimgmt apiversionset.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|*|
## apimgmt authorizationserver

### apimgmt authorizationserver create

create a apimgmt authorizationserver.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--authsid|YES|default|Identifier of the authorization server.|*|
|--description|NO|str|Description of the authorization server. Can contain HTML formatting tags.|/*|
|--authorization_methods|NO|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/*|
|--client_authentication_method|NO|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/*|
|--token_body_parameters|NO|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/*|
|--token_endpoint|NO|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/*|
|--support_state|NO|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/*|
|--default_scope|NO|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/*|
|--bearer_token_sending_methods|NO|list|Specifies the mechanism by which access token is passed to the API. |/*|
|--client_secret|NO|str|Client or app secret registered with this authorization server.|/*|
|--resource_owner_username|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/*|
|--resource_owner_password|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/*|
|--display_name|NO|str|User-friendly authorization server name.|/*|
|--client_registration_endpoint|NO|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/*|
|--authorization_endpoint|NO|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/*|
|--grant_types|NO|list|Form of an authorization grant, which the client uses to request the access token.|/*|
|--client_id|NO|str|Client or app id registered with this authorization server.|/*|
### apimgmt authorizationserver update

update a apimgmt authorizationserver.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--authsid|YES|default|Identifier of the authorization server.|*|
|--description|NO|str|Description of the authorization server. Can contain HTML formatting tags.|/*|
|--authorization_methods|NO|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/*|
|--client_authentication_method|NO|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/*|
|--token_body_parameters|NO|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/*|
|--token_endpoint|NO|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/*|
|--support_state|NO|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/*|
|--default_scope|NO|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/*|
|--bearer_token_sending_methods|NO|list|Specifies the mechanism by which access token is passed to the API. |/*|
|--client_secret|NO|str|Client or app secret registered with this authorization server.|/*|
|--resource_owner_username|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/*|
|--resource_owner_password|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/*|
|--display_name|NO|str|User-friendly authorization server name.|/*|
|--client_registration_endpoint|NO|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/*|
|--authorization_endpoint|NO|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/*|
|--grant_types|NO|list|Form of an authorization grant, which the client uses to request the access token.|/*|
|--client_id|NO|str|Client or app id registered with this authorization server.|/*|
### apimgmt authorizationserver delete

delete a apimgmt authorizationserver.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--authsid|YES|default|Identifier of the authorization server.|*|
### apimgmt authorizationserver list

list a apimgmt authorizationserver.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt authorizationserver show

show a apimgmt authorizationserver.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--authsid|YES|default|Identifier of the authorization server.|*|
## apimgmt backend

### apimgmt backend create

create a apimgmt backend.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|*|
|--title|NO|str|Backend Title.|/*|
|--description|NO|str|Backend Description.|/*|
|--resource_id|NO|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/*|
|--service_fabric_cluster|NO|dict|Backend Service Fabric Cluster Properties|/*|
|--credentials|NO|dict|Backend Credentials Contract Properties|/*|
|--proxy|NO|dict|Backend Proxy Contract Properties|/*|
|--tls|NO|dict|Backend TLS Properties|/*|
|--url|NO|str|Runtime Url of the Backend.|/*|
|--protocol|NO|str|Backend communication protocol.|/*|
### apimgmt backend update

update a apimgmt backend.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|*|
|--title|NO|str|Backend Title.|/*|
|--description|NO|str|Backend Description.|/*|
|--resource_id|NO|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/*|
|--service_fabric_cluster|NO|dict|Backend Service Fabric Cluster Properties|/*|
|--credentials|NO|dict|Backend Credentials Contract Properties|/*|
|--proxy|NO|dict|Backend Proxy Contract Properties|/*|
|--tls|NO|dict|Backend TLS Properties|/*|
|--url|NO|str|Runtime Url of the Backend.|/*|
|--protocol|NO|str|Backend communication protocol.|/*|
### apimgmt backend delete

delete a apimgmt backend.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|*|
### apimgmt backend list

list a apimgmt backend.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt backend show

show a apimgmt backend.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|*|
## apimgmt cache

### apimgmt cache create

create a apimgmt cache.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|*|
|--description|NO|str|Cache description|/*|
|--connection_string|NO|str|Runtime connection string to cache|/*|
|--resource_id|NO|str|Original uri of entity in external system cache points to|/*|
### apimgmt cache update

update a apimgmt cache.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|*|
|--description|NO|str|Cache description|/*|
|--connection_string|NO|str|Runtime connection string to cache|/*|
|--resource_id|NO|str|Original uri of entity in external system cache points to|/*|
### apimgmt cache delete

delete a apimgmt cache.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|*|
### apimgmt cache list

list a apimgmt cache.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt cache show

show a apimgmt cache.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|*|
## apimgmt certificate

### apimgmt certificate create

create a apimgmt certificate.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|*|
|--data|NO|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/*|
|--password|NO|str|Password for the Certificate|/*|
### apimgmt certificate update

update a apimgmt certificate.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|*|
|--data|NO|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/*|
|--password|NO|str|Password for the Certificate|/*|
### apimgmt certificate delete

delete a apimgmt certificate.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|*|
### apimgmt certificate list

list a apimgmt certificate.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt certificate show

show a apimgmt certificate.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|*|
## apimgmt

### apimgmt create

create a apimgmt.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--tags|NO|unknown[DictionaryType {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]|Resource tags.|/|
|--notification_sender_email|NO|str|Email address from which the notification will be sent.|/*|
|--hostname_configurations|NO|list|Custom hostname configuration of the API Management service.|/*|
|--virtual_network_configuration|NO|dict|Virtual network configuration of the API Management service.|/*|
|--additional_locations|NO|list|Additional datacenter locations of the API Management service.|/*|
|--custom_properties|NO|unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.|/*|
|--certificates|NO|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/*|
|--enable_client_certificate|NO|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/*|
|--virtual_network_type|NO|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/*|
|--publisher_email|NO|str|Publisher email.|/*|
|--publisher_name|NO|str|Publisher name.|/*|
|--sku_name|NO|str|Name of the Sku.|/sku/name|
|--sku_capacity|NO|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|
|--identity|NO|dict|Managed service identity of the Api Management service.|/|
|--location|NO|str|Resource location.|/|
### apimgmt update

update a apimgmt.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--tags|NO|unknown[DictionaryType {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]|Resource tags.|/|
|--notification_sender_email|NO|str|Email address from which the notification will be sent.|/*|
|--hostname_configurations|NO|list|Custom hostname configuration of the API Management service.|/*|
|--virtual_network_configuration|NO|dict|Virtual network configuration of the API Management service.|/*|
|--additional_locations|NO|list|Additional datacenter locations of the API Management service.|/*|
|--custom_properties|NO|unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.|/*|
|--certificates|NO|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/*|
|--enable_client_certificate|NO|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/*|
|--virtual_network_type|NO|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/*|
|--publisher_email|NO|str|Publisher email.|/*|
|--publisher_name|NO|str|Publisher name.|/*|
|--sku_name|NO|str|Name of the Sku.|/sku/name|
|--sku_capacity|NO|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|
|--identity|NO|dict|Managed service identity of the Api Management service.|/|
|--location|NO|str|Resource location.|/|
### apimgmt delete

delete a apimgmt.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
### apimgmt list

list a apimgmt.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
### apimgmt show

show a apimgmt.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
## apimgmt diagnostic

### apimgmt diagnostic create

create a apimgmt diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/*|
|--logger_id|NO|str|Resource Id of a target logger.|/*|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/*|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/*|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/*|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/*|
### apimgmt diagnostic update

update a apimgmt diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/*|
|--logger_id|NO|str|Resource Id of a target logger.|/*|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/*|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/*|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/*|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/*|
### apimgmt diagnostic delete

delete a apimgmt diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
### apimgmt diagnostic list

list a apimgmt diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt diagnostic show

show a apimgmt diagnostic.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|*|
## apimgmt template

### apimgmt template create

create a apimgmt template.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Email Template Name Identifier.|*|
|--subject|NO|str|Subject of the Template.|/*|
|--title|NO|str|Title of the Template.|/*|
|--description|NO|str|Description of the Email Template.|/*|
|--body|NO|str|Email Template Body. This should be a valid XDocument|/*|
### apimgmt template update

update a apimgmt template.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Email Template Name Identifier.|*|
|--subject|NO|str|Subject of the Template.|/*|
|--title|NO|str|Title of the Template.|/*|
|--description|NO|str|Description of the Email Template.|/*|
|--body|NO|str|Email Template Body. This should be a valid XDocument|/*|
### apimgmt template delete

delete a apimgmt template.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Email Template Name Identifier.|*|
### apimgmt template list

list a apimgmt template.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt template show

show a apimgmt template.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Email Template Name Identifier.|*|
## apimgmt group

### apimgmt group create

create a apimgmt group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
|--display_name|NO|str|Group name.|/*|
|--description|NO|str|Group description.|/*|
|--type|NO|str|Group type.|/*|
|--external_id|NO|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/*|
### apimgmt group update

update a apimgmt group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
|--display_name|NO|str|Group name.|/*|
|--description|NO|str|Group description.|/*|
|--type|NO|str|Group type.|/*|
|--external_id|NO|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/*|
### apimgmt group delete

delete a apimgmt group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
### apimgmt group list

list a apimgmt group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt group show

show a apimgmt group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
## apimgmt group user

### apimgmt group user create

create a apimgmt group user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
|--state|NO|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/*|
|--note|NO|str|Optional note about a user set by the administrator.|/*|
|--identities|NO|list|Collection of user identities.|/*|
|--first_name|NO|str|First name.|/*|
|--last_name|NO|str|Last name.|/*|
|--email|NO|str|Email address.|/*|
|--registration_date|NO|datetime|Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>|/*|
|--groups|NO|list|Collection of groups user is part of.|/*|
### apimgmt group user delete

delete a apimgmt group user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
### apimgmt group user list

list a apimgmt group user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
## apimgmt identityprovider

### apimgmt identityprovider create

create a apimgmt identityprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Identity Provider Type identifier.|*|
|--type|NO|str|Identity Provider Type identifier.|/*|
|--allowed_tenants|NO|list|List of Allowed Tenants when configuring Azure Active Directory login.|/*|
|--authority|NO|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/*|
|--signup_policy_name|NO|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--signin_policy_name|NO|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--profile_editing_policy_name|NO|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--password_reset_policy_name|NO|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--client_id|NO|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/*|
|--client_secret|NO|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/*|
### apimgmt identityprovider update

update a apimgmt identityprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Identity Provider Type identifier.|*|
|--type|NO|str|Identity Provider Type identifier.|/*|
|--allowed_tenants|NO|list|List of Allowed Tenants when configuring Azure Active Directory login.|/*|
|--authority|NO|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/*|
|--signup_policy_name|NO|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--signin_policy_name|NO|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--profile_editing_policy_name|NO|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--password_reset_policy_name|NO|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/*|
|--client_id|NO|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/*|
|--client_secret|NO|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/*|
### apimgmt identityprovider delete

delete a apimgmt identityprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Identity Provider Type identifier.|*|
### apimgmt identityprovider list

list a apimgmt identityprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt identityprovider show

show a apimgmt identityprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Identity Provider Type identifier.|*|
## apimgmt logger

### apimgmt logger create

create a apimgmt logger.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|*|
|--logger_type|NO|str|Logger type.|/*|
|--description|NO|str|Logger description.|/*|
|--credentials|NO|unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/*|
|--is_buffered|NO|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/*|
|--resource_id|NO|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/*|
### apimgmt logger update

update a apimgmt logger.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|*|
|--logger_type|NO|str|Logger type.|/*|
|--description|NO|str|Logger description.|/*|
|--credentials|NO|unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/*|
|--is_buffered|NO|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/*|
|--resource_id|NO|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/*|
### apimgmt logger delete

delete a apimgmt logger.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|*|
### apimgmt logger list

list a apimgmt logger.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt logger show

show a apimgmt logger.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|*|
## apimgmt notification

### apimgmt notification create

create a apimgmt notification.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Notification Name Identifier.|*|
|--title|NO|str|Title of the Notification.|/*|
|--description|NO|str|Description of the Notification.|/*|
|--recipients|NO|dict|Recipient Parameter values.|/*|
### apimgmt notification update

update a apimgmt notification.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Notification Name Identifier.|*|
|--title|NO|str|Title of the Notification.|/*|
|--description|NO|str|Description of the Notification.|/*|
|--recipients|NO|dict|Recipient Parameter values.|/*|
### apimgmt notification list

list a apimgmt notification.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt notification show

show a apimgmt notification.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--name|YES|default|Notification Name Identifier.|*|
## apimgmt notification recipientuser

### apimgmt notification recipientuser create

create a apimgmt notification recipientuser.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
### apimgmt notification recipientuser update

update a apimgmt notification recipientuser.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
### apimgmt notification recipientuser delete

delete a apimgmt notification recipientuser.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
### apimgmt notification recipientuser list

list a apimgmt notification recipientuser.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
## apimgmt notification recipientemail

### apimgmt notification recipientemail create

create a apimgmt notification recipientemail.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
|--email|YES|default|Email identifier.|*|
### apimgmt notification recipientemail update

update a apimgmt notification recipientemail.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
|--email|YES|default|Email identifier.|*|
### apimgmt notification recipientemail delete

delete a apimgmt notification recipientemail.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
|--email|YES|default|Email identifier.|*|
### apimgmt notification recipientemail list

list a apimgmt notification recipientemail.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--notification_name|YES|default|Notification Name Identifier.|*|
## apimgmt openidconnectprovider

### apimgmt openidconnectprovider create

create a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|*|
|--display_name|NO|str|User-friendly OpenID Connect Provider name.|/*|
|--description|NO|str|User-friendly description of OpenID Connect Provider.|/*|
|--metadata_endpoint|NO|str|Metadata endpoint URI.|/*|
|--client_id|NO|str|Client ID of developer console which is the client application.|/*|
|--client_secret|NO|str|Client Secret of developer console which is the client application.|/*|
### apimgmt openidconnectprovider update

update a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|*|
|--display_name|NO|str|User-friendly OpenID Connect Provider name.|/*|
|--description|NO|str|User-friendly description of OpenID Connect Provider.|/*|
|--metadata_endpoint|NO|str|Metadata endpoint URI.|/*|
|--client_id|NO|str|Client ID of developer console which is the client application.|/*|
|--client_secret|NO|str|Client Secret of developer console which is the client application.|/*|
### apimgmt openidconnectprovider delete

delete a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|*|
### apimgmt openidconnectprovider list

list a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt openidconnectprovider show

show a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|*|
## apimgmt policy

### apimgmt policy create

create a apimgmt policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt policy update

update a apimgmt policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt policy delete

delete a apimgmt policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
### apimgmt policy list

list a apimgmt policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt policy show

show a apimgmt policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--format|NO|default|Format of the policyContent.|/*|
## apimgmt portalsetting

### apimgmt portalsetting create

create a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--enabled|NO|boolean|Redirect Anonymous users to the Sign-In page.|/*|
### apimgmt portalsetting update

update a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--enabled|NO|boolean|Redirect Anonymous users to the Sign-In page.|/*|
### apimgmt portalsetting show

show a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
## apimgmt portalsetting

### apimgmt portalsetting create

create a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--enabled|NO|boolean|Allow users to sign up on a developer portal.|/*|
|--terms_of_service|NO|dict|Terms of service contract properties.|/*|
### apimgmt portalsetting update

update a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--enabled|NO|boolean|Allow users to sign up on a developer portal.|/*|
|--terms_of_service|NO|dict|Terms of service contract properties.|/*|
### apimgmt portalsetting show

show a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
## apimgmt portalsetting

### apimgmt portalsetting create

create a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--url|NO|str|A delegation Url.|/*|
|--validation_key|NO|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/*|
|--subscriptions|NO|dict|Subscriptions delegation settings.|/*|
|--user_registration|NO|dict|User registration delegation settings.|/*|
### apimgmt portalsetting update

update a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
|--url|NO|str|A delegation Url.|/*|
|--validation_key|NO|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/*|
|--subscriptions|NO|dict|Subscriptions delegation settings.|/*|
|--user_registration|NO|dict|User registration delegation settings.|/*|
### apimgmt portalsetting show

show a apimgmt portalsetting.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--name|YES|default|The name of the API Management service.|*|
## apimgmt product

### apimgmt product create

create a apimgmt product.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--description|NO|str|Product description. May include HTML formatting tags.|/*|
|--terms|NO|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/*|
|--subscription_required|NO|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/*|
|--approval_required|NO|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/*|
|--subscriptions_limit|NO|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/*|
|--state|NO|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/*|
|--display_name|NO|str|Product name.|/*|
### apimgmt product update

update a apimgmt product.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--description|NO|str|Product description. May include HTML formatting tags.|/*|
|--terms|NO|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/*|
|--subscription_required|NO|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/*|
|--approval_required|NO|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/*|
|--subscriptions_limit|NO|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/*|
|--state|NO|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/*|
|--display_name|NO|str|Product name.|/*|
### apimgmt product delete

delete a apimgmt product.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
### apimgmt product list

list a apimgmt product.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt product show

show a apimgmt product.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
## apimgmt product api

### apimgmt product api create

create a apimgmt product api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/*|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/*|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/*|
|--type|NO|str|Type of API.|/*|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/*|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/*|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/*|
|--is_online|NO|boolean|Indicates if API revision is accessible via the gateway.|/*|
|--api_revision_description|NO|str|Description of the Api Revision.|/*|
|--api_version_description|NO|str|Description of the Api Version.|/*|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/*|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/*|
|--source_api_id|NO|str|API identifier of the source API.|/*|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/*|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/*|
|--path|NO|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/*|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/*|
|--api_version_set|NO|dict|Version set details|/*|
### apimgmt product api update

update a apimgmt product api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/*|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/*|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/*|
|--type|NO|str|Type of API.|/*|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/*|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/*|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/*|
|--is_online|NO|boolean|Indicates if API revision is accessible via the gateway.|/*|
|--api_revision_description|NO|str|Description of the Api Revision.|/*|
|--api_version_description|NO|str|Description of the Api Version.|/*|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/*|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/*|
|--source_api_id|NO|str|API identifier of the source API.|/*|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/*|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/*|
|--path|NO|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/*|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/*|
|--api_version_set|NO|dict|Version set details|/*|
### apimgmt product api delete

delete a apimgmt product api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|*|
### apimgmt product api list

list a apimgmt product api.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
## apimgmt product group

### apimgmt product group create

create a apimgmt product group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
|--display_name|NO|str|Group name.|/*|
|--description|NO|str|Group description. Can contain HTML formatting tags.|/*|
|--built_in|NO|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/*|
|--type|NO|str|Group type.|/*|
|--external_id|NO|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/*|
### apimgmt product group update

update a apimgmt product group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
|--display_name|NO|str|Group name.|/*|
|--description|NO|str|Group description. Can contain HTML formatting tags.|/*|
|--built_in|NO|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/*|
|--type|NO|str|Group type.|/*|
|--external_id|NO|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/*|
### apimgmt product group delete

delete a apimgmt product group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|*|
### apimgmt product group list

list a apimgmt product group.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
## apimgmt product policy

### apimgmt product policy create

create a apimgmt product policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt product policy update

update a apimgmt product policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--value|NO|str|Contents of the Policy as defined by the format.|/*|
|--format|NO|str|Format of the policyContent.|/*|
### apimgmt product policy delete

delete a apimgmt product policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
### apimgmt product policy list

list a apimgmt product policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
### apimgmt product policy show

show a apimgmt product policy.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|*|
|--policy_id|YES|default|The identifier of the Policy.|*|
|--format|NO|default|Format of the policyContent.|/*|
## apimgmt property

### apimgmt property create

create a apimgmt property.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--prop_id|YES|default|Identifier of the property.|*|
|--tags|NO|list|Optional tags that when provided can be used to filter the property list.|/*|
|--secret|NO|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/*|
|--display_name|NO|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/*|
|--value|NO|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/*|
### apimgmt property update

update a apimgmt property.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--prop_id|YES|default|Identifier of the property.|*|
|--tags|NO|list|Optional tags that when provided can be used to filter the property list.|/*|
|--secret|NO|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/*|
|--display_name|NO|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/*|
|--value|NO|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/*|
### apimgmt property delete

delete a apimgmt property.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--prop_id|YES|default|Identifier of the property.|*|
### apimgmt property list

list a apimgmt property.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt property show

show a apimgmt property.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--prop_id|YES|default|Identifier of the property.|*|
## apimgmt subscription

### apimgmt subscription create

create a apimgmt subscription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|*|
|--notify|NO|default|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |*|
|--owner_id|NO|str|User (user id path) for whom subscription is being created in form /users/{userId}|/*|
|--scope|NO|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/*|
|--display_name|NO|str|Subscription name.|/*|
|--primary_key|NO|str|Primary subscription key. If not specified during request key will be generated automatically.|/*|
|--secondary_key|NO|str|Secondary subscription key. If not specified during request key will be generated automatically.|/*|
|--state|NO|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/*|
|--allow_tracing|NO|boolean|Determines whether tracing can be enabled|/*|
### apimgmt subscription update

update a apimgmt subscription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|*|
|--notify|NO|default|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |*|
|--owner_id|NO|str|User (user id path) for whom subscription is being created in form /users/{userId}|/*|
|--scope|NO|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/*|
|--display_name|NO|str|Subscription name.|/*|
|--primary_key|NO|str|Primary subscription key. If not specified during request key will be generated automatically.|/*|
|--secondary_key|NO|str|Secondary subscription key. If not specified during request key will be generated automatically.|/*|
|--state|NO|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/*|
|--allow_tracing|NO|boolean|Determines whether tracing can be enabled|/*|
### apimgmt subscription delete

delete a apimgmt subscription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|*|
### apimgmt subscription list

list a apimgmt subscription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt subscription show

show a apimgmt subscription.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|*|
## apimgmt user

### apimgmt user create

create a apimgmt user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
|--state|NO|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/*|
|--note|NO|str|Optional note about a user set by the administrator.|/*|
|--identities|NO|list|Collection of user identities.|/*|
|--email|NO|str|Email address. Must not be empty and must be unique within the service instance.|/*|
|--first_name|NO|str|First name.|/*|
|--last_name|NO|str|Last name.|/*|
|--password|NO|str|User Password. If no value is provided, a default password is generated.|/*|
|--confirmation|NO|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/*|
### apimgmt user update

update a apimgmt user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
|--state|NO|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/*|
|--note|NO|str|Optional note about a user set by the administrator.|/*|
|--identities|NO|list|Collection of user identities.|/*|
|--email|NO|str|Email address. Must not be empty and must be unique within the service instance.|/*|
|--first_name|NO|str|First name.|/*|
|--last_name|NO|str|Last name.|/*|
|--password|NO|str|User Password. If no value is provided, a default password is generated.|/*|
|--confirmation|NO|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/*|
### apimgmt user delete

delete a apimgmt user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|
### apimgmt user list

list a apimgmt user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
### apimgmt user show

show a apimgmt user.

|Option|Required|Type|Description|Target Path|
|------|--------|----|-----------|-----------|
|--resource_group|YES|default|The name of the resource group.|*|
|--service_name|YES|default|The name of the API Management service.|*|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|*|