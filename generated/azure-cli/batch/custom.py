# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_batchaccount
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
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['auto_storage'] = auto_storage
    body.get('auto_storage', {}).get('storage_account_id', {})['storage_account_id'] = storage_account_id
    body['pool_allocation_mode'] = pool_allocation_mode
    body['key_vault_reference'] = key_vault_reference
    body['account_endpoint'] = account_endpoint
    return client.batch_account.create(resource_group_name=resource_group, account_name=name, parameters=body)

# module equivalent: azure_rm_batchaccount
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
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['auto_storage'] = auto_storage
    body.get('auto_storage', {}).get('storage_account_id', {})['storage_account_id'] = storage_account_id
    body['pool_allocation_mode'] = pool_allocation_mode
    body['key_vault_reference'] = key_vault_reference
    body['account_endpoint'] = account_endpoint
    return client.batch_account.update(resource_group_name=resource_group, account_name=name, parameters=body)

# module equivalent: azure_rm_batchaccount
def delete_batch(cmd, client,
                 resource_group,
                 name):
    return client.batch_account.delete(resource_group_name=resource_group, account_name=name)

# module equivalent: azure_rm_batchaccount
def list_batch(cmd, client,
               resource_group):
    return client.batch_account.list()

# module equivalent: azure_rm_batchaccount
def show_batch(cmd, client,
               resource_group,
               name):
    return client.batch_account.get(resource_group_name=resource_group, account_name=name)

# module equivalent: azure_rm_batchapplicationpackage
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
    body={}
    body['properties'] = properties
    body['state'] = state
    body['format'] = format
    body['storage_url'] = storage_url
    body['storage_url_expiry'] = storage_url_expiry
    body['last_activation_time'] = last_activation_time
    return client.application_package.create(resource_group_name=resource_group, account_name=account_name, application_name=application_name, version_name=name)

# module equivalent: azure_rm_batchapplicationpackage
def delete_batch_application_version(cmd, client,
                                     resource_group,
                                     account_name,
                                     application_name,
                                     name):
    return client.application_package.delete(resource_group_name=resource_group, account_name=account_name, application_name=application_name, version_name=name)

# module equivalent: azure_rm_batchapplicationpackage
def list_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name):
    return client.application_package.list(resource_group_name=resource_group, account_name=account_name, application_name=application_name)

# module equivalent: azure_rm_batchapplicationpackage
def show_batch_application_version(cmd, client,
                                   resource_group,
                                   account_name,
                                   application_name,
                                   name):
    return client.application_package.get(resource_group_name=resource_group, account_name=account_name, application_name=application_name, version_name=name)

# module equivalent: azure_rm_batchapplication
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
    body={}
    body['properties'] = properties
    body['display_name'] = display_name
    body['allow_updates'] = allow_updates
    body['default_version'] = default_version
    return client.application.create(resource_group_name=resource_group, account_name=account_name, application_name=name)

# module equivalent: azure_rm_batchapplication
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
    body={}
    body['properties'] = properties
    body['display_name'] = display_name
    body['allow_updates'] = allow_updates
    body['default_version'] = default_version
    return client.application.update(resource_group_name=resource_group, account_name=account_name, application_name=name, parameters=body)

# module equivalent: azure_rm_batchapplication
def delete_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name):
    return client.application.delete(resource_group_name=resource_group, account_name=account_name, application_name=name)

# module equivalent: azure_rm_batchapplication
def list_batch_application(cmd, client,
                           resource_group,
                           account_name):
    return client.application.list(resource_group_name=resource_group, account_name=account_name)

# module equivalent: azure_rm_batchapplication
def show_batch_application(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.application.get(resource_group_name=resource_group, account_name=account_name, application_name=name)

# module equivalent: azure_rm_batchcertificate
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
    body={}
    body['properties'] = properties
    body['thumbprint_algorithm'] = thumbprint_algorithm
    body['thumbprint'] = thumbprint
    body['format'] = format
    body['data'] = data
    body['password'] = password
    body['provisioning_state_transition_time'] = provisioning_state_transition_time
    body['previous_provisioning_state'] = previous_provisioning_state
    body['previous_provisioning_state_transition_time'] = previous_provisioning_state_transition_time
    body['public_data'] = public_data
    body['delete_certificate_error'] = delete_certificate_error
    return client.certificate.create(resource_group_name=resource_group, account_name=account_name, certificate_name=name, parameters=body)

# module equivalent: azure_rm_batchcertificate
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
    body={}
    body['properties'] = properties
    body['thumbprint_algorithm'] = thumbprint_algorithm
    body['thumbprint'] = thumbprint
    body['format'] = format
    body['data'] = data
    body['password'] = password
    body['provisioning_state_transition_time'] = provisioning_state_transition_time
    body['previous_provisioning_state'] = previous_provisioning_state
    body['previous_provisioning_state_transition_time'] = previous_provisioning_state_transition_time
    body['public_data'] = public_data
    body['delete_certificate_error'] = delete_certificate_error
    return client.certificate.update(resource_group_name=resource_group, account_name=account_name, certificate_name=name, parameters=body)

# module equivalent: azure_rm_batchcertificate
def delete_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name):
    return client.certificate.delete(resource_group_name=resource_group, account_name=account_name, certificate_name=name)

