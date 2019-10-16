# ApiManagementCreateBackendProxyBackend
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
BACKEND_NAME="mybackend"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/backends/$BACKEND_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "description": "description5308",
    "url": "https://backendname2644/",
    "protocol": "http",
    "tls": {
      "validateCertificateChain": True,
      "validateCertificateName": True
    },
    "proxy": {
      "url": "http://192.168.1.1:8080",
      "username": "Contoso\\admin",
      "password": "opensesame"
    },
    "credentials": {
      "query": {
        "sv": [
          "xx",
          "bb",
          "cc"
        ]
      },
      "header": {
        "x-my-1": [
          "val1",
          "val2"
        ]
      },
      "authorization": {
        "scheme": "Basic",
        "parameter": "opensesma"
      }
    }
  }
}
'