# GetFailedOperationResult
LOCATION_NAME="mylocation"
OPERATION_RESULT_NAME="myoperationresult"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/operationResults/$OPERATION_RESULT_NAME?api-version=2019-04-01