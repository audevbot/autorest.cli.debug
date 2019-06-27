# Creates a recovery plan with the given details.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_RECOVERY_PLAN_NAME="myreplicationrecoveryplan"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationRecoveryPlans/$REPLICATION_RECOVERY_PLAN_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "primaryFabricId": "/Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1",
    "recoveryFabricId": "Microsoft Azure",
    "failoverDeploymentModel": "ResourceManager",
    "groups": [
      {
        "groupType": "Boot",
        "replicationProtectedItems": [
          {
            "id": "/Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1/replicationProtectionContainers/cloud_6d224fc6-f326-5d35-96de-fbf51efb3179/replicationProtectedItems/f8491e4f-817a-40dd-a90c-af773978c75b",
            "virtualMachineId": "f8491e4f-817a-40dd-a90c-af773978c75b"
          }
        ],
        "startGroupActions": [],
        "endGroupActions": []
      }
    ]
  }
}
'