# EventSubscriptions_CreateOrUpdateForCustomTopic_HybridConnectionDestination
{SCOPE}_NAME="myscope"
MICROSOFT.EVENT_GRID_NAME="mymicrosofteventgrid"
RESOURCE_GROUP="myresourcegroup"
NAMESPACE_NAME="my"
HYBRID_CONNECTION_NAME="myhybridconnection"
STORAGE_ACCOUNT_NAME="mystorageaccount"

az rest --method put --uri /{scope}/${SCOPE}_NAME/Microsoft.EventGrid/$MICROSOFT.EVENT_GRID_NAME/{eventSubscriptionName}?api-version=2019-01-01 --body '
{
  "properties": {
    "destination": {
      "endpointType": "HybridConnection",
      "properties": {
        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Relay/namespaces/" + NAMESPACE_NAME + "/hybridConnections/" + HYBRID_CONNECTION_NAME + ""
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