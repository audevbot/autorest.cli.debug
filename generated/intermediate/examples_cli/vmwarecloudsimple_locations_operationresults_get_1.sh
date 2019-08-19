# GetOperationResult
LOCATION_NAME="mylocation"
OPERATION_RESULT_NAME="myoperationresult"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.VMwareCloudSimple/locations/$LOCATION_NAME/operationResults/$OPERATION_RESULT_NAME --api-version 2019-04-01