# GetDedicatedCloudService
RESOURCE_GROUP="myresourcegroup"
DEDICATED_CLOUD_SERVICE_NAME="mydedicatedcloudservice"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/$DEDICATED_CLOUD_SERVICE_NAME --api-version 2019-04-01