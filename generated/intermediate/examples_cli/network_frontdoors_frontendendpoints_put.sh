# Create or update specific Frontend Endpoint
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"
FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME="myfrontdoorwebapplicationfirewallpolicy"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/frontendEndpoints/$FRONTEND_ENDPOINT_NAME --api-version 2019-04-01 --is-full-object --properties '
{
  "name": "frontendEndpoint1",
  "properties": {
    "hostName": "www.contoso.com",
    "sessionAffinityEnabledState": "Enabled",
    "sessionAffinityTtlSeconds": "60",
    "webApplicationFirewallPolicyLink": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/" + FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME + ""
    }
  }
}
'