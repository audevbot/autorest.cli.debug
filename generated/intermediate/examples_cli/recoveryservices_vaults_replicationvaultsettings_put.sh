# Updates vault setting. A vault setting object is a singleton per vault and it is always present by default.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_VAULT_SETTING_NAME="myreplicationvaultsetting"
MIGRATE_PROJECT_NAME="mymigrateproject"
SOLUTION_NAME="mysolution"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationVaultSettings/$REPLICATION_VAULT_SETTING_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "migrationSolutionId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Migrate/MigrateProjects/" + MIGRATE_PROJECT_NAME + "/Solutions/" + SOLUTION_NAME + ""
  }
}
'