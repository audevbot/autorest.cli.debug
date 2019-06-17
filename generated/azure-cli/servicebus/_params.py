# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces_name', namespaces_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces authorizationrules_name', namespaces authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces disasterrecoveryconfigs') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces disasterrecoveryconfigs_name', namespaces disasterrecoveryconfigs_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces disasterrecoveryconfigs authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces disasterrecoveryconfigs authorizationrules_name', namespaces disasterrecoveryconfigs authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces disasterrecoveryconfigs authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces disasterrecoveryconfigs authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces migrationconfigurations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces migrationconfigurations_name', namespaces migrationconfigurations_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces migrationconfigurations') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces migrationconfigurations') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces queues') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces queues_name', namespaces queues_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces queues authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces queues authorizationrules_name', namespaces queues authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces queues authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces queues authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces topics') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces topics_name', namespaces topics_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces topics authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces topics authorizationrules_name', namespaces topics authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces topics authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces topics subscriptions_name', namespaces topics subscriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces topics subscriptions_name', namespaces topics subscriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces topics subscriptions rules_name', namespaces topics subscriptions rules_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces topics subscriptions rules_name', namespaces topics subscriptions rules_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('namespaces topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('sku') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('sku_name', sku_name_type, options_list=['--name', '-n'])

    with self.argument_context('sku') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('namespaces') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('namespaces_name', namespaces_name_type, options_list=['--name', '-n'])

    with self.argument_context('namespaces') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])