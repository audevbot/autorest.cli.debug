# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import json

# module equivalent: azure_rm_servicebusnamespace
def create_servicebus(cmd, client,
                      resource_group,
                      name,
                      location=None,
                      tags=None,
                      sku=None):
    body={}
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"13","$type":"DictionaryType","valueType":{"$id":"14","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"15","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"16","fixed":false},"deprecated":false}]
    body['sku'] = json.loads(sku) if isinstance(sku, str) else sku
    return client.namespaces.create_or_update(resource_group_name=resource_group, namespace_name=name, parameters=body)

# module equivalent: azure_rm_servicebusnamespace
def update_servicebus(cmd, client,
                      resource_group,
                      name,
                      location=None,
                      tags=None,
                      sku=None):
    body={}
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"13","$type":"DictionaryType","valueType":{"$id":"14","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"15","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"16","fixed":false},"deprecated":false}]
    body['sku'] = json.loads(sku) if isinstance(sku, str) else sku
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
                                             partner_namespace=None,
                                             alternate_name=None):
    body={}
    body['partner_namespace'] = partner_namespace # str
    body['alternate_name'] = alternate_name # str
    return client.disaster_recovery_configs.create_or_update(resource_group_name=resource_group, namespace_name=name, alias=alias, parameters=body)

# module equivalent: azure_rm_servicebusdisasterrecoveryconfig
def update_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias,
                                             partner_namespace=None,
                                             alternate_name=None):
    body={}
    body['partner_namespace'] = partner_namespace # str
    body['alternate_name'] = alternate_name # str
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
                            lock_duration=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            requires_session=None,
                            default_message_time_to_live=None,
                            dead_lettering_on_message_expiration=None,
                            duplicate_detection_history_time_window=None,
                            max_delivery_count=None,
                            status=None,
                            enable_batched_operations=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None,
                            forward_to=None,
                            forward_dead_lettered_messages_to=None):
    body={}
    body['lock_duration'] = lock_duration # unknown-primary[timeSpan]
    body['max_size_in_megabytes'] = max_size_in_megabytes # number
    body['requires_duplicate_detection'] = requires_duplicate_detection # boolean
    body['requires_session'] = requires_session # boolean
    body['default_message_time_to_live'] = default_message_time_to_live # unknown-primary[timeSpan]
    body['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration # boolean
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window # unknown-primary[timeSpan]
    body['max_delivery_count'] = max_delivery_count # number
    body['status'] = status # str
    body['enable_batched_operations'] = enable_batched_operations # boolean
    body['auto_delete_on_idle'] = auto_delete_on_idle # unknown-primary[timeSpan]
    body['enable_partitioning'] = enable_partitioning # boolean
    body['enable_express'] = enable_express # boolean
    body['forward_to'] = forward_to # str
    body['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to # str
    return client.queues.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name, parameters=body)

# module equivalent: azure_rm_servicebusqueue
def update_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            lock_duration=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            requires_session=None,
                            default_message_time_to_live=None,
                            dead_lettering_on_message_expiration=None,
                            duplicate_detection_history_time_window=None,
                            max_delivery_count=None,
                            status=None,
                            enable_batched_operations=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None,
                            forward_to=None,
                            forward_dead_lettered_messages_to=None):
    body={}
    body['lock_duration'] = lock_duration # unknown-primary[timeSpan]
    body['max_size_in_megabytes'] = max_size_in_megabytes # number
    body['requires_duplicate_detection'] = requires_duplicate_detection # boolean
    body['requires_session'] = requires_session # boolean
    body['default_message_time_to_live'] = default_message_time_to_live # unknown-primary[timeSpan]
    body['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration # boolean
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window # unknown-primary[timeSpan]
    body['max_delivery_count'] = max_delivery_count # number
    body['status'] = status # str
    body['enable_batched_operations'] = enable_batched_operations # boolean
    body['auto_delete_on_idle'] = auto_delete_on_idle # unknown-primary[timeSpan]
    body['enable_partitioning'] = enable_partitioning # boolean
    body['enable_express'] = enable_express # boolean
    body['forward_to'] = forward_to # str
    body['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to # str
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
                            default_message_time_to_live=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            duplicate_detection_history_time_window=None,
                            enable_batched_operations=None,
                            status=None,
                            support_ordering=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None):
    body={}
    body['default_message_time_to_live'] = default_message_time_to_live # unknown-primary[timeSpan]
    body['max_size_in_megabytes'] = max_size_in_megabytes # number
    body['requires_duplicate_detection'] = requires_duplicate_detection # boolean
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window # unknown-primary[timeSpan]
    body['enable_batched_operations'] = enable_batched_operations # boolean
    body['status'] = status # str
    body['support_ordering'] = support_ordering # boolean
    body['auto_delete_on_idle'] = auto_delete_on_idle # unknown-primary[timeSpan]
    body['enable_partitioning'] = enable_partitioning # boolean
    body['enable_express'] = enable_express # boolean
    return client.topics.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name, parameters=body)

