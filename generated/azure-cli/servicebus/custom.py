# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def list_(cmd, client):
    body={}
    return client.operations.list()


def create_servicebus(cmd, client,
                      resource_group,
                      name,
                      location=None,
                      tags=None,
                      sku=None,
                      properties=None,
                      provisioning_state=None,
                      created_at=None,
                      updated_at=None,
                      service_bus_endpoint=None,
                      metric_id=None,
                      id=None,
                      type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['sku'] = sku
    body['properties'] = properties
    body['provisioning_state'] = provisioning_state
    body['created_at'] = created_at
    body['updated_at'] = updated_at
    body['service_bus_endpoint'] = service_bus_endpoint
    body['metric_id'] = metric_id
    return client.namespaces.create_or_update(resource_group_name=resource_group, namespace_name=name, parameters=body)


def update_servicebus(cmd, client,
                      resource_group,
                      name,
                      location=None,
                      tags=None,
                      sku=None,
                      properties=None,
                      provisioning_state=None,
                      created_at=None,
                      updated_at=None,
                      service_bus_endpoint=None,
                      metric_id=None,
                      id=None,
                      type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['sku'] = sku
    body['properties'] = properties
    body['provisioning_state'] = provisioning_state
    body['created_at'] = created_at
    body['updated_at'] = updated_at
    body['service_bus_endpoint'] = service_bus_endpoint
    body['metric_id'] = metric_id
    return client.namespaces.create_or_update(resource_group_name=resource_group, namespace_name=name, parameters=body)


def delete_servicebus(cmd, client,
                      resource_group,
                      name):
    body={}
    return client.namespaces.delete(resource_group_name=resource_group, namespace_name=name)


def list_servicebus(cmd, client,
                    resource_group,
                    name):
    body={}
    return client.namespaces.list(resource_group_name=resource_group, namespace_name=name)


def show_servicebus(cmd, client,
                    resource_group,
                    name):
    body={}
    return client.namespaces.get(resource_group_name=resource_group, namespace_name=name)


def list_servicebus_authorizationrule(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      name):
    body={}
    return client.namespaces.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name)


def show_servicebus_authorizationrule(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      name):
    body={}
    return client.namespaces.get(resource_group_name=resource_group, namespace_name=namespace_name)


def create_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias,
                                             properties=None,
                                             partner_namespace=None,
                                             alternate_name=None,
                                             provisioning_state=None,
                                             pending_replication_operations_count=None,
                                             role=None,
                                             id=None,
                                             type=None):
    body={}
    body['properties'] = properties
    body['partner_namespace'] = partner_namespace
    body['alternate_name'] = alternate_name
    body['provisioning_state'] = provisioning_state
    body['pending_replication_operations_count'] = pending_replication_operations_count
    body['role'] = role
    return client.disaster_recovery_configs.create_or_update(resource_group_name=resource_group, namespace_name=name, alias=alias, parameters=body)


def delete_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias):
    body={}
    return client.disaster_recovery_configs.delete(resource_group_name=resource_group, namespace_name=name, alias=alias)


def list_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    body={}
    return client.disaster_recovery_configs.list(resource_group_name=resource_group, namespace_name=name, alias=alias)


def show_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    body={}
    return client.disaster_recovery_configs.get(resource_group_name=resource_group, namespace_name=name, alias=alias)


def list_servicebus_disasterrecoveryconfig_authorizationrule(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             alias,
                                                             name):
    body={}
    return client.disaster_recovery_configs.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, alias=alias)


def show_servicebus_disasterrecoveryconfig_authorizationrule(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             alias,
                                                             name):
    body={}
    return client.disaster_recovery_configs.get(resource_group_name=resource_group, namespace_name=namespace_name, alias=alias)


def show_servicebus_migrationconfiguration(cmd, client,
                                           resource_group,
                                           namespace_name,
                                           name):
    body={}
    return client.migration_configs.get(resource_group_name=resource_group, namespace_name=namespace_name, config_name=name)


def list_servicebus_migrationconfiguration(cmd, client,
                                           resource_group,
                                           namespace_name,
                                           name):
    body={}
    return client.migration_configs.list(resource_group_name=resource_group, namespace_name=namespace_name, config_name=name)


def create_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            properties=None,
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
                            forward_dead_lettered_messages_to=None,
                            count_details=None,
                            created_at=None,
                            updated_at=None,
                            accessed_at=None,
                            size_in_bytes=None,
                            message_count=None,
                            id=None,
                            type=None):
    body={}
    body['properties'] = properties
    body['lock_duration'] = lock_duration
    body['max_size_in_megabytes'] = max_size_in_megabytes
    body['requires_duplicate_detection'] = requires_duplicate_detection
    body['requires_session'] = requires_session
    body['default_message_time_to_live'] = default_message_time_to_live
    body['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window
    body['max_delivery_count'] = max_delivery_count
    body['status'] = status
    body['enable_batched_operations'] = enable_batched_operations
    body['auto_delete_on_idle'] = auto_delete_on_idle
    body['enable_partitioning'] = enable_partitioning
    body['enable_express'] = enable_express
    body['forward_to'] = forward_to
    body['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to
    body['count_details'] = count_details
    body['created_at'] = created_at
    body['updated_at'] = updated_at
    body['accessed_at'] = accessed_at
    body['size_in_bytes'] = size_in_bytes
    body['message_count'] = message_count
    return client.queues.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name, parameters=body)


def delete_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    body={}
    return client.queues.delete(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name)


def list_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    body={}
    return client.queues.list_by_namespace(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name)


def show_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    body={}
    return client.queues.get(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=name)


def list_servicebus_queue_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            queue_name,
                                            name):
    body={}
    return client.queues.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=queue_name)


