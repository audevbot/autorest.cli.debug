# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('compute') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('compute_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('compute create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('identifier', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('compute delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('compute') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('compute_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('compute show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('compute image') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('compute image_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('compute image create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('eula', name_arg_type, id_part=None)
        c.argument('privacy_statement_uri', name_arg_type, id_part=None)
        c.argument('release_note_uri', name_arg_type, id_part=None)
        c.argument('os_type', name_arg_type, id_part=None)
        c.argument('os_state', name_arg_type, id_part=None)
        c.argument('end_of_life_date', name_arg_type, id_part=None)
        c.argument('identifier', name_arg_type, id_part=None)
        c.argument('recommended', name_arg_type, id_part=None)
        c.argument('disallowed', name_arg_type, id_part=None)
        c.argument('purchase_plan', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('compute image delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('compute image') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('compute image_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('compute image show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('compute image version') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('compute image version_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('compute image version create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('gallery_image_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('publishing_profile', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('storage_profile', name_arg_type, id_part=None)
        c.argument('replication_status', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('compute image version delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('gallery_image_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('gallery_image_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('gallery_image_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('compute image version') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('compute image version_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('compute image version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('gallery_image_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('gallery_name', name_arg_type, id_part=None)
        c.argument('gallery_image_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])