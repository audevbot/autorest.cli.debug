# Azure CLI Module Creation Report

## aro

### aro create

create a aro.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the OpenShift managed cluster resource.|resource_name|resourceName|
|**--location**|str|Resource location|/location|/location|
|**--open-shift-version**|str|Version of OpenShift specified when creating the cluster.|/open_shift_version|/properties/openShiftVersion|
|--tags|dictionary|Resource tags|/tags|/tags|
|--plan|dict|Define the resource plan as required by ARM for billing purposes|/plan|/plan|
|--network-profile|dict|Configuration for OpenShift networking.|/network_profile|/properties/networkProfile|
|--router-profiles|list|Configuration for OpenShift router(s).|/router_profiles|/properties/routerProfiles|
|--master-pool-profile|dict|Configuration for OpenShift master VMs.|/master_pool_profile|/properties/masterPoolProfile|
|--agent-pool-profiles|list|Configuration of OpenShift cluster VMs.|/agent_pool_profiles|/properties/agentPoolProfiles|
|--auth-profile|dict|Configures OpenShift authentication.|/auth_profile|/properties/authProfile|

**Example: Create/Update OpenShift Managed Cluster**

```
aro create --resource-group rg1
        --name clustername1
        --location location1
        --open-shift-version v3.11
```
### aro update

update a aro.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the OpenShift managed cluster resource.|resource_name|resourceName|
|**--location**|str|Resource location|/location|/location|
|**--open-shift-version**|str|Version of OpenShift specified when creating the cluster.|/open_shift_version|/properties/openShiftVersion|
|--tags|dictionary|Resource tags|/tags|/tags|
|--plan|dict|Define the resource plan as required by ARM for billing purposes|/plan|/plan|
|--network-profile|dict|Configuration for OpenShift networking.|/network_profile|/properties/networkProfile|
|--router-profiles|list|Configuration for OpenShift router(s).|/router_profiles|/properties/routerProfiles|
|--master-pool-profile|dict|Configuration for OpenShift master VMs.|/master_pool_profile|/properties/masterPoolProfile|
|--agent-pool-profiles|list|Configuration of OpenShift cluster VMs.|/agent_pool_profiles|/properties/agentPoolProfiles|
|--auth-profile|dict|Configures OpenShift authentication.|/auth_profile|/properties/authProfile|
### aro delete

delete a aro.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the OpenShift managed cluster resource.|resource_name|resourceName|

**Example: Delete OpenShift Managed Cluster**

```
aro delete --resource-group rg1
        --name clustername1
```
### aro list

list a aro.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
### aro show

show a aro.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the OpenShift managed cluster resource.|resource_name|resourceName|