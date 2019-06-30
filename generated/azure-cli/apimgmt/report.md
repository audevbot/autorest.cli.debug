# Azure CLI Module Creation Report

## apimgmt

### apimgmt create

create a apimgmt.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
|--publisher_email|YES|str|Publisher email.|/publisher_email|/properties/publisherEmail|
|--publisher_name|YES|str|Publisher name.|/publisher_name|/properties/publisherName|
|--sku_name|YES|str|Name of the Sku.|/sku/name|/sku/name|
|--location|YES|str|Resource location.|/location|/location|
|--tags|NO|unknown[DictionaryType {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]|Resource tags.|/tags|/tags|
|--notification_sender_email|NO|str|Email address from which the notification will be sent.|/notification_sender_email|/properties/notificationSenderEmail|
|--hostname_configurations|NO|list|Custom hostname configuration of the API Management service.|/hostname_configurations|/properties/hostnameConfigurations|
|--virtual_network_configuration|NO|dict|Virtual network configuration of the API Management service.|/virtual_network_configuration|/properties/virtualNetworkConfiguration|
|--additional_locations|NO|list|Additional datacenter locations of the API Management service.|/additional_locations|/properties/additionalLocations|
|--custom_properties|NO|unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.|/custom_properties|/properties/customProperties|
|--certificates|NO|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/certificates|/properties/certificates|
|--enable_client_certificate|NO|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/enable_client_certificate|/properties/enableClientCertificate|
|--virtual_network_type|NO|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/virtual_network_type|/properties/virtualNetworkType|
|--sku_capacity|NO|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|/sku/capacity|
|--identity|NO|dict|Managed service identity of the Api Management service.|/identity|/identity|
### apimgmt update

update a apimgmt.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
|--publisher_email|YES|str|Publisher email.|/publisher_email|/properties/publisherEmail|
|--publisher_name|YES|str|Publisher name.|/publisher_name|/properties/publisherName|
|--sku_name|YES|str|Name of the Sku.|/sku/name|/sku/name|
|--location|YES|str|Resource location.|/location|/location|
|--tags|NO|unknown[DictionaryType {"$id":"2630","$type":"DictionaryType","valueType":{"$id":"2631","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2632","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2633","fixed":false},"deprecated":false}]|Resource tags.|/tags|/tags|
|--notification_sender_email|NO|str|Email address from which the notification will be sent.|/notification_sender_email|/properties/notificationSenderEmail|
|--hostname_configurations|NO|list|Custom hostname configuration of the API Management service.|/hostname_configurations|/properties/hostnameConfigurations|
|--virtual_network_configuration|NO|dict|Virtual network configuration of the API Management service.|/virtual_network_configuration|/properties/virtualNetworkConfiguration|
|--additional_locations|NO|list|Additional datacenter locations of the API Management service.|/additional_locations|/properties/additionalLocations|
|--custom_properties|NO|unknown[DictionaryType {"$id":"2519","$type":"DictionaryType","valueType":{"$id":"2520","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"2521","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"2522","fixed":false},"deprecated":false}]|Custom properties of the API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168` will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0, 1.1 and 1.2).</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11` can be used to disable just TLS 1.1.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10` can be used to disable TLS 1.0 on an API Management service.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11` can be used to disable just TLS 1.1 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10` can be used to disable TLS 1.0 for communications with backends.</br>Setting `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2` can be used to enable HTTP2 protocol on an API Management service.</br>Not specifying any of these properties on PATCH operation will reset omitted properties' values to their defaults. For all the settings except Http2 the default value is `True` if the service was created on or before April 1st 2018 and `False` otherwise. Http2 setting's default value is `False`.|/custom_properties|/properties/customProperties|
|--certificates|NO|list|List of Certificates that need to be installed in the API Management service. Max supported certificates that can be installed is 10.|/certificates|/properties/certificates|
|--enable_client_certificate|NO|boolean|Property only meant to be used for Consumption SKU Service. This enforces a client certificate to be presented on each request to the gateway. This also enables the ability to authenticate the certificate in the policy on the gateway.|/enable_client_certificate|/properties/enableClientCertificate|
|--virtual_network_type|NO|str|The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that API Management deployment is setup inside a Virtual Network having an Intranet Facing Endpoint only.|/virtual_network_type|/properties/virtualNetworkType|
|--sku_capacity|NO|number|Capacity of the SKU (number of deployed units of the SKU).|/sku/capacity|/sku/capacity|
|--identity|NO|dict|Managed service identity of the Api Management service.|/identity|/identity|
### apimgmt delete

delete a apimgmt.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt list

list a apimgmt.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
### apimgmt show

show a apimgmt.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
## apimgmt api

### apimgmt api create

create a apimgmt api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--path|YES|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|NO|str|Type of API.|/type|/properties/type|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--api_revision_description|NO|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|NO|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|NO|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|NO|dict|Version set details|/api_version_set|/properties/apiVersionSet|
|--value|NO|str|Content value when Importing an API.|/value|/properties/value|
|--format|NO|str|Format of the Content in which the API is getting imported.|/format|/properties/format|
|--wsdl_selector|NO|dict|Criteria to limit import of WSDL to a subset of the document.|/wsdl_selector|/properties/wsdlSelector|
|--api_type|NO|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/api_type|/properties/apiType|
### apimgmt api update

update a apimgmt api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--path|YES|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|NO|str|Type of API.|/type|/properties/type|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--api_revision_description|NO|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|NO|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|NO|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|NO|dict|Version set details|/api_version_set|/properties/apiVersionSet|
|--value|NO|str|Content value when Importing an API.|/value|/properties/value|
|--format|NO|str|Format of the Content in which the API is getting imported.|/format|/properties/format|
|--wsdl_selector|NO|dict|Criteria to limit import of WSDL to a subset of the document.|/wsdl_selector|/properties/wsdlSelector|
|--api_type|NO|str|Type of Api to create. <br> * `http` creates a SOAP to REST API <br> * `soap` creates a SOAP pass-through API .|/api_type|/properties/apiType|
### apimgmt api delete

delete a apimgmt api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apimgmt api list

list a apimgmt api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt api show

show a apimgmt api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
## apimgmt api diagnostic

### apimgmt api diagnostic create

create a apimgmt api diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|--logger_id|YES|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|
### apimgmt api diagnostic update

update a apimgmt api diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|--logger_id|YES|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|
### apimgmt api diagnostic delete

delete a apimgmt api diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
### apimgmt api diagnostic list

list a apimgmt api diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
### apimgmt api diagnostic show

show a apimgmt api diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
## apimgmt api issue

### apimgmt api issue create

create a apimgmt api issue.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--title|YES|str|The issue title.|/title|/properties/title|
|--description|YES|str|Text describing the issue.|/description|/properties/description|
|--user_id|YES|str|A resource identifier for the user created the issue.|/user_id|/properties/userId|
|--created_date|NO|datetime|Date and time when the issue was created.|/created_date|/properties/createdDate|
|--state|NO|str|Status of the issue.|/state|/properties/state|
### apimgmt api issue update

update a apimgmt api issue.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--title|YES|str|The issue title.|/title|/properties/title|
|--description|YES|str|Text describing the issue.|/description|/properties/description|
|--user_id|YES|str|A resource identifier for the user created the issue.|/user_id|/properties/userId|
|--created_date|NO|datetime|Date and time when the issue was created.|/created_date|/properties/createdDate|
|--state|NO|str|Status of the issue.|/state|/properties/state|
### apimgmt api issue delete

delete a apimgmt api issue.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
### apimgmt api issue list

list a apimgmt api issue.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
### apimgmt api issue show

show a apimgmt api issue.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
## apimgmt api issue attachment

### apimgmt api issue attachment create

create a apimgmt api issue attachment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
|--title|YES|str|Filename by which the binary data will be saved.|/title|/properties/title|
|--content_format|YES|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/content_format|/properties/contentFormat|
|--content|YES|str|An HTTP link or Base64-encoded binary data.|/content|/properties/content|
### apimgmt api issue attachment update

update a apimgmt api issue attachment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
|--title|YES|str|Filename by which the binary data will be saved.|/title|/properties/title|
|--content_format|YES|str|Either 'link' if content is provided via an HTTP link or the MIME type of the Base64-encoded binary data provided in the 'content' property.|/content_format|/properties/contentFormat|
|--content|YES|str|An HTTP link or Base64-encoded binary data.|/content|/properties/content|
### apimgmt api issue attachment delete

delete a apimgmt api issue attachment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
### apimgmt api issue attachment list

list a apimgmt api issue attachment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
### apimgmt api issue attachment show

show a apimgmt api issue attachment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--attachment_id|YES|default|Attachment identifier within an Issue. Must be unique in the current Issue.|attachment_id|attachmentId|
## apimgmt api issue comment

### apimgmt api issue comment create

create a apimgmt api issue comment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
|--text|YES|str|Comment text.|/text|/properties/text|
|--user_id|YES|str|A resource identifier for the user who left the comment.|/user_id|/properties/userId|
|--created_date|NO|datetime|Date and time when the comment was created.|/created_date|/properties/createdDate|
### apimgmt api issue comment update

update a apimgmt api issue comment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
|--text|YES|str|Comment text.|/text|/properties/text|
|--user_id|YES|str|A resource identifier for the user who left the comment.|/user_id|/properties/userId|
|--created_date|NO|datetime|Date and time when the comment was created.|/created_date|/properties/createdDate|
### apimgmt api issue comment delete

delete a apimgmt api issue comment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
### apimgmt api issue comment list

list a apimgmt api issue comment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
### apimgmt api issue comment show

show a apimgmt api issue comment.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--issue_id|YES|default|Issue identifier. Must be unique in the current API Management service instance.|issue_id|issueId|
|--comment_id|YES|default|Comment identifier within an Issue. Must be unique in the current Issue.|comment_id|commentId|
## apimgmt api operation

### apimgmt api operation create

create a apimgmt api operation.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|--display_name|YES|str|Operation Name.|/display_name|/properties/displayName|
|--method|YES|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/method|/properties/method|
|--url_template|YES|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/url_template|/properties/urlTemplate|
|--template_parameters|NO|list|Collection of URL template parameters.|/template_parameters|/properties/templateParameters|
|--description|NO|str|Description of the operation. May include HTML formatting tags.|/description|/properties/description|
|--request|NO|dict|An entity containing request details.|/request|/properties/request|
|--responses|NO|list|Array of Operation responses.|/responses|/properties/responses|
|--policies|NO|str|Operation Policies|/policies|/properties/policies|
### apimgmt api operation update

update a apimgmt api operation.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|--display_name|YES|str|Operation Name.|/display_name|/properties/displayName|
|--method|YES|str|A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.|/method|/properties/method|
|--url_template|YES|str|Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date={date}|/url_template|/properties/urlTemplate|
|--template_parameters|NO|list|Collection of URL template parameters.|/template_parameters|/properties/templateParameters|
|--description|NO|str|Description of the operation. May include HTML formatting tags.|/description|/properties/description|
|--request|NO|dict|An entity containing request details.|/request|/properties/request|
|--responses|NO|list|Array of Operation responses.|/responses|/properties/responses|
|--policies|NO|str|Operation Policies|/policies|/properties/policies|
### apimgmt api operation delete

delete a apimgmt api operation.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
### apimgmt api operation list

list a apimgmt api operation.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apimgmt api operation show

show a apimgmt api operation.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
## apimgmt api operation policy

### apimgmt api operation policy create

create a apimgmt api operation policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt api operation policy update

update a apimgmt api operation policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt api operation policy delete

delete a apimgmt api operation policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
### apimgmt api operation policy list

list a apimgmt api operation policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
### apimgmt api operation policy show

show a apimgmt api operation policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--operation_id|YES|default|Operation identifier within an API. Must be unique in the current API Management service instance.|operation_id|operationId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--format|NO|default|Format of the policyContent.|/format|/properties/format|
## apimgmt api policy

### apimgmt api policy create

create a apimgmt api policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt api policy update

update a apimgmt api policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt api policy delete

delete a apimgmt api policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
### apimgmt api policy list

list a apimgmt api policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apimgmt api policy show

show a apimgmt api policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--format|NO|default|Format of the policyContent.|/format|/properties/format|
## apimgmt api release

### apimgmt api release create

create a apimgmt api release.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
|--notes|NO|str|Release Notes|/notes|/properties/notes|
### apimgmt api release update

update a apimgmt api release.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
|--notes|NO|str|Release Notes|/notes|/properties/notes|
### apimgmt api release delete

delete a apimgmt api release.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
### apimgmt api release list

list a apimgmt api release.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
### apimgmt api release show

show a apimgmt api release.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API identifier. Must be unique in the current API Management service instance.|api_id|apiId|
|--release_id|YES|default|Release identifier within an API. Must be unique in the current API Management service instance.|release_id|releaseId|
## apimgmt api schema

### apimgmt api schema create

create a apimgmt api schema.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
|--content_type|YES|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/content_type|/properties/contentType|
|--document|NO|dict|Create or update Properties of the Schema Document.|/document|/properties/document|
### apimgmt api schema update

update a apimgmt api schema.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
|--content_type|YES|str|Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`.|/content_type|/properties/contentType|
|--document|NO|dict|Create or update Properties of the Schema Document.|/document|/properties/document|
### apimgmt api schema delete

delete a apimgmt api schema.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
### apimgmt api schema list

list a apimgmt api schema.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apimgmt api schema show

show a apimgmt api schema.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--schema_id|YES|default|Schema identifier within an API. Must be unique in the current API Management service instance.|schema_id|schemaId|
## apimgmt api tagdescription

### apimgmt api tagdescription create

create a apimgmt api tagdescription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--description|NO|str|Description of the Tag.|/description|/properties/description|
|--external_docs_url|NO|str|Absolute URL of external resources describing the tag.|/external_docs_url|/properties/externalDocsUrl|
|--external_docs_description|NO|str|Description of the external resources describing the tag.|/external_docs_description|/properties/externalDocsDescription|
### apimgmt api tagdescription update

update a apimgmt api tagdescription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--description|NO|str|Description of the Tag.|/description|/properties/description|
|--external_docs_url|NO|str|Absolute URL of external resources describing the tag.|/external_docs_url|/properties/externalDocsUrl|
|--external_docs_description|NO|str|Description of the external resources describing the tag.|/external_docs_description|/properties/externalDocsDescription|
### apimgmt api tagdescription delete

delete a apimgmt api tagdescription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
### apimgmt api tagdescription list

list a apimgmt api tagdescription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apimgmt api tagdescription show

show a apimgmt api tagdescription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
## apimgmt apiversionset

### apimgmt apiversionset create

create a apimgmt apiversionset.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
|--display_name|YES|str|Name of API Version Set|/display_name|/properties/displayName|
|--versioning_scheme|YES|str|An value that determines where the API Version identifer will be located in a HTTP request.|/versioning_scheme|/properties/versioningScheme|
|--description|NO|str|Description of API Version Set.|/description|/properties/description|
|--version_query_name|NO|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/version_query_name|/properties/versionQueryName|
|--version_header_name|NO|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/version_header_name|/properties/versionHeaderName|
### apimgmt apiversionset update

update a apimgmt apiversionset.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
|--display_name|YES|str|Name of API Version Set|/display_name|/properties/displayName|
|--versioning_scheme|YES|str|An value that determines where the API Version identifer will be located in a HTTP request.|/versioning_scheme|/properties/versioningScheme|
|--description|NO|str|Description of API Version Set.|/description|/properties/description|
|--version_query_name|NO|str|Name of query parameter that indicates the API Version if versioningScheme is set to `query`.|/version_query_name|/properties/versionQueryName|
|--version_header_name|NO|str|Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.|/version_header_name|/properties/versionHeaderName|
### apimgmt apiversionset delete

delete a apimgmt apiversionset.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
### apimgmt apiversionset list

list a apimgmt apiversionset.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt apiversionset show

show a apimgmt apiversionset.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--version_set_id|YES|default|Api Version Set identifier. Must be unique in the current API Management service instance.|version_set_id|versionSetId|
## apimgmt authorizationserver

### apimgmt authorizationserver create

create a apimgmt authorizationserver.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--authsid|YES|default|Identifier of the authorization server.|authsid|authsid|
|--display_name|YES|str|User-friendly authorization server name.|/display_name|/properties/displayName|
|--client_registration_endpoint|YES|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/client_registration_endpoint|/properties/clientRegistrationEndpoint|
|--authorization_endpoint|YES|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/authorization_endpoint|/properties/authorizationEndpoint|
|--grant_types|YES|list|Form of an authorization grant, which the client uses to request the access token.|/grant_types|/properties/grantTypes|
|--client_id|YES|str|Client or app id registered with this authorization server.|/client_id|/properties/clientId|
|--description|NO|str|Description of the authorization server. Can contain HTML formatting tags.|/description|/properties/description|
|--authorization_methods|NO|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/authorization_methods|/properties/authorizationMethods|
|--client_authentication_method|NO|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/client_authentication_method|/properties/clientAuthenticationMethod|
|--token_body_parameters|NO|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/token_body_parameters|/properties/tokenBodyParameters|
|--token_endpoint|NO|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/token_endpoint|/properties/tokenEndpoint|
|--support_state|NO|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/support_state|/properties/supportState|
|--default_scope|NO|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/default_scope|/properties/defaultScope|
|--bearer_token_sending_methods|NO|list|Specifies the mechanism by which access token is passed to the API. |/bearer_token_sending_methods|/properties/bearerTokenSendingMethods|
|--client_secret|NO|str|Client or app secret registered with this authorization server.|/client_secret|/properties/clientSecret|
|--resource_owner_username|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/resource_owner_username|/properties/resourceOwnerUsername|
|--resource_owner_password|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/resource_owner_password|/properties/resourceOwnerPassword|
### apimgmt authorizationserver update

update a apimgmt authorizationserver.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--authsid|YES|default|Identifier of the authorization server.|authsid|authsid|
|--display_name|YES|str|User-friendly authorization server name.|/display_name|/properties/displayName|
|--client_registration_endpoint|YES|str|Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced.|/client_registration_endpoint|/properties/clientRegistrationEndpoint|
|--authorization_endpoint|YES|str|OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2.|/authorization_endpoint|/properties/authorizationEndpoint|
|--grant_types|YES|list|Form of an authorization grant, which the client uses to request the access token.|/grant_types|/properties/grantTypes|
|--client_id|YES|str|Client or app id registered with this authorization server.|/client_id|/properties/clientId|
|--description|NO|str|Description of the authorization server. Can contain HTML formatting tags.|/description|/properties/description|
|--authorization_methods|NO|list|HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional.|/authorization_methods|/properties/authorizationMethods|
|--client_authentication_method|NO|list|Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format.|/client_authentication_method|/properties/clientAuthenticationMethod|
|--token_body_parameters|NO|list|Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {"name" : "name value", "value": "a value"}.|/token_body_parameters|/properties/tokenBodyParameters|
|--token_endpoint|NO|str|OAuth token endpoint. Contains absolute URI to entity being referenced.|/token_endpoint|/properties/tokenEndpoint|
|--support_state|NO|boolean|If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security.|/support_state|/properties/supportState|
|--default_scope|NO|str|Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values.|/default_scope|/properties/defaultScope|
|--bearer_token_sending_methods|NO|list|Specifies the mechanism by which access token is passed to the API. |/bearer_token_sending_methods|/properties/bearerTokenSendingMethods|
|--client_secret|NO|str|Client or app secret registered with this authorization server.|/client_secret|/properties/clientSecret|
|--resource_owner_username|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.|/resource_owner_username|/properties/resourceOwnerUsername|
|--resource_owner_password|NO|str|Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.|/resource_owner_password|/properties/resourceOwnerPassword|
### apimgmt authorizationserver delete

delete a apimgmt authorizationserver.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--authsid|YES|default|Identifier of the authorization server.|authsid|authsid|
### apimgmt authorizationserver list

list a apimgmt authorizationserver.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt authorizationserver show

show a apimgmt authorizationserver.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--authsid|YES|default|Identifier of the authorization server.|authsid|authsid|
## apimgmt backend

### apimgmt backend create

create a apimgmt backend.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
|--url|YES|str|Runtime Url of the Backend.|/url|/properties/url|
|--protocol|YES|str|Backend communication protocol.|/protocol|/properties/protocol|
|--title|NO|str|Backend Title.|/title|/properties/title|
|--description|NO|str|Backend Description.|/description|/properties/description|
|--resource_id|NO|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/resource_id|/properties/resourceId|
|--service_fabric_cluster|NO|dict|Backend Service Fabric Cluster Properties|/service_fabric_cluster|/properties/properties/serviceFabricCluster|
|--credentials|NO|dict|Backend Credentials Contract Properties|/credentials|/properties/credentials|
|--proxy|NO|dict|Backend Proxy Contract Properties|/proxy|/properties/proxy|
|--tls|NO|dict|Backend TLS Properties|/tls|/properties/tls|
### apimgmt backend update

update a apimgmt backend.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
|--url|YES|str|Runtime Url of the Backend.|/url|/properties/url|
|--protocol|YES|str|Backend communication protocol.|/protocol|/properties/protocol|
|--title|NO|str|Backend Title.|/title|/properties/title|
|--description|NO|str|Backend Description.|/description|/properties/description|
|--resource_id|NO|str|Management Uri of the Resource in External System. This url can be the Arm Resource Id of Logic Apps, Function Apps or Api Apps.|/resource_id|/properties/resourceId|
|--service_fabric_cluster|NO|dict|Backend Service Fabric Cluster Properties|/service_fabric_cluster|/properties/properties/serviceFabricCluster|
|--credentials|NO|dict|Backend Credentials Contract Properties|/credentials|/properties/credentials|
|--proxy|NO|dict|Backend Proxy Contract Properties|/proxy|/properties/proxy|
|--tls|NO|dict|Backend TLS Properties|/tls|/properties/tls|
### apimgmt backend delete

delete a apimgmt backend.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
### apimgmt backend list

list a apimgmt backend.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt backend show

show a apimgmt backend.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--backend_id|YES|default|Identifier of the Backend entity. Must be unique in the current API Management service instance.|backend_id|backendId|
## apimgmt cache

### apimgmt cache create

create a apimgmt cache.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
|--connection_string|YES|str|Runtime connection string to cache|/connection_string|/properties/connectionString|
|--description|NO|str|Cache description|/description|/properties/description|
|--resource_id|NO|str|Original uri of entity in external system cache points to|/resource_id|/properties/resourceId|
### apimgmt cache update

update a apimgmt cache.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
|--connection_string|YES|str|Runtime connection string to cache|/connection_string|/properties/connectionString|
|--description|NO|str|Cache description|/description|/properties/description|
|--resource_id|NO|str|Original uri of entity in external system cache points to|/resource_id|/properties/resourceId|
### apimgmt cache delete

delete a apimgmt cache.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
### apimgmt cache list

list a apimgmt cache.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt cache show

show a apimgmt cache.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--cache_id|YES|default|Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).|cache_id|cacheId|
## apimgmt certificate

