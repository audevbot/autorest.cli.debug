# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_batchaccount
def create_batch(cmd, client,
                 resource_group,
                 name,
                 parameters=None):
    body={}
    return client.batch_account.create(resource_group_name=resource_group, account_name=name, parameters=body)

# module equivalent: azure_rm_batchaccount
def update_batch(cmd, client,
                 resource_group,
                 name,
                 parameters=None):
    body={}
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
                                     name,
                                     parameters=None):
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
                             parameters=None):
    body={}
    return client.application.create(resource_group_name=resource_group, account_name=account_name, application_name=name, parameters=body)

# module equivalent: azure_rm_batchapplication
def update_batch_application(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             parameters=None):
    body={}
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
                             parameters=None):
    body={}
    return client.certificate.create(resource_group_name=resource_group, account_name=account_name, certificate_name=name, parameters=body)

# module equivalent: azure_rm_batchcertificate
def update_batch_certificate(cmd, client,
                             resource_group,
                             account_name,
                             name,
                             parameters=None):
    body={}
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
                      parameters=None):
    body={}
    return client.pool.create(resource_group_name=resource_group, account_name=account_name, pool_name=name, parameters=body)

# module equivalent: azure_rm_batchpool
def update_batch_pool(cmd, client,
                      resource_group,
                      account_name,
                      name,
                      parameters=None):
    body={}
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