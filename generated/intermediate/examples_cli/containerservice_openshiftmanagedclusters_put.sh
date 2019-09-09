# Create/Update OpenShift Managed Cluster
RESOURCE_GROUP="myresourcegroup"
OPEN_SHIFT_MANAGED_CLUSTER_NAME="myopenshiftmanagedcluster"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.ContainerService/openShiftManagedClusters/$OPEN_SHIFT_MANAGED_CLUSTER_NAME?api-version=2019-04-30 --body '
{
  "location": "location1",
  "tags": {
    "tier": "production",
    "archv2": ""
  },
  "properties": {
    "openShiftVersion": "v3.11",
    "networkProfile": {
      "vnetCidr": "10.0.0.0/8"
    },
    "masterPoolProfile": {
      "name": "master",
      "count": "3",
      "vmSize": "Standard_D4s_v3",
      "osType": "Linux",
      "subnetCidr": "10.0.0.0/24"
    },
    "agentPoolProfiles": [
      {
        "name": "infra",
        "role": "infra",
        "count": "2",
        "vmSize": "Standard_D4s_v3",
        "osType": "Linux",
        "subnetCidr": "10.0.0.0/24"
      },
      {
        "name": "compute",
        "role": "compute",
        "count": "4",
        "vmSize": "Standard_D4s_v3",
        "osType": "Linux",
        "subnetCidr": "10.0.0.0/24"
      }
    ],
    "routerProfiles": [
      {
        "name": "default"
      }
    ],
    "authProfile": {
      "identityProviders": [
        {
          "name": "Azure AD",
          "provider": {
            "kind": "AADIdentityProvider",
            "clientId": "clientId",
            "secret": "secret",
            "tenantId": "tenantId",
            "customerAdminGroupId": "customerAdminGroupId"
          }
        }
      ]
    }
  }
}
'