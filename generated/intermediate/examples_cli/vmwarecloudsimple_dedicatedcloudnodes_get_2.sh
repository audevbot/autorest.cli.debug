# GetDedicatedCloudNode
RESOURCE_GROUP="myresourcegroup"
DEDICATED_CLOUD_NODE_NAME="mydedicatedcloudnode"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/$DEDICATED_CLOUD_NODE_NAME --api-version 2019-04-01