# StopInQueryVirtualMachine
RESOURCE_GROUP="myresourcegroup"
VIRTUAL_MACHINE_NAME="myvirtualmachine"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/virtualMachines/$VIRTUAL_MACHINE_NAME/stop?api-version=2019-04-01 --body '
{}
'