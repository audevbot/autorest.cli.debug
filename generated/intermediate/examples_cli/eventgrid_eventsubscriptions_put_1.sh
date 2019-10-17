# EventSubscriptions_CreateOrUpdateForResourceGroup
EVENT_SUBSCRIPTION_NAME="myeventsubscription"

az rest --method put --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "destination": {
      "endpointType": "WebHook",
      "properties": {
        "endpointUrl": "https://requestb.in/15ksip71"
      }
    },
    "filter": {
      "isSubjectCaseSensitive": False,
      "subjectBeginsWith": "ExamplePrefix",
      "subjectEndsWith": "ExampleSuffix"
    }
  }
}
'