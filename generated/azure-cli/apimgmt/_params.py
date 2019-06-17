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

    with self.argument_context('service apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis_name', service apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis_name', service apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis_name', service apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis releases') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis releases_name', service apis releases_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis releases') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis releases_name', service apis releases_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis releases') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis operations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis operations_name', service apis operations_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis operations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis operations_name', service apis operations_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis operations policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis operations policies_name', service apis operations policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis operations policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis operations policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis operations policies_name', service apis operations policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis operations policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis operations policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service tags') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service tags_name', service tags_name_type, options_list=['--name', '-n'])

    with self.argument_context('service tags') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service tags') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service tags') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service tags') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service tags') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service tags apis products operations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service tags apis products operations_name', service tags apis products operations_name_type, options_list=['--name', '-n'])

    with self.argument_context('service tags apis products operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service tags apis products operations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis_name', service apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis policies_name', service apis policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis policies_name', service apis policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis schemas') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis schemas_name', service apis schemas_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis schemas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis schemas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis schemas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis schemas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis schemas') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis schemas_name', service apis schemas_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis schemas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis schemas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis diagnostics') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis diagnostics_name', service apis diagnostics_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis diagnostics') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis diagnostics_name', service apis diagnostics_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis issues') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis issues_name', service apis issues_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis issues') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis issues_name', service apis issues_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis issues comments') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis issues comments_name', service apis issues comments_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis issues comments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues comments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues comments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues comments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis issues comments') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis issues comments_name', service apis issues comments_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis issues comments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues comments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis issues attachments') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis issues attachments_name', service apis issues attachments_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis issues attachments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues attachments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues attachments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues attachments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis issues attachments') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis issues attachments_name', service apis issues attachments_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis issues attachments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis issues attachments') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis tagdescriptions_name', service apis tagdescriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis tagdescriptions_name', service apis tagdescriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apis tagdescriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis_name', service apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apiversionsets') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apiversionsets_name', service apiversionsets_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apiversionsets') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apiversionsets_name', service apiversionsets_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service apiversionsets') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service authorizationservers') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service authorizationservers_name', service authorizationservers_name_type, options_list=['--name', '-n'])

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service authorizationservers') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service authorizationservers_name', service authorizationservers_name_type, options_list=['--name', '-n'])

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service authorizationservers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service backends') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service backends_name', service backends_name_type, options_list=['--name', '-n'])

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service backends') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service backends_name', service backends_name_type, options_list=['--name', '-n'])

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service backends') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service caches') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service caches_name', service caches_name_type, options_list=['--name', '-n'])

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service caches') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service caches_name', service caches_name_type, options_list=['--name', '-n'])

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service caches') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service certificates') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service certificates_name', service certificates_name_type, options_list=['--name', '-n'])

    with self.argument_context('service certificates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service certificates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service certificates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service certificates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service certificates') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service certificates_name', service certificates_name_type, options_list=['--name', '-n'])

    with self.argument_context('service certificates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service certificates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', _name_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service diagnostics') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service diagnostics_name', service diagnostics_name_type, options_list=['--name', '-n'])

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service diagnostics') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service diagnostics_name', service diagnostics_name_type, options_list=['--name', '-n'])

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service diagnostics') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service templates') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service templates_name', service templates_name_type, options_list=['--name', '-n'])

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service templates') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service templates_name', service templates_name_type, options_list=['--name', '-n'])

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service templates') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service groups') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service groups_name', service groups_name_type, options_list=['--name', '-n'])

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service groups') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service groups_name', service groups_name_type, options_list=['--name', '-n'])

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service groups users') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service groups users_name', service groups users_name_type, options_list=['--name', '-n'])

    with self.argument_context('service groups users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service groups users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service groups') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service groups_name', service groups_name_type, options_list=['--name', '-n'])

    with self.argument_context('service groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service identityproviders') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service identityproviders_name', service identityproviders_name_type, options_list=['--name', '-n'])

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service identityproviders') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service identityproviders_name', service identityproviders_name_type, options_list=['--name', '-n'])

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service identityproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service issues') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service issues_name', service issues_name_type, options_list=['--name', '-n'])

    with self.argument_context('service issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service issues') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service loggers') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service loggers_name', service loggers_name_type, options_list=['--name', '-n'])

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service loggers') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service loggers_name', service loggers_name_type, options_list=['--name', '-n'])

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service loggers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service locations') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service locations_name', service locations_name_type, options_list=['--name', '-n'])

    with self.argument_context('service locations') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service notifications') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service notifications_name', service notifications_name_type, options_list=['--name', '-n'])

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service notifications') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service notifications_name', service notifications_name_type, options_list=['--name', '-n'])

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service notifications recipientusers') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service notifications recipientusers_name', service notifications recipientusers_name_type, options_list=['--name', '-n'])

    with self.argument_context('service notifications recipientusers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications recipientusers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications recipientusers') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service notifications') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service notifications_name', service notifications_name_type, options_list=['--name', '-n'])

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service notifications recipientemails') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service notifications recipientemails_name', service notifications recipientemails_name_type, options_list=['--name', '-n'])

    with self.argument_context('service notifications recipientemails') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications recipientemails') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service notifications recipientemails') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service notifications') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service notifications_name', service notifications_name_type, options_list=['--name', '-n'])

    with self.argument_context('service notifications') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service openidconnectproviders_name', service openidconnectproviders_name_type, options_list=['--name', '-n'])

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service openidconnectproviders_name', service openidconnectproviders_name_type, options_list=['--name', '-n'])

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service openidconnectproviders') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service policies_name', service policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service policies_name', service policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products_name', service products_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products_name', service products_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products apis_name', service products apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products_name', service products_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products groups') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products groups_name', service products groups_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products groups') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products_name', service products_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products_name', service products_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products policies_name', service products policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service products policies') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service products policies_name', service products policies_name_type, options_list=['--name', '-n'])

    with self.argument_context('service products policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service products policies') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service properties') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service properties_name', service properties_name_type, options_list=['--name', '-n'])

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service properties') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service properties_name', service properties_name_type, options_list=['--name', '-n'])

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service properties') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service quotas') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service quotas_name', service quotas_name_type, options_list=['--name', '-n'])

    with self.argument_context('service quotas') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service quotas periods') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service quotas periods_name', service quotas periods_name_type, options_list=['--name', '-n'])

    with self.argument_context('service quotas periods') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service subscriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service subscriptions_name', service subscriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service subscriptions') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service subscriptions_name', service subscriptions_name_type, options_list=['--name', '-n'])

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service subscriptions') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service_name', service_name_type, options_list=['--name', '-n'])

    with self.argument_context('service') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service tenant_name', service tenant_name_type, options_list=['--name', '-n'])

    with self.argument_context('service tenant') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service tenant_name', service tenant_name_type, options_list=['--name', '-n'])

    with self.argument_context('service tenant') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service tenant_name', service tenant_name_type, options_list=['--name', '-n'])
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service users') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service users_name', service users_name_type, options_list=['--name', '-n'])

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service users') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service users_name', service users_name_type, options_list=['--name', '-n'])

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service users') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service users_name', service users_name_type, options_list=['--name', '-n'])

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service users') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service users_name', service users_name_type, options_list=['--name', '-n'])

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service users') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service users_name', service users_name_type, options_list=['--name', '-n'])

    with self.argument_context('service users') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('service apis') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('service apis_name', service apis_name_type, options_list=['--name', '-n'])

    with self.argument_context('service apis') as c:
        c.argument('apimgmt_name', apimgmt_name_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', apimanagement_name_type, options_list=['--name', '-n'])