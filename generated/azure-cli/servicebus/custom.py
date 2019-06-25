# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_servicebusnamespace
def create_servicebus(cmd, client,
                      resource_group,
                      name,
                      parameters=None):
    body={}
    return client.namespaces.create_or_update(resource_group_name=resource_group, namespace_name=name, parameters=body)

# module equivalent: azure_rm_servicebusnamespace
def update_servicebus(cmd, client,
                      resource_group,
                      name,
                      parameters=None):
    body={}
    return client.namespaces.create_or_update(resource_group_name=resource_group, namespace_name=name, parameters=body)

# module equivalent: azure_rm_servicebusnamespace
def delete_servicebus(cmd, client,
                      resource_group,
                      name):
    return client.namespaces.delete(resource_group_name=resource_group, namespace_name=name)

# module equivalent: azure_rm_servicebusnamespace
def list_servicebus(cmd, client,
                    resource_group,
                    name):
    if resource_group is not None and name is not None:
        return client.namespaces.list_authorization_rules(resource_group_name=resource_group, namespace_name=name)
    elif resource_group is not None:
        return client.namespaces.list_by_resource_group(resource_group_name=resource_group)
    else:
        return client.namespaces.list()

# module equivalent: azure_rm_servicebusnamespace
def show_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.namespaces.get(resource_group_name=resource_group, namespace_name=name)

# module equivalent: azure_rm_servicebusdisasterrecoveryconfig
def create_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias,
                                             parameters=None):
    body={}
    return client.disaster_recovery_configs.create_or_update(resource_group_name=resource_group, namespace_name=name, alias=alias, parameters=body)

# module equivalent: azure_rm_servicebusdisasterrecoveryconfig
def update_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias,
                                             parameters=None):
    body={}
    return client.disaster_recovery_configs.create_or_update(resource_group_name=resource_group, namespace_name=name, alias=alias, parameters=body)

# module equivalent: azure_rm_servicebusdisasterrecoveryconfig
def delete_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias):
    return client.disaster_recovery_configs.delete(resource_group_name=resource_group, namespace_name=name, alias=alias)

# module equivalent: azure_rm_servicebusdisasterrecoveryconfig
def list_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    if resource_group is not None and name is not None and alias is not None:
        return client.disaster_recovery_configs.list_authorization_rules(resource_group_name=resource_group, namespace_name=name, alias=alias)
    else:
        return client.disaster_recovery_configs.list(resource_group_name=resource_group, namespace_name=name)

# module equivalent: azure_rm_servicebusdisasterrecoveryconfig
def show_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    return client.disaster_recovery_configs.get(resource_group_name=resource_group, namespace_name=name, alias=alias)

# module equivalent: azure_rm_servicebusqueue
def create_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            parameters=None):
    body={}
    return client.queues.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name, parameters=body)

# module equivalent: azure_rm_servicebusqueue
def update_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            parameters=None):
    body={}
    return client.queues.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name, parameters=body)

# module equivalent: azure_rm_servicebusqueue
def delete_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    return client.queues.delete(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name)

# module equivalent: azure_rm_servicebusqueue
def list_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    if resource_group is not None and namespace_name is not None and name is not None:
        return client.queues.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name)
    else:
        return client.queues.list_by_namespace(resource_group_name=resource_group, namespace_name=namespace_name)

# module equivalent: azure_rm_servicebusqueue
def show_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.queues.get(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name)

# module equivalent: azure_rm_servicebustopic
def create_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            parameters=None):
    body={}
    return client.topics.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name, parameters=body)

# module equivalent: azure_rm_servicebustopic
def update_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            parameters=None):
    body={}
    return client.topics.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name, parameters=body)

# module equivalent: azure_rm_servicebustopic
def delete_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    return client.topics.delete(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name)

# module equivalent: azure_rm_servicebustopic
def list_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    if resource_group is not None and namespace_name is not None and name is not None:
        return client.topics.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name)
    else:
        return client.topics.list_by_namespace(resource_group_name=resource_group, namespace_name=namespace_name)

# module equivalent: azure_rm_servicebustopic
def show_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.topics.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name)

# module equivalent: azure_rm_servicebussubscription
def create_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name,
                                         parameters=None):
    body={}
    return client.subscriptions.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name, parameters=body)

# module equivalent: azure_rm_servicebussubscription
def update_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name,
                                         parameters=None):
    body={}
    return client.subscriptions.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name, parameters=body)

# module equivalent: azure_rm_servicebussubscription
def delete_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name):
    return client.subscriptions.delete(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)

# module equivalent: azure_rm_servicebussubscription
def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name):
    return client.subscriptions.list_by_topic(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name)

# module equivalent: azure_rm_servicebussubscription
def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)

# module equivalent: azure_rm_servicebusrule
def create_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name,
                                              parameters=None):
    body={}
    return client.rules.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name, parameters=body)

# module equivalent: azure_rm_servicebusrule
def update_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name,
                                              parameters=None):
    body={}
    return client.rules.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name, parameters=body)

# module equivalent: azure_rm_servicebusrule
def delete_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name):
    return client.rules.delete(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)

# module equivalent: azure_rm_servicebusrule
def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name):
    return client.rules.list_by_subscriptions(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name)

# module equivalent: azure_rm_servicebusrule
def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)