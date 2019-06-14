# ApiManagementCreateUser
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
USER_NAME="myuser"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/users/$USER_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "firstName": "foo",
    "lastName": "bar",
    "email": "foobar@outlook.com",
    "confirmation": "signup"
  }
}
'