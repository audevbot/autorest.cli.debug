# ApiManagementCreateGroup
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
GROUP_NAME="mygroup"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/groups/$GROUP_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "displayName": "temp group"
  }
}
'