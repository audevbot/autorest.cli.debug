# NameSpaceCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME --api-version 2017-04-01 --is-full-object --properties '
{
  "sku": {
    "name": "Standard",
    "tier": "Standard"
  },
  "location": "South Central US",
  "tags": {
    "tag1": "value1",
    "tag2": "value2"
  }
}
'