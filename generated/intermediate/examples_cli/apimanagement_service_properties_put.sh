# ApiManagementCreateProperty
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
PROPERTY_NAME="myproperty"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/properties/$PROPERTY_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "displayName": "prop3name",
    "value": "propValue",
    "tags": [
      "foo",
      "bar"
    ],
    "secret": True
  }
}
'