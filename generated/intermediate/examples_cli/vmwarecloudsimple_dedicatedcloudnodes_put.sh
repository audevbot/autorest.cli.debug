# CreateDedicatedCloudNode
RESOURCE_GROUP="myresourcegroup"
DEDICATED_CLOUD_NODE_NAME="mydedicatedcloudnode"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/$DEDICATED_CLOUD_NODE_NAME?api-version=2019-04-01 --body '
{
  "location": "westus",
  "properties": {
    "skuDescription": {
      "id": "general",
      "name": "CS28-Node"
    },
    "placementGroupId": "n1",
    "availabilityZoneId": "az1",
    "nodesCount": "1",
    "purchaseId": "56acbd46-3d36-4bbf-9b08-57c30fdf6932"
  },
  "sku": {
    "name": "VMware_CloudSimple_CS28"
  }
}
'