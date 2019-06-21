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


    with self.argument_context('frontdoor create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('location', name_arg_type, id_part=None,Resource location.)
        c.argument('tags', name_arg_type, id_part=None,Resource tags.)
        c.argument('properties', name_arg_type, id_part=None,Properties of the Front Door Load Balancer)
        c.argument('friendly_name', name_arg_type, id_part=None,A friendly name for the frontDoor)
        c.argument('routing_rules', name_arg_type, id_part=None,Routing rules associated with this Front Door.)
        c.argument('load_balancing_settings', name_arg_type, id_part=None,Load balancing settings associated with this Front Door instance.)
        c.argument('health_probe_settings', name_arg_type, id_part=None,Health probe settings associated with this Front Door instance.)
        c.argument('backend_pools', name_arg_type, id_part=None,Backend pools available to routing rules.)
        c.argument('frontend_endpoints', name_arg_type, id_part=None,Frontend endpoints available to routing rules.)
        c.argument('backend_pools_settings', name_arg_type, id_part=None,Settings for all backendPools)
        c.argument('enabled_state', name_arg_type, id_part=None,Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled')
        c.argument('resource_state', name_arg_type, id_part=None,Resource status of the Front Door.)
        c.argument('provisioning_state', name_arg_type, id_part=None,Provisioning state of the Front Door.)
        c.argument('cname', name_arg_type, id_part=None,The host that each frontendEndpoint must CNAME to.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor routingrule create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Routing Rule which is unique within the Front Door.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('properties', name_arg_type, id_part=None,Properties of the Front Door Routing Rule)
        c.argument('frontend_endpoints', name_arg_type, id_part=None,Frontend endpoints associated with this rule)
        c.argument('accepted_protocols', name_arg_type, id_part=None,Protocol schemes to match for this rule)
        c.argument('patterns_to_match', name_arg_type, id_part=None,The route patterns of the rule.)
        c.argument('enabled_state', name_arg_type, id_part=None,Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled')
        c.argument('route_configuration', name_arg_type, id_part=None,A reference to the routing configuration.)
        c.argument('resource_state', name_arg_type, id_part=None,Resource status.)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Routing Rule which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Routing Rule which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Routing Rule which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor routingrule show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Routing Rule which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Routing Rule which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor healthprobesetting create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the health probe settings which is unique within the Front Door.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('properties', name_arg_type, id_part=None,Properties of the health probe settings)
        c.argument('path', name_arg_type, id_part=None,The path to use for the health probe. Default is /)
        c.argument('protocol', name_arg_type, id_part=None,Protocol scheme to use for this probe)
        c.argument('interval_in_seconds', name_arg_type, id_part=None,The number of seconds between health probes.)
        c.argument('resource_state', name_arg_type, id_part=None,Resource status.)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the health probe settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the health probe settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the health probe settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor healthprobesetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the health probe settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the health probe settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor loadbalancingsetting create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the load balancing settings which is unique within the Front Door.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('properties', name_arg_type, id_part=None,Properties of the load balancing settings)
        c.argument('sample_size', name_arg_type, id_part=None,The number of samples to consider for load balancing decisions)
        c.argument('successful_samples_required', name_arg_type, id_part=None,The number of samples within the sample period that must succeed)
        c.argument('additional_latency_milliseconds', name_arg_type, id_part=None,The additional latency in milliseconds for probes to fall into the lowest latency bucket)
        c.argument('resource_state', name_arg_type, id_part=None,Resource status.)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the load balancing settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the load balancing settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the load balancing settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor loadbalancingsetting show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the load balancing settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the load balancing settings which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor backendpool create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Backend Pool which is unique within the Front Door.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('properties', name_arg_type, id_part=None,Properties of the Front Door Backend Pool)
        c.argument('backends', name_arg_type, id_part=None,The set of backends for this pool)
        c.argument('load_balancing_settings', name_arg_type, id_part=None,Load balancing settings for a backend pool)
        c.argument('health_probe_settings', name_arg_type, id_part=None,L7 health probe settings for a backend pool)
        c.argument('resource_state', name_arg_type, id_part=None,Resource status.)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Backend Pool which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Backend Pool which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Backend Pool which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor backendpool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Backend Pool which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Backend Pool which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor frontendendpoint create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Frontend endpoint which is unique within the Front Door.)
        c.argument('id', name_arg_type, id_part=None,Resource ID.)
        c.argument('properties', name_arg_type, id_part=None,Properties of the Frontend endpoint)
        c.argument('host_name', name_arg_type, id_part=None,The host name of the frontendEndpoint. Must be a domain name.)
        c.argument('session_affinity_enabled_state', name_arg_type, id_part=None,Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled')
        c.argument('session_affinity_ttl_seconds', name_arg_type, id_part=None,UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable.)
        c.argument('web_application_firewall_policy_link', name_arg_type, id_part=None,Defines the Web Application Firewall policy for each host (if applicable))
        c.argument('resource_state', name_arg_type, id_part=None,Resource status.)
        c.argument('custom_https_provisioning_state', name_arg_type, id_part=None,Provisioning status of Custom Https of the frontendEndpoint.)
        c.argument('custom_https_provisioning_substate', name_arg_type, id_part=None,Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step.)
        c.argument('custom_https_configuration', name_arg_type, id_part=None,The configuration specifying how to enable HTTPS)
        c.argument('name', name_arg_type, id_part=None,Resource name.)
        c.argument('type', name_arg_type, id_part=None,Resource type.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Frontend endpoint which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Frontend endpoint which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Frontend endpoint which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor frontendendpoint show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Frontend endpoint which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,Name of the Resource group within the Azure subscription.)
        c.argument('front_door_name', name_arg_type, id_part=None,Name of the Front Door which is globally unique.)
        c.argument('name', name_arg_type, id_part=None,Name of the Frontend endpoint which is unique within the Front Door.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])