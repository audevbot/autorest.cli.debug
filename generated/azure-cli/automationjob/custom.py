# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_automationjob_job(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job.create()


def list_automationjob_job(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job.list()


def show_automationjob_job(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job.show()


def show_automationjob_job(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job.show()


def list_automationjob_job(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job.list()


def show_automationjob_job_stream(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job_stream.show()


def list_automationjob_job_stream(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.job_stream.list()