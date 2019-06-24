# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_softwareupdateconfiguration
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
    body={}
    body['properties'] = properties
    body['update_configuration'] = update_configuration
    body['schedule_info'] = schedule_info
    body['error'] = error
    body['tasks'] = tasks
    body['provisioning_state'] = provisioning_state
    body['creation_time'] = creation_time
    body['created_by'] = created_by
    body['last_modified_time'] = last_modified_time
    body['last_modified_by'] = last_modified_by
    return client.software_update_configurations.create(resource_group_name=resource_group, automation_account_name=automation_account_name, software_update_configuration_name=name, parameters=body)

# module equivalent: azure_rm_softwareupdateconfiguration
def delete_automationcfg_softwareupdateconfiguration(cmd, client,
                                                     resource_group,
                                                     automation_account_name,
                                                     name):
    return client.software_update_configurations.delete(resource_group_name=resource_group, automation_account_name=automation_account_name, software_update_configuration_name=name)

# module equivalent: azure_rm_softwareupdateconfiguration
def list_automationcfg_softwareupdateconfiguration(cmd, client,
                                                   resource_group,
                                                   automation_account_name,
                                                   name):
    return client.software_update_configurations.list()