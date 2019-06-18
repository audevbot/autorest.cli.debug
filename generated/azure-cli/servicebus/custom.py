# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.operations.list()


def create_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.create()


def update_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.update()


def delete_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.delete()


def list_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.list()


def show_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.show()


def list_servicebus authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.list()


def show_servicebus authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.namespaces.show()


def create_servicebus disasterrecoveryconfigs(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.disaster_recovery_configs.create()


def delete_servicebus disasterrecoveryconfigs(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.disaster_recovery_configs.delete()


def list_servicebus disasterrecoveryconfigs(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.disaster_recovery_configs.list()


def show_servicebus disasterrecoveryconfigs(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.disaster_recovery_configs.show()


def list_servicebus disasterrecoveryconfigs authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.disaster_recovery_configs.list()


def show_servicebus disasterrecoveryconfigs authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.disaster_recovery_configs.show()


def show_servicebus migrationconfigurations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.migration_configs.show()


def list_servicebus migrationconfigurations(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.migration_configs.list()


def create_servicebus queues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.queues.create()


def delete_servicebus queues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.queues.delete()


def list_servicebus queues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.queues.list()


def show_servicebus queues(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.queues.show()


def list_servicebus queues authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.queues.list()


def show_servicebus queues authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.queues.show()


def create_servicebus topics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.create()


def delete_servicebus topics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.delete()


def list_servicebus topics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.list()


def show_servicebus topics(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.show()


def list_servicebus topics authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.list()


def show_servicebus topics authorizationrules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.topics.show()


def create_servicebus topics subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscriptions.create()


def delete_servicebus topics subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscriptions.delete()


def list_servicebus topics subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscriptions.list()


def show_servicebus topics subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscriptions.show()


def list_servicebus topics subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscriptions.list()


def show_servicebus topics subscriptions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.subscriptions.show()


def create_servicebus topics subscriptions rules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.rules.create()


def delete_servicebus topics subscriptions rules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.rules.delete()


def list_servicebus topics subscriptions rules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.rules.list()


def show_servicebus topics subscriptions rules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.rules.show()


def show_servicebus topics subscriptions rules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.rules.show()


def list_servicebus topics subscriptions rules(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.rules.list()


def list_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.regions.list()


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.premium_messaging_regions.list()


def list_servicebus(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.event_hubs.list()