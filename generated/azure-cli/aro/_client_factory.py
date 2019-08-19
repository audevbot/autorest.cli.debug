# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_aro(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.containerservice import OpenShift
    return get_mgmt_service_client(cli_ctx, OpenShift)


def cf_open_shift_managed_clusters(cli_ctx, *_):
    return cf_aro(cli_ctx).open_shift_managed_clusters

