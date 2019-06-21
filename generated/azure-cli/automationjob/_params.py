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

    with self.argument_context('automationjob job') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('automationjob job_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('automationjob job create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('runbook', name_arg_type, id_part=None)
        c.argument('parameters', name_arg_type, id_part=None)
        c.argument('run_on', name_arg_type, id_part=None)
        c.argument('started_by', name_arg_type, id_part=None)
        c.argument('job_id', name_arg_type, id_part=None)
        c.argument('creation_time', name_arg_type, id_part=None)
        c.argument('status', name_arg_type, id_part=None)
        c.argument('status_details', name_arg_type, id_part=None)
        c.argument('start_time', name_arg_type, id_part=None)
        c.argument('end_time', name_arg_type, id_part=None)
        c.argument('exception', name_arg_type, id_part=None)
        c.argument('last_modified_time', name_arg_type, id_part=None)
        c.argument('last_status_modified_time', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('client_request_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('automationjob job list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationjob job show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('automationjob job') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('automationjob job_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('automationjob job show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationjob job list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('automationjob job stream') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('automationjob job stream_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('automationjob job stream show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('job_stream_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationjob job stream list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('automation_account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('job_stream_id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])