# module equivalent: azure_rm_batchcertificate
def list_batch_certificate(cmd, client,
                           resource_group,
                           account_name):
    return client.certificate.list_by_batch_account(resource_group_name=resource_group, account_name=account_name)

# module equivalent: azure_rm_batchcertificate
def show_batch_certificate(cmd, client,
                           resource_group,
                           account_name,
                           name):
    return client.certificate.get(resource_group_name=resource_group, account_name=account_name, certificate_name=name)

# module equivalent: azure_rm_batchpool
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
    body={}
    body['properties'] = properties
    body['display_name'] = display_name
    body['vm_size'] = vm_size
    body['deployment_configuration'] = deployment_configuration
    body['scale_settings'] = scale_settings
    body['inter_node_communication'] = inter_node_communication
    body['network_configuration'] = network_configuration
    body['max_tasks_per_node'] = max_tasks_per_node
    body['task_scheduling_policy'] = task_scheduling_policy
    body['user_accounts'] = user_accounts
    body['metadata'] = metadata
    body['start_task'] = start_task
    body['certificates'] = certificates
    body['application_packages'] = application_packages
    body['application_licenses'] = application_licenses
    body['last_modified'] = last_modified
    body['creation_time'] = creation_time
    body['provisioning_state_transition_time'] = provisioning_state_transition_time
    body['allocation_state'] = allocation_state
    body['allocation_state_transition_time'] = allocation_state_transition_time
    body['current_dedicated_nodes'] = current_dedicated_nodes
    body['current_low_priority_nodes'] = current_low_priority_nodes
    body['auto_scale_run'] = auto_scale_run
    body['resize_operation_status'] = resize_operation_status
    return client.pool.create(resource_group_name=resource_group, account_name=account_name, pool_name=name, parameters=body)

# module equivalent: azure_rm_batchpool
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
    body={}
    body['properties'] = properties
    body['display_name'] = display_name
    body['vm_size'] = vm_size
    body['deployment_configuration'] = deployment_configuration
    body['scale_settings'] = scale_settings
    body['inter_node_communication'] = inter_node_communication
    body['network_configuration'] = network_configuration
    body['max_tasks_per_node'] = max_tasks_per_node
    body['task_scheduling_policy'] = task_scheduling_policy
    body['user_accounts'] = user_accounts
    body['metadata'] = metadata
    body['start_task'] = start_task
    body['certificates'] = certificates
    body['application_packages'] = application_packages
    body['application_licenses'] = application_licenses
    body['last_modified'] = last_modified
    body['creation_time'] = creation_time
    body['provisioning_state_transition_time'] = provisioning_state_transition_time
    body['allocation_state'] = allocation_state
    body['allocation_state_transition_time'] = allocation_state_transition_time
    body['current_dedicated_nodes'] = current_dedicated_nodes
    body['current_low_priority_nodes'] = current_low_priority_nodes
    body['auto_scale_run'] = auto_scale_run
    body['resize_operation_status'] = resize_operation_status
    return client.pool.update(resource_group_name=resource_group, account_name=account_name, pool_name=name, parameters=body)

# module equivalent: azure_rm_batchpool
def delete_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name):
    return client.pool.delete(resource_group_name=resource_group, account_name=account_name, pool_name=name)

# module equivalent: azure_rm_batchpool
def list_batch_pool(cmd, client,
                    resource_group,
                    account_name):
    return client.pool.list_by_batch_account(resource_group_name=resource_group, account_name=account_name)

# module equivalent: azure_rm_batchpool
def show_batch_pool(cmd, client,
                    resource_group,
                    account_name,
                    name):
    return client.pool.get(resource_group_name=resource_group, account_name=account_name, pool_name=name)