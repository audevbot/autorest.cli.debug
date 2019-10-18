# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.servicebus
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtServiceBusTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtServiceBusTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.servicebus.ServiceBusManagementClient
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_servicebus(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.operations.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "sdk-Namespace-2924"
        }
        azure_operation_poller = self.mgmt_client.namespaces.check_name_availability_method(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "sku": {
            "name": "Standard",
            "tier": "Standard"
          },
          "location": "South Central US",
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        azure_operation_poller = self.mgmt_client.namespaces.create_or_update(resource_group.name, NAMESPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.delete(resource_group.name, NAMESPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.get(resource_group.name, NAMESPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "South Central US",
          "tags": {
            "tag3": "value3",
            "tag4": "value4"
          }
        }
        azure_operation_poller = self.mgmt_client.namespaces.update(resource_group.name, NAMESPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.list_authorization_rules(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "rights": [
              "Listen",
              "Send"
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.namespaces.create_or_update_authorization_rule(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.delete_authorization_rule(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.get_authorization_rule(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.list_keys(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "key_type": "PrimaryKey"
        }
        azure_operation_poller = self.mgmt_client.namespaces.regenerate_keys(resource_group.name, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "South Central US",
          "tags": {
            "tag3": "value3",
            "tag4": "value4"
          }
        }
        azure_operation_poller = self.mgmt_client.namespaces.update(resource_group.name, NAMESPACE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "default_action": "Deny",
            "virtual_network_rules": [
              {
                "subnet": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                },
                "ignore_missing_vnet_service_endpoint": True
              },
              {
                "subnet": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                },
                "ignore_missing_vnet_service_endpoint": False
              },
              {
                "subnet": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""
                },
                "ignore_missing_vnet_service_endpoint": False
              }
            ],
            "ip_rules": [
              {
                "ip_mask": "1.1.1.1",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.2",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.3",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.4",
                "action": "Allow"
              },
              {
                "ip_mask": "1.1.1.5",
                "action": "Allow"
              }
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.namespaces.create_or_update_network_rule_set(resource_group.name, NAMESPACE_NAME, NETWORK_RULE_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.get_network_rule_set(resource_group.name, NAMESPACE_NAME, NETWORK_RULE_SET_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.list_network_rule_sets(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "sdk-DisasterRecovery-9474"
        }
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.check_name_availability_method(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.list(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "partner_namespace": "sdk-Namespace-37",
            "alternate_name": "alternameforAlias-Namespace-8860"
          }
        }
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.create_or_update(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.delete(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.get(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.break_pairing(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.fail_over(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.namespaces.list_authorization_rules(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.get_authorization_rule(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.disaster_recovery_configs.list_keys(resource_group.name, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.migration_configs.list(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "target_namespace": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ServiceBus/namespaces/" + NAMESPACE_NAME + "",
            "post_migration_name": "sdk-PostMigration-5919"
          }
        }
        azure_operation_poller = self.mgmt_client.migration_configs.create_and_start_migration(resource_group.name, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.migration_configs.delete(resource_group.name, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.migration_configs.get(resource_group.name, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.migration_configs.complete_migration(resource_group.name, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.migration_configs.revert(resource_group.name, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.list_by_namespace(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enable_partitioning": True
          }
        }
        azure_operation_poller = self.mgmt_client.queues.create_or_update(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.delete(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.get(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.list_authorization_rules(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "rights": [
              "Listen",
              "Send"
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.queues.create_or_update_authorization_rule(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.delete_authorization_rule(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.get_authorization_rule(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.queues.list_keys(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "key_type": "PrimaryKey"
        }
        azure_operation_poller = self.mgmt_client.queues.regenerate_keys(resource_group.name, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.list_by_namespace(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enable_express": True
          }
        }
        azure_operation_poller = self.mgmt_client.topics.create_or_update(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.delete(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.list_by_namespace(resource_group.name, NAMESPACE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.list_authorization_rules(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "rights": [
              "Listen",
              "Send"
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.topics.create_or_update_authorization_rule(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.get_authorization_rule(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.delete_authorization_rule(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.topics.list_keys(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "key_type": "PrimaryKey"
        }
        azure_operation_poller = self.mgmt_client.topics.regenerate_keys(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscriptions.list_by_topic(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "enable_batched_operations": True
          }
        }
        azure_operation_poller = self.mgmt_client.subscriptions.create_or_update(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscriptions.delete(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.subscriptions.get(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.rules.list_by_subscriptions(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.rules.create_or_update(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "filter_type": "SqlFilter",
            "sql_filter": {
              "sql_expression": "myproperty=test"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.rules.create_or_update(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "filter_type": "CorrelationFilter",
            "correlation_filter": {
              "properties": {
                "topic_hint": "Crop"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.rules.create_or_update(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.rules.delete(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.rules.get(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.regions.list_by_sku(SKU_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.premium_messaging_regions.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.rules.create_or_update(resource_group.name, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()