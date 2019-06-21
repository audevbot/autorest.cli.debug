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

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('authentication_settings', name_arg_type, id_part=None)
        c.argument('subscription_key_parameter_names', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('api_revision', name_arg_type, id_part=None)
        c.argument('api_version', name_arg_type, id_part=None)
        c.argument('is_current', name_arg_type, id_part=None)
        c.argument('api_revision_description', name_arg_type, id_part=None)
        c.argument('api_version_description', name_arg_type, id_part=None)
        c.argument('api_version_set_id', name_arg_type, id_part=None)
        c.argument('subscription_required', name_arg_type, id_part=None)
        c.argument('source_api_id', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('service_url', name_arg_type, id_part=None)
        c.argument('path', name_arg_type, id_part=None)
        c.argument('protocols', name_arg_type, id_part=None)
        c.argument('api_version_set', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('wsdl_selector', name_arg_type, id_part=None)
        c.argument('api_type', name_arg_type, id_part=None)
        c.argument('is_online', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('authentication_settings', name_arg_type, id_part=None)
        c.argument('subscription_key_parameter_names', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('api_revision', name_arg_type, id_part=None)
        c.argument('api_version', name_arg_type, id_part=None)
        c.argument('is_current', name_arg_type, id_part=None)
        c.argument('api_revision_description', name_arg_type, id_part=None)
        c.argument('api_version_description', name_arg_type, id_part=None)
        c.argument('api_version_set_id', name_arg_type, id_part=None)
        c.argument('subscription_required', name_arg_type, id_part=None)
        c.argument('source_api_id', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('service_url', name_arg_type, id_part=None)
        c.argument('path', name_arg_type, id_part=None)
        c.argument('protocols', name_arg_type, id_part=None)
        c.argument('api_version_set', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('wsdl_selector', name_arg_type, id_part=None)
        c.argument('api_type', name_arg_type, id_part=None)
        c.argument('is_online', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api release') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api release_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api release create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('notes', name_arg_type, id_part=None)
        c.argument('created_date_time', name_arg_type, id_part=None)
        c.argument('updated_date_time', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api release update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('notes', name_arg_type, id_part=None)
        c.argument('created_date_time', name_arg_type, id_part=None)
        c.argument('updated_date_time', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api release delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api release list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api release show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api release') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api release_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api release show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api release list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('release_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api operation') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('template_parameters', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('request', name_arg_type, id_part=None)
        c.argument('responses', name_arg_type, id_part=None)
        c.argument('policies', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('method', name_arg_type, id_part=None)
        c.argument('url_template', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('template_parameters', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('request', name_arg_type, id_part=None)
        c.argument('responses', name_arg_type, id_part=None)
        c.argument('policies', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('method', name_arg_type, id_part=None)
        c.argument('url_template', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api operation') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation policy create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation policy delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api operation policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api operation policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api operation policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api operation policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt tag') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tag_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tag create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt tag update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt tag delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt tag list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt tag show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt tag api product operation') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tag api product operation_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tag api product operation list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt tag api product operation show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('operation_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api policy create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api policy delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api schema') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api schema_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api schema create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('schema_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('content_type', name_arg_type, id_part=None)
        c.argument('document', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api schema delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('schema_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api schema list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('schema_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api schema show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('schema_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api schema') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api schema_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api schema show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('schema_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api schema list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('schema_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api diagnostic_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api diagnostic create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('always_log', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('sampling', name_arg_type, id_part=None)
        c.argument('frontend', name_arg_type, id_part=None)
        c.argument('backend', name_arg_type, id_part=None)
        c.argument('enable_http_correlation_headers', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('always_log', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('sampling', name_arg_type, id_part=None)
        c.argument('frontend', name_arg_type, id_part=None)
        c.argument('backend', name_arg_type, id_part=None)
        c.argument('enable_http_correlation_headers', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api diagnostic_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api diagnostic show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api diagnostic list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api issue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('created_date', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('created_date', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api issue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue comment_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue comment create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('comment_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('text', name_arg_type, id_part=None)
        c.argument('created_date', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue comment delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('comment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue comment list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('comment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue comment show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('comment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api issue comment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue comment_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue comment show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('comment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue comment list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('comment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue attachment_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue attachment create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('attachment_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('content_format', name_arg_type, id_part=None)
        c.argument('content', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('attachment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('attachment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('attachment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api issue attachment') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api issue attachment_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api issue attachment show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('attachment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api issue attachment list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('attachment_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api tagdescription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api tagdescription create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('external_docs_url', name_arg_type, id_part=None)
        c.argument('external_docs_description', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api tagdescription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api tagdescription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api tagdescription show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt api tagdescription list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('tag_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt apiversionset_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt apiversionset create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('version_query_name', name_arg_type, id_part=None)
        c.argument('version_header_name', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('versioning_scheme', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt apiversionset update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('version_query_name', name_arg_type, id_part=None)
        c.argument('version_header_name', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('versioning_scheme', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt apiversionset delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt apiversionset list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt apiversionset show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt apiversionset') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt apiversionset_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt apiversionset show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt apiversionset list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('version_set_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt authorizationserver_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt authorizationserver create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('authorization_methods', name_arg_type, id_part=None)
        c.argument('client_authentication_method', name_arg_type, id_part=None)
        c.argument('token_body_parameters', name_arg_type, id_part=None)
        c.argument('token_endpoint', name_arg_type, id_part=None)
        c.argument('support_state', name_arg_type, id_part=None)
        c.argument('default_scope', name_arg_type, id_part=None)
        c.argument('bearer_token_sending_methods', name_arg_type, id_part=None)
        c.argument('client_secret', name_arg_type, id_part=None)
        c.argument('resource_owner_username', name_arg_type, id_part=None)
        c.argument('resource_owner_password', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('client_registration_endpoint', name_arg_type, id_part=None)
        c.argument('authorization_endpoint', name_arg_type, id_part=None)
        c.argument('grant_types', name_arg_type, id_part=None)
        c.argument('client_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('authorization_methods', name_arg_type, id_part=None)
        c.argument('client_authentication_method', name_arg_type, id_part=None)
        c.argument('token_body_parameters', name_arg_type, id_part=None)
        c.argument('token_endpoint', name_arg_type, id_part=None)
        c.argument('support_state', name_arg_type, id_part=None)
        c.argument('default_scope', name_arg_type, id_part=None)
        c.argument('bearer_token_sending_methods', name_arg_type, id_part=None)
        c.argument('client_secret', name_arg_type, id_part=None)
        c.argument('resource_owner_username', name_arg_type, id_part=None)
        c.argument('resource_owner_password', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('client_registration_endpoint', name_arg_type, id_part=None)
        c.argument('authorization_endpoint', name_arg_type, id_part=None)
        c.argument('grant_types', name_arg_type, id_part=None)
        c.argument('client_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt authorizationserver') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt authorizationserver_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt authorizationserver show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt authorizationserver list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('authsid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt backend') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt backend_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt backend create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('service_fabric_cluster', name_arg_type, id_part=None)
        c.argument('credentials', name_arg_type, id_part=None)
        c.argument('proxy', name_arg_type, id_part=None)
        c.argument('tls', name_arg_type, id_part=None)
        c.argument('url', name_arg_type, id_part=None)
        c.argument('protocol', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt backend update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('service_fabric_cluster', name_arg_type, id_part=None)
        c.argument('credentials', name_arg_type, id_part=None)
        c.argument('proxy', name_arg_type, id_part=None)
        c.argument('tls', name_arg_type, id_part=None)
        c.argument('url', name_arg_type, id_part=None)
        c.argument('protocol', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt backend delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt backend list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt backend show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt backend') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt backend_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt backend show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt backend list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('backend_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt cache') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt cache_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt cache create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('connection_string', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt cache update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('connection_string', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt cache delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt cache list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt cache show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt cache') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt cache_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt cache show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt cache list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('cache_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt certificate') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt certificate_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt certificate create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('certificate_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('data', name_arg_type, id_part=None)
        c.argument('password', name_arg_type, id_part=None)
        c.argument('subject', name_arg_type, id_part=None)
        c.argument('thumbprint', name_arg_type, id_part=None)
        c.argument('expiration_date', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt certificate delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('certificate_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt certificate list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('certificate_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt certificate show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('certificate_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt certificate') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt certificate_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt certificate show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('certificate_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt certificate list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('certificate_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('notification_sender_email', name_arg_type, id_part=None)
        c.argument('hostname_configurations', name_arg_type, id_part=None)
        c.argument('virtual_network_configuration', name_arg_type, id_part=None)
        c.argument('additional_locations', name_arg_type, id_part=None)
        c.argument('custom_properties', name_arg_type, id_part=None)
        c.argument('certificates', name_arg_type, id_part=None)
        c.argument('enable_client_certificate', name_arg_type, id_part=None)
        c.argument('virtual_network_type', name_arg_type, id_part=None)
        c.argument('publisher_email', name_arg_type, id_part=None)
        c.argument('publisher_name', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('target_provisioning_state', name_arg_type, id_part=None)
        c.argument('created_at_utc', name_arg_type, id_part=None)
        c.argument('gateway_url', name_arg_type, id_part=None)
        c.argument('gateway_regional_url', name_arg_type, id_part=None)
        c.argument('portal_url', name_arg_type, id_part=None)
        c.argument('management_api_url', name_arg_type, id_part=None)
        c.argument('scm_url', name_arg_type, id_part=None)
        c.argument('public_ip_addresses', name_arg_type, id_part=None)
        c.argument('private_ip_addresses', name_arg_type, id_part=None)
        c.argument('sku', name_arg_type, id_part=None)
        c.argument('identity', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('notification_sender_email', name_arg_type, id_part=None)
        c.argument('hostname_configurations', name_arg_type, id_part=None)
        c.argument('virtual_network_configuration', name_arg_type, id_part=None)
        c.argument('additional_locations', name_arg_type, id_part=None)
        c.argument('custom_properties', name_arg_type, id_part=None)
        c.argument('certificates', name_arg_type, id_part=None)
        c.argument('enable_client_certificate', name_arg_type, id_part=None)
        c.argument('virtual_network_type', name_arg_type, id_part=None)
        c.argument('publisher_email', name_arg_type, id_part=None)
        c.argument('publisher_name', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('target_provisioning_state', name_arg_type, id_part=None)
        c.argument('created_at_utc', name_arg_type, id_part=None)
        c.argument('gateway_url', name_arg_type, id_part=None)
        c.argument('gateway_regional_url', name_arg_type, id_part=None)
        c.argument('portal_url', name_arg_type, id_part=None)
        c.argument('management_api_url', name_arg_type, id_part=None)
        c.argument('scm_url', name_arg_type, id_part=None)
        c.argument('public_ip_addresses', name_arg_type, id_part=None)
        c.argument('private_ip_addresses', name_arg_type, id_part=None)
        c.argument('sku', name_arg_type, id_part=None)
        c.argument('identity', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt diagnostic_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt diagnostic create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('always_log', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('sampling', name_arg_type, id_part=None)
        c.argument('frontend', name_arg_type, id_part=None)
        c.argument('backend', name_arg_type, id_part=None)
        c.argument('enable_http_correlation_headers', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt diagnostic update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('always_log', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('sampling', name_arg_type, id_part=None)
        c.argument('frontend', name_arg_type, id_part=None)
        c.argument('backend', name_arg_type, id_part=None)
        c.argument('enable_http_correlation_headers', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt diagnostic delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt diagnostic list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt diagnostic show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt diagnostic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt diagnostic_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt diagnostic show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt diagnostic list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('diagnostic_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt template') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt template_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt template create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('subject', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('body', name_arg_type, id_part=None)
        c.argument('parameters', name_arg_type, id_part=None)
        c.argument('is_default', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt template update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('subject', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('body', name_arg_type, id_part=None)
        c.argument('parameters', name_arg_type, id_part=None)
        c.argument('is_default', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt template delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt template list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt template show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt template') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt template_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt template show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt template list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('external_id', name_arg_type, id_part=None)
        c.argument('built_in', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('external_id', name_arg_type, id_part=None)
        c.argument('built_in', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt group user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group user_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group user create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('note', name_arg_type, id_part=None)
        c.argument('identities', name_arg_type, id_part=None)
        c.argument('first_name', name_arg_type, id_part=None)
        c.argument('last_name', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('registration_date', name_arg_type, id_part=None)
        c.argument('groups', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group user delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt group user list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt group_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt group list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt identityprovider_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt identityprovider create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('allowed_tenants', name_arg_type, id_part=None)
        c.argument('authority', name_arg_type, id_part=None)
        c.argument('signup_policy_name', name_arg_type, id_part=None)
        c.argument('signin_policy_name', name_arg_type, id_part=None)
        c.argument('profile_editing_policy_name', name_arg_type, id_part=None)
        c.argument('password_reset_policy_name', name_arg_type, id_part=None)
        c.argument('client_id', name_arg_type, id_part=None)
        c.argument('client_secret', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt identityprovider update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('allowed_tenants', name_arg_type, id_part=None)
        c.argument('authority', name_arg_type, id_part=None)
        c.argument('signup_policy_name', name_arg_type, id_part=None)
        c.argument('signin_policy_name', name_arg_type, id_part=None)
        c.argument('profile_editing_policy_name', name_arg_type, id_part=None)
        c.argument('password_reset_policy_name', name_arg_type, id_part=None)
        c.argument('client_id', name_arg_type, id_part=None)
        c.argument('client_secret', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt identityprovider delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt identityprovider list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt identityprovider show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt identityprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt identityprovider_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt identityprovider show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt identityprovider list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt issue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt issue_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt issue show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt issue list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('issue_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt logger') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt logger_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt logger create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('logger_type', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('credentials', name_arg_type, id_part=None)
        c.argument('is_buffered', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt logger update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('logger_type', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('credentials', name_arg_type, id_part=None)
        c.argument('is_buffered', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt logger delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt logger list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt logger show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt logger') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt logger_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt logger show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt logger list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('logger_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt location') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt location_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt location list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('title', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('recipients', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt notification recipientuser') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification recipientuser_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification recipientuser create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification recipientuser delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification recipientuser list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt notification recipientemail') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification recipientemail_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification recipientemail create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification recipientemail delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt notification recipientemail list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt notification') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt notification_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt notification list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt openidconnectprovider_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt openidconnectprovider create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('metadata_endpoint', name_arg_type, id_part=None)
        c.argument('client_id', name_arg_type, id_part=None)
        c.argument('client_secret', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('metadata_endpoint', name_arg_type, id_part=None)
        c.argument('client_id', name_arg_type, id_part=None)
        c.argument('client_secret', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt openidconnectprovider') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt openidconnectprovider_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt openidconnectprovider show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt openidconnectprovider list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('opid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt policy create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt policy delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('enabled', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('enabled', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('enabled', name_arg_type, id_part=None)
        c.argument('terms_of_service', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('enabled', name_arg_type, id_part=None)
        c.argument('terms_of_service', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('url', name_arg_type, id_part=None)
        c.argument('validation_key', name_arg_type, id_part=None)
        c.argument('subscriptions', name_arg_type, id_part=None)
        c.argument('user_registration', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('url', name_arg_type, id_part=None)
        c.argument('validation_key', name_arg_type, id_part=None)
        c.argument('subscriptions', name_arg_type, id_part=None)
        c.argument('user_registration', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('terms', name_arg_type, id_part=None)
        c.argument('subscription_required', name_arg_type, id_part=None)
        c.argument('approval_required', name_arg_type, id_part=None)
        c.argument('subscriptions_limit', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('terms', name_arg_type, id_part=None)
        c.argument('subscription_required', name_arg_type, id_part=None)
        c.argument('approval_required', name_arg_type, id_part=None)
        c.argument('subscriptions_limit', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product api create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('authentication_settings', name_arg_type, id_part=None)
        c.argument('subscription_key_parameter_names', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('api_revision', name_arg_type, id_part=None)
        c.argument('api_version', name_arg_type, id_part=None)
        c.argument('is_current', name_arg_type, id_part=None)
        c.argument('is_online', name_arg_type, id_part=None)
        c.argument('api_revision_description', name_arg_type, id_part=None)
        c.argument('api_version_description', name_arg_type, id_part=None)
        c.argument('api_version_set_id', name_arg_type, id_part=None)
        c.argument('subscription_required', name_arg_type, id_part=None)
        c.argument('source_api_id', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('service_url', name_arg_type, id_part=None)
        c.argument('path', name_arg_type, id_part=None)
        c.argument('protocols', name_arg_type, id_part=None)
        c.argument('api_version_set', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product api delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product api list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product group') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product group_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product group create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('description', name_arg_type, id_part=None)
        c.argument('built_in', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('external_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product group delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product group list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('group_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product policy create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product policy delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt product policy') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt product policy_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt product policy show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt product policy list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('product_id', name_arg_type, id_part=None)
        c.argument('policy_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt property') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt property_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt property create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('secret', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt property update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('secret', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('value', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt property delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt property list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt property show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt property') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt property_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt property show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt property list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('prop_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt quota') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt quota_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt quota list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('quota_counter_key', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt quota period') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt quota period_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt quota period show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('quota_counter_key', name_arg_type, id_part=None)
        c.argument('quota_period_key', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt subscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt subscription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt subscription create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('owner_id', name_arg_type, id_part=None)
        c.argument('scope', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('primary_key', name_arg_type, id_part=None)
        c.argument('secondary_key', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('allow_tracing', name_arg_type, id_part=None)
        c.argument('created_date', name_arg_type, id_part=None)
        c.argument('start_date', name_arg_type, id_part=None)
        c.argument('expiration_date', name_arg_type, id_part=None)
        c.argument('end_date', name_arg_type, id_part=None)
        c.argument('notification_date', name_arg_type, id_part=None)
        c.argument('state_comment', name_arg_type, id_part=None)
        c.argument('notify', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt subscription update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('owner_id', name_arg_type, id_part=None)
        c.argument('scope', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('primary_key', name_arg_type, id_part=None)
        c.argument('secondary_key', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('allow_tracing', name_arg_type, id_part=None)
        c.argument('created_date', name_arg_type, id_part=None)
        c.argument('start_date', name_arg_type, id_part=None)
        c.argument('expiration_date', name_arg_type, id_part=None)
        c.argument('end_date', name_arg_type, id_part=None)
        c.argument('notification_date', name_arg_type, id_part=None)
        c.argument('state_comment', name_arg_type, id_part=None)
        c.argument('notify', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt subscription delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt subscription list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt subscription show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt subscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt subscription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt subscription list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt subscription show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('sid', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tenant_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tenant show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tenant_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt tenant show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('service_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt tenant') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt tenant_name', name_arg_type, options_list=['--name', '-n'])
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('note', name_arg_type, id_part=None)
        c.argument('identities', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('first_name', name_arg_type, id_part=None)
        c.argument('last_name', name_arg_type, id_part=None)
        c.argument('password', name_arg_type, id_part=None)
        c.argument('confirmation', name_arg_type, id_part=None)
        c.argument('registration_date', name_arg_type, id_part=None)
        c.argument('groups', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt user update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('note', name_arg_type, id_part=None)
        c.argument('identities', name_arg_type, id_part=None)
        c.argument('email', name_arg_type, id_part=None)
        c.argument('first_name', name_arg_type, id_part=None)
        c.argument('last_name', name_arg_type, id_part=None)
        c.argument('password', name_arg_type, id_part=None)
        c.argument('confirmation', name_arg_type, id_part=None)
        c.argument('registration_date', name_arg_type, id_part=None)
        c.argument('groups', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('apimgmt user delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt user list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt user show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('apimgmt user list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt user') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt user_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt user list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('user_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('apimgmt api') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimgmt api_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('apimgmt api show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('api_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])