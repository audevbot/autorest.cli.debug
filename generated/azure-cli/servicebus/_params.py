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

    with self.argument_context('servicebus') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus_name', servicebus_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus authorizationrules_name', servicebus authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus disasterrecoveryconfigs') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus disasterrecoveryconfigs_name', servicebus disasterrecoveryconfigs_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfigs') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus disasterrecoveryconfigs authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus disasterrecoveryconfigs authorizationrules_name', servicebus disasterrecoveryconfigs authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus disasterrecoveryconfigs authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfigs authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus migrationconfigurations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus migrationconfigurations_name', servicebus migrationconfigurations_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus migrationconfigurations') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus migrationconfigurations') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus queues') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus queues_name', servicebus queues_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus queues') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus queues authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus queues authorizationrules_name', servicebus queues authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus queues authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus queues authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus topics') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topics_name', servicebus topics_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus topics authorizationrules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topics authorizationrules_name', servicebus topics authorizationrules_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topics authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics authorizationrules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topics subscriptions_name', servicebus topics subscriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topics subscriptions_name', servicebus topics subscriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topics subscriptions rules_name', servicebus topics subscriptions rules_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topics subscriptions rules_name', servicebus topics subscriptions rules_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)

    with self.argument_context('servicebus topics subscriptions rules') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus_name', servicebus_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('servicebus') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus_name', servicebus_name_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus') as c:
        c.argument('servicebus_name', servicebus_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])