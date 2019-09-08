# Creates or updates a WAF policy within a resource group
RESOURCE_GROUP="myresourcegroup"
APPLICATION_GATEWAY_WEB_APPLICATION_FIREWALL_POLICY_NAME="myapplicationgatewaywebapplicationfirewallpolicy"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/ApplicationGatewayWebApplicationFirewallPolicies/$APPLICATION_GATEWAY_WEB_APPLICATION_FIREWALL_POLICY_NAME?api-version=2019-06-01 --body '
{
  "location": "WestUs",
  "properties": {
    "customRules": [
      {
        "name": "Rule1",
        "priority": "1",
        "ruleType": "MatchRule",
        "action": "Block",
        "matchConditions": [
          {
            "matchVariables": [
              {
                "variableName": "RemoteAddr",
                "selector": null
              }
            ],
            "operator": "IPMatch",
            "matchValues": [
              "192.168.1.0/24",
              "10.0.0.0/24"
            ]
          }
        ]
      },
      {
        "name": "Rule2",
        "priority": "2",
        "ruleType": "MatchRule",
        "matchConditions": [
          {
            "matchVariables": [
              {
                "variableName": "RemoteAddr",
                "selector": null
              }
            ],
            "operator": "IPMatch",
            "matchValues": [
              "192.168.1.0/24"
            ]
          },
          {
            "matchVariables": [
              {
                "variableName": "RequestHeaders",
                "selector": "UserAgent"
              }
            ],
            "operator": "Contains",
            "matchValues": [
              "Windows"
            ]
          }
        ],
        "action": "Block"
      }
    ]
  }
}
'