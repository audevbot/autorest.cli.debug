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
    with self.command_group('namespaces', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_namespaces')
        g.custom_command('update', 'update_namespaces')
        g.custom_command('delete', 'delete_namespaces')
        g.custom_command('list', 'list_namespaces')
        g.custom_command('show', 'show_namespaces')
    with self.command_group('namespaces authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_namespaces_authorizationrules')
        g.custom_command('show', 'show_namespaces_authorizationrules')
    with self.command_group('namespaces disasterrecoveryconfigs', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_namespaces_disasterrecoveryconfigs')
        g.custom_command('delete', 'delete_namespaces_disasterrecoveryconfigs')
        g.custom_command('list', 'list_namespaces_disasterrecoveryconfigs')
        g.custom_command('show', 'show_namespaces_disasterrecoveryconfigs')
    with self.command_group('namespaces disasterrecoveryconfigs authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_namespaces_disasterrecoveryconfigs_authorizationrules')
        g.custom_command('show', 'show_namespaces_disasterrecoveryconfigs_authorizationrules')
    with self.command_group('namespaces migrationconfigurations', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('show', 'show_namespaces_migrationconfigurations')
        g.custom_command('list', 'list_namespaces_migrationconfigurations')
    with self.command_group('namespaces queues', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_namespaces_queues')
        g.custom_command('delete', 'delete_namespaces_queues')
        g.custom_command('list', 'list_namespaces_queues')
        g.custom_command('show', 'show_namespaces_queues')
    with self.command_group('namespaces queues authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_namespaces_queues_authorizationrules')
        g.custom_command('show', 'show_namespaces_queues_authorizationrules')
    with self.command_group('namespaces topics', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_namespaces_topics')
        g.custom_command('delete', 'delete_namespaces_topics')
        g.custom_command('list', 'list_namespaces_topics')
        g.custom_command('show', 'show_namespaces_topics')
    with self.command_group('namespaces topics authorizationrules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_namespaces_topics_authorizationrules')
        g.custom_command('show', 'show_namespaces_topics_authorizationrules')
    with self.command_group('namespaces topics subscriptions', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_namespaces_topics_subscriptions')
        g.custom_command('delete', 'delete_namespaces_topics_subscriptions')
        g.custom_command('list', 'list_namespaces_topics_subscriptions')
        g.custom_command('show', 'show_namespaces_topics_subscriptions')
    with self.command_group('namespaces topics subscriptions', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_namespaces_topics_subscriptions')
        g.custom_command('show', 'show_namespaces_topics_subscriptions')
    with self.command_group('namespaces topics subscriptions rules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('create', 'create_namespaces_topics_subscriptions_rules')
        g.custom_command('delete', 'delete_namespaces_topics_subscriptions_rules')
        g.custom_command('list', 'list_namespaces_topics_subscriptions_rules')
        g.custom_command('show', 'show_namespaces_topics_subscriptions_rules')
    with self.command_group('namespaces topics subscriptions rules', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('show', 'show_namespaces_topics_subscriptions_rules')
        g.custom_command('list', 'list_namespaces_topics_subscriptions_rules')
    with self.command_group('sku', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_sku')
    with self.command_group('', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_')
    with self.command_group('namespaces', servicebus_sdk, client_factory=cf_servicebus) as g:
        g.custom_command('list', 'list_namespaces')