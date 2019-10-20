# ListRGDedicatedCloudServices
RESOURCE_GROUP="myresourcegroup"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices?api-version=2019-04-01