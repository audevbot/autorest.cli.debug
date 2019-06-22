# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_batch(cmd, client,
                 resource_group,
                 name,
                 location=None,
                 tags=None,
                 properties=None,
                 auto_storage=None,
                 auto_storage_account_id=None,
                 pool_allocation_mode=None,
                 key_vault_reference=None,
                 account_endpoint=None,
                 id=None):
    return client.batch_account.create(resource_group, name, body)


def update_batch(cmd, client,
                 resource_group,
                 name,
                 location=None,
                 tags=None,
                 properties=None,
                 auto_storage=None,
                 auto_storage_account_id=None,
                 pool_allocation_mode=None,
                 key_vault_reference=None,
                 account_endpoint=None,
                 id=None):
    return client.batch_account.update(resource_group, name, body)


def delete_batch(cmd, client,
                 resource_group,
                 name):
    return client.batch_account.delete(resource_group, name)


def list_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.list(resource_group, name)


def show_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.show(resource_group, name)


def show_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.show(resource_group, name)


def list_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.list(resource_group, name)


def create_batch_application_version(cmd, client,
                                     resource_group,
                                     account_name,
                                     application_name,
                                     name,
                                     properties=None,
                                     state=None,
                                     format=None,
                                     storage_url=None,
                                     storage_url_expiry=None,
                                     last_activation_time=None,
                                     id=None,
                                     etag=None):
    return client.application_package.create(resource_group, account_name, application_name, name)


def delete_batch_application_version(cmd, client,
                                     resource_group,
                                     account_name,
                                     application_name,
                                     name):
    return client.application_package.delete(resource_group, account_name, application_name, name)


def list_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.list(resource_group, account_name, application_name, name)


def show_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.show(resource_group, account_name, application_name, name)


def show_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.show(resource_group, account_name, application_name, name)


def list_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.list(resource_group, account_name, application_name, name)


def create_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties=None,
                             display_name=None,
                             allow_updates=None,
                             default_version=None,
                             id=None,
                             etag=None):
    return client.application.create(resource_group, account_name, name)


def update_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties=None,
                             display_name=None,
                             allow_updates=None,
                             default_version=None,
                             id=None,
                             etag=None):
    return client.application.update(resource_group, account_name, name, body)


def delete_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name):
    return client.application.delete(resource_group, account_name, name)


def list_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.list(resource_group, account_name, name)


def show_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.show(resource_group, account_name, name)


def show_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.show(resource_group, account_name, name)


def list_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.list(resource_group, account_name, name)


def list_(cmd, client):
    return client.operations.list()


def create_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties=None,
                             thumbprint_algorithm=None,
                             thumbprint=None,
                             format=None,
                             data=None,
                             password=None,
                             provisioning_state_transition_time=None,
                             previous_provisioning_state=None,
                             previous_provisioning_state_transition_time=None,
                             public_data=None,
                             delete_certificate_error=None,
                             id=None,
                             etag=None):
    return client.certificate.create(resource_group, account_name, name, body)


def update_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             properties=None,
                             thumbprint_algorithm=None,
                             thumbprint=None,
                             format=None,
                             data=None,
                             password=None,
                             provisioning_state_transition_time=None,
                             previous_provisioning_state=None,
                             previous_provisioning_state_transition_time=None,
                             public_data=None,
                             delete_certificate_error=None,
                             id=None,
                             etag=None):
    return client.certificate.update(resource_group, account_name, name, body)


def delete_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name):
    return client.certificate.delete(resource_group, account_name, name)


def list_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.list(resource_group, account_name, name)


def show_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.show(resource_group, account_name, name)


def show_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.show(resource_group, account_name, name)


def list_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.list(resource_group, account_name, name)


def create_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name,
                      properties=None,
                      display_name=None,
                      vm_size=None,
                      deployment_configuration=None,
                      scale_settings=None,
                      inter_node_communication=None,
                      network_configuration=None,
                      max_tasks_per_node=None,
                      task_scheduling_policy=None,
                      user_accounts=None,
                      metadata=None,
                      start_task=None,
                      certificates=None,
                      application_packages=None,
                      application_licenses=None,
                      last_modified=None,
                      creation_time=None,
                      provisioning_state_transition_time=None,
                      allocation_state=None,
                      allocation_state_transition_time=None,
                      current_dedicated_nodes=None,
                      current_low_priority_nodes=None,
                      auto_scale_run=None,
                      resize_operation_status=None,
                      id=None,
                      etag=None):
    return client.pool.create(resource_group, account_name, name, body)


def update_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name,
                      properties=None,
                      display_name=None,
                      vm_size=None,
                      deployment_configuration=None,
                      scale_settings=None,
                      inter_node_communication=None,
                      network_configuration=None,
                      max_tasks_per_node=None,
                      task_scheduling_policy=None,
                      user_accounts=None,
                      metadata=None,
                      start_task=None,
                      certificates=None,
                      application_packages=None,
                      application_licenses=None,
                      last_modified=None,
                      creation_time=None,
                      provisioning_state_transition_time=None,
                      allocation_state=None,
                      allocation_state_transition_time=None,
                      current_dedicated_nodes=None,
                      current_low_priority_nodes=None,
                      auto_scale_run=None,
                      resize_operation_status=None,
                      id=None,
                      etag=None):
    return client.pool.update(resource_group, account_name, name, body)


def delete_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name):
    return client.pool.delete(resource_group, account_name, name)


def list_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.list(resource_group, account_name, name)


def show_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.show(resource_group, account_name, name)


def show_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.show(resource_group, account_name, name)


def list_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.list(resource_group, account_name, name)