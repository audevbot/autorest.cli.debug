# ApiManagementCreateSubscription
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
USER_NAME="myuser"
PRODUCT_NAME="myproduct"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/subscriptions/$SUBSCRIPTION_ID --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "ownerId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/users/" + USER_NAME + "",
    "scope": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ApiManagement/service/" + SERVICE_NAME + "/products/" + PRODUCT_NAME + "",
    "displayName": "testsub"
  }
}
'