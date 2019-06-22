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
    return client.batch_account.create()


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
                                     properties=None,
                                     state=None,
                                     format=None,
                                     storage_url=None,
                                     storage_url_expiry=None,
                                     last_activation_time=None,
                                     id=None,
                                     etag=None):
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
                             properties=None,
                             display_name=None,
                             allow_updates=None,
                             default_version=None,
                             id=None,
                             etag=None):
    return client.application.create()


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
    return client.certificate.create()


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
    return client.pool.create()


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