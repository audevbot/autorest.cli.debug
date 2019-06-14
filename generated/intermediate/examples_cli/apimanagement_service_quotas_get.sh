# ApiManagementGetQuotaCounterKeys
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
QUOTA_NAME="myquota"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/quotas/$QUOTA_NAME --api-version 2019-01-01