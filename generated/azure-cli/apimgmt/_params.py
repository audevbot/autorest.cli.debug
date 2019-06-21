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

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', apimgmt api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', apimgmt api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', apimgmt api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api release') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api release_name', apimgmt api release_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api release') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api release_name', apimgmt api release_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api release') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api operation') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation_name', apimgmt api operation_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api operation') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation_name', apimgmt api operation_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation policy_name', apimgmt api operation policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation policy_name', apimgmt api operation policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt tag') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tag_name', apimgmt tag_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tag') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt tag') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt tag') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt tag') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt tag') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt tag api product operation') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tag api product operation_name', apimgmt tag api product operation_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tag api product operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt tag api product operation') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', apimgmt api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api policy_name', apimgmt api policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api policy_name', apimgmt api policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api schema') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api schema_name', apimgmt api schema_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api schema') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api schema') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api schema') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api schema') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api schema') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api schema_name', apimgmt api schema_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api schema') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api schema') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api diagnostic_name', apimgmt api diagnostic_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api diagnostic_name', apimgmt api diagnostic_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api issue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue_name', apimgmt api issue_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api issue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue_name', apimgmt api issue_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue comment_name', apimgmt api issue comment_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue comment_name', apimgmt api issue comment_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue attachment_name', apimgmt api issue attachment_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue attachment_name', apimgmt api issue attachment_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api tagdescription_name', apimgmt api tagdescription_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api tagdescription_name', apimgmt api tagdescription_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', apimgmt api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt apiversionset_name', apimgmt apiversionset_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt apiversionset_name', apimgmt apiversionset_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt authorizationserver_name', apimgmt authorizationserver_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt authorizationserver_name', apimgmt authorizationserver_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt backend') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt backend_name', apimgmt backend_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt backend') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt backend_name', apimgmt backend_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt backend') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt cache') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt cache_name', apimgmt cache_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt cache') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt cache_name', apimgmt cache_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt cache') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt certificate') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt certificate_name', apimgmt certificate_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt certificate') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt certificate') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt certificate') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt certificate') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt certificate') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt certificate_name', apimgmt certificate_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt certificate') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt certificate') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt diagnostic_name', apimgmt diagnostic_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt diagnostic_name', apimgmt diagnostic_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt template') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt template_name', apimgmt template_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt template') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt template_name', apimgmt template_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt template') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group_name', apimgmt group_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group_name', apimgmt group_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt group user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group user_name', apimgmt group user_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt group user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group_name', apimgmt group_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt identityprovider_name', apimgmt identityprovider_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt identityprovider_name', apimgmt identityprovider_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt issue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt issue_name', apimgmt issue_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt issue') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt logger') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt logger_name', apimgmt logger_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt logger') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt logger_name', apimgmt logger_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt logger') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt location') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt location_name', apimgmt location_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt location') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', apimgmt notification_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', apimgmt notification_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt notification recipientuser') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification recipientuser_name', apimgmt notification recipientuser_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification recipientuser') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification recipientuser') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification recipientuser') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', apimgmt notification_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt notification recipientemail') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification recipientemail_name', apimgmt notification recipientemail_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification recipientemail') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification recipientemail') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt notification recipientemail') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', apimgmt notification_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt openidconnectprovider_name', apimgmt openidconnectprovider_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt openidconnectprovider_name', apimgmt openidconnectprovider_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt policy_name', apimgmt policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt policy_name', apimgmt policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', apimgmt product_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', apimgmt product_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product api_name', apimgmt product api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', apimgmt product_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product group_name', apimgmt product group_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product group') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', apimgmt product_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', apimgmt product_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product policy_name', apimgmt product policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt product policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product policy_name', apimgmt product policy_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt product policy') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt property') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt property_name', apimgmt property_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt property') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt property_name', apimgmt property_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt property') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt quota') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt quota_name', apimgmt quota_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt quota') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt quota period') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt quota period_name', apimgmt quota period_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt quota period') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt subscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt subscription_name', apimgmt subscription_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt subscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt subscription_name', apimgmt subscription_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt subscription') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', apimgmt_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tenant_name', apimgmt tenant_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tenant') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tenant_name', apimgmt tenant_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tenant') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tenant_name', apimgmt tenant_name_type, options_list=['--name', '-n'])
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', apimgmt user_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', apimgmt user_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', apimgmt user_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', apimgmt user_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', apimgmt user_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', apimgmt api_name_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])