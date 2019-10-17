# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

BODY = {}
        output = mgmt_client.operations.list(, BODY)
BODY = {
  "name": "sdk-Namespace-2924"
}
        output = mgmt_client.namespaces.check_name_availability_method(, BODY)
BODY = {}
        output = mgmt_client.namespaces.list(, BODY)
BODY = {}
        output = mgmt_client.namespaces.list_by_resource_group(RESOURCE_GROUP, , BODY)
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
        output = mgmt_client.namespaces.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.delete(RESOURCE_GROUP, NAMESPACE_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.get(RESOURCE_GROUP, NAMESPACE_NAME, BODY)
BODY = {
  "location": "South Central US",
  "tags": {
    "tag3": "value3",
    "tag4": "value4"
  }
}
        output = mgmt_client.namespaces.update(RESOURCE_GROUP, NAMESPACE_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.list_authorization_rules(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
BODY = {
  "properties": {
    "rights": [
      "Listen",
      "Send"
    ]
  }
}
        output = mgmt_client.namespaces.create_or_update_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.delete_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.get_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.list_keys(RESOURCE_GROUP, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {
  "key_type": "PrimaryKey"
}
        output = mgmt_client.namespaces.regenerate_keys(RESOURCE_GROUP, NAMESPACE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {
  "target_namespace_type": "EventHub"
}
        output = mgmt_client.namespaces.migrate(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
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
        output = mgmt_client.namespaces.create_or_update_network_rule_set(RESOURCE_GROUP, NAMESPACE_NAME, NETWORK_RULE_SET_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.get_network_rule_set(RESOURCE_GROUP, NAMESPACE_NAME, NETWORK_RULE_SET_NAME, BODY)
BODY = {}
        output = mgmt_client.namespaces.list_network_rule_sets(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
BODY = {
  "name": "sdk-DisasterRecovery-9474"
}
        output = mgmt_client.disaster_recovery_configs.check_name_availability_method(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.list(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
BODY = {
  "properties": {
    "partner_namespace": "sdk-Namespace-37",
    "alternate_name": "alternameforAlias-Namespace-8860"
  }
}
        output = mgmt_client.disaster_recovery_configs.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.delete(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.get(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.break_pairing(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, , BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.fail_over(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, , BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.list_authorization_rules(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, , BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.get_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.disaster_recovery_configs.list_keys(RESOURCE_GROUP, NAMESPACE_NAME, DISASTER_RECOVERY_CONFIG_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {}
        output = mgmt_client.migration_configs.list(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
BODY = {
  "properties": {
    "target_namespace": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ServiceBus/namespaces/" + NAMESPACE_NAME + "",
    "post_migration_name": "sdk-PostMigration-5919"
  }
}
        output = mgmt_client.migration_configs.create_and_start_migration(RESOURCE_GROUP, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, BODY)
BODY = {}
        output = mgmt_client.migration_configs.delete(RESOURCE_GROUP, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, BODY)
BODY = {}
        output = mgmt_client.migration_configs.get(RESOURCE_GROUP, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, BODY)
BODY = {}
        output = mgmt_client.migration_configs.complete_migration(RESOURCE_GROUP, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, , BODY)
BODY = {}
        output = mgmt_client.migration_configs.revert(RESOURCE_GROUP, NAMESPACE_NAME, MIGRATION_CONFIGURATION_NAME, , BODY)
BODY = {}
        output = mgmt_client.queues.list_by_namespace(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
BODY = {
  "properties": {
    "enable_partitioning": True
  }
}
        output = mgmt_client.queues.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, BODY)
BODY = {}
        output = mgmt_client.queues.delete(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, BODY)
BODY = {}
        output = mgmt_client.queues.get(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, BODY)
BODY = {}
        output = mgmt_client.queues.list_authorization_rules(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, , BODY)
BODY = {
  "properties": {
    "rights": [
      "Listen",
      "Send"
    ]
  }
}
        output = mgmt_client.queues.create_or_update_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.queues.delete_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.queues.get_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.queues.list_keys(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {
  "key_type": "PrimaryKey"
}
        output = mgmt_client.queues.regenerate_keys(RESOURCE_GROUP, NAMESPACE_NAME, QUEUE_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {}
        output = mgmt_client.topics.list_by_namespace(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)
BODY = {
  "properties": {
    "enable_express": True
  }
}
        output = mgmt_client.topics.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, BODY)
BODY = {}
        output = mgmt_client.topics.delete(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, BODY)
BODY = {}
        output = mgmt_client.topics.get(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, BODY)
BODY = {}
        output = mgmt_client.topics.list_authorization_rules(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, , BODY)
BODY = {
  "properties": {
    "rights": [
      "Listen",
      "Send"
    ]
  }
}
        output = mgmt_client.topics.create_or_update_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.topics.get_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.topics.delete_authorization_rule(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.topics.list_keys(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {
  "key_type": "PrimaryKey"
}
        output = mgmt_client.topics.regenerate_keys(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, AUTHORIZATION_RULE_NAME, , BODY)
BODY = {}
        output = mgmt_client.subscriptions.list_by_topic(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, , BODY)
BODY = {
  "properties": {
    "enable_batched_operations": True
  }
}
        output = mgmt_client.subscriptions.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, , BODY)
BODY = {}
        output = mgmt_client.subscriptions.delete(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, , BODY)
BODY = {}
        output = mgmt_client.subscriptions.get(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, , BODY)
BODY = {}
        output = mgmt_client.rules.list_by_subscriptions(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, , BODY)
BODY = {}
        output = mgmt_client.rules.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
BODY = {
  "properties": {
    "filter_type": "SqlFilter",
    "sql_filter": {
      "sql_expression": "myproperty=test"
    }
  }
}
        output = mgmt_client.rules.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
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
        output = mgmt_client.rules.create_or_update(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.rules.delete(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.rules.get(RESOURCE_GROUP, NAMESPACE_NAME, TOPIC_NAME, RULE_NAME, BODY)
BODY = {}
        output = mgmt_client.regions.list_by_sku(SKU_NAME, , BODY)
BODY = {}
        output = mgmt_client.premium_messaging_regions.list(, BODY)
BODY = {}
        output = mgmt_client.event_hubs.list_by_namespace(RESOURCE_GROUP, NAMESPACE_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()