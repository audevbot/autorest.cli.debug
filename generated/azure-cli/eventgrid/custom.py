# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_eventgrid eventsubscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.create()


def update_eventgrid eventsubscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.update()


def delete_eventgrid eventsubscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.delete()


def list_eventgrid eventsubscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.list()


def show_eventgrid eventsubscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.show()


def list_eventgrid eventsubscriptions locations topictypes providers {providernamespace} {resourcetypename}(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.list()


def show_eventgrid eventsubscriptions locations topictypes providers {providernamespace} {resourcetypename}(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_subscriptions.show()


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.operations.list()


def create_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.create()


def update_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.update()


def delete_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.delete()


def list_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.list()


def show_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.show()


def list_eventgrid providers {providernamespace} {resourcetypename}(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.list()


def show_eventgrid providers {providernamespace} {resourcetypename}(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.show()


def list_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topic_types.list()


def show_eventgrid(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topic_types.show()