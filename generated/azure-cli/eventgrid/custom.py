# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_eventgrideventsubscription
def create_eventgrid(cmd, client,
                     name,
                     scope=None,
                     filter=None,
                     labels=None,
                     retry_policy=None):
    body={}
    body['filter'] = filter
    body['labels'] = labels
    body['retry_policy'] = retry_policy
    return client.event_subscriptions.create_or_update(scope=scope, event_subscription_name=name)

# module equivalent: azure_rm_eventgrideventsubscription
def update_eventgrid(cmd, client,
                     name,
                     scope=None,
                     filter=None,
                     labels=None,
                     retry_policy=None):
    body={}
    body['filter'] = filter
    body['labels'] = labels
    body['retry_policy'] = retry_policy
    return client.event_subscriptions.create_or_update(scope=scope, event_subscription_name=name)

# module equivalent: azure_rm_eventgrideventsubscription
def delete_eventgrid(cmd, client,
                     name,
                     scope=None):
    return client.event_subscriptions.delete(scope=scope, event_subscription_name=name)

# module equivalent: azure_rm_eventgrideventsubscription
def list_eventgrid(cmd, client):
    if:
        return client.event_subscriptions.list_by_resource()
    elif:
        return client.event_subscriptions.list_regional_by_resource_group_for_topic_type()
    elif:
        return client.event_subscriptions.list_global_by_resource_group_for_topic_type()
    elif:
        return client.event_subscriptions.list_regional_by_resource_group()
    elif:
        return client.event_subscriptions.list_regional_by_subscription_for_topic_type()
    elif:
        return client.event_subscriptions.list_global_by_resource_group()
    elif:
        return client.event_subscriptions.list_global_by_subscription_for_topic_type()
    elif:
        return client.event_subscriptions.list_regional_by_subscription()
    else:
        return client.event_subscriptions.list_global_by_subscription()

# module equivalent: azure_rm_eventgrideventsubscription
def show_eventgrid(cmd, client,
                   name,
                   scope=None):
    return client.event_subscriptions.get(scope=scope, event_subscription_name=name)

# module equivalent: azure_rm_eventgridtopic
def create_eventgrid(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    return client.topics.create_or_update(resource_group_name=resource_group, topic_name=name)

# module equivalent: azure_rm_eventgridtopic
def update_eventgrid(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    return client.topics.create_or_update(resource_group_name=resource_group, topic_name=name)

# module equivalent: azure_rm_eventgridtopic
def delete_eventgrid(cmd, client,
                     resource_group,
                     name):
    return client.topics.delete(resource_group_name=resource_group, topic_name=name)

# module equivalent: azure_rm_eventgridtopic
def list_eventgrid(cmd, client,
                   resource_group):
    if resource_group is not None:
        return client.topics.list_event_types(resource_group_name=resource_group)
    elif resource_group is not None:
        return client.topics.list_by_resource_group(resource_group_name=resource_group)
    else:
        return client.topics.list_by_subscription()

# module equivalent: azure_rm_eventgridtopic
def show_eventgrid(cmd, client,
                   resource_group,
                   name):
    return client.topics.get(resource_group_name=resource_group, topic_name=name)