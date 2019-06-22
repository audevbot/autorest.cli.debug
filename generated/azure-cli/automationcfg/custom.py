# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_automationcfg_softwareupdateconfiguration(cmd, client,
                                                     resource_group,
                                                     automation_account_name,
                                                     name,
                                                     client_request_id=None,
                                                     properties=None,
                                                     update_configuration=None,
                                                     schedule_info=None,
                                                     error=None,
                                                     tasks=None,
                                                     provisioning_state=None,
                                                     creation_time=None,
                                                     created_by=None,
                                                     last_modified_time=None,
                                                     last_modified_by=None,
                                                     id=None,
                                                     type=None):
    return client.software_update_configurations.create()


def delete_automationcfg_softwareupdateconfiguration(cmd, client,
                                                     resource_group,
                                                     automation_account_name,
                                                     name):
    return client.software_update_configurations.delete()


def list_automationcfg_softwareupdateconfiguration(cmd, client,
                                                   resource_group,
                                                   automation_account_name,
                                                   name):
    return client.software_update_configurations.list()


def list_automationcfg_softwareupdateconfiguration(cmd, client,
                                                   resource_group,
                                                   automation_account_name,
                                                   name):
    return client.software_update_configurations.list()