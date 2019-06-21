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


    with self.argument_context('compute create') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('location', name_arg_type, id_part=None, help='Resource location')
        c.argument('tags', name_arg_type, id_part=None, help='Resource tags')
        c.argument('properties', name_arg_type, id_part=None, help='undefined')
        c.argument('description', name_arg_type, id_part=None, help='The description of this Shared Image Gallery resource. This property is updatable.')
        c.argument('identifier', name_arg_type, id_part=None, help='undefined')
        c.argument('provisioning_state', name_arg_type, id_part=None, help='The provisioning state, which only appears in the response.')
        c.argument('id', name_arg_type, id_part=None, help='Resource Id')
        c.argument('name', name_arg_type, id_part=None, help='Resource name')
        c.argument('type', name_arg_type, id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('compute delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('compute show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('compute image create') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('location', name_arg_type, id_part=None, help='Resource location')
        c.argument('tags', name_arg_type, id_part=None, help='Resource tags')
        c.argument('properties', name_arg_type, id_part=None, help='undefined')
        c.argument('description', name_arg_type, id_part=None, help='The description of this gallery Image Definition resource. This property is updatable.')
        c.argument('eula', name_arg_type, id_part=None, help='The Eula agreement for the gallery Image Definition.')
        c.argument('privacy_statement_uri', name_arg_type, id_part=None, help='The privacy statement uri.')
        c.argument('release_note_uri', name_arg_type, id_part=None, help='The release note uri.')
        c.argument('os_type', name_arg_type, id_part=None, help='This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**')
        c.argument('os_state', name_arg_type, id_part=None, help='The allowed values for OS State are 'Generalized'.')
        c.argument('end_of_life_date', name_arg_type, id_part=None, help='The end of life date of the gallery Image Definition. This property can be used for decommissioning purposes. This property is updatable.')
        c.argument('identifier', name_arg_type, id_part=None, help='undefined')
        c.argument('recommended', name_arg_type, id_part=None, help='undefined')
        c.argument('disallowed', name_arg_type, id_part=None, help='undefined')
        c.argument('purchase_plan', name_arg_type, id_part=None, help='undefined')
        c.argument('provisioning_state', name_arg_type, id_part=None, help='The provisioning state, which only appears in the response.')
        c.argument('id', name_arg_type, id_part=None, help='Resource Id')
        c.argument('name', name_arg_type, id_part=None, help='Resource name')
        c.argument('type', name_arg_type, id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('compute image delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('compute image show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Definition to be retrieved.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Definition to be retrieved.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('compute image version create') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition resides.')
        c.argument('gallery_image_name', name_arg_type, id_part=None, help='The name of the gallery Image Definition in which the Image Version is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>')
        c.argument('location', name_arg_type, id_part=None, help='Resource location')
        c.argument('tags', name_arg_type, id_part=None, help='Resource tags')
        c.argument('properties', name_arg_type, id_part=None, help='undefined')
        c.argument('publishing_profile', name_arg_type, id_part=None, help='undefined')
        c.argument('provisioning_state', name_arg_type, id_part=None, help='The provisioning state, which only appears in the response.')
        c.argument('storage_profile', name_arg_type, id_part=None, help='undefined')
        c.argument('replication_status', name_arg_type, id_part=None, help='undefined')
        c.argument('id', name_arg_type, id_part=None, help='Resource Id')
        c.argument('name', name_arg_type, id_part=None, help='Resource name')
        c.argument('type', name_arg_type, id_part=None, help='Resource type')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('compute image version delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition resides.')
        c.argument('gallery_image_name', name_arg_type, id_part=None, help='The name of the gallery Image Definition in which the Image Version is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition resides.')
        c.argument('gallery_image_name', name_arg_type, id_part=None, help='The name of the gallery Image Definition in which the Image Version is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition resides.')
        c.argument('gallery_image_name', name_arg_type, id_part=None, help='The name of the gallery Image Definition in which the Image Version is to be created.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: <MajorVersion>.<MinorVersion>.<Patch>')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('compute image version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition resides.')
        c.argument('gallery_image_name', name_arg_type, id_part=None, help='The name of the gallery Image Definition in which the Image Version resides.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Version to be retrieved.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('compute image version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None, help='The name of the resource group.')
        c.argument('gallery_name', name_arg_type, id_part=None, help='The name of the Shared Image Gallery in which the Image Definition resides.')
        c.argument('gallery_image_name', name_arg_type, id_part=None, help='The name of the gallery Image Definition in which the Image Version resides.')
        c.argument('name', name_arg_type, id_part=None, help='The name of the gallery Image Version to be retrieved.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])