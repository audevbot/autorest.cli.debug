# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.servicebus._client_factory import cf_servicebus
def load_command_table(self, _):

    servicebus_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.servicebus.operations#ApiManagementOperations.{}',
        client_factory=cf_servicebus)


    with self.command_group('', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_')
    with self.command_group('servicebus', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus')
        g.custom_command('update', 'update_servicebus')
        g.custom_command('delete', 'delete_servicebus')
        g.custom_command('list', 'list_servicebus')
        g.custom_command('show', 'show_servicebus')
    with self.command_group('servicebus authorizationrule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_authorizationrule')
        g.custom_command('show', 'show_servicebus_authorizationrule')
    with self.command_group('servicebus disasterrecoveryconfig', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_disasterrecoveryconfig')
        g.custom_command('update', 'update_servicebus_disasterrecoveryconfig')
        g.custom_command('delete', 'delete_servicebus_disasterrecoveryconfig')
        g.custom_command('list', 'list_servicebus_disasterrecoveryconfig')
        g.custom_command('show', 'show_servicebus_disasterrecoveryconfig')
    with self.command_group('servicebus disasterrecoveryconfig authorizationrule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_disasterrecoveryconfig_authorizationrule')
        g.custom_command('show', 'show_servicebus_disasterrecoveryconfig_authorizationrule')
    with self.command_group('servicebus migrationconfiguration', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('show', 'show_servicebus_migrationconfiguration')
        g.custom_command('list', 'list_servicebus_migrationconfiguration')
    with self.command_group('servicebus queue', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_queue')
        g.custom_command('update', 'update_servicebus_queue')
        g.custom_command('delete', 'delete_servicebus_queue')
        g.custom_command('list', 'list_servicebus_queue')
        g.custom_command('show', 'show_servicebus_queue')
    with self.command_group('servicebus queue authorizationrule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_queue_authorizationrule')
        g.custom_command('show', 'show_servicebus_queue_authorizationrule')
    with self.command_group('servicebus topic', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_topic')
        g.custom_command('update', 'update_servicebus_topic')
        g.custom_command('delete', 'delete_servicebus_topic')
        g.custom_command('list', 'list_servicebus_topic')
        g.custom_command('show', 'show_servicebus_topic')
    with self.command_group('servicebus topic authorizationrule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_topic_authorizationrule')
        g.custom_command('show', 'show_servicebus_topic_authorizationrule')
    with self.command_group('servicebus topic subscription', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_topic_subscription')
        g.custom_command('update', 'update_servicebus_topic_subscription')
        g.custom_command('delete', 'delete_servicebus_topic_subscription')
        g.custom_command('list', 'list_servicebus_topic_subscription')
        g.custom_command('show', 'show_servicebus_topic_subscription')
    with self.command_group('servicebus topic subscription', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_topic_subscription')
        g.custom_command('show', 'show_servicebus_topic_subscription')
    with self.command_group('servicebus topic subscription rule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_topic_subscription_rule')
        g.custom_command('update', 'update_servicebus_topic_subscription_rule')
        g.custom_command('delete', 'delete_servicebus_topic_subscription_rule')
        g.custom_command('list', 'list_servicebus_topic_subscription_rule')
        g.custom_command('show', 'show_servicebus_topic_subscription_rule')
    with self.command_group('servicebus topic subscription rule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('show', 'show_servicebus_topic_subscription_rule')
        g.custom_command('list', 'list_servicebus_topic_subscription_rule')
    with self.command_group('servicebus', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus')
    with self.command_group('', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_')
    with self.command_group('servicebus', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus')