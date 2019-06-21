# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_batch(cmd, client,
                 resource_group,
                 name,
                 location,
                 tags,
                 properties,
                 auto_storage,
                 auto_storage_account_id,
                 auto_storage_account_id,
                 pool_allocation_mode,
                 key_vault_reference,
                 account_endpoint,
                 id):
    return client.batch_account.create()


def update_batch(cmd, client,
                 resource_group,
                 name,
                 location,
                 tags,
                 properties,
                 auto_storage,
                 auto_storage_account_id,
                 auto_storage_account_id,
                 pool_allocation_mode,
                 key_vault_reference,
                 account_endpoint,
                 id):
    return client.batch_account.update()


def delete_batch(cmd, client,
                 resource_group,
                 name):
    return client.batch_account.delete()


def list_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.list()


def show_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.show()


def show_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.show()


def list_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.list()


def create_batch_application_version(cmd, client,
                                     resource_group,
                                     account_name,
                                     application_name,
                                     name,
                                     properties,
                                     state,
                                     format,
                                     storage_url,
                                     storage_url_expiry,
                                     last_activation_time,
                                     id,
                                     etag):
    return client.application_package.create()


def delete_batch_application_version(cmd, client,
                                     resource_group,
                                     account_name,
                                     application_name,
                                     name):
    return client.application_package.delete()


def list_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.list()


def show_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.show()


def show_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.show()


def list_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.list()


def create_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties,
                             display_name,
                             allow_updates,
                             default_version,
                             id,
                             etag):
    return client.application.create()


def update_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties,
                             display_name,
                             allow_updates,
                             default_version,
                             id,
                             etag):
    return client.application.update()


def delete_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name):
    return client.application.delete()


def list_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.list()


def show_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.show()


def show_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.show()


def list_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.list()


def list_(cmd, client):
    return client.operations.list()


def create_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties,
                             thumbprint_algorithm,
                             thumbprint,
                             format,
                             data,
                             password,
                             provisioning_state_transition_time,
                             previous_provisioning_state,
                             previous_provisioning_state_transition_time,
                             public_data,
                             delete_certificate_error,
                             id,
                             etag):
    return client.certificate.create()


def update_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties,
                             thumbprint_algorithm,
                             thumbprint,
                             format,
                             data,
                             password,
                             provisioning_state_transition_time,
                             previous_provisioning_state,
                             previous_provisioning_state_transition_time,
                             public_data,
                             delete_certificate_error,
                             id,
                             etag):
    return client.certificate.update()


def delete_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name):
    return client.certificate.delete()


def list_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.list()


def show_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.show()


def show_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.show()


def list_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.list()


def create_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name,
                      properties,
                      display_name,
                      vm_size,
                      deployment_configuration,
                      scale_settings,
                      inter_node_communication,
                      network_configuration,
                      max_tasks_per_node,
                      task_scheduling_policy,
                      user_accounts,
                      metadata,
                      start_task,
                      certificates,
                      application_packages,
                      application_licenses,
                      last_modified,
                      creation_time,
                      provisioning_state_transition_time,
                      allocation_state,
                      allocation_state_transition_time,
                      current_dedicated_nodes,
                      current_low_priority_nodes,
                      auto_scale_run,
                      resize_operation_status,
                      id,
                      etag):
    return client.pool.create()


def update_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name,
                      properties,
                      display_name,
                      vm_size,
                      deployment_configuration,
                      scale_settings,
                      inter_node_communication,
                      network_configuration,
                      max_tasks_per_node,
                      task_scheduling_policy,
                      user_accounts,
                      metadata,
                      start_task,
                      certificates,
                      application_packages,
                      application_licenses,
                      last_modified,
                      creation_time,
                      provisioning_state_transition_time,
                      allocation_state,
                      allocation_state_transition_time,
                      current_dedicated_nodes,
                      current_low_priority_nodes,
                      auto_scale_run,
                      resize_operation_status,
                      id,
                      etag):
    return client.pool.update()


def delete_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name):
    return client.pool.delete()


def list_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.list()


def show_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.show()


def show_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.show()


def list_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.list()