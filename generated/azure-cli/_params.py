# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)


def load_arguments(self, _):

    with self.argument_context('alerts create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('alert_rule_name', id_part=None, help='The name of the alert rule.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('description', id_part=None, help='The alert rule description.')
        c.argument('state', arg_type=get_enum_type(['Enabled', 'Disabled']), id_part=None, help='The alert rule state.')
        c.argument('severity', arg_type=get_enum_type(['Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4']), id_part=None, help='The alert rule severity.')
        c.argument('frequency', id_part=None, help='The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes.')
        c.argument('detector', id_part=None, help='The alert rule\'s detector.')
        c.argument('scope', id_part=None, help='The alert rule resources scope.')
        c.argument('action_groups', id_part=None, help='The alert rule actions.')
        c.argument('throttling', id_part=None, help='The alert rule throttling information.')

    with self.argument_context('alerts update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('alert_rule_name', id_part=None, help='The name of the alert rule.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('description', id_part=None, help='The alert rule description.')
        c.argument('state', arg_type=get_enum_type(['Enabled', 'Disabled']), id_part=None, help='The alert rule state.')
        c.argument('severity', arg_type=get_enum_type(['Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4']), id_part=None, help='The alert rule severity.')
        c.argument('frequency', id_part=None, help='The alert rule frequency in ISO8601 format. The time granularity must be in minutes and minimum value is 5 minutes.')
        c.argument('detector', id_part=None, help='The alert rule\'s detector.')
        c.argument('scope', id_part=None, help='The alert rule resources scope.')
        c.argument('action_groups', id_part=None, help='The alert rule actions.')
        c.argument('throttling', id_part=None, help='The alert rule throttling information.')

    with self.argument_context('alerts delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('alert_rule_name', id_part=None, help='The name of the alert rule.')

    with self.argument_context('alerts list') as c:
        c.argument('resource_group', resource_group_name_type)

    with self.argument_context('alerts show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('alert_rule_name', id_part=None, help='The name of the alert rule.')
