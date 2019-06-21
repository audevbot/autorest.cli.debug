# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def list_(cmd, client):
    return client.operations.list()


def create_servicebus(cmd, client,
                      resource_group,
                      name,
                      location,
                      tags,
                      sku,
                      properties,
                      provisioning_state,
                      created_at,
                      updated_at,
                      service_bus_endpoint,
                      metric_id,
                      id,
                      name,
                      type):
    return client.namespaces.create()


def update_servicebus(cmd, client,
                      resource_group,
                      name,
                      location,
                      tags,
                      sku,
                      properties,
                      provisioning_state,
                      created_at,
                      updated_at,
                      service_bus_endpoint,
                      metric_id,
                      id,
                      name,
                      type):
    return client.namespaces.update()


def delete_servicebus(cmd, client,
                      resource_group,
                      name):
    return client.namespaces.delete()


def list_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.namespaces.list()


def show_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.namespaces.show()


def list_servicebus_authorizationrule(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      name):
    return client.namespaces.list()


def show_servicebus_authorizationrule(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      name):
    return client.namespaces.show()


def create_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias,
                                             properties,
                                             partner_namespace,
                                             alternate_name,
                                             provisioning_state,
                                             pending_replication_operations_count,
                                             role,
                                             id,
                                             name,
                                             type):
    return client.disaster_recovery_configs.create()


def delete_servicebus_disasterrecoveryconfig(cmd, client,
                                             resource_group,
                                             name,
                                             alias):
    return client.disaster_recovery_configs.delete()


def list_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    return client.disaster_recovery_configs.list()


def show_servicebus_disasterrecoveryconfig(cmd, client,
                                           resource_group,
                                           name,
                                           alias):
    return client.disaster_recovery_configs.show()


def list_servicebus_disasterrecoveryconfig_authorizationrule(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             alias,
                                                             name):
    return client.disaster_recovery_configs.list()


def show_servicebus_disasterrecoveryconfig_authorizationrule(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             alias,
                                                             name):
    return client.disaster_recovery_configs.show()


def show_servicebus_migrationconfiguration(cmd, client,
                                           resource_group,
                                           namespace_name,
                                           name):
    return client.migration_configs.show()


def list_servicebus_migrationconfiguration(cmd, client,
                                           resource_group,
                                           namespace_name,
                                           name):
    return client.migration_configs.list()


def create_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            properties,
                            lock_duration,
                            max_size_in_megabytes,
                            requires_duplicate_detection,
                            requires_session,
                            default_message_time_to_live,
                            dead_lettering_on_message_expiration,
                            duplicate_detection_history_time_window,
                            max_delivery_count,
                            status,
                            enable_batched_operations,
                            auto_delete_on_idle,
                            enable_partitioning,
                            enable_express,
                            forward_to,
                            forward_dead_lettered_messages_to,
                            count_details,
                            created_at,
                            updated_at,
                            accessed_at,
                            size_in_bytes,
                            message_count,
                            id,
                            name,
                            type):
    return client.queues.create()


def delete_servicebus_queue(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    return client.queues.delete()


def list_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.queues.list()


def show_servicebus_queue(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.queues.show()


def list_servicebus_queue_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            queue_name,
                                            name):
    return client.queues.list()


def show_servicebus_queue_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            queue_name,
                                            name):
    return client.queues.show()


def create_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name,
                            properties,
                            default_message_time_to_live,
                            max_size_in_megabytes,
                            requires_duplicate_detection,
                            duplicate_detection_history_time_window,
                            enable_batched_operations,
                            status,
                            support_ordering,
                            auto_delete_on_idle,
                            enable_partitioning,
                            enable_express,
                            size_in_bytes,
                            created_at,
                            updated_at,
                            accessed_at,
                            subscription_count,
                            count_details,
                            id,
                            name,
                            type):
    return client.topics.create()


def delete_servicebus_topic(cmd, client,
                            resource_group,
                            namespace_name,
                            name):
    return client.topics.delete()


def list_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.topics.list()


def show_servicebus_topic(cmd, client,
                          resource_group,
                          namespace_name,
                          name):
    return client.topics.show()


def list_servicebus_topic_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            name):
    return client.topics.list()


def show_servicebus_topic_authorizationrule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            name):
    return client.topics.show()


def create_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name,
                                         properties,
                                         lock_duration,
                                         requires_session,
                                         default_message_time_to_live,
                                         dead_lettering_on_filter_evaluation_exceptions,
                                         dead_lettering_on_message_expiration,
                                         duplicate_detection_history_time_window,
                                         max_delivery_count,
                                         status,
                                         enable_batched_operations,
                                         auto_delete_on_idle,
                                         forward_to,
                                         forward_dead_lettered_messages_to,
                                         message_count,
                                         created_at,
                                         accessed_at,
                                         updated_at,
                                         count_details,
                                         id,
                                         name,
                                         type):
    return client.subscriptions.create()


def delete_servicebus_topic_subscription(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         topic_name,
                                         name):
    return client.subscriptions.delete()


def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.list()


def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.show()


def list_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.list()


def show_servicebus_topic_subscription(cmd, client,
                                       resource_group,
                                       namespace_name,
                                       topic_name,
                                       name):
    return client.subscriptions.show()


def create_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name,
                                              properties,
                                              action,
                                              filter_type,
                                              sql_filter,
                                              correlation_filter,
                                              id,
                                              name,
                                              type):
    return client.rules.create()


def delete_servicebus_topic_subscription_rule(cmd, client,
                                              resource_group,
                                              namespace_name,
                                              topic_name,
                                              subscription_name,
                                              name):
    return client.rules.delete()


def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.list()


def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.show()


def show_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.show()


def list_servicebus_topic_subscription_rule(cmd, client,
                                            resource_group,
                                            namespace_name,
                                            topic_name,
                                            subscription_name,
                                            name):
    return client.rules.list()


def list_servicebus(cmd, client,
                    sku):
    return client.regions.list()


def list_(cmd, client):
    return client.premium_messaging_regions.list()


def list_servicebus(cmd, client,
                    resource_group,
                    name):
    return client.event_hubs.list()