# Create or update specific Backend Pool
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
BACKEND_POOL_NAME="mybackendpool"
LOAD_BALANCING_SETTING_NAME="myloadbalancingsetting"
HEALTH_PROBE_SETTING_NAME="myhealthprobesetting"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/backendPools/$BACKEND_POOL_NAME --api-version 2019-04-01 --is-full-object --properties '
{
  "name": "backendPool1",
  "properties": {
    "backends": [
      {
        "address": "w3.contoso.com",
        "httpPort": "80",
        "httpsPort": "443",
        "weight": "1",
        "priority": "2"
      },
      {
        "address": "contoso.com.website-us-west-2.othercloud.net",
        "httpPort": "80",
        "httpsPort": "443",
        "weight": "2",
        "priority": "1"
      },
      {
        "address": "contoso1.azurewebsites.net",
        "httpPort": "80",
        "httpsPort": "443",
        "weight": "1",
        "priority": "1"
      }
    ],
    "loadBalancingSettings": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""
    },
    "healthProbeSettings": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""
    }
  }
}
'