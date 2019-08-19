# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group


def load_arguments(self, _):
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('aro create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the OpenShift managed cluster resource.')
        c.argument('parameters', id_part=None, help='undefined')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('plan', id_part=None, help='Define the resource plan as required by ARM for billing purposes')
        c.argument('open_shift_version', id_part=None, help='Version of OpenShift specified when creating the cluster.')
        c.argument('network_profile', id_part=None, help='Configuration for OpenShift networking.')
        c.argument('router_profiles', id_part=None, help='Configuration for OpenShift router(s).')
        c.argument('master_pool_profile', id_part=None, help='Configuration for OpenShift master VMs.')
        c.argument('agent_pool_profiles', id_part=None, help='Configuration of OpenShift cluster VMs.')
        c.argument('auth_profile', id_part=None, help='Configures OpenShift authentication.')

    with self.argument_context('aro update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the OpenShift managed cluster resource.')
        c.argument('parameters', id_part=None, help='undefined')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('plan', id_part=None, help='Define the resource plan as required by ARM for billing purposes')
        c.argument('open_shift_version', id_part=None, help='Version of OpenShift specified when creating the cluster.')
        c.argument('network_profile', id_part=None, help='Configuration for OpenShift networking.')
        c.argument('router_profiles', id_part=None, help='Configuration for OpenShift router(s).')
        c.argument('master_pool_profile', id_part=None, help='Configuration for OpenShift master VMs.')
        c.argument('agent_pool_profiles', id_part=None, help='Configuration of OpenShift cluster VMs.')
        c.argument('auth_profile', id_part=None, help='Configures OpenShift authentication.')

    with self.argument_context('aro delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the OpenShift managed cluster resource.')

    with self.argument_context('aro list') as c:
        c.argument('resource_group', resource_group_name_type)

    with self.argument_context('aro show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the OpenShift managed cluster resource.')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])
