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

    with self.argument_context('eventgrid eventsubscription') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid eventsubscription_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid eventsubscription create') as c:
        c.argument('scope', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('destination', name_arg_type, id_part=None)
        c.argument('filter', name_arg_type, id_part=None)
        c.argument('labels', name_arg_type, id_part=None)
        c.argument('retry_policy', name_arg_type, id_part=None)
        c.argument('dead_letter_destination', name_arg_type, id_part=None)
        c.argument('topic', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription update') as c:
        c.argument('scope', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('destination', name_arg_type, id_part=None)
        c.argument('filter', name_arg_type, id_part=None)
        c.argument('labels', name_arg_type, id_part=None)
        c.argument('retry_policy', name_arg_type, id_part=None)
        c.argument('dead_letter_destination', name_arg_type, id_part=None)
        c.argument('topic', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription delete') as c:
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription list') as c:
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription show') as c:
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename}') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename}_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename} list') as c:
        c.argument('event_subscription_name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('topic_type_name', name_arg_type, id_part=None)
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('provider_namespace', name_arg_type, id_part=None)
        c.argument('resource_type_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename} show') as c:
        c.argument('event_subscription_name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('topic_type_name', name_arg_type, id_part=None)
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('provider_namespace', name_arg_type, id_part=None)
        c.argument('resource_type_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
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

    with self.argument_context('eventgrid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid create') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('endpoint', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid update') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('location', name_arg_type, id_part=None)
        c.argument('tags', name_arg_type, id_part=None)
        c.argument('properties', name_arg_type, id_part=None)
        c.argument('provisioning_state', name_arg_type, id_part=None)
        c.argument('endpoint', name_arg_type, id_part=None)
        c.argument('id', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('type', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid provider {providernamespace} {resourcetypename}') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid provider {providernamespace} {resourcetypename}_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid provider {providernamespace} {resourcetypename} list') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('provider_namespace', name_arg_type, id_part=None)
        c.argument('resource_type_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid provider {providernamespace} {resourcetypename} show') as c:
        c.argument('resource_group', name_arg_type, id_part=None)
        c.argument('topic_name', name_arg_type, id_part=None)
        c.argument('provider_namespace', name_arg_type, id_part=None)
        c.argument('resource_type_name', name_arg_type, id_part=None)
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid list') as c:
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid show') as c:
        c.argument('name', name_arg_type, id_part=None)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])