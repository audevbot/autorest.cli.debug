# Create or update specific LoadBalancingSettings
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
LOAD_BALANCING_SETTING_NAME="myloadbalancingsetting"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/loadBalancingSettings/$LOAD_BALANCING_SETTING_NAME --api-version 2019-04-01 --is-full-object --properties '
{
  "name": "loadBalancingSettings1",
  "properties": {
    "sampleSize": "4",
    "successfulSamplesRequired": "2"
  }
}
'