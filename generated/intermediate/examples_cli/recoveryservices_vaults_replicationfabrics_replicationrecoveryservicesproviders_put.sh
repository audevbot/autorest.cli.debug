# Adds a recovery services provider.
SUBSCRIPTION_NAME="mysubscription"
RESOURCE_GROUP="myresourcegroup"
VAULT_NAME="myvault"
REPLICATION_FABRIC_NAME="myreplicationfabric"
REPLICATION_RECOVERY_SERVICES_PROVIDER_NAME="myreplicationrecoveryservicesprovider"

az resource create --id /Subscriptions/$SUBSCRIPTION_NAME/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/vaults/$VAULT_NAME/replicationFabrics/$REPLICATION_FABRIC_NAME/replicationRecoveryServicesProviders/$REPLICATION_RECOVERY_SERVICES_PROVIDER_NAME --api-version 2018-07-10 --is-full-object --properties '
{
  "properties": {
    "machineName": "vmwareprovider1",
    "authenticationIdentityInput": {
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "applicationId": "f66fce08-c0c6-47a1-beeb-0ede5ea94f90",
      "objectId": "141360b8-5686-4240-a027-5e24e6affeba",
      "audience": "https://microsoft.onmicrosoft.com/cf19e349-644c-4c6a-bcae-9c8f35357874",
      "aadAuthority": "https://login.microsoftonline.com"
    },
    "resourceAccessIdentityInput": {
      "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "applicationId": "f66fce08-c0c6-47a1-beeb-0ede5ea94f90",
      "objectId": "141360b8-5686-4240-a027-5e24e6affeba",
      "audience": "https://microsoft.onmicrosoft.com/cf19e349-644c-4c6a-bcae-9c8f35357874",
      "aadAuthority": "https://login.microsoftonline.com"
    }
  }
}
'