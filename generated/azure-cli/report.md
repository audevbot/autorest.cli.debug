# Azure CLI Module Creation Report

## vmwarecs

### vmwarecs create

create a vmwarecs.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group|resource_group_name|resourceGroupName|
|**--name**|str|virtual machine name|virtual_machine_name|virtualMachineName|
|**--location**|str|Azure region|/location|/location|
|**--amount-of-ram**|number|The amount of memory|/amount_of_ram|/properties/amountOfRam|
|**--number-of-cores**|number|The number of CPU cores|/number_of_cores|/properties/numberOfCores|
|**--private-cloud-id**|str|Private Cloud Id|/private_cloud_id|/properties/privateCloudId|
|--referer|str|referer url|referer|Referer|
|--disks|list|The list of Virtual Disks|/disks|/properties/disks|
|--expose-to-guest-vm|boolean|Expose Guest OS or not|/expose_to_guest_vm|/properties/exposeToGuestVM|
|--nics|list|The list of Virtual NICs|/nics|/properties/nics|
|--password|str|Password for login|/password|/properties/password|
|--resource-pool|dict|Virtual Machines Resource Pool|/resource_pool|/properties/resourcePool|
|--template-id|str|Virtual Machine Template Id|/template_id|/properties/templateId|
|--username|str|Username for login|/username|/properties/username|
|--v-sphere-networks|list|The list of Virtual VSphere Networks|/v_sphere_networks|/properties/vSphereNetworks|
|--tags|dictionary|The list of tags|/tags|/tags|

**Example: CreateVirtualMachine**

```
vmwarecs create --resource-group myResourceGroup
        --referer https://management.azure.com/
        --name myVirtualMachine
        --location westus2
        --amount-of-ram 4096
        --number-of-cores 2
        --private-cloud-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}"
        --template-id "/subscriptions/{{ subscription_id }}/providers/Microsoft.VMwareCloudSimple/locations/{{ location_name }}/privateClouds/{{ private_cloud_name }}/virtualMachineTemplates/{{ virtual_machine_template_name }}"
```
### vmwarecs update

update a vmwarecs.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group|resource_group_name|resourceGroupName|
|**--name**|str|virtual machine name|virtual_machine_name|virtualMachineName|
|**--location**|str|Azure region|/location|/location|
|**--amount-of-ram**|number|The amount of memory|/amount_of_ram|/properties/amountOfRam|
|**--number-of-cores**|number|The number of CPU cores|/number_of_cores|/properties/numberOfCores|
|**--private-cloud-id**|str|Private Cloud Id|/private_cloud_id|/properties/privateCloudId|
|--referer|str|referer url|referer|Referer|
|--disks|list|The list of Virtual Disks|/disks|/properties/disks|
|--expose-to-guest-vm|boolean|Expose Guest OS or not|/expose_to_guest_vm|/properties/exposeToGuestVM|
|--nics|list|The list of Virtual NICs|/nics|/properties/nics|
|--password|str|Password for login|/password|/properties/password|
|--resource-pool|dict|Virtual Machines Resource Pool|/resource_pool|/properties/resourcePool|
|--template-id|str|Virtual Machine Template Id|/template_id|/properties/templateId|
|--username|str|Username for login|/username|/properties/username|
|--v-sphere-networks|list|The list of Virtual VSphere Networks|/v_sphere_networks|/properties/vSphereNetworks|
|--tags|dictionary|The list of tags|/tags|/tags|

**Example: PatchVirtualMachine**

```
vmwarecs update --resource-group myResourceGroup
        --name myVirtualMachine
```
### vmwarecs delete

delete a vmwarecs.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group|resource_group_name|resourceGroupName|
|**--name**|str|virtual machine name|virtual_machine_name|virtualMachineName|
|--referer|str|referer url|referer|Referer|

**Example: DeleteVirtualMachine**

```
vmwarecs delete --resource-group myResourceGroup
        --referer https://management.azure.com/
        --name myVirtualMachine
```
### vmwarecs list

list a vmwarecs.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group|resource_group_name|resourceGroupName|
### vmwarecs show

show a vmwarecs.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group|resource_group_name|resourceGroupName|
|**--name**|str|virtual machine name|virtual_machine_name|virtualMachineName|