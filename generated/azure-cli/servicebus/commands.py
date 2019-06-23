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


    with self.command_group('servicebus namespace', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_namespace')
        g.custom_command('update', 'update_servicebus_namespace')
        g.custom_command('delete', 'delete_servicebus_namespace')
        g.custom_command('list', 'list_servicebus_namespace')
        g.custom_command('show', 'show_servicebus_namespace')
    with self.command_group('servicebus namespace disasterrecoveryconfig', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_namespace_disasterrecoveryconfig')
        g.custom_command('update', 'update_servicebus_namespace_disasterrecoveryconfig')
        g.custom_command('delete', 'delete_servicebus_namespace_disasterrecoveryconfig')
        g.custom_command('list', 'list_servicebus_namespace_disasterrecoveryconfig')
        g.custom_command('show', 'show_servicebus_namespace_disasterrecoveryconfig')
    with self.command_group('servicebus namespace queue', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_namespace_queue')
        g.custom_command('update', 'update_servicebus_namespace_queue')
        g.custom_command('delete', 'delete_servicebus_namespace_queue')
        g.custom_command('list', 'list_servicebus_namespace_queue')
        g.custom_command('show', 'show_servicebus_namespace_queue')
    with self.command_group('servicebus namespace topic', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_namespace_topic')
        g.custom_command('update', 'update_servicebus_namespace_topic')
        g.custom_command('delete', 'delete_servicebus_namespace_topic')
        g.custom_command('list', 'list_servicebus_namespace_topic')
        g.custom_command('show', 'show_servicebus_namespace_topic')
    with self.command_group('servicebus namespace topic subscription', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_namespace_topic_subscription')
        g.custom_command('update', 'update_servicebus_namespace_topic_subscription')
        g.custom_command('delete', 'delete_servicebus_namespace_topic_subscription')
        g.custom_command('list', 'list_servicebus_namespace_topic_subscription')
        g.custom_command('show', 'show_servicebus_namespace_topic_subscription')
    with self.command_group('servicebus namespace topic subscription rule', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_namespace_topic_subscription_rule')
        g.custom_command('update', 'update_servicebus_namespace_topic_subscription_rule')
        g.custom_command('delete', 'delete_servicebus_namespace_topic_subscription_rule')
        g.custom_command('list', 'list_servicebus_namespace_topic_subscription_rule')
        g.custom_command('show', 'show_servicebus_namespace_topic_subscription_rule')