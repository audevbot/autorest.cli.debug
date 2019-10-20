# Topics_CreateOrUpdate
RESOURCE_GROUP="myresourcegroup"
TOPIC_NAME="mytopic"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/topics/$TOPIC_NAME?api-version=2019-01-01 --body '
{
  "location": "westus2",
  "tags": {
    "tag1": "value1",
    "tag2": "value2"
  }
}
'