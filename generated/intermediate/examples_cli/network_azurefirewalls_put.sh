# Create Azure Firewall
RESOURCE_GROUP="myresourcegroup"
AZURE_FIREWALL_NAME="myazurefirewall"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"
PUBLIC_IP_ADDRESS_NAME="mypublicipaddress"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/azureFirewalls/$AZURE_FIREWALL_NAME --api-version 2018-11-01 --is-full-object --properties '
{
  "tags": {
    "key1": "value1"
  },
  "properties": {
    "ipConfigurations": [
      {
        "name": "azureFirewallIpConfiguration",
        "properties": {
          "subnet": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
          },
          "publicIPAddress": {
            "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/publicIPAddresses/" + PUBLIC_IP_ADDRESS_NAME + ""
          }
        }
      }
    ],
    "applicationRuleCollections": [
      {
        "name": "apprulecoll",
        "properties": {
          "priority": "110",
          "action": {
            "type": "Deny"
          },
          "rules": [
            {
              "name": "rule1",
              "description": "Deny inbound rule",
              "protocols": [
                {
                  "protocolType": "Https",
                  "port": "443"
                }
              ],
              "targetFqdns": [
                "www.test.com"
              ],
              "sourceAddresses": [
                "216.58.216.164",
                "10.0.0.0/24"
              ]
            }
          ]
        }
      }
    ],
    "natRuleCollections": [
      {
        "name": "natrulecoll",
        "properties": {
          "priority": "112",
          "action": {
            "type": "Dnat"
          },
          "rules": [
            {
              "name": "DNAT-HTTPS-traffic",
              "description": "D-NAT all outbound web traffic for inspection",
              "sourceAddresses": [
                "*"
              ],
              "destinationAddresses": [
                "1.2.3.4"
              ],
              "destinationPorts": [
                "443"
              ],
              "protocols": [
                "TCP"
              ],
              "translatedAddress": "1.2.3.5",
              "translatedPort": "8443"
            }
          ]
        }
      }
    ],
    "networkRuleCollections": [
      {
        "name": "netrulecoll",
        "properties": {
          "priority": "112",
          "action": {
            "type": "Deny"
          },
          "rules": [
            {
              "name": "L4-traffic",
              "description": "Block traffic based on source IPs and ports",
              "sourceAddresses": [
                "192.168.1.1-192.168.1.12",
                "10.1.4.12-10.1.4.255"
              ],
              "destinationPorts": [
                "443-444",
                "8443"
              ],
              "destinationAddresses": [
                "*"
              ],
              "protocols": [
                "TCP"
              ]
            }
          ]
        }
      }
    ]
  }
}
'