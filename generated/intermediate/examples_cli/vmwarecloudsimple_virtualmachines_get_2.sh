# GetVirtualMachine
RESOURCE_GROUP="myresourcegroup"
VIRTUAL_MACHINE_NAME="myvirtualmachine"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/virtualMachines/$VIRTUAL_MACHINE_NAME --api-version 2019-04-01