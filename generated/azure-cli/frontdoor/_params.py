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

    with self.argument_context('frontdoor') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('friendly_name', name_arg_type, id_part=None)
        c.argument('routing_rules', name_arg_type, id_part=None)
        c.argument('load_balancing_settings', name_arg_type, id_part=None)
        c.argument('health_probe_settings', name_arg_type, id_part=None)
        c.argument('backend_pools', name_arg_type, id_part=None)
        c.argument('frontend_endpoints', name_arg_type, id_part=None)
        c.argument('backend_pools_settings', name_arg_type, id_part=None)
        c.argument('enabled_state', name_arg_type, id_part=None)
        c.argument('resource_state', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('cname', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor routingrule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor routingrule create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('frontend_endpoints', name_arg_type, id_part=None)
        c.argument('accepted_protocols', name_arg_type, id_part=None)
        c.argument('patterns_to_match', name_arg_type, id_part=None)
        c.argument('enabled_state', name_arg_type, id_part=None)
        c.argument('route_configuration', name_arg_type, id_part=None)
        c.argument('resource_state', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor routingrule') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor routingrule_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor routingrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor healthprobesetting_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor healthprobesetting create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('path', name_arg_type, id_part=None)
        c.argument('protocol', name_arg_type, id_part=None)
        c.argument('interval_in_seconds', name_arg_type, id_part=None)
        c.argument('resource_state', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor healthprobesetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor healthprobesetting_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor healthprobesetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor loadbalancingsetting_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor loadbalancingsetting create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('sample_size', name_arg_type, id_part=None)
        c.argument('successful_samples_required', name_arg_type, id_part=None)
        c.argument('additional_latency_milliseconds', name_arg_type, id_part=None)
        c.argument('resource_state', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor loadbalancingsetting') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor loadbalancingsetting_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor loadbalancingsetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor backendpool_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor backendpool create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('backends', name_arg_type, id_part=None)
        c.argument('load_balancing_settings', name_arg_type, id_part=None)
        c.argument('health_probe_settings', name_arg_type, id_part=None)
        c.argument('resource_state', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor backendpool') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor backendpool_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor backendpool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor frontendendpoint_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor frontendendpoint create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('host_name', name_arg_type, id_part=None)
        c.argument('session_affinity_enabled_state', name_arg_type, id_part=None)
        c.argument('session_affinity_ttl_seconds', name_arg_type, id_part=None)
        c.argument('web_application_firewall_policy_link', name_arg_type, id_part=None)
        c.argument('resource_state', name_arg_type, id_part=None)
        c.argument('custom_https_provisioning_state', name_arg_type, id_part=None)
        c.argument('custom_https_provisioning_substate', name_arg_type, id_part=None)
        c.argument('custom_https_configuration', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('frontdoor frontendendpoint') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('frontdoor frontendendpoint_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('frontdoor frontendendpoint show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('front_door_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])