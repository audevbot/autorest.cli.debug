# Creates the policy.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_POLICY_NAME="myreplicationpolicy"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationPolicies/$REPLICATION_POLICY_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "providerSpecificInput": {
      "instanceType": "HyperVReplicaAzure"
    }
  }
}
'