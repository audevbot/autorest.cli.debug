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
    with self.command_group('servicebus authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_authorizationrules')
        g.custom_command('show', 'show_servicebus_authorizationrules')
    with self.command_group('servicebus disasterrecoveryconfigs', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_disasterrecoveryconfigs')
        g.custom_command('delete', 'delete_servicebus_disasterrecoveryconfigs')
        g.custom_command('list', 'list_servicebus_disasterrecoveryconfigs')
        g.custom_command('show', 'show_servicebus_disasterrecoveryconfigs')
    with self.command_group('servicebus disasterrecoveryconfigs authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_disasterrecoveryconfigs_authorizationrules')
        g.custom_command('show', 'show_servicebus_disasterrecoveryconfigs_authorizationrules')
    with self.command_group('servicebus migrationconfigurations', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('show', 'show_servicebus_migrationconfigurations')
        g.custom_command('list', 'list_servicebus_migrationconfigurations')
    with self.command_group('servicebus queues', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_queues')
        g.custom_command('delete', 'delete_servicebus_queues')
        g.custom_command('list', 'list_servicebus_queues')
        g.custom_command('show', 'show_servicebus_queues')
    with self.command_group('servicebus queues authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_queues_authorizationrules')
        g.custom_command('show', 'show_servicebus_queues_authorizationrules')
    with self.command_group('servicebus topics', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_topics')
        g.custom_command('delete', 'delete_servicebus_topics')
        g.custom_command('list', 'list_servicebus_topics')
        g.custom_command('show', 'show_servicebus_topics')
    with self.command_group('servicebus topics authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_topics_authorizationrules')
        g.custom_command('show', 'show_servicebus_topics_authorizationrules')
    with self.command_group('servicebus topics subscriptions', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_topics_subscriptions')
        g.custom_command('delete', 'delete_servicebus_topics_subscriptions')
        g.custom_command('list', 'list_servicebus_topics_subscriptions')
        g.custom_command('show', 'show_servicebus_topics_subscriptions')
    with self.command_group('servicebus topics subscriptions', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus_topics_subscriptions')
        g.custom_command('show', 'show_servicebus_topics_subscriptions')
    with self.command_group('servicebus topics subscriptions rules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_servicebus_topics_subscriptions_rules')
        g.custom_command('delete', 'delete_servicebus_topics_subscriptions_rules')
        g.custom_command('list', 'list_servicebus_topics_subscriptions_rules')
        g.custom_command('show', 'show_servicebus_topics_subscriptions_rules')
    with self.command_group('servicebus topics subscriptions rules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('show', 'show_servicebus_topics_subscriptions_rules')
        g.custom_command('list', 'list_servicebus_topics_subscriptions_rules')
    with self.command_group('servicebus', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus')
    with self.command_group('', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_')
    with self.command_group('servicebus', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_servicebus')