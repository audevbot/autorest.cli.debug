# Azure CLI Module Creation Report

## alerts

### alerts create

create a alerts.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--alert-rule-name**|str|The name of the alert rule.|alert_rule_name|alertRuleName|
|**--state**|str|The alert rule state.|/state|/properties/state|
|**--severity**|str|The alert rule severity.|/severity|/properties/severity|
|**--frequency**|unknown-primary[timeSpan]|The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes.|/frequency|/properties/frequency|
|**--detector**|dict|The alert rule's detector.|/detector|/properties/detector|
|**--scope**|list|The alert rule resources scope.|/scope|/properties/scope|
|**--action-groups**|dict|The alert rule actions.|/action_groups|/properties/actionGroups|
|--location|str|The resource location.|/location|/location|
|--tags|unknown-primary[object]|The resource tags.|/tags|/tags|
|--description|str|The alert rule description.|/description|/properties/description|
|--throttling|dict|The alert rule throttling information.|/throttling|/properties/throttling|

**Example: Create or update a Smart Detector alert rule**

```
alerts create --resource-group MyAlertRules
        --alert-rule-name MyAlertRule
        --description "Sample smart detector alert rule description"
        --state Enabled
        --severity Sev3
        --frequency PT5M
        --scope /subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1
```
### alerts update

update a alerts.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--alert-rule-name**|str|The name of the alert rule.|alert_rule_name|alertRuleName|
|**--state**|str|The alert rule state.|/state|/properties/state|
|**--severity**|str|The alert rule severity.|/severity|/properties/severity|
|**--frequency**|unknown-primary[timeSpan]|The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes.|/frequency|/properties/frequency|
|**--detector**|dict|The alert rule's detector.|/detector|/properties/detector|
|**--scope**|list|The alert rule resources scope.|/scope|/properties/scope|
|**--action-groups**|dict|The alert rule actions.|/action_groups|/properties/actionGroups|
|--location|str|The resource location.|/location|/location|
|--tags|unknown-primary[object]|The resource tags.|/tags|/tags|
|--description|str|The alert rule description.|/description|/properties/description|
|--throttling|dict|The alert rule throttling information.|/throttling|/properties/throttling|
### alerts delete

delete a alerts.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--alert-rule-name**|str|The name of the alert rule.|alert_rule_name|alertRuleName|

**Example: Delete a Smart Detector alert rule**

```
alerts delete --resource-group MyAlertRules
        --alert-rule-name MyAlertRule
```
### alerts list

list a alerts.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
### alerts show

show a alerts.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--alert-rule-name**|str|The name of the alert rule.|alert_rule_name|alertRuleName|