### apimgmt certificate create

create a apimgmt certificate.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
|--data|YES|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/data|/properties/data|
|--password|YES|str|Password for the Certificate|/password|/properties/password|
### apimgmt certificate update

update a apimgmt certificate.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
|--data|YES|str|Base 64 encoded certificate using the application/x-pkcs12 representation.|/data|/properties/data|
|--password|YES|str|Password for the Certificate|/password|/properties/password|
### apimgmt certificate delete

delete a apimgmt certificate.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
### apimgmt certificate list

list a apimgmt certificate.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt certificate show

show a apimgmt certificate.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--certificate_id|YES|default|Identifier of the certificate entity. Must be unique in the current API Management service instance.|certificate_id|certificateId|
## apimgmt diagnostic

### apimgmt diagnostic create

create a apimgmt diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|--logger_id|YES|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|
### apimgmt diagnostic update

update a apimgmt diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
|--logger_id|YES|str|Resource Id of a target logger.|/logger_id|/properties/loggerId|
|--always_log|NO|str|Specifies for what type of messages sampling settings should not apply.|/always_log|/properties/alwaysLog|
|--sampling|NO|dict|Sampling settings for Diagnostic.|/sampling|/properties/sampling|
|--frontend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.|/frontend|/properties/frontend|
|--backend|NO|dict|Diagnostic settings for incoming/outgoing HTTP messages to the Backend|/backend|/properties/backend|
|--enable_http_correlation_headers|NO|boolean|Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.|/enable_http_correlation_headers|/properties/enableHttpCorrelationHeaders|
### apimgmt diagnostic delete

