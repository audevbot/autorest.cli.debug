# EventSubscriptions_GetFullUrlForResourceGroup
EVENT_SUBSCRIPTION_NAME="myeventsubscription"

az rest --method post --uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/$EVENT_SUBSCRIPTION_NAME/getFullUrl?api-version=2019-01-01 --body '
{}
'