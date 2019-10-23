# ApiManagementCreateServiceWithSystemCertificates
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "certificates": [
      {
        "encoded_certificate": "*******Base64 encoded Certificate******************",
        "certificate_password": "Password",
        "store_name": "CertificateAuthority"
      }
    ],
    "publisherEmail": "apim@autorestsdk.com",
    "publisherName": "autorestsdk"
  },
  "sku": {
    "name": "Basic",
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