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

    with self.argument_context('batchaccounts') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts_name', batchaccounts_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts_name', batchaccounts_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts applications versions_name', batchaccounts applications versions_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts applications versions_name', batchaccounts applications versions_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications versions') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts applications') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts applications_name', batchaccounts applications_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts applications') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts applications_name', batchaccounts applications_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts applications') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('locations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('locations_name', locations_name_type, options_list=['--name', '-n'])
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts certificates_name', batchaccounts certificates_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts certificates_name', batchaccounts certificates_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts certificates') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts pools') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts pools_name', batchaccounts pools_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('batchaccounts pools') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batchaccounts pools_name', batchaccounts pools_name_type, options_list=['--name', '-n'])

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)

    with self.argument_context('batchaccounts pools') as c:
        c.argument('batch_name', batch_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])