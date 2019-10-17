# ApiManagementCreateServiceHavingMsi
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "publisherEmail": "apim@autorestsdk.com",
    "publisherName": "autorestsdk"
  },
  "sku": {
    "name": "Consumption"
  },
  "identity": {
    "type": "SystemAssigned"
  },
  "location": "West US",
  "tags": {
    "tag1": "value1",
    "tag2": "value2",
    "tag3": "value3"
  }
}
'