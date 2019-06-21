# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_automationjob_job(cmd, client,
                             resource_group,
                             automation_account_name,
                             name,
                             properties,
                             runbook,
                             parameters,
                             run_on,
                             started_by,
                             job_id,
                             creation_time,
                             status,
                             status_details,
                             start_time,
                             end_time,
                             exception,
                             last_modified_time,
                             last_status_modified_time,
                             provisioning_state,
                             client_request_id,
                             id,
                             type):
    return client.job.create()


def list_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    return client.job.list()


def show_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    return client.job.show()


def show_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    return client.job.show()


def list_automationjob_job(cmd, client,
                           resource_group,
                           automation_account_name,
                           name):
    return client.job.list()


def show_automationjob_job_stream(cmd, client,
                                  resource_group,
                                  automation_account_name,
                                  name,
                                  job_stream_id):
    return client.job_stream.show()


def list_automationjob_job_stream(cmd, client,
                                  resource_group,
                                  automation_account_name,
                                  name,
                                  job_stream_id):
    return client.job_stream.list()