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

    with self.argument_context('galleries') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('galleries_name', galleries_name_type, options_list=['--name', '-n'])

    with self.argument_context('galleries') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries') as c:
        c.argument('compute_name', compute_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('galleries') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('galleries_name', galleries_name_type, options_list=['--name', '-n'])

    with self.argument_context('galleries') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries') as c:
        c.argument('compute_name', compute_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('galleries images') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('galleries images_name', galleries images_name_type, options_list=['--name', '-n'])

    with self.argument_context('galleries images') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images') as c:
        c.argument('compute_name', compute_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('galleries images') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('galleries images_name', galleries images_name_type, options_list=['--name', '-n'])

    with self.argument_context('galleries images') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images') as c:
        c.argument('compute_name', compute_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('galleries images versions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('galleries images versions_name', galleries images versions_name_type, options_list=['--name', '-n'])

    with self.argument_context('galleries images versions') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images versions') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images versions') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images versions') as c:
        c.argument('compute_name', compute_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('galleries images versions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('galleries images versions_name', galleries images versions_name_type, options_list=['--name', '-n'])

    with self.argument_context('galleries images versions') as c:
        c.argument('compute_name', compute_name_type, id_part=None)

    with self.argument_context('galleries images versions') as c:
        c.argument('compute_name', compute_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])