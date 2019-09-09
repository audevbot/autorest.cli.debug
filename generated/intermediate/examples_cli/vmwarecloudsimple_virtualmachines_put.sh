# CreateVirtualMachine
RESOURCE_GROUP="myresourcegroup"
VIRTUAL_MACHINE_NAME="myvirtualmachine"
LOCATION_NAME="mylocation"
PRIVATE_CLOUD_NAME="myprivatecloud"
VIRTUAL_MACHINE_TEMPLATE_NAME="myvirtualmachinetemplate"
RESOURCE_POOL_NAME="myresourcepool"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.VMwareCloudSimple/virtualMachines/$VIRTUAL_MACHINE_NAME?api-version=2019-04-01 --body '
{
  "location": "westus2",
  "properties": {
    "privateCloudId": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "",
    "templateId": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualMachineTemplates/" + VIRTUAL_MACHINE_TEMPLATE_NAME + "",
    "numberOfCores": "2",
    "amountOfRam": "4096",
    "disks": [
      {
        "controllerId": "1000",
        "independenceMode": "persistent",
        "totalSize": "10485760",
        "virtualDiskId": "2000"
      }
    ],
    "resourcePool": {
      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/resourcePools/" + RESOURCE_POOL_NAME + ""
    },
    "guestOS": "Other (32-bit)",
    "guestOSType": "other",
    "nics": [
      {
        "network": {
          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/providers/Microsoft.VMwareCloudSimple/locations/" + LOCATION_NAME + "/privateClouds/" + PRIVATE_CLOUD_NAME + "/virtualNetworks/" + VIRTUAL_NETWORK_NAME + ""
        },
        "nicType": "E1000",
        "powerOnBoot": True,
        "virtualNicId": "4000"
      }
    ]
  }
}
'