# ApiManagementCreateMultiRegionServiceWithCustomHostname
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME?api-version=2019-01-01 --body '
{
  "location": "Central US",
  "sku": {
    "name": "Premium",
    "capacity": "1"
  },
  "properties": {
    "publisherEmail": "admin@live.com",
    "publisherName": "contoso",
    "additionalLocations": [
      {
        "location": "North Europe",
        "sku": {
          "name": "Premium",
          "capacity": "1"
        },
        "virtual_network_configuration": {
          "subnet_resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        }
      }
    ],
    "hostnameConfigurations": [
      {
        "type": "Proxy",
        "host_name": "proxyhostname1.contoso.com",
        "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificate_password": "**************Password of the Certificate************************************************"
      },
      {
        "type": "Proxy",
        "host_name": "proxyhostname2.contoso.com",
        "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificate_password": "**************Password of the Certificate************************************************",
        "negotiate_client_certificate": True
      },
      {
        "type": "Portal",
        "host_name": "portalhostname1.contoso.com",
        "encoded_certificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificate_password": "**************Password of the Certificate************************************************"
      }
    ],
    "virtualNetworkConfiguration": {
      "subnetResourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
    },
    "virtualNetworkType": "External"
  }
}
'