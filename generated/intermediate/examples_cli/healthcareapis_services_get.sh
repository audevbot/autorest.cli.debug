# Get metadata
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az resource show --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.HealthcareApis/services/$SERVICE_NAME --api-version 2019-09-16