delete a apimgmt diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
### apimgmt diagnostic list

list a apimgmt diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt diagnostic show

show a apimgmt diagnostic.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--diagnostic_id|YES|default|Diagnostic identifier. Must be unique in the current API Management service instance.|diagnostic_id|diagnosticId|
## apimgmt group

### apimgmt group create

create a apimgmt group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|--display_name|YES|str|Group name.|/display_name|/properties/displayName|
|--description|NO|str|Group description.|/description|/properties/description|
|--type|NO|str|Group type.|/type|/properties/type|
|--external_id|NO|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|
### apimgmt group update

update a apimgmt group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|--display_name|YES|str|Group name.|/display_name|/properties/displayName|
|--description|NO|str|Group description.|/description|/properties/description|
|--type|NO|str|Group type.|/type|/properties/type|
|--external_id|NO|str|Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|
### apimgmt group delete

delete a apimgmt group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
### apimgmt group list

list a apimgmt group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt group show

show a apimgmt group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
## apimgmt group user

### apimgmt group user create

create a apimgmt group user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|--state|NO|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|NO|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|NO|list|Collection of user identities.|/identities|/properties/identities|
|--first_name|NO|str|First name.|/first_name|/properties/firstName|
|--last_name|NO|str|Last name.|/last_name|/properties/lastName|
|--email|NO|str|Email address.|/email|/properties/email|
|--registration_date|NO|datetime|Date of user registration. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>|/registration_date|/properties/registrationDate|
|--groups|NO|list|Collection of groups user is part of.|/groups|/properties/groups|
### apimgmt group user delete

