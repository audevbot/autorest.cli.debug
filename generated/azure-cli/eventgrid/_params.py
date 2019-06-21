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

    with self.argument_context('eventgrid eventsubscription') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename}') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename}_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename}') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid eventsubscription location topictype provider {providernamespace} {resourcetypename}') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid provider {providernamespace} {resourcetypename}') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid provider {providernamespace} {resourcetypename}_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid provider {providernamespace} {resourcetypename}') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid provider {providernamespace} {resourcetypename}') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('eventgrid') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('eventgrid_name', name_arg_type, options_list=['--name', '-n'])

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)

    with self.argument_context('eventgrid') as c:
        c.argument('eventgrid_name', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])