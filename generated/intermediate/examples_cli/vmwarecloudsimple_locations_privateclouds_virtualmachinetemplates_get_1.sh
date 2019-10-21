# GetVirtualMachineTemplate
LOCATION_NAME="mylocation"
PRIVATE_CLOUD_NAME="myprivatecloud"
VIRTUAL_MACHINE_TEMPLATE_NAME="myvirtualmachinetemplate"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/privateClouds/$PRIVATE_CLOUD_NAME/virtualMachineTemplates/$VIRTUAL_MACHINE_TEMPLATE_NAME?api-version=2019-04-01