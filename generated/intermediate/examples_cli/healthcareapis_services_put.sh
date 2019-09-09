# Create or Update a service with all parameters
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
      },
      {
        "objectId": "5b307da8-43d4-492b-8b66-b0294ade872f"
      }
    ],
    "cosmosDbConfiguration": {
      "offerThroughput": "1000"
    },
    "authenticationConfiguration": {
      "authority": "https://login.microsoftonline.com/common",
      "audience": "https://azurehealthcareapis.com",
      "smartProxyEnabled": True
    },
    "corsConfiguration": {
      "origins": [
        "*"
      ],
      "headers": [
        "*"
      ],
      "methods": [
        "DELETE",
        "GET",
        "OPTIONS",
        "PATCH",
        "POST",
        "PUT"
      ],
      "maxAge": "1440",
      "allowCredentials": False
    }
  }
}
'