delete a apimgmt group user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
### apimgmt group user list

list a apimgmt group user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
## apimgmt identityprovider

### apimgmt identityprovider create

create a apimgmt identityprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
|--client_id|YES|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/client_id|/properties/clientId|
|--client_secret|YES|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/client_secret|/properties/clientSecret|
|--type|NO|str|Identity Provider Type identifier.|/type|/properties/type|
|--allowed_tenants|NO|list|List of Allowed Tenants when configuring Azure Active Directory login.|/allowed_tenants|/properties/allowedTenants|
|--authority|NO|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/authority|/properties/authority|
|--signup_policy_name|NO|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/signup_policy_name|/properties/signupPolicyName|
|--signin_policy_name|NO|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/signin_policy_name|/properties/signinPolicyName|
|--profile_editing_policy_name|NO|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/profile_editing_policy_name|/properties/profileEditingPolicyName|
|--password_reset_policy_name|NO|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/password_reset_policy_name|/properties/passwordResetPolicyName|
### apimgmt identityprovider update

update a apimgmt identityprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
|--client_id|YES|str|Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.|/client_id|/properties/clientId|
|--client_secret|YES|str|Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.|/client_secret|/properties/clientSecret|
|--type|NO|str|Identity Provider Type identifier.|/type|/properties/type|
|--allowed_tenants|NO|list|List of Allowed Tenants when configuring Azure Active Directory login.|/allowed_tenants|/properties/allowedTenants|
|--authority|NO|str|OpenID Connect discovery endpoint hostname for AAD or AAD B2C.|/authority|/properties/authority|
|--signup_policy_name|NO|str|Signup Policy Name. Only applies to AAD B2C Identity Provider.|/signup_policy_name|/properties/signupPolicyName|
|--signin_policy_name|NO|str|Signin Policy Name. Only applies to AAD B2C Identity Provider.|/signin_policy_name|/properties/signinPolicyName|
|--profile_editing_policy_name|NO|str|Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.|/profile_editing_policy_name|/properties/profileEditingPolicyName|
|--password_reset_policy_name|NO|str|Password Reset Policy Name. Only applies to AAD B2C Identity Provider.|/password_reset_policy_name|/properties/passwordResetPolicyName|
### apimgmt identityprovider delete

