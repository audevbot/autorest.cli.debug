# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_automationcfg_softwareupdateconfiguration(cmd, client,
                                                     resource_group,
                                                     automation_account_name,
                                                     name,
                                                     client_request_id,
                                                     properties,
                                                     update_configuration,
                                                     schedule_info,
                                                     error,
                                                     tasks,
                                                     provisioning_state,
                                                     creation_time,
                                                     created_by,
                                                     last_modified_time,
                                                     last_modified_by,
                                                     name,
                                                     id,
                                                     type):
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