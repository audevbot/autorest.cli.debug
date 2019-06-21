# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_eventgrid_eventsubscription(cmd, client,
                                       scope,
                                       name,
                                       properties,
                                       destination,
                                       filter,
                                       labels,
                                       retry_policy,
                                       dead_letter_destination,
                                       topic,
                                       provisioning_state,
                                       id,
                                       name,
                                       type):
    return client.event_subscriptions.create()


def update_eventgrid_eventsubscription(cmd, client,
                                       scope,
                                       name,
                                       properties,
                                       destination,
                                       filter,
                                       labels,
                                       retry_policy,
                                       dead_letter_destination,
                                       topic,
                                       provisioning_state,
                                       id,
                                       name,
                                       type):
    return client.event_subscriptions.update()


def delete_eventgrid_eventsubscription(cmd, client,
                                       name):
    return client.event_subscriptions.delete()


def list_eventgrid_eventsubscription(cmd, client,
                                     name):
    return client.event_subscriptions.list()


def show_eventgrid_eventsubscription(cmd, client,
                                     name):
    return client.event_subscriptions.show()


def list_eventgrid_eventsubscription_location_topictype_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                                                        event_subscription_name,
                                                                                                        location,
                                                                                                        topic_type_name,
                                                                                                        resource_group,
                                                                                                        provider_namespace,
                                                                                                        resource_type_name,
                                                                                                        name):
    return client.event_subscriptions.list()


def show_eventgrid_eventsubscription_location_topictype_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                                                        event_subscription_name,
                                                                                                        location,
                                                                                                        topic_type_name,
                                                                                                        resource_group,
                                                                                                        provider_namespace,
                                                                                                        resource_type_name,
                                                                                                        name):
    return client.event_subscriptions.show()


def list_(cmd, client):
    return client.operations.list()


def create_eventgrid(cmd, client,
                     resource_group,
                     name,
                     location,
                     tags,
                     properties,
                     provisioning_state,
                     endpoint,
                     id,
                     name,
                     type):
    return client.topics.create()


def update_eventgrid(cmd, client,
                     resource_group,
                     name,
                     location,
                     tags,
                     properties,
                     provisioning_state,
                     endpoint,
                     id,
                     name,
                     type):
    return client.topics.update()


def delete_eventgrid(cmd, client,
                     resource_group,
                     name):
    return client.topics.delete()


def list_eventgrid(cmd, client,
                   resource_group,
                   name):
    return client.topics.list()


def show_eventgrid(cmd, client,
                   resource_group,
                   name):
    return client.topics.show()


def list_eventgrid_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                   resource_group,
                                                                   topic_name,
                                                                   provider_namespace,
                                                                   resource_type_name,
                                                                   name):
    return client.topics.list()


def show_eventgrid_provider_{providernamespace}_{resourcetypename}(cmd, client,
                                                                   resource_group,
                                                                   topic_name,
                                                                   provider_namespace,
                                                                   resource_type_name,
                                                                   name):
    return client.topics.show()


def list_eventgrid(cmd, client,
                   name):
    return client.topic_types.list()


def show_eventgrid(cmd, client,
                   name):
    return client.topic_types.show()