# ApiManagementCreateBackendServiceFabric
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
BACKEND_NAME="mybackend"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME/backends/$BACKEND_NAME?api-version=2019-01-01 --body '
{
  "properties": {
    "description": "Service Fabric Test App 1",
    "protocol": "http",
    "url": "fabric:/mytestapp/mytestservice",
    "properties": {
      "serviceFabricCluster": {
        "managementEndpoints": [
          "https://somecluster.com"
        ],
        "clientCertificatethumbprint": "EBA029198AA3E76EF0D70482626E5BCF148594A6",
        "serverX509Names": [
          {
            "name": "ServerCommonName1",
            "issuerCertificateThumbprint": "IssuerCertificateThumbprint1"
          }
        ],
        "maxPartitionResolutionRetries": "5"
      }
    }
  }
}
'