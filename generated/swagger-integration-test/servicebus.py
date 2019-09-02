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

        # servicebus_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.ServiceBus/operations?api-version=2016-07-01 '
                 , checks=[
                          ])

        # servicebus_checknameavailability_post
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

        # servicebus_namespaces_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/namespaces?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_put
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

        # servicebus_namespaces_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_authorizationrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_authorizationrules_put
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

        # servicebus_namespaces_authorizationrules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_authorizationrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_authorizationrules_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}/listKeys?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_authorizationrules_regeneratekeys_post
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

        # servicebus_namespaces_migrate_post
        body = (
                 '{'
                 '  "targetNamespaceType": "EventHub"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrate?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_networkrulesets_put
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

        # servicebus_namespaces_networkrulesets_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/networkRuleSets/{NETWORK_RULE_SET_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_post
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

        # servicebus_namespaces_disasterrecoveryconfigs_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_put
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

        # servicebus_namespaces_disasterrecoveryconfigs_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_breakpairing_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/breakPairing?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_failover_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/failover?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_authorizationrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/AuthorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_authorizationrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_disasterrecoveryconfigs_authorizationrules_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/disasterRecoveryConfigs/{DISASTER_RECOVERY_CONFIG_NAME}/AuthorizationRules/{AUTHORIZATION_RULE_NAME}/listKeys?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_migrationconfigurations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_migrationconfigurations_put
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

        # servicebus_namespaces_migrationconfigurations_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_migrationconfigurations_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_migrationconfigurations_upgrade_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}/upgrade?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_migrationconfigurations_revert_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/migrationConfigurations/{MIGRATION_CONFIGURATION_NAME}/revert?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_queues_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_queues_put
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

        # servicebus_namespaces_queues_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_queues_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_queues_authorizationrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_queues_authorizationrules_put
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

        # servicebus_namespaces_queues_authorizationrules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2015-08-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_queues_authorizationrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_queues_authorizationrules_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/queues/{QUEUE_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}/ListKeys?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_queues_authorizationrules_regeneratekeys_post
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

        # servicebus_namespaces_topics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_put
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

        # servicebus_namespaces_topics_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_authorizationrules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_authorizationrules_put
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

        # servicebus_namespaces_topics_authorizationrules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_authorizationrules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_authorizationrules_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/authorizationRules/{AUTHORIZATION_RULE_NAME}/ListKeys?api-version=2015-08-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_topics_authorizationrules_regeneratekeys_post
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

        # servicebus_namespaces_topics_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_put_1
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

        # servicebus_namespaces_topics_delete_1
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_rules_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_rules_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # servicebus_namespaces_topics_rules_put_1
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

        # servicebus_namespaces_topics_rules_put_2
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

        # servicebus_namespaces_topics_rules_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_topics_rules_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/topics/{TOPIC_NAME}/subscriptions/{sub}/rules/{RULE_NAME}?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_sku_regions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/sku/{SKU_NAME}/regions?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_premiummessagingregions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.ServiceBus/premiumMessagingRegions?api-version=2017-04-01 '
                 , checks=[
                          ])

        # servicebus_namespaces_eventhubs_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.ServiceBus/namespaces/{NAMESPACE_NAME}/eventhubs?api-version=2017-04-01 '
                 , checks=[
                          ])