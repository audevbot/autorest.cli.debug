# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_healthcareapis(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from .vendored_sdks.healthcareapis import HealthCareApis
    return get_mgmt_service_client(cli_ctx, HealthCareApis)


def cf_services(cli_ctx, *_):
    return cf_healthcareapis(cli_ctx).services


def cf_operations(cli_ctx, *_):
    return cf_healthcareapis(cli_ctx).operations


def cf_operation_results(cli_ctx, *_):
    return cf_healthcareapis(cli_ctx).operation_results
