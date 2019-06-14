# ApiManagementCreateMultiRegionServiceWithCustomHostname
RESOURCE_GROUP="myresourcegroup"
SERVICE_NAME="myservice"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ApiManagement/service/$SERVICE_NAME --api-version 2019-01-01 --is-full-object --properties '
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
        "virtualNetworkConfiguration": {
          "subnetResourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
        }
      }
    ],
    "hostnameConfigurations": [
      {
        "type": "Proxy",
        "hostName": "proxyhostname1.contoso.com",
        "encodedCertificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificatePassword": "**************Password of the Certificate************************************************"
      },
      {
        "type": "Proxy",
        "hostName": "proxyhostname2.contoso.com",
        "encodedCertificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificatePassword": "**************Password of the Certificate************************************************",
        "negotiateClientCertificate": True
      },
      {
        "type": "Portal",
        "hostName": "portalhostname1.contoso.com",
        "encodedCertificate": "************Base 64 Encoded Pfx Certificate************************",
        "certificatePassword": "**************Password of the Certificate************************************************"
      }
    ],
    "virtualNetworkConfiguration": {
      "subnetResourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
    },
    "virtualNetworkType": "External"
  }
}
'