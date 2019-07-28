# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_alerts(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.alertsmanagement import RecoveryServices
    return get_mgmt_service_client(cli_ctx, RecoveryServices)


def cf_smart_detector_alert_rules(cli_ctx, *_):
    return cf_alerts(cli_ctx).smart_detector_alert_rules

