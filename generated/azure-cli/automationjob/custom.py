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
                             properties=None,
                             runbook=None,
                             parameters=None,
                             run_on=None,
                             started_by=None,
                             job_id=None,
                             creation_time=None,
                             status=None,
                             status_details=None,
                             start_time=None,
                             end_time=None,
                             exception=None,
                             last_modified_time=None,
                             last_status_modified_time=None,
                             provisioning_state=None,
                             client_request_id=None,
                             id=None,
                             type=None):
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