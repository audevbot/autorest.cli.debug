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

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('sku', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('created_at', name_arg_type, id_part=None)
        c.argument('updated_at', name_arg_type, id_part=None)
        c.argument('service_bus_endpoint', name_arg_type, id_part=None)
        c.argument('metric_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('sku', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('created_at', name_arg_type, id_part=None)
        c.argument('updated_at', name_arg_type, id_part=None)
        c.argument('service_bus_endpoint', name_arg_type, id_part=None)
        c.argument('metric_id', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus authorizationrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus authorizationrule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus authorizationrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus authorizationrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus disasterrecoveryconfig') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus disasterrecoveryconfig_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus disasterrecoveryconfig create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('alias', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('partner_namespace', name_arg_type, id_part=None)
        c.argument('alternate_name', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('pending_replication_operations_count', name_arg_type, id_part=None)
        c.argument('role', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('alias', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('alias', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('alias', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus disasterrecoveryconfig authorizationrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus disasterrecoveryconfig authorizationrule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus disasterrecoveryconfig authorizationrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('alias', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus disasterrecoveryconfig authorizationrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('alias', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus migrationconfiguration') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus migrationconfiguration_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus migrationconfiguration show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus migrationconfiguration list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus queue') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus queue_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus queue create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('lock_duration', name_arg_type, id_part=None)
        c.argument('max_size_in_megabytes', name_arg_type, id_part=None)
        c.argument('requires_duplicate_detection', name_arg_type, id_part=None)
        c.argument('requires_session', name_arg_type, id_part=None)
        c.argument('default_message_time_to_live', name_arg_type, id_part=None)
        c.argument('dead_lettering_on_message_expiration', name_arg_type, id_part=None)
        c.argument('duplicate_detection_history_time_window', name_arg_type, id_part=None)
        c.argument('max_delivery_count', name_arg_type, id_part=None)
        c.argument('status', name_arg_type, id_part=None)
        c.argument('enable_batched_operations', name_arg_type, id_part=None)
        c.argument('auto_delete_on_idle', name_arg_type, id_part=None)
        c.argument('enable_partitioning', name_arg_type, id_part=None)
        c.argument('enable_express', name_arg_type, id_part=None)
        c.argument('forward_to', name_arg_type, id_part=None)
        c.argument('forward_dead_lettered_messages_to', name_arg_type, id_part=None)
        c.argument('count_details', name_arg_type, id_part=None)
        c.argument('created_at', name_arg_type, id_part=None)
        c.argument('updated_at', name_arg_type, id_part=None)
        c.argument('accessed_at', name_arg_type, id_part=None)
        c.argument('size_in_bytes', name_arg_type, id_part=None)
        c.argument('message_count', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus queue authorizationrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus queue authorizationrule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus queue authorizationrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('queue_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus queue authorizationrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('queue_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus topic') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topic_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topic create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('default_message_time_to_live', name_arg_type, id_part=None)
        c.argument('max_size_in_megabytes', name_arg_type, id_part=None)
        c.argument('requires_duplicate_detection', name_arg_type, id_part=None)
        c.argument('duplicate_detection_history_time_window', name_arg_type, id_part=None)
        c.argument('enable_batched_operations', name_arg_type, id_part=None)
        c.argument('status', name_arg_type, id_part=None)
        c.argument('support_ordering', name_arg_type, id_part=None)
        c.argument('auto_delete_on_idle', name_arg_type, id_part=None)
        c.argument('enable_partitioning', name_arg_type, id_part=None)
        c.argument('enable_express', name_arg_type, id_part=None)
        c.argument('size_in_bytes', name_arg_type, id_part=None)
        c.argument('created_at', name_arg_type, id_part=None)
        c.argument('updated_at', name_arg_type, id_part=None)
        c.argument('accessed_at', name_arg_type, id_part=None)
        c.argument('subscription_count', name_arg_type, id_part=None)
        c.argument('count_details', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus topic authorizationrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topic authorizationrule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topic authorizationrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic authorizationrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus topic subscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topic subscription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topic subscription create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('lock_duration', name_arg_type, id_part=None)
        c.argument('requires_session', name_arg_type, id_part=None)
        c.argument('default_message_time_to_live', name_arg_type, id_part=None)
        c.argument('dead_lettering_on_filter_evaluation_exceptions', name_arg_type, id_part=None)
        c.argument('dead_lettering_on_message_expiration', name_arg_type, id_part=None)
        c.argument('duplicate_detection_history_time_window', name_arg_type, id_part=None)
        c.argument('max_delivery_count', name_arg_type, id_part=None)
        c.argument('status', name_arg_type, id_part=None)
        c.argument('enable_batched_operations', name_arg_type, id_part=None)
        c.argument('auto_delete_on_idle', name_arg_type, id_part=None)
        c.argument('forward_to', name_arg_type, id_part=None)
        c.argument('forward_dead_lettered_messages_to', name_arg_type, id_part=None)
        c.argument('message_count', name_arg_type, id_part=None)
        c.argument('created_at', name_arg_type, id_part=None)
        c.argument('accessed_at', name_arg_type, id_part=None)
        c.argument('updated_at', name_arg_type, id_part=None)
        c.argument('count_details', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus topic subscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topic subscription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topic subscription list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus topic subscription rule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topic subscription rule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topic subscription rule create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('subscription_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('action', name_arg_type, id_part=None)
        c.argument('filter_type', name_arg_type, id_part=None)
        c.argument('sql_filter', name_arg_type, id_part=None)
        c.argument('correlation_filter', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('subscription_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('subscription_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('subscription_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus topic subscription rule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus topic subscription rule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus topic subscription rule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('subscription_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('servicebus topic subscription rule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('namespace_name', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('subscription_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('servicebus') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus list') as c:
        c.argument('sku', name_arg_type, id_part=None)
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

    with self.argument_context('servicebus') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('servicebus_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('servicebus list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])