# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_eventgrid_eventsubscription(cmd, client,
                                       scope=None,
                                       name,
                                       properties=None,
                                       destination=None,
                                       filter=None,
                                       labels=None,
                                       retry_policy=None,
                                       dead_letter_destination=None,
                                       topic=None,
                                       provisioning_state=None,
                                       id=None,
                                       type=None):
    body={}
    body['properties'] = properties
    body['destination'] = destination
    body['filter'] = filter
    body['labels'] = labels
    body['retry_policy'] = retry_policy
    body['dead_letter_destination'] = dead_letter_destination
    body['topic'] = topic
    body['provisioning_state'] = provisioning_state
    return client.event_subscriptions.create_or_update(scope=scope, event_subscription_name=name, eventSubscriptionInfo=eventSubscriptionInfo)


def update_eventgrid_eventsubscription(cmd, client,
                                       scope=None,
                                       name,
                                       properties=None,
                                       destination=None,
                                       filter=None,
                                       labels=None,
                                       retry_policy=None,
                                       dead_letter_destination=None,
                                       topic=None,
                                       provisioning_state=None,
                                       id=None,
                                       type=None):
    body={}
    body['properties'] = properties
    body['destination'] = destination
    body['filter'] = filter
    body['labels'] = labels
    body['retry_policy'] = retry_policy
    body['dead_letter_destination'] = dead_letter_destination
    body['topic'] = topic
    body['provisioning_state'] = provisioning_state
    return client.event_subscriptions.create_or_update(scope=scope, event_subscription_name=name, eventSubscriptionInfo=eventSubscriptionInfo)


def delete_eventgrid_eventsubscription(cmd, client,
                                       name):
    body={}
    return client.event_subscriptions.delete(scope=scope, event_subscription_name=name)


def list_eventgrid_eventsubscription(cmd, client,
                                     name):
    body={}
    return client.event_subscriptions.list_global_by_subscription(scope=scope, event_subscription_name=name)


def show_eventgrid_eventsubscription(cmd, client,
                                     name):
    body={}
    return client.event_subscriptions.get(scope=scope, event_subscription_name=name)


def list_eventgrid_eventsubscription_location_topictype_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                                                        event_subscription_name,
                                                                                                        location,
                                                                                                        topic_type_name,
                                                                                                        resource_group,
                                                                                                        provider_namespace,
                                                                                                        resource_type_name,
                                                                                                        name):
    body={}
    return client.event_subscriptions.list_by_resource(scope=scope, event_subscription_name=event_subscription_name)


def show_eventgrid_eventsubscription_location_topictype_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                                                        event_subscription_name,
                                                                                                        location,
                                                                                                        topic_type_name,
                                                                                                        resource_group,
                                                                                                        provider_namespace,
                                                                                                        resource_type_name,
                                                                                                        name):
    body={}
    return client.event_subscriptions.get(scope=scope, event_subscription_name=event_subscription_name)


def list_(cmd, client):
    body={}
    return client.operations.list()


def create_eventgrid(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None,
                     properties=None,
                     provisioning_state=None,
                     endpoint=None,
                     id=None,
                     type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['provisioning_state'] = provisioning_state
    body['endpoint'] = endpoint
    return client.topics.create_or_update(resource_group_name=resource_group, topic_name=name, topicInfo=topicInfo)


def update_eventgrid(cmd, client,
                     resource_group,
                     name,
                     location=None,
                     tags=None,
                     properties=None,
                     provisioning_state=None,
                     endpoint=None,
                     id=None,
                     type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['provisioning_state'] = provisioning_state
    body['endpoint'] = endpoint
    return client.topics.create_or_update(resource_group_name=resource_group, topic_name=name, topicInfo=topicInfo)


def delete_eventgrid(cmd, client,
                     resource_group,
                     name):
    body={}
    return client.topics.delete(resource_group_name=resource_group, topic_name=name)


def list_eventgrid(cmd, client,
                   resource_group,
                   name):
    body={}
    return client.topics.list_by_subscription(resource_group_name=resource_group, topic_name=name)


def show_eventgrid(cmd, client,
                   resource_group,
                   name):
    body={}
    return client.topics.get(resource_group_name=resource_group, topic_name=name)


def list_eventgrid_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                   resource_group,
                                                                   topic_name,
                                                                   provider_namespace,
                                                                   resource_type_name,
                                                                   name):
    body={}
    return client.topics.list_event_types(resource_group_name=resource_group, topic_name=topic_name)


def show_eventgrid_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                   resource_group,
                                                                   topic_name,
                                                                   provider_namespace,
                                                                   resource_type_name,
                                                                   name):
    body={}
    return client.topics.get(resource_group_name=resource_group, topic_name=topic_name)


def list_eventgrid(cmd, client,
                   name):
    body={}
    return client.topic_types.list_event_types(topic_type_name=name)


def show_eventgrid(cmd, client,
                   name):
    body={}
    return client.topic_types.get(topic_type_name=name)