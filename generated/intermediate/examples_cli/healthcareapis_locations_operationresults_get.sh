# Get operation result
LOCATION_NAME="mylocation"
OPERATIONRESULT_NAME="myoperationresult"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.HealthcareApis/locations/$LOCATION_NAME/operationresults/$OPERATIONRESULT_NAME?api-version=2019-09-16