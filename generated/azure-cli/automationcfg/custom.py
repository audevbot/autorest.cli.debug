# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_automationcfg_softwareupdateconfiguration(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.software_update_configurations.create()


def delete_automationcfg_softwareupdateconfiguration(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.software_update_configurations.delete()


def list_automationcfg_softwareupdateconfiguration(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.software_update_configurations.list()


def list_automationcfg_softwareupdateconfiguration(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.software_update_configurations.list()