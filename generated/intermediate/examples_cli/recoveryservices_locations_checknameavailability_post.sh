# Availability status of Resource Name when no resource with same name, type and subscription exists, nor has been deleted within last 24 hours
RESOURCE_GROUP="myresourcegroup"
LOCATION_NAME="mylocation"

az rest --method post --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.RecoveryServices/locations/$LOCATION_NAME/checkNameAvailability?api-version=2016-06-01 --body '
{
  "name": "swaggerExample",
  "type": "Microsoft.RecoveryServices/Vaults"
}
'