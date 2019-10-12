# NameSpaceNetworkRuleSetCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
NETWORK_RULE_SET_NAME="mynetworkruleset"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/networkRuleSets/$NETWORK_RULE_SET_NAME?api-version=2017-04-01 --body '
{
  "properties": {
    "defaultAction": "Deny",
    "virtualNetworkRules": [
      {
        "subnet": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        },
        "ignore_missing_vnet_service_endpoint": True
      },
      {
        "subnet": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        },
        "ignore_missing_vnet_service_endpoint": False
      },
      {
        "subnet": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        },
        "ignore_missing_vnet_service_endpoint": False
      }
    ],
    "ipRules": [
      {
        "ip_mask": "1.1.1.1",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.2",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.3",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.4",
        "action": "Allow"
      },
      {
        "ip_mask": "1.1.1.5",
        "action": "Allow"
      }
    ]
  }
}
'