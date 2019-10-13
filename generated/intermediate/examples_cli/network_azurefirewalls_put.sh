# Create Azure Firewall
RESOURCE_GROUP="myresourcegroup"
AZURE_FIREWALL_NAME="myazurefirewall"
VIRTUAL_NETWORK_NAME="myvirtualnetwork"
SUBNET_NAME="mysubnet"
PUBLIC_IP_ADDRESS_NAME="mypublicipaddress"

az rest --method put --uri /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Network/azureFirewalls/$AZURE_FIREWALL_NAME?api-version=2018-11-01 --body '
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
          "public_ip_address": {
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
                  "protocol_type": "Https",
                  "port": "443"
                }
              ],
              "target_fqdns": [
                "www.test.com"
              ],
              "source_addresses": [
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
              "source_addresses": [
                "*"
              ],
              "destination_addresses": [
                "1.2.3.4"
              ],
              "destination_ports": [
                "443"
              ],
              "protocols": [
                "TCP"
              ],
              "translated_address": "1.2.3.5",
              "translated_port": "8443"
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
              "source_addresses": [
                "192.168.1.1-192.168.1.12",
                "10.1.4.12-10.1.4.255"
              ],
              "destination_ports": [
                "443-444",
                "8443"
              ],
              "destination_addresses": [
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