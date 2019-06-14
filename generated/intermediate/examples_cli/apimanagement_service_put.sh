# ApiManagementCreateService
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME --api-version 2019-01-01 --is-full-object --properties '
{
  "properties": {
    "publisherEmail": "apim@autorestsdk.com",
    "publisherName": "autorestsdk"
  },
  "sku": {
    "name": "Developer",
    "capacity": "1"
  },
  "location": "Central US",
  "tags": {
    "tag1": "value1",
    "tag2": "value2",
    "tag3": "value3"
  }
}
'