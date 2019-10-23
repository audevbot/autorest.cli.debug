# RulesCreateOrUpdate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
TOPIC_NAME="mytopic"
RULE_NAME="myrule"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/topics/$TOPIC_NAME/subscriptions/$SUBSCRIPTION_ID/rules/$RULE_NAME?api-version=2017-04-01 --body '
{}
'