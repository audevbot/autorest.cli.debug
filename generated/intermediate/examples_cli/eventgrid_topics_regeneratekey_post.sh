# Topics_RegenerateKey
RESOURCE_GROUP="myresourcegroup"
TOPIC_NAME="mytopic"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.EventGrid/topics/$TOPIC_NAME/regenerateKey?api-version=2019-01-01 --body '
{
  "keyName": "key1"
}
'