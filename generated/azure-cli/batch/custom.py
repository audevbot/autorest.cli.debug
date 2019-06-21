# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.create()


def update_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.update()


def delete_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.delete()


def list_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.list()


def show_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.show()


def show_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.show()


def list_batch(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.batch_account.list()


def create_batch_applications_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application_package.create()


def delete_batch_applications_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application_package.delete()


def list_batch_applications_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application_package.list()


def show_batch_applications_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application_package.show()


def show_batch_applications_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application_package.show()


def list_batch_applications_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application_package.list()


def create_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.create()


def update_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.update()


def delete_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.delete()


def list_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.list()


def show_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.show()


def show_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.show()


def list_batch_applications(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.application.list()


def list_(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.operations.list()


def create_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.create()


def update_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.update()


def delete_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.delete()


def list_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.list()


def show_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.show()


def show_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.show()


def list_batch_certificates(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.certificate.list()


def create_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.create()


def update_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.update()


def delete_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.delete()


def list_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.list()


def show_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.show()


def show_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.show()


def list_batch_pools(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.pool.list()