# module equivalent: azure_rm_servicebustopic
def update_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            default_message_time_to_live=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            duplicate_detection_history_time_window=None,
                            enable_batched_operations=None,
                            status=None,
                            support_ordering=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None):
    body={}
    body['default_message_time_to_live'] = default_message_time_to_live # unknown-primary[timeSpan]
    body['max_size_in_megabytes'] = max_size_in_megabytes # number
    body['requires_duplicate_detection'] = requires_duplicate_detection # boolean
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window # unknown-primary[timeSpan]
    body['enable_batched_operations'] = enable_batched_operations # boolean
    body['status'] = status # str
    body['support_ordering'] = support_ordering # boolean
    body['auto_delete_on_idle'] = auto_delete_on_idle # unknown-primary[timeSpan]
    body['enable_partitioning'] = enable_partitioning # boolean
    body['enable_express'] = enable_express # boolean
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
                                         lock_duration=None,
                                         requires_session=None,
                                         default_message_time_to_live=None,
                                         dead_lettering_on_filter_evaluation_exceptions=None,
                                         dead_lettering_on_message_expiration=None,
                                         duplicate_detection_history_time_window=None,
                                         max_delivery_count=None,
                                         status=None,
                                         enable_batched_operations=None,
                                         auto_delete_on_idle=None,
                                         forward_to=None,
                                         forward_dead_lettered_messages_to=None):
    body={}
    body['lock_duration'] = lock_duration # unknown-primary[timeSpan]
    body['requires_session'] = requires_session # boolean
    body['default_message_time_to_live'] = default_message_time_to_live # unknown-primary[timeSpan]
    body['dead_lettering_on_filter_evaluation_exceptions'] = dead_lettering_on_filter_evaluation_exceptions # boolean
    body['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration # boolean
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window # unknown-primary[timeSpan]
    body['max_delivery_count'] = max_delivery_count # number
    body['status'] = status # str
    body['enable_batched_operations'] = enable_batched_operations # boolean
    body['auto_delete_on_idle'] = auto_delete_on_idle # unknown-primary[timeSpan]
    body['forward_to'] = forward_to # str
    body['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to # str
    return client.subscriptions.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name, parameters=body)

# module equivalent: azure_rm_servicebussubscription
def update_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name,
                                         lock_duration=None,
                                         requires_session=None,
                                         default_message_time_to_live=None,
                                         dead_lettering_on_filter_evaluation_exceptions=None,
                                         dead_lettering_on_message_expiration=None,
                                         duplicate_detection_history_time_window=None,
                                         max_delivery_count=None,
                                         status=None,
                                         enable_batched_operations=None,
                                         auto_delete_on_idle=None,
                                         forward_to=None,
                                         forward_dead_lettered_messages_to=None):
    body={}
    body['lock_duration'] = lock_duration # unknown-primary[timeSpan]
    body['requires_session'] = requires_session # boolean
    body['default_message_time_to_live'] = default_message_time_to_live # unknown-primary[timeSpan]
    body['dead_lettering_on_filter_evaluation_exceptions'] = dead_lettering_on_filter_evaluation_exceptions # boolean
    body['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration # boolean
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window # unknown-primary[timeSpan]
    body['max_delivery_count'] = max_delivery_count # number
    body['status'] = status # str
    body['enable_batched_operations'] = enable_batched_operations # boolean
    body['auto_delete_on_idle'] = auto_delete_on_idle # unknown-primary[timeSpan]
    body['forward_to'] = forward_to # str
    body['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to # str
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
                                              action=None,
                                              filter_type=None,
                                              sql_filter=None,
                                              correlation_filter=None):
    body={}
    body['action'] = json.loads(action) if isinstance(action, str) else action
    body['filter_type'] = filter_type # str
    body['sql_filter'] = json.loads(sql_filter) if isinstance(sql_filter, str) else sql_filter
    body['correlation_filter'] = json.loads(correlation_filter) if isinstance(correlation_filter, str) else correlation_filter
    return client.rules.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name, parameters=body)

# module equivalent: azure_rm_servicebusrule
def update_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name,
                                              action=None,
                                              filter_type=None,
                                              sql_filter=None,
                                              correlation_filter=None):
    body={}
    body['action'] = json.loads(action) if isinstance(action, str) else action
    body['filter_type'] = filter_type # str
    body['sql_filter'] = json.loads(sql_filter) if isinstance(sql_filter, str) else sql_filter
    body['correlation_filter'] = json.loads(correlation_filter) if isinstance(correlation_filter, str) else correlation_filter
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