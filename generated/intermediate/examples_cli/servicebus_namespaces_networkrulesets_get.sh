# NameSpaceNetworkRuleSetGet
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
NETWORK_RULE_SET_NAME="mynetworkruleset"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/networkRuleSets/$NETWORK_RULE_SET_NAME --api-version 2017-04-01