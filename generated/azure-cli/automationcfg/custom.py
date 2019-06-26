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
                                                     update_configuration=None,
                                                     schedule_info=None,
                                                     error=None,
                                                     tasks=None):
    body={}
    body['update_configuration'] = update_configuration
    body['schedule_info'] = schedule_info
    body['error'] = error
    body['tasks'] = tasks
    return client.software_update_configurations.create(resource_group_name=resource_group, automation_account_name=automation_account_name, software_update_configuration_name=name, client_request_id=client_request_id, parameters=body)

# module equivalent: azure_rm_softwareupdateconfiguration
def delete_automationcfg_softwareupdateconfiguration(cmd, client,
                                                     resource_group,
                                                     automation_account_name,
                                                     name,
                                                     client_request_id=None):
    return client.software_update_configurations.delete(resource_group_name=resource_group, automation_account_name=automation_account_name, software_update_configuration_name=name, client_request_id=client_request_id)

# module equivalent: azure_rm_softwareupdateconfiguration
def list_automationcfg_softwareupdateconfiguration(cmd, client,
                                                   resource_group,
                                                   automation_account_name,
                                                   client_request_id=None):
    return client.software_update_configurations.list(resource_group_name=resource_group, automation_account_name=automation_account_name, client_request_id=client_request_id)