delete a apimgmt identityprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
### apimgmt identityprovider list

list a apimgmt identityprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt identityprovider show

show a apimgmt identityprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Identity Provider Type identifier.|identity_provider_name|identityProviderName|
## apimgmt logger

### apimgmt logger create

create a apimgmt logger.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
|--logger_type|YES|str|Logger type.|/logger_type|/properties/loggerType|
|--credentials|YES|unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/credentials|/properties/credentials|
|--description|NO|str|Logger description.|/description|/properties/description|
|--is_buffered|NO|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/is_buffered|/properties/isBuffered|
|--resource_id|NO|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/resource_id|/properties/resourceId|
### apimgmt logger update

update a apimgmt logger.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
|--logger_type|YES|str|Logger type.|/logger_type|/properties/loggerType|
|--credentials|YES|unknown[DictionaryType {"$id":"3331","$type":"DictionaryType","valueType":{"$id":"3332","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"3333","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"3334","fixed":false},"deprecated":false}]|The name and SendRule connection string of the event hub for azureEventHub logger.<br>Instrumentation key for applicationInsights logger.|/credentials|/properties/credentials|
|--description|NO|str|Logger description.|/description|/properties/description|
|--is_buffered|NO|boolean|Whether records are buffered in the logger before publishing. Default is assumed to be true.|/is_buffered|/properties/isBuffered|
|--resource_id|NO|str|Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource).|/resource_id|/properties/resourceId|
### apimgmt logger delete

