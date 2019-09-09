# Create or update specific HealthProbeSettings
RESOURCE_GROUP="myresourcegroup"
FRONT_DOOR_NAME="myfrontdoor"
HEALTH_PROBE_SETTING_NAME="myhealthprobesetting"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/frontDoors/$FRONT_DOOR_NAME/healthProbeSettings/$HEALTH_PROBE_SETTING_NAME?api-version=2019-04-01 --body '
{
  "name": "healthProbeSettings1",
  "properties": {
    "path": "/",
    "protocol": "Http",
    "intervalInSeconds": "120"
  }
}
'