# Create or update specific Front Door
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
FRONTEND_ENDPOINT_NAME="myfrontendendpoint"
BACKEND_POOL_NAME="mybackendpool"
LOAD_BALANCING_SETTING_NAME="myloadbalancingsetting"
HEALTH_PROBE_SETTING_NAME="myhealthprobesetting"
FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME="myfrontdoorwebapplicationfirewallpolicy"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME?api-version=2019-04-01 --body '
{
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
          "frontend_endpoints": [
            {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
            },
            {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/frontendEndpoints/" + FRONTEND_ENDPOINT_NAME + ""
            }
          ],
          "accepted_protocols": [
            "Http"
          ],
          "patterns_to_match": [
            "/*"
          ],
          "route_configuration": {
            "@odata.type": "#Microsoft.Azure.FrontDoor.Models.FrontdoorForwardingConfiguration",
            "backend_pool": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/backendPools/" + BACKEND_POOL_NAME + ""
            }
          },
          "enabled_state": "Enabled"
        }
      }
    ],
    "healthProbeSettings": [
      {
        "name": "healthProbeSettings1",
        "properties": {
          "path": "/",
          "protocol": "Http",
          "interval_in_seconds": "120"
        }
      }
    ],
    "loadBalancingSettings": [
      {
        "name": "loadBalancingSettings1",
        "properties": {
          "sample_size": "4",
          "successful_samples_required": "2"
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
              "http_port": "80",
              "https_port": "443",
              "weight": "1",
              "priority": "2"
            },
            {
              "address": "contoso.com.website-us-west-2.othercloud.net",
              "http_port": "80",
              "https_port": "443",
              "weight": "2",
              "priority": "1"
            },
            {
              "address": "contoso1.azurewebsites.net",
              "http_port": "80",
              "https_port": "443",
              "weight": "1",
              "priority": "1"
            }
          ],
          "load_balancing_settings": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/loadBalancingSettings/" + LOAD_BALANCING_SETTING_NAME + ""
          },
          "health_probe_settings": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoors/" + FRONT_DOOR_NAME + "/healthProbeSettings/" + HEALTH_PROBE_SETTING_NAME + ""
          }
        }
      }
    ],
    "frontendEndpoints": [
      {
        "name": "frontendEndpoint1",
        "properties": {
          "host_name": "www.contoso.com",
          "session_affinity_enabled_state": "Enabled",
          "session_affinity_ttl_seconds": "60",
          "web_application_firewall_policy_link": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/frontDoorWebApplicationFirewallPolicies/" + FRONT_DOOR_WEB_APPLICATION_FIREWALL_POLICY_NAME + ""
          }
        }
      },
      {
        "name": "default",
        "properties": {
          "host_name": "frontDoor1.azurefd.net"
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