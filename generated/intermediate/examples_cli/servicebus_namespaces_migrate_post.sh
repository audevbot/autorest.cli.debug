# NameSpaceUpdate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/migrate?api-version=2017-04-01 --body '
{
  "targetNamespaceType": "EventHub"
}
'