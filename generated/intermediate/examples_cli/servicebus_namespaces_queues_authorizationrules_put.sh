# QueueAuthorizationRuleCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
QUEUE_NAME="myqueue"
AUTHORIZATION_RULE_NAME="myauthorizationrule"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/queues/$QUEUE_NAME/authorizationRules/$AUTHORIZATION_RULE_NAME --api-version 2017-04-01 --is-full-object --properties '
{
  "properties": {
    "rights": [
      "Listen",
      "Send"
    ]
  }
}
'