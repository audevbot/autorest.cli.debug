# ApiManagementCreateCertificate
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
CERTIFICATE_NAME="mycertificate"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/certificates/$CERTIFICATE_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "data": "****************Base 64 Encoded Certificate *******************************",
    "password": "****Certificate Password******"
  }
}
'