# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import json

# module equivalent: azure_rm_batchaccount
def create_batch(cmd, client,
                 resource_group,
                 name,
                 location=None,
                 tags=None,
                 auto_storage_account_id=None,
                 pool_allocation_mode=None,
                 key_vault_reference=None):
    body={}
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"61","$type":"DictionaryType","valueType":{"$id":"62","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"63","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"64","fixed":false},"deprecated":false}]
    body.setdefault('auto_storage', {})['storage_account_id'] = auto_storage_account_id # str
    body['pool_allocation_mode'] = pool_allocation_mode # str
    body['key_vault_reference'] = json.parse(key_vault_reference) if isinstance(key_vault_reference, str) else key_vault_reference
    return client.batch_account.create(resource_group_name=resource_group, account_name=name, parameters=body)

# module equivalent: azure_rm_batchaccount
def update_batch(cmd, client,
                 resource_group,
                 name,
                 location=None,
                 tags=None,
                 auto_storage_account_id=None,
                 pool_allocation_mode=None,
                 key_vault_reference=None):
    body={}
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"61","$type":"DictionaryType","valueType":{"$id":"62","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"63","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"64","fixed":false},"deprecated":false}]
    body.setdefault('auto_storage', {})['storage_account_id'] = auto_storage_account_id # str
    body['pool_allocation_mode'] = pool_allocation_mode # str
    body['key_vault_reference'] = json.parse(key_vault_reference) if isinstance(key_vault_reference, str) else key_vault_reference
    return client.batch_account.update(resource_group_name=resource_group, account_name=name, parameters=body)

# module equivalent: azure_rm_batchaccount
def delete_batch(cmd, client,
                 resource_group,
                 name):
    return client.batch_account.delete(resource_group_name=resource_group, account_name=name)

# module equivalent: azure_rm_batchaccount
def list_batch(cmd, client,
               resource_group):
    if resource_group is not None:
        return client.batch_account.list_by_resource_group(resource_group_name=resource_group)
    else:
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
                                     name):
    body={}
    return client.application_package.create(resource_group_name=resource_group, account_name=account_name, application_name=application_name, version_name=name, parameters=body)

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
                             display_name=None,
                             allow_updates=None,
                             default_version=None):
    body={}
    body['display_name'] = display_name # str
    body['allow_updates'] = allow_updates # boolean
    body['default_version'] = default_version # str
    return client.application.create(resource_group_name=resource_group, account_name=account_name, application_name=name, parameters=body)

# module equivalent: azure_rm_batchapplication
def update_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             display_name=None,
                             allow_updates=None,
                             default_version=None):
    body={}
    body['display_name'] = display_name # str
    body['allow_updates'] = allow_updates # boolean
    body['default_version'] = default_version # str
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
                             thumbprint_algorithm=None,
                             thumbprint=None,
                             format=None,
                             data=None,
                             password=None):
    body={}
    body['thumbprint_algorithm'] = thumbprint_algorithm # str
    body['thumbprint'] = thumbprint # str
    body['format'] = format # str
    body['data'] = data # str
    body['password'] = password # str
    return client.certificate.create(resource_group_name=resource_group, account_name=account_name, certificate_name=name, parameters=body)

# module equivalent: azure_rm_batchcertificate
def update_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             thumbprint_algorithm=None,
                             thumbprint=None,
                             format=None,
                             data=None,
                             password=None):
    body={}
    body['thumbprint_algorithm'] = thumbprint_algorithm # str
    body['thumbprint'] = thumbprint # str
    body['format'] = format # str
    body['data'] = data # str
    body['password'] = password # str
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
                      application_licenses=None):
    body={}
    body['display_name'] = display_name # str
    body['vm_size'] = vm_size # str
    body['deployment_configuration'] = json.parse(deployment_configuration) if isinstance(deployment_configuration, str) else deployment_configuration
    body['scale_settings'] = json.parse(scale_settings) if isinstance(scale_settings, str) else scale_settings
    body['inter_node_communication'] = inter_node_communication # str
    body['network_configuration'] = json.parse(network_configuration) if isinstance(network_configuration, str) else network_configuration
    body['max_tasks_per_node'] = max_tasks_per_node # number
    body['task_scheduling_policy'] = json.parse(task_scheduling_policy) if isinstance(task_scheduling_policy, str) else task_scheduling_policy
    body['user_accounts'] = json.parse(user_accounts) if isinstance(user_accounts, str) else user_accounts
    body['metadata'] = json.parse(metadata) if isinstance(metadata, str) else metadata
    body['start_task'] = json.parse(start_task) if isinstance(start_task, str) else start_task
    body['certificates'] = json.parse(certificates) if isinstance(certificates, str) else certificates
    body['application_packages'] = json.parse(application_packages) if isinstance(application_packages, str) else application_packages
    body['application_licenses'] = application_licenses # str
    return client.pool.create(resource_group_name=resource_group, account_name=account_name, pool_name=name, parameters=body)

# module equivalent: azure_rm_batchpool
def update_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name,
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
                      application_licenses=None):
    body={}
    body['display_name'] = display_name # str
    body['vm_size'] = vm_size # str
    body['deployment_configuration'] = json.parse(deployment_configuration) if isinstance(deployment_configuration, str) else deployment_configuration
    body['scale_settings'] = json.parse(scale_settings) if isinstance(scale_settings, str) else scale_settings
    body['inter_node_communication'] = inter_node_communication # str
    body['network_configuration'] = json.parse(network_configuration) if isinstance(network_configuration, str) else network_configuration
    body['max_tasks_per_node'] = max_tasks_per_node # number
    body['task_scheduling_policy'] = json.parse(task_scheduling_policy) if isinstance(task_scheduling_policy, str) else task_scheduling_policy
    body['user_accounts'] = json.parse(user_accounts) if isinstance(user_accounts, str) else user_accounts
    body['metadata'] = json.parse(metadata) if isinstance(metadata, str) else metadata
    body['start_task'] = json.parse(start_task) if isinstance(start_task, str) else start_task
    body['certificates'] = json.parse(certificates) if isinstance(certificates, str) else certificates
    body['application_packages'] = json.parse(application_packages) if isinstance(application_packages, str) else application_packages
    body['application_licenses'] = application_licenses # str
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