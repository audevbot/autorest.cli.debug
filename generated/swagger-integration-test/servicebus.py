# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import time
import mock
import unittest

from azure_devtools.scenario_tests.const import MOCKED_SUBSCRIPTION_ID
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, LiveScenarioTest, ResourceGroupPreparer, create_random_name, live_only, record_only
from azure.cli.core.util import get_file_json


class ResourceGroupScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_rg_scenario')
    def test_resource_group(self, resource_group):

        self.cmd('group create -n {rg} -l westus --tag a=b c', checks=[
            self.check('name', '{rg}'),
            self.check('tags', {'a': 'b', 'c': ''})
        ])

        self.kwargs['sub'] = self.get_subscription_id()
        self.kwargs['name'] = 'zimsxyzname'

        # OperationsList
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.ServiceBus/operations?api-version=2016-07-01 '
                 , checks=[
                          ])

        # NameSpaceCheckNameAvailability
        body = (
                 '{'
                 '  "name": "sdk-Namespace-2924"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/CheckNameAvailability?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/namespaces?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceListByResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceCreate
        body = (
                 '{'
                 '  "sku": {'
                 '    "name": "Standard",'
                 '    "tier": "Standard"'
                 '  },'
                 '  "location": "South Central US",'
                 '  "tags": {'
                 '    "tag1": "value1",'
                 '    "tag2": "value2"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceUpdate
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleListAll
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "rights": ['
                 '      "Listen",'
                 '      "Send"'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleListKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}/listKeys?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleRegenerateKey
        body = (
                 '{'
                 '  "keyType": "PrimaryKey"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}/regenerateKeys?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceUpdate
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # NameSpaceNetworkRuleSetCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "defaultAction": "Deny",'
                 '    "virtualNetworkRules": ['
                 '      {'
                 '        "subnet": {'
                 '          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""'
                 '        },'
                 '        "ignoreMissingVnetServiceEndpoint": True'
                 '      },'
                 '      {'
                 '        "subnet": {'
                 '          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""'
                 '        },'
                 '        "ignoreMissingVnetServiceEndpoint": False'
                 '      },'
                 '      {'
                 '        "subnet": {'
                 '          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + ""'
                 '        },'
                 '        "ignoreMissingVnetServiceEndpoint": False'
                 '      }'
                 '    ],'
                 '    "ipRules": ['
                 '      {'
                 '        "ipMask": "1.1.1.1",'
                 '        "action": "Allow"'
                 '      },'
                 '      {'
                 '        "ipMask": "1.1.1.2",'
                 '        "action": "Allow"'
                 '      },'
                 '      {'
                 '        "ipMask": "1.1.1.3",'
                 '        "action": "Allow"'
                 '      },'
                 '      {'
                 '        "ipMask": "1.1.1.4",'
                 '        "action": "Allow"'
                 '      },'
                 '      {'
                 '        "ipMask": "1.1.1.5",'
                 '        "action": "Allow"'
                 '      }'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/networkRuleSets/{NETWORK_RULE_SET_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceNetworkRuleSetGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/networkRuleSets/{NETWORK_RULE_SET_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # AliasNameAvailability
        body = (
                 '{'
                 '  "name": "sdk-DisasterRecovery-9474"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # SBAliasList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs?api-version=2017-04-01 '
                 , checks=[
                          ])

        # SBAliasCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "partnerNamespace": "sdk-Namespace-37",'
                 '    "alternateName": "alternameforAlias-Namespace-8860"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # SBAliasDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # SBAliasGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # SBEHAliasBreakPairing
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/breakPairing?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # SBAliasFailOver
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/failover?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # NameSpaceAuthorizationRuleListAll
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # DisasterRecoveryConfigsAuthorizationRuleGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # DisasterRecoveryConfigsAuthorizationRuleListKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}/listKeys?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # MigrationConfigurationsList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations?api-version=2017-04-01 '
                 , checks=[
                          ])

        # MigrationConfigurationsStartMigration
        body = (
                 '{'
                 '  "properties": {'
                 '    "targetNamespace": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.ServiceBus/namespaces/" + NAMESPACE_NAME + "",'
                 '    "postMigrationName": "sdk-PostMigration-5919"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # MigrationConfigurationsDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # MigrationConfigurationsGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # MigrationConfigurationsCompleteMigration
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}/upgrade?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # MigrationConfigurationsRevert
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}/revert?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # QueueListByNameSpace
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues?api-version=2017-04-01 '
                 , checks=[
                          ])

        # QueueCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "enablePartitioning": True'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # QueueDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # QueueGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # QueueAuthorizationRuleListAll
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # QueueAuthorizationRuleCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "rights": ['
                 '      "Listen",'
                 '      "Send"'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # QueueAuthorizationRuleDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2015-08-01 '
                 , checks=[
                          ])

        # QueueAuthorizationRuleGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # QueueAuthorizationRuleListKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}/ListKeys?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # QueueAuthorizationRuleRegenerateKey
        body = (
                 '{'
                 '  "keyType": "PrimaryKey"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}/regenerateKeys?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # TopicGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics?api-version=2017-04-01 '
                 , checks=[
                          ])

        # TopicCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "enableExpress": True'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # TopicDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # TopicGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics?api-version=2017-04-01 '
                 , checks=[
                          ])

        # TopicAuthorizationRuleListAll
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # TopicAuthorizationRuleCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "rights": ['
                 '      "Listen",'
                 '      "Send"'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # TopicAuthorizationRuleGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # TopicAuthorizationRuleDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # TopicAuthorizationRuleListKey
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}/ListKeys?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # TopicAuthorizationRuleRegenerateKey
        body = (
                 '{'
                 '  "keyType": "PrimaryKey"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}/regenerateKeys?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # SubscriptionListByTopic
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # SubscriptionCreate
        body = (
                 '{'
                 '  "properties": {'
                 '    "enableBatchedOperations": True'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # SubscriptionDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # SubscriptionGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # RulesListBySubscriptions
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # RulesCreateOrUpdate
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # RulesCreateSqlFilter
        body = (
                 '{'
                 '  "properties": {'
                 '    "filterType": "SqlFilter",'
                 '    "sqlFilter": {'
                 '      "sqlExpression": "myproperty=test"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # RulesCreateCorrelationFilter
        body = (
                 '{'
                 '  "properties": {'
                 '    "filterType": "CorrelationFilter",'
                 '    "correlationFilter": {'
                 '      "properties": {'
                 '        "topicHint": "Crop"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # RulesDelete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # RulesGet
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # RegionsListBySku
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/sku/{SKU_NAME}/regions?api-version=2017-04-01 '
                 , checks=[
                          ])

        # PremiumMessagingRegionsList
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/premiumMessagingRegions?api-version=2017-04-01 '
                 , checks=[
                          ])

        # RulesCreateOrUpdate
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])