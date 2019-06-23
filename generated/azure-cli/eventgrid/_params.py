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


    with self.argument_context('eventgrid  eventsubscription create') as c:
        c.argument('scope', id_part=None, help='The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use \'/subscriptions/{subscriptionId}/\' for a subscription, \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}\' for a resource group, and \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}\' for a resource, and \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}\' for an EventGrid topic.')
        c.argument('name', id_part=None, help='Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.')
        c.argument('properties', id_part=None, help='Properties of the event subscription')
        c.argument('destination', id_part=None, help='Information about the destination where events have to be delivered for the event subscription.')
        c.argument('filter', id_part=None, help='Information about the filter for the event subscription.')
        c.argument('labels', id_part=None, help='List of user defined labels.')
        c.argument('retry_policy', id_part=None, help='The retry policy for events. This can be used to configure maximum number of delivery attempts and time to live for events.')
        c.argument('dead_letter_destination', id_part=None, help='The DeadLetter destination of the event subscription.')
        c.argument('topic', id_part=None, help='Name of the topic of the event subscription.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the event subscription.')
        c.argument('id', id_part=None, help='Fully qualified identifier of the resource')
        c.argument('type', id_part=None, help='Type of the resource')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid  eventsubscription update') as c:
        c.argument('scope', id_part=None, help='The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use \'/subscriptions/{subscriptionId}/\' for a subscription, \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}\' for a resource group, and \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}\' for a resource, and \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}\' for an EventGrid topic.')
        c.argument('name', id_part=None, help='Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.')
        c.argument('properties', id_part=None, help='Properties of the event subscription')
        c.argument('destination', id_part=None, help='Information about the destination where events have to be delivered for the event subscription.')
        c.argument('filter', id_part=None, help='Information about the filter for the event subscription.')
        c.argument('labels', id_part=None, help='List of user defined labels.')
        c.argument('retry_policy', id_part=None, help='The retry policy for events. This can be used to configure maximum number of delivery attempts and time to live for events.')
        c.argument('dead_letter_destination', id_part=None, help='The DeadLetter destination of the event subscription.')
        c.argument('topic', id_part=None, help='Name of the topic of the event subscription.')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the event subscription.')
        c.argument('id', id_part=None, help='Fully qualified identifier of the resource')
        c.argument('type', id_part=None, help='Type of the resource')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid  eventsubscription delete') as c:
        c.argument('name', id_part=None, help='Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid  eventsubscription list') as c:
        c.argument('name', id_part=None, help='Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid  eventsubscription show') as c:
        c.argument('name', id_part=None, help='Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('eventgrid topic create') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group within the user\'s subscription.')
        c.argument('name', id_part=None, help='Name of the topic')
        c.argument('location', id_part=None, help='Location of the resource')
        c.argument('tags', id_part=None, help='Tags of the resource')
        c.argument('properties', id_part=None, help='Properties of the topic')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the topic.')
        c.argument('endpoint', id_part=None, help='Endpoint for the topic.')
        c.argument('id', id_part=None, help='Fully qualified identifier of the resource')
        c.argument('type', id_part=None, help='Type of the resource')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid topic update') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group within the user\'s subscription.')
        c.argument('name', id_part=None, help='Name of the topic')
        c.argument('location', id_part=None, help='Location of the resource')
        c.argument('tags', id_part=None, help='Tags of the resource')
        c.argument('properties', id_part=None, help='Properties of the topic')
        c.argument('provisioning_state', id_part=None, help='Provisioning state of the topic.')
        c.argument('endpoint', id_part=None, help='Endpoint for the topic.')
        c.argument('id', id_part=None, help='Fully qualified identifier of the resource')
        c.argument('type', id_part=None, help='Type of the resource')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('eventgrid topic delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group within the user\'s subscription.')
        c.argument('name', id_part=None, help='Name of the topic')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid topic list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group within the user\'s subscription.')
        c.argument('name', id_part=None, help='Name of the topic')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('eventgrid topic show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group within the user\'s subscription.')
        c.argument('name', id_part=None, help='Name of the topic')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])