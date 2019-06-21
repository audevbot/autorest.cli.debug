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


    with self.argument_context('automationjob job create') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('properties', id_part=None, help='Gets or sets the list of job properties.')
        c.argument('runbook', id_part=None, help='Gets or sets the runbook.')
        c.argument('parameters', id_part=None, help='Gets or sets the parameters of the job.')
        c.argument('run_on', id_part=None, help='Gets or sets the runOn which specifies the group name where the job is to be executed.')
        c.argument('started_by', id_part=None, help='Gets or sets the job started by.')
        c.argument('job_id', id_part=None, help='Gets or sets the id of the job.')
        c.argument('creation_time', id_part=None, help='Gets or sets the creation time of the job.')
        c.argument('status', id_part=None, help='Gets or sets the status of the job.')
        c.argument('status_details', id_part=None, help='Gets or sets the status details of the job.')
        c.argument('start_time', id_part=None, help='Gets or sets the start time of the job.')
        c.argument('end_time', id_part=None, help='Gets or sets the end time of the job.')
        c.argument('exception', id_part=None, help='Gets or sets the exception of the job.')
        c.argument('last_modified_time', id_part=None, help='Gets or sets the last modified time of the job.')
        c.argument('last_status_modified_time', id_part=None, help='Gets or sets the last status modified time of the job.')
        c.argument('provisioning_state', id_part=None, help='The current provisioning state of the job.')
        c.argument('client_request_id', id_part=None, help='Identifies this specific client request.')
        c.argument('id', id_part=None, help='Fully qualified resource Id for the resource')
        c.argument('name', id_part=None, help='The name of the resource')
        c.argument('type', id_part=None, help='The type of the resource.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('automationjob job list') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationjob job show') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('automationjob job show') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationjob job list') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('automationjob job stream show') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('job_stream_id', id_part=None, help='The job stream id.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('automationjob job stream list') as c:
        c.argument('resource_group', id_part=None, help='Name of an Azure Resource group.')
        c.argument('automation_account_name', id_part=None, help='The name of the automation account.')
        c.argument('name', id_part=None, help='The job name.')
        c.argument('job_stream_id', id_part=None, help='The job stream id.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])