def show_servicebus_queue_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            queue_name,
                                            name):
    body={}
    return client.queues.get(resource_group_name=resource_group, namespace_name=namespace_name, queue_name=queue_name)


def create_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            properties=None,
                            default_message_time_to_live=None,
                            max_size_in_megabytes=None,
                            requires_duplicate_detection=None,
                            duplicate_detection_history_time_window=None,
                            enable_batched_operations=None,
                            status=None,
                            support_ordering=None,
                            auto_delete_on_idle=None,
                            enable_partitioning=None,
                            enable_express=None,
                            size_in_bytes=None,
                            created_at=None,
                            updated_at=None,
                            accessed_at=None,
                            subscription_count=None,
                            count_details=None,
                            id=None,
                            type=None):
    body={}
    body['properties'] = properties
    body['default_message_time_to_live'] = default_message_time_to_live
    body['max_size_in_megabytes'] = max_size_in_megabytes
    body['requires_duplicate_detection'] = requires_duplicate_detection
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window
    body['enable_batched_operations'] = enable_batched_operations
    body['status'] = status
    body['support_ordering'] = support_ordering
    body['auto_delete_on_idle'] = auto_delete_on_idle
    body['enable_partitioning'] = enable_partitioning
    body['enable_express'] = enable_express
    body['size_in_bytes'] = size_in_bytes
    body['created_at'] = created_at
    body['updated_at'] = updated_at
    body['accessed_at'] = accessed_at
    body['subscription_count'] = subscription_count
    body['count_details'] = count_details
    return client.topics.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name, parameters=body)


def delete_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    body={}
    return client.topics.delete(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name)


def list_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    body={}
    return client.topics.list_by_namespace(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name)


def show_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    body={}
    return client.topics.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=name)


def list_servicebus_topic_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            name):
    body={}
    return client.topics.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name)


def show_servicebus_topic_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            name):
    body={}
    return client.topics.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name)


def create_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name,
                                         properties=None,
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
                                         forward_dead_lettered_messages_to=None,
                                         message_count=None,
                                         created_at=None,
                                         accessed_at=None,
                                         updated_at=None,
                                         count_details=None,
                                         id=None,
                                         type=None):
    body={}
    body['properties'] = properties
    body['lock_duration'] = lock_duration
    body['requires_session'] = requires_session
    body['default_message_time_to_live'] = default_message_time_to_live
    body['dead_lettering_on_filter_evaluation_exceptions'] = dead_lettering_on_filter_evaluation_exceptions
    body['dead_lettering_on_message_expiration'] = dead_lettering_on_message_expiration
    body['duplicate_detection_history_time_window'] = duplicate_detection_history_time_window
    body['max_delivery_count'] = max_delivery_count
    body['status'] = status
    body['enable_batched_operations'] = enable_batched_operations
    body['auto_delete_on_idle'] = auto_delete_on_idle
    body['forward_to'] = forward_to
    body['forward_dead_lettered_messages_to'] = forward_dead_lettered_messages_to
    body['message_count'] = message_count
    body['created_at'] = created_at
    body['accessed_at'] = accessed_at
    body['updated_at'] = updated_at
    body['count_details'] = count_details
    return client.subscriptions.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name, parameters=body)


def delete_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name):
    body={}
    return client.subscriptions.delete(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)


def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    body={}
    return client.subscriptions.list_by_topic(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)


def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    body={}
    return client.subscriptions.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)


def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    body={}
    return client.subscriptions.list_by_topic(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)


def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    body={}
    return client.subscriptions.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=name)


def create_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name,
                                              properties=None,
                                              action=None,
                                              filter_type=None,
                                              sql_filter=None,
                                              correlation_filter=None,
                                              id=None,
                                              type=None):
    body={}
    body['properties'] = properties
    body['action'] = action
    body['filter_type'] = filter_type
    body['sql_filter'] = sql_filter
    body['correlation_filter'] = correlation_filter
    return client.rules.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name, parameters=body)


def delete_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name):
    body={}
    return client.rules.delete(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)


def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    body={}
    return client.rules.list_by_subscriptions(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)


def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    body={}
    return client.rules.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)


def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    body={}
    return client.rules.get(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)


def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    body={}
    return client.rules.list_by_subscriptions(resource_group_name=resource_group, namespace_name=namespace_name, topic_name=topic_name, subscription_name=subscription_name, rule_name=name)


def list_servicebus(cmd, client,
                    sku):
    body={}
    return client.regions.list_by_sku()


def list_(cmd, client):
    body={}
    return client.premium_messaging_regions.list()


def list_servicebus(cmd, client,
                    resource_group,
                    name):
    body={}
    return client.event_hubs.list_by_namespace()