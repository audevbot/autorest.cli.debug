# EventSubscriptions_CreateOrUpdateForCustomTopic_EventHubDestination
{SCOPE}_NAME="myscope"
MICROSOFT.EVENT_GRID_NAME="mymicrosofteventgrid"
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
EVENTHUB_NAME="myeventhub"
STORAGE_ACCOUNT_NAME="mystorageaccount"

az resource create --id /{scope}/${SCOPE}_NAME/Microsoft.EventGrid/$MICROSOFT.EVENT_GRID_NAME/{eventSubscriptionName} --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "destination": {
      "endpointType": "EventHub",
      "properties": {
        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME + ""
      }
    },
    "filter": {
      "isSubjectCaseSensitive": False,
      "subjectBeginsWith": "ExamplePrefix",
      "subjectEndsWith": "ExampleSuffix"
    },
    "deadLetterDestination": {
      "endpointType": "StorageBlob",
      "properties": {
        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
        "blobContainerName": "contosocontainer"
      }
    }
  }
}
'