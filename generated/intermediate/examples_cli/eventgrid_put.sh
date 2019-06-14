# EventSubscriptions_CreateOrUpdateForSubscription
{SCOPE}_NAME="myscope"
MICROSOFT.EVENT_GRID_NAME="mymicrosofteventgrid"

az resource create --id /{scope}/${SCOPE}_NAME/Microsoft.EventGrid/$MICROSOFT.EVENT_GRID_NAME/{eventSubscriptionName} --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "destination": {
      "endpointType": "WebHook",
      "properties": {
        "endpointUrl": "https://requestb.in/15ksip71"
      }
    },
    "filter": {
      "isSubjectCaseSensitive": False
    }
  }
}
'