# CreateDedicatedCloudService
RESOURCE_GROUP="myresourcegroup"
DEDICATED_CLOUD_SERVICE_NAME="mydedicatedcloudservice"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/$DEDICATED_CLOUD_SERVICE_NAME?api-version=2019-04-01 --body '
{
  "location": "westus",
  "properties": {
    "gatewaySubnet": "10.0.0.0"
  }
}
'