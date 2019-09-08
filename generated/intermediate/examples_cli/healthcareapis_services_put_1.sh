# Create or Update a service with minimum parameters
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.HealthcareApis/services/$SERVICE_NAME?api-version=2019-09-16 --body '
{
  "location": "westus2",
  "tags": {},
  "kind": "fhir-R4",
  "properties": {
    "accessPolicies": [
      {
        "objectId": "c487e7d1-3210-41a3-8ccc-e9372b78da47"
      }
    ]
  }
}
'