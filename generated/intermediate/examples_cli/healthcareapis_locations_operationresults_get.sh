# OperationResultsGet
LOCATION_NAME="mylocation"
OPERATIONRESULT_NAME="myoperationresult"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.HealthcareApis/locations/$LOCATION_NAME/operationresults/$OPERATIONRESULT_NAME --api-version 2018-08-20-preview