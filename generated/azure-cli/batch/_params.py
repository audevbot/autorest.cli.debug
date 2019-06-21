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

    with self.argument_context('batch') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('auto_storage', name_arg_type, id_part=None)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None)
        c.argument('pool_allocation_mode', name_arg_type, id_part=None)
        c.argument('key_vault_reference', name_arg_type, id_part=None)
        c.argument('account_endpoint', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('auto_storage', name_arg_type, id_part=None)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None)
        c.argument('pool_allocation_mode', name_arg_type, id_part=None)
        c.argument('key_vault_reference', name_arg_type, id_part=None)
        c.argument('account_endpoint', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch application version') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch application version_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch application version create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('application_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('state', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('storage_url', name_arg_type, id_part=None)
        c.argument('storage_url_expiry', name_arg_type, id_part=None)
        c.argument('last_activation_time', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application version delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('application_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('application_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('application_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch application version') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch application version_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch application version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('application_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('application_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch application') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch application_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch application create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('allow_updates', name_arg_type, id_part=None)
        c.argument('default_version', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('allow_updates', name_arg_type, id_part=None)
        c.argument('default_version', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch application') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch application_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch application show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch_name', name_arg_type, options_list=['--name', '-n'])
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch certificate') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch certificate_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch certificate create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('thumbprint_algorithm', name_arg_type, id_part=None)
        c.argument('thumbprint', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('data', name_arg_type, id_part=None)
        c.argument('password', name_arg_type, id_part=None)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None)
        c.argument('previous_provisioning_state', name_arg_type, id_part=None)
        c.argument('previous_provisioning_state_transition_time', name_arg_type, id_part=None)
        c.argument('public_data', name_arg_type, id_part=None)
        c.argument('delete_certificate_error', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch certificate update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('thumbprint_algorithm', name_arg_type, id_part=None)
        c.argument('thumbprint', name_arg_type, id_part=None)
        c.argument('format', name_arg_type, id_part=None)
        c.argument('data', name_arg_type, id_part=None)
        c.argument('password', name_arg_type, id_part=None)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None)
        c.argument('previous_provisioning_state', name_arg_type, id_part=None)
        c.argument('previous_provisioning_state_transition_time', name_arg_type, id_part=None)
        c.argument('public_data', name_arg_type, id_part=None)
        c.argument('delete_certificate_error', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch certificate delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch certificate') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch certificate_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch certificate show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch pool') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch pool_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch pool create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('vm_size', name_arg_type, id_part=None)
        c.argument('deployment_configuration', name_arg_type, id_part=None)
        c.argument('scale_settings', name_arg_type, id_part=None)
        c.argument('inter_node_communication', name_arg_type, id_part=None)
        c.argument('network_configuration', name_arg_type, id_part=None)
        c.argument('max_tasks_per_node', name_arg_type, id_part=None)
        c.argument('task_scheduling_policy', name_arg_type, id_part=None)
        c.argument('user_accounts', name_arg_type, id_part=None)
        c.argument('metadata', name_arg_type, id_part=None)
        c.argument('start_task', name_arg_type, id_part=None)
        c.argument('certificates', name_arg_type, id_part=None)
        c.argument('application_packages', name_arg_type, id_part=None)
        c.argument('application_licenses', name_arg_type, id_part=None)
        c.argument('last_modified', name_arg_type, id_part=None)
        c.argument('creation_time', name_arg_type, id_part=None)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None)
        c.argument('allocation_state', name_arg_type, id_part=None)
        c.argument('allocation_state_transition_time', name_arg_type, id_part=None)
        c.argument('current_dedicated_nodes', name_arg_type, id_part=None)
        c.argument('current_low_priority_nodes', name_arg_type, id_part=None)
        c.argument('auto_scale_run', name_arg_type, id_part=None)
        c.argument('resize_operation_status', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch pool update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('display_name', name_arg_type, id_part=None)
        c.argument('vm_size', name_arg_type, id_part=None)
        c.argument('deployment_configuration', name_arg_type, id_part=None)
        c.argument('scale_settings', name_arg_type, id_part=None)
        c.argument('inter_node_communication', name_arg_type, id_part=None)
        c.argument('network_configuration', name_arg_type, id_part=None)
        c.argument('max_tasks_per_node', name_arg_type, id_part=None)
        c.argument('task_scheduling_policy', name_arg_type, id_part=None)
        c.argument('user_accounts', name_arg_type, id_part=None)
        c.argument('metadata', name_arg_type, id_part=None)
        c.argument('start_task', name_arg_type, id_part=None)
        c.argument('certificates', name_arg_type, id_part=None)
        c.argument('application_packages', name_arg_type, id_part=None)
        c.argument('application_licenses', name_arg_type, id_part=None)
        c.argument('last_modified', name_arg_type, id_part=None)
        c.argument('creation_time', name_arg_type, id_part=None)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None)
        c.argument('allocation_state', name_arg_type, id_part=None)
        c.argument('allocation_state_transition_time', name_arg_type, id_part=None)
        c.argument('current_dedicated_nodes', name_arg_type, id_part=None)
        c.argument('current_low_priority_nodes', name_arg_type, id_part=None)
        c.argument('auto_scale_run', name_arg_type, id_part=None)
        c.argument('resize_operation_status', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('etag', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch pool delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('batch pool') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('batch pool_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('batch pool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('account_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])