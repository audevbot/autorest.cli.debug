# Gets an email notification(alert) configuration.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_ALERT_SETTING_NAME="myreplicationalertsetting"

az resource show --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationAlertSettings/$REPLICATION_ALERT_SETTING_NAME --api-version 2018-07-10