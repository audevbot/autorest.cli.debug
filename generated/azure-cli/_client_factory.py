# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_vmwarecs(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from .vendored_sdks.vmwarecs operation-result import VMwareCloudSimple
    return get_mgmt_service_client(cli_ctx, VMwareCloudSimple)


def cf_dedicated_cloud_nodes(cli_ctx, *_):
    return cf_vmwarecs(cli_ctx).dedicated_cloud_nodes


def cf_dedicated_cloud_services(cli_ctx, *_):
    return cf_vmwarecs(cli_ctx).dedicated_cloud_services


def cf_virtual_machines(cli_ctx, *_):
    return cf_vmwarecs(cli_ctx).virtual_machines