delete a apimgmt logger.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
### apimgmt logger list

list a apimgmt logger.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt logger show

show a apimgmt logger.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--logger_id|YES|default|Logger identifier. Must be unique in the API Management service instance.|logger_id|loggerId|
## apimgmt notification

### apimgmt notification create

create a apimgmt notification.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--title|YES|str|Title of the Notification.|/title|/properties/title|
|--description|NO|str|Description of the Notification.|/description|/properties/description|
|--recipients|NO|dict|Recipient Parameter values.|/recipients|/properties/recipients|
### apimgmt notification update

update a apimgmt notification.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--title|YES|str|Title of the Notification.|/title|/properties/title|
|--description|NO|str|Description of the Notification.|/description|/properties/description|
|--recipients|NO|dict|Recipient Parameter values.|/recipients|/properties/recipients|
### apimgmt notification list

list a apimgmt notification.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt notification show

show a apimgmt notification.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Notification Name Identifier.|notification_name|notificationName|
## apimgmt notification recipientemail

### apimgmt notification recipientemail create

create a apimgmt notification recipientemail.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--email|YES|default|Email identifier.|email|email|
### apimgmt notification recipientemail update

update a apimgmt notification recipientemail.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--email|YES|default|Email identifier.|email|email|
### apimgmt notification recipientemail delete

delete a apimgmt notification recipientemail.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--email|YES|default|Email identifier.|email|email|
### apimgmt notification recipientemail list

list a apimgmt notification recipientemail.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
## apimgmt notification recipientuser

### apimgmt notification recipientuser create

create a apimgmt notification recipientuser.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
### apimgmt notification recipientuser update

update a apimgmt notification recipientuser.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
### apimgmt notification recipientuser delete

delete a apimgmt notification recipientuser.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
### apimgmt notification recipientuser list

list a apimgmt notification recipientuser.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--notification_name|YES|default|Notification Name Identifier.|notification_name|notificationName|
## apimgmt openidconnectprovider

### apimgmt openidconnectprovider create

create a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|opid|opid|
|--display_name|YES|str|User-friendly OpenID Connect Provider name.|/display_name|/properties/displayName|
|--metadata_endpoint|YES|str|Metadata endpoint URI.|/metadata_endpoint|/properties/metadataEndpoint|
|--client_id|YES|str|Client ID of developer console which is the client application.|/client_id|/properties/clientId|
|--description|NO|str|User-friendly description of OpenID Connect Provider.|/description|/properties/description|
|--client_secret|NO|str|Client Secret of developer console which is the client application.|/client_secret|/properties/clientSecret|
### apimgmt openidconnectprovider update

update a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|opid|opid|
|--display_name|YES|str|User-friendly OpenID Connect Provider name.|/display_name|/properties/displayName|
|--metadata_endpoint|YES|str|Metadata endpoint URI.|/metadata_endpoint|/properties/metadataEndpoint|
|--client_id|YES|str|Client ID of developer console which is the client application.|/client_id|/properties/clientId|
|--description|NO|str|User-friendly description of OpenID Connect Provider.|/description|/properties/description|
|--client_secret|NO|str|Client Secret of developer console which is the client application.|/client_secret|/properties/clientSecret|
### apimgmt openidconnectprovider delete

delete a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|opid|opid|
### apimgmt openidconnectprovider list

list a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt openidconnectprovider show

show a apimgmt openidconnectprovider.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--opid|YES|default|Identifier of the OpenID Connect Provider.|opid|opid|
## apimgmt policy

### apimgmt policy create

create a apimgmt policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt policy update

update a apimgmt policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt policy delete

delete a apimgmt policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
### apimgmt policy list

list a apimgmt policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt policy show

show a apimgmt policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--format|NO|default|Format of the policyContent.|/format|/properties/format|
## apimgmt portalsetting

### apimgmt portalsetting create

create a apimgmt portalsetting.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
|--url|NO|str|A delegation Url.|/url|/properties/url|
|--validation_key|NO|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/validation_key|/properties/validationKey|
|--subscriptions|NO|dict|Subscriptions delegation settings.|/subscriptions|/properties/subscriptions|
|--user_registration|NO|dict|User registration delegation settings.|/user_registration|/properties/userRegistration|
### apimgmt portalsetting update

update a apimgmt portalsetting.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
|--url|NO|str|A delegation Url.|/url|/properties/url|
|--validation_key|NO|str|A base64-encoded validation key to validate, that a request is coming from Azure API Management.|/validation_key|/properties/validationKey|
|--subscriptions|NO|dict|Subscriptions delegation settings.|/subscriptions|/properties/subscriptions|
|--user_registration|NO|dict|User registration delegation settings.|/user_registration|/properties/userRegistration|
### apimgmt portalsetting show

show a apimgmt portalsetting.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--name|YES|default|The name of the API Management service.|service_name|serviceName|
## apimgmt product

### apimgmt product create

create a apimgmt product.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--display_name|YES|str|Product name.|/display_name|/properties/displayName|
|--description|NO|str|Product description. May include HTML formatting tags.|/description|/properties/description|
|--terms|NO|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/terms|/properties/terms|
|--subscription_required|NO|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/subscription_required|/properties/subscriptionRequired|
|--approval_required|NO|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/approval_required|/properties/approvalRequired|
|--subscriptions_limit|NO|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/subscriptions_limit|/properties/subscriptionsLimit|
|--state|NO|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/state|/properties/state|
### apimgmt product update

