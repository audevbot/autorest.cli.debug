# LocationGetQuotas
LOCATION_NAME="mylocation"

az rest --method get --uri /subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Batch/locations/$LOCATION_NAME/quotas?api-version=2018-12-01