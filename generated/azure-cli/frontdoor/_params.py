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
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('location', id_part=None, help='Resource location.')
        c.argument('tags', id_part=None, help='Resource tags.')
        c.argument('properties', id_part=None, help='Properties of the Front Door Load Balancer')
        c.argument('friendly_name', id_part=None, help='A friendly name for the frontDoor')
        c.argument('routing_rules', id_part=None, help='Routing rules associated with this Front Door.')
        c.argument('load_balancing_settings', id_part=None, help='Load balancing settings associated with this Front Door instance.')
        c.argument('health_probe_settings', id_part=None, help='Health probe settings associated with this Front Door instance.')
        c.argument('backend_pools', id_part=None, help='Backend pools available to routing rules.')
        c.argument('frontend_endpoints', id_part=None, help='Frontend endpoints available to routing rules.')
        c.argument('backend_pools_settings', id_part=None, help='Settings for all backendPools')
        c.argument('enabled_state', id_part=None, help='Operational status of the Front Door load balancer. Permitted values are \'Enabled\' or \'Disabled\'')
        c.argument('resource_state', id_part=None, help='Resource status of the Front Door.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the Front Door.')
        c.argument('cname', id_part=None, help='The host that each frontendEndpoint must CNAME to.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('location', id_part=None, help='Resource location.')
        c.argument('tags', id_part=None, help='Resource tags.')
        c.argument('properties', id_part=None, help='Properties of the Front Door Load Balancer')
        c.argument('friendly_name', id_part=None, help='A friendly name for the frontDoor')
        c.argument('routing_rules', id_part=None, help='Routing rules associated with this Front Door.')
        c.argument('load_balancing_settings', id_part=None, help='Load balancing settings associated with this Front Door instance.')
        c.argument('health_probe_settings', id_part=None, help='Health probe settings associated with this Front Door instance.')
        c.argument('backend_pools', id_part=None, help='Backend pools available to routing rules.')
        c.argument('frontend_endpoints', id_part=None, help='Frontend endpoints available to routing rules.')
        c.argument('backend_pools_settings', id_part=None, help='Settings for all backendPools')
        c.argument('enabled_state', id_part=None, help='Operational status of the Front Door load balancer. Permitted values are \'Enabled\' or \'Disabled\'')
        c.argument('resource_state', id_part=None, help='Resource status of the Front Door.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the Front Door.')
        c.argument('cname', id_part=None, help='The host that each frontendEndpoint must CNAME to.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor routingrule create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Routing Rule which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the Front Door Routing Rule')
        c.argument('frontend_endpoints', id_part=None, help='Frontend endpoints associated with this rule')
        c.argument('accepted_protocols', id_part=None, help='Protocol schemes to match for this rule')
        c.argument('patterns_to_match', id_part=None, help='The route patterns of the rule.')
        c.argument('enabled_state', id_part=None, help='Whether to enable use of this rule. Permitted values are \'Enabled\' or \'Disabled\'')
        c.argument('route_configuration', id_part=None, help='A reference to the routing configuration.')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Routing Rule which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the Front Door Routing Rule')
        c.argument('frontend_endpoints', id_part=None, help='Frontend endpoints associated with this rule')
        c.argument('accepted_protocols', id_part=None, help='Protocol schemes to match for this rule')
        c.argument('patterns_to_match', id_part=None, help='The route patterns of the rule.')
        c.argument('enabled_state', id_part=None, help='Whether to enable use of this rule. Permitted values are \'Enabled\' or \'Disabled\'')
        c.argument('route_configuration', id_part=None, help='A reference to the routing configuration.')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Routing Rule which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor routingrule show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Routing Rule which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor healthprobesetting create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the health probe settings which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the health probe settings')
        c.argument('path', id_part=None, help='The path to use for the health probe. Default is /')
        c.argument('protocol', id_part=None, help='Protocol scheme to use for this probe')
        c.argument('interval_in_seconds', id_part=None, help='The number of seconds between health probes.')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the health probe settings which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the health probe settings')
        c.argument('path', id_part=None, help='The path to use for the health probe. Default is /')
        c.argument('protocol', id_part=None, help='Protocol scheme to use for this probe')
        c.argument('interval_in_seconds', id_part=None, help='The number of seconds between health probes.')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the health probe settings which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor healthprobesetting show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the health probe settings which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor loadbalancingsetting create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the load balancing settings which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the load balancing settings')
        c.argument('sample_size', id_part=None, help='The number of samples to consider for load balancing decisions')
        c.argument('successful_samples_required', id_part=None, help='The number of samples within the sample period that must succeed')
        c.argument('additional_latency_milliseconds', id_part=None, help='The additional latency in milliseconds for probes to fall into the lowest latency bucket')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the load balancing settings which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the load balancing settings')
        c.argument('sample_size', id_part=None, help='The number of samples to consider for load balancing decisions')
        c.argument('successful_samples_required', id_part=None, help='The number of samples within the sample period that must succeed')
        c.argument('additional_latency_milliseconds', id_part=None, help='The additional latency in milliseconds for probes to fall into the lowest latency bucket')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the load balancing settings which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor loadbalancingsetting show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the load balancing settings which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor backendpool create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Backend Pool which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the Front Door Backend Pool')
        c.argument('backends', id_part=None, help='The set of backends for this pool')
        c.argument('load_balancing_settings', id_part=None, help='Load balancing settings for a backend pool')
        c.argument('health_probe_settings', id_part=None, help='L7 health probe settings for a backend pool')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Backend Pool which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the Front Door Backend Pool')
        c.argument('backends', id_part=None, help='The set of backends for this pool')
        c.argument('load_balancing_settings', id_part=None, help='Load balancing settings for a backend pool')
        c.argument('health_probe_settings', id_part=None, help='L7 health probe settings for a backend pool')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Backend Pool which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor backendpool show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Backend Pool which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('frontdoor frontendendpoint create') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Frontend endpoint which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the Frontend endpoint')
        c.argument('host_name', id_part=None, help='The host name of the frontendEndpoint. Must be a domain name.')
        c.argument('session_affinity_enabled_state', id_part=None, help='Whether to allow session affinity on this host. Valid options are \'Enabled\' or \'Disabled\'')
        c.argument('session_affinity_ttl_seconds', id_part=None, help='UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable.')
        c.argument('web_application_firewall_policy_link', id_part=None, help='Defines the Web Application Firewall policy for each host (if applicable)')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('custom_https_provisioning_state', id_part=None, help='Provisioning status of Custom Https of the frontendEndpoint.')
        c.argument('custom_https_provisioning_substate', id_part=None, help='Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step.')
        c.argument('custom_https_configuration', id_part=None, help='The configuration specifying how to enable HTTPS')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint update') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Frontend endpoint which is unique within the Front Door.')
        c.argument('id', id_part=None, help='Resource ID.')
        c.argument('properties', id_part=None, help='Properties of the Frontend endpoint')
        c.argument('host_name', id_part=None, help='The host name of the frontendEndpoint. Must be a domain name.')
        c.argument('session_affinity_enabled_state', id_part=None, help='Whether to allow session affinity on this host. Valid options are \'Enabled\' or \'Disabled\'')
        c.argument('session_affinity_ttl_seconds', id_part=None, help='UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable.')
        c.argument('web_application_firewall_policy_link', id_part=None, help='Defines the Web Application Firewall policy for each host (if applicable)')
        c.argument('resource_state', id_part=None, help='Resource status.')
        c.argument('custom_https_provisioning_state', id_part=None, help='Provisioning status of Custom Https of the frontendEndpoint.')
        c.argument('custom_https_provisioning_substate', id_part=None, help='Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step.')
        c.argument('custom_https_configuration', id_part=None, help='The configuration specifying how to enable HTTPS')
        c.argument('type', id_part=None, help='Resource type.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint delete') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Frontend endpoint which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint list') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('frontdoor frontendendpoint show') as c:
        c.argument('resource_group', id_part=None, help='Name of the Resource group within the Azure subscription.')
        c.argument('front_door_name', id_part=None, help='Name of the Front Door which is globally unique.')
        c.argument('name', id_part=None, help='Name of the Frontend endpoint which is unique within the Front Door.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])