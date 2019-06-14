# Create or update specific Front Door
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"
BACKEND_POOL_NAME="mybackendpool"
LOAD_BALANCING_SETTING_NAME="myloadbalancingsetting"
HEALTH_PROBE_SETTING_NAME="myhealthprobesetting"
FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME="myfrontdoorwebapplicationfirewallpolicy"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME --api-version 2019-04-01 --is-full-object --properties '
{
  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "",
  "location": "westus",
  "tags": {
    "tag1": "value1",
    "tag2": "value2"
  },
  "properties": {
    "routingRules": [
      {
        "name": "routingRule1",
        "properties": {
          "frontendEndpoints": [
            {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
            },
            {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
            }
          ],
          "acceptedProtocols": [
            "Http"
          ],
          "patternsToMatch": [
            "/*"
          ],
          "routeConfiguration": {
            "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",
            "backendPool": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""
            }
          },
          "enabledState": "Enabled"
        }
      }
    ],
    "healthProbeSettings": [
      {
        "name": "healthProbeSettings1",
        "properties": {
          "path": "/",
          "protocol": "Http",
          "intervalInSeconds": "120"
        }
      }
    ],
    "loadBalancingSettings": [
      {
        "name": "loadBalancingSettings1",
        "properties": {
          "sampleSize": "4",
          "successfulSamplesRequired": "2"
        }
      }
    ],
    "backendPools": [
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
    ],
    "frontendEndpoints": [
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
      },
      {
        "name": "default",
        "properties": {
          "hostName": "frontDoor1.azurefd.net"
        }
      }
    ],
    "backendPoolsSettings": {
      "enforceCertificateNameCheck": "Enabled"
    },
    "enabledState": "Enabled"
  }
}
'