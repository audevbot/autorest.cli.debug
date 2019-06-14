# ApiManagementCreateOpenIdConnectProvider
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
OPENID_CONNECT_PROVIDER_NAME="myopenidconnectprovider"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/openidConnectProviders/$OPENID_CONNECT_PROVIDER_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "displayName": "templateoidprovider3",
    "metadataEndpoint": "https://oidprovider-template3.net",
    "clientId": "oidprovidertemplate3"
  }
}
'