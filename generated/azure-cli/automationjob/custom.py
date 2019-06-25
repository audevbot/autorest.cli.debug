# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_automationjob
def create_automationjob_job(cmd, client,
                             resource_group,
                             automation_account_name,
                             name,
                             parameters=None,
                             client_request_id=None):
    body={}
    body['parameters'] = parameters
    return client.job.create(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name, parameters=body, client_request_id=client_request_id)

# module equivalent: azure_rm_automationjob
def list_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           client_request_id=None):
    return client.job.list_by_automation_account(resource_group_name=resource_group, automation_account_name=automation_account_name, client_request_id=client_request_id)

# module equivalent: azure_rm_automationjob
def show_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name,
                           client_request_id=None):
    return client.job.get(resource_group_name=resource_group, automation_account_name=automation_account_name, job_name=name, client_request_id=client_request_id)