# EventSubscriptions_CreateOrUpdateForCustomTopic_WebhookDestination
EVENT_SUBSCRIPTION_NAME="myeventsubscription"
RESOURCE_GROUP="myresourcegroup"
STORAGE_ACCOUNT_NAME="mystorageaccount"

az rest --method put --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "destination": {
      "endpointType": "WebHook",
      "properties": {
        "endpointUrl": "https://contosofunction.azurewebsites.net/api/HttpTriggerCSharp1?code=<HIDDEN>"
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