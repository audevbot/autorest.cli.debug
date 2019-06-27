# Add vCenter.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATIONV_CENTER_NAME="myreplicationvcenter"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationvCenters/$REPLICATIONV_CENTER_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "friendlyName": "esx-78",
    "ipAddress": "inmtest78",
    "processServerId": "5A720CAB-39CB-F445-BD1662B0B33164B5",
    "port": "443",
    "runAsAccountId": "2"
  }
}
'