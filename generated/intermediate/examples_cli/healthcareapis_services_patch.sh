# Patch service
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method patch --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.HealthcareApis/services/$SERVICE_NAME?api-version=2019-09-16