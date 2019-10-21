# TopicAuthorizationRuleCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
TOPIC_NAME="mytopic"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/topics/$TOPIC_NAME/authorizationRules/$AUTHORIZATION_RULE_NAME?api-version=2017-04-01 --body '
{
  "properties": {
    "rights": [
      "Listen",
      "Send"
    ]
  }
}
'