update a apimgmt product.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--display_name|YES|str|Product name.|/display_name|/properties/displayName|
|--description|NO|str|Product description. May include HTML formatting tags.|/description|/properties/description|
|--terms|NO|str|Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.|/terms|/properties/terms|
|--subscription_required|NO|boolean|Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.|/subscription_required|/properties/subscriptionRequired|
|--approval_required|NO|boolean|whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.|/approval_required|/properties/approvalRequired|
|--subscriptions_limit|NO|number|Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.|/subscriptions_limit|/properties/subscriptionsLimit|
|--state|NO|str|whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.|/state|/properties/state|
### apimgmt product delete

delete a apimgmt product.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
### apimgmt product list

list a apimgmt product.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt product show

show a apimgmt product.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
## apimgmt product api

### apimgmt product api create

create a apimgmt product api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--path|YES|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|NO|str|Type of API.|/type|/properties/type|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--is_online|NO|boolean|Indicates if API revision is accessible via the gateway.|/is_online|/properties/isOnline|
|--api_revision_description|NO|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|NO|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|NO|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|NO|dict|Version set details|/api_version_set|/properties/apiVersionSet|
### apimgmt product api update

update a apimgmt product api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
|--path|YES|str|Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.|/path|/properties/path|
|--description|NO|str|Description of the API. May include HTML formatting tags.|/description|/properties/description|
|--authentication_settings|NO|dict|Collection of authentication settings included into this API.|/authentication_settings|/properties/authenticationSettings|
|--subscription_key_parameter_names|NO|dict|Protocols over which API is made available.|/subscription_key_parameter_names|/properties/subscriptionKeyParameterNames|
|--type|NO|str|Type of API.|/type|/properties/type|
|--api_revision|NO|str|Describes the Revision of the Api. If no value is provided, default revision 1 is created|/api_revision|/properties/apiRevision|
|--api_version|NO|str|Indicates the Version identifier of the API if the API is versioned|/api_version|/properties/apiVersion|
|--is_current|NO|boolean|Indicates if API revision is current api revision.|/is_current|/properties/isCurrent|
|--is_online|NO|boolean|Indicates if API revision is accessible via the gateway.|/is_online|/properties/isOnline|
|--api_revision_description|NO|str|Description of the Api Revision.|/api_revision_description|/properties/apiRevisionDescription|
|--api_version_description|NO|str|Description of the Api Version.|/api_version_description|/properties/apiVersionDescription|
|--api_version_set_id|NO|str|A resource identifier for the related ApiVersionSet.|/api_version_set_id|/properties/apiVersionSetId|
|--subscription_required|NO|boolean|Specifies whether an API or Product subscription is required for accessing the API.|/subscription_required|/properties/subscriptionRequired|
|--source_api_id|NO|str|API identifier of the source API.|/source_api_id|/properties/sourceApiId|
|--display_name|NO|str|API name. Must be 1 to 300 characters long.|/display_name|/properties/displayName|
|--service_url|NO|str|Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.|/service_url|/properties/serviceUrl|
|--protocols|NO|list|Describes on which protocols the operations in this API can be invoked.|/protocols|/properties/protocols|
|--api_version_set|NO|dict|Version set details|/api_version_set|/properties/apiVersionSet|
### apimgmt product api delete

delete a apimgmt product api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--api_id|YES|default|API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.|api_id|apiId|
### apimgmt product api list

list a apimgmt product api.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
## apimgmt product group

### apimgmt product group create

create a apimgmt product group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|--display_name|YES|str|Group name.|/display_name|/properties/displayName|
|--description|NO|str|Group description. Can contain HTML formatting tags.|/description|/properties/description|
|--built_in|NO|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/built_in|/properties/builtIn|
|--type|NO|str|Group type.|/type|/properties/type|
|--external_id|NO|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|
### apimgmt product group update

update a apimgmt product group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
|--display_name|YES|str|Group name.|/display_name|/properties/displayName|
|--description|NO|str|Group description. Can contain HTML formatting tags.|/description|/properties/description|
|--built_in|NO|boolean|true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.|/built_in|/properties/builtIn|
|--type|NO|str|Group type.|/type|/properties/type|
|--external_id|NO|str|For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.|/external_id|/properties/externalId|
### apimgmt product group delete

delete a apimgmt product group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--group_id|YES|default|Group identifier. Must be unique in the current API Management service instance.|group_id|groupId|
### apimgmt product group list

list a apimgmt product group.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
## apimgmt product policy

### apimgmt product policy create

create a apimgmt product policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt product policy update

update a apimgmt product policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--value|YES|str|Contents of the Policy as defined by the format.|/value|/properties/value|
|--format|NO|str|Format of the policyContent.|/format|/properties/format|
### apimgmt product policy delete

delete a apimgmt product policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
### apimgmt product policy list

list a apimgmt product policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
### apimgmt product policy show

show a apimgmt product policy.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--product_id|YES|default|Product identifier. Must be unique in the current API Management service instance.|product_id|productId|
|--policy_id|YES|default|The identifier of the Policy.|policy_id|policyId|
|--format|NO|default|Format of the policyContent.|/format|/properties/format|
## apimgmt property

### apimgmt property create

create a apimgmt property.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--prop_id|YES|default|Identifier of the property.|prop_id|propId|
|--display_name|YES|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/display_name|/properties/displayName|
|--value|YES|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/value|/properties/value|
|--tags|NO|list|Optional tags that when provided can be used to filter the property list.|/tags|/properties/tags|
|--secret|NO|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/secret|/properties/secret|
### apimgmt property update

update a apimgmt property.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--prop_id|YES|default|Identifier of the property.|prop_id|propId|
|--display_name|YES|str|Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters.|/display_name|/properties/displayName|
|--value|YES|str|Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace.|/value|/properties/value|
|--tags|NO|list|Optional tags that when provided can be used to filter the property list.|/tags|/properties/tags|
|--secret|NO|boolean|Determines whether the value is a secret and should be encrypted or not. Default value is false.|/secret|/properties/secret|
### apimgmt property delete

delete a apimgmt property.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--prop_id|YES|default|Identifier of the property.|prop_id|propId|
### apimgmt property list

list a apimgmt property.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt property show

show a apimgmt property.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--prop_id|YES|default|Identifier of the property.|prop_id|propId|
## apimgmt subscription

### apimgmt subscription create

create a apimgmt subscription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
|--scope|YES|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/scope|/properties/scope|
|--display_name|YES|str|Subscription name.|/display_name|/properties/displayName|
|--notify|NO|default|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |notify|notify|
|--owner_id|NO|str|User (user id path) for whom subscription is being created in form /users/{userId}|/owner_id|/properties/ownerId|
|--primary_key|NO|str|Primary subscription key. If not specified during request key will be generated automatically.|/primary_key|/properties/primaryKey|
|--secondary_key|NO|str|Secondary subscription key. If not specified during request key will be generated automatically.|/secondary_key|/properties/secondaryKey|
|--state|NO|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/state|/properties/state|
|--allow_tracing|NO|boolean|Determines whether tracing can be enabled|/allow_tracing|/properties/allowTracing|
### apimgmt subscription update

update a apimgmt subscription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
|--scope|YES|str|Scope like /products/{productId} or /apis or /apis/{apiId}.|/scope|/properties/scope|
|--display_name|YES|str|Subscription name.|/display_name|/properties/displayName|
|--notify|NO|default|Notify change in Subscription State. <br> - If false, do not send any email notification for change of state of subscription <br> - If true, send email notification of change of state of subscription |notify|notify|
|--owner_id|NO|str|User (user id path) for whom subscription is being created in form /users/{userId}|/owner_id|/properties/ownerId|
|--primary_key|NO|str|Primary subscription key. If not specified during request key will be generated automatically.|/primary_key|/properties/primaryKey|
|--secondary_key|NO|str|Secondary subscription key. If not specified during request key will be generated automatically.|/secondary_key|/properties/secondaryKey|
|--state|NO|str|Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.|/state|/properties/state|
|--allow_tracing|NO|boolean|Determines whether tracing can be enabled|/allow_tracing|/properties/allowTracing|
### apimgmt subscription delete

delete a apimgmt subscription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
### apimgmt subscription list

list a apimgmt subscription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt subscription show

show a apimgmt subscription.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--sid|YES|default|Subscription entity Identifier. The entity represents the association between a user and a product in API Management.|sid|sid|
## apimgmt tag

### apimgmt tag create

create a apimgmt tag.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--display_name|YES|str|Tag name.|/display_name|/properties/displayName|
### apimgmt tag update

update a apimgmt tag.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
|--display_name|YES|str|Tag name.|/display_name|/properties/displayName|
### apimgmt tag delete

delete a apimgmt tag.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
### apimgmt tag list

list a apimgmt tag.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt tag show

show a apimgmt tag.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--tag_id|YES|default|Tag identifier. Must be unique in the current API Management service instance.|tag_id|tagId|
## apimgmt template

### apimgmt template create

create a apimgmt template.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Email Template Name Identifier.|template_name|templateName|
|--subject|NO|str|Subject of the Template.|/subject|/properties/subject|
|--title|NO|str|Title of the Template.|/title|/properties/title|
|--description|NO|str|Description of the Email Template.|/description|/properties/description|
|--body|NO|str|Email Template Body. This should be a valid XDocument|/body|/properties/body|
### apimgmt template update

update a apimgmt template.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Email Template Name Identifier.|template_name|templateName|
|--subject|NO|str|Subject of the Template.|/subject|/properties/subject|
|--title|NO|str|Title of the Template.|/title|/properties/title|
|--description|NO|str|Description of the Email Template.|/description|/properties/description|
|--body|NO|str|Email Template Body. This should be a valid XDocument|/body|/properties/body|
### apimgmt template delete

delete a apimgmt template.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Email Template Name Identifier.|template_name|templateName|
### apimgmt template list

list a apimgmt template.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt template show

show a apimgmt template.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--name|YES|default|Email Template Name Identifier.|template_name|templateName|
## apimgmt user

### apimgmt user create

create a apimgmt user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|--email|YES|str|Email address. Must not be empty and must be unique within the service instance.|/email|/properties/email|
|--first_name|YES|str|First name.|/first_name|/properties/firstName|
|--last_name|YES|str|Last name.|/last_name|/properties/lastName|
|--state|NO|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|NO|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|NO|list|Collection of user identities.|/identities|/properties/identities|
|--password|NO|str|User Password. If no value is provided, a default password is generated.|/password|/properties/password|
|--confirmation|NO|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/confirmation|/properties/confirmation|
### apimgmt user update

update a apimgmt user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
|--email|YES|str|Email address. Must not be empty and must be unique within the service instance.|/email|/properties/email|
|--first_name|YES|str|First name.|/first_name|/properties/firstName|
|--last_name|YES|str|Last name.|/last_name|/properties/lastName|
|--state|NO|str|Account state. Specifies whether the user is active or not. Blocked users are unable to sign into the developer portal or call any APIs of subscribed products. Default state is Active.|/state|/properties/state|
|--note|NO|str|Optional note about a user set by the administrator.|/note|/properties/note|
|--identities|NO|list|Collection of user identities.|/identities|/properties/identities|
|--password|NO|str|User Password. If no value is provided, a default password is generated.|/password|/properties/password|
|--confirmation|NO|str|Determines the type of confirmation e-mail that will be sent to the newly created user.|/confirmation|/properties/confirmation|
### apimgmt user delete

delete a apimgmt user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|
### apimgmt user list

list a apimgmt user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
### apimgmt user show

show a apimgmt user.

|Option|Required|Type|Description|Path (SDK)|Path (swagger)|
|------|--------|----|-----------|----------|--------------|
|--resource_group|YES|default|The name of the resource group.|resource_group_name|resourceGroupName|
|--service_name|YES|default|The name of the API Management service.|service_name|serviceName|
|--user_id|YES|default|User identifier. Must be unique in the current API Management service instance.|user_id|userId|