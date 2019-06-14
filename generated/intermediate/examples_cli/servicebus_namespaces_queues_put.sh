# QueueCreate
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
QUEUE_NAME="myqueue"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ServiceBus/namespaces/$NAMESPACE_NAME/queues/$QUEUE_NAME --api-version 2015-08-01 --is-full-object --properties '
{
  "properties": {
    "enablePartitioning": True
  }
}
'