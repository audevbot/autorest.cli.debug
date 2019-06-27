# Gets the requested recovery plan.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_RECOVERY_PLAN_NAME="myreplicationrecoveryplan"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationRecoveryPlans/$REPLICATION_RECOVERY_PLAN_NAME --api-version 2018-07-10