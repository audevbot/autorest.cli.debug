# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

import json


# module equivalent: azure_rm_alertsmanagementsmartdetectoralertrule
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{{ smart_detector_alert_rule_name }}
def create_alerts(cmd, client,
                  resource_group,
                  name,
                  state,
                  severity,
                  frequency,
                  detector,
                  scope,
                  action_groups,
                  location=None,
                  tags=None,
                  description=None,
                  throttling=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # unknown-primary[object]
    body['description'] = description  # str
    body['state'] = state  # str
    body['severity'] = severity  # str
    body['frequency'] = frequency  # unknown-primary[timeSpan]
    body['detector'] = json.loads(detector) if isinstance(detector, str) else detector
    body['scope'] = json.loads(scope) if isinstance(scope, str) else scope
    body['action_groups'] = json.loads(action_groups) if isinstance(action_groups, str) else action_groups
    body['throttling'] = json.loads(throttling) if isinstance(throttling, str) else throttling
    return client.create_or_update(resource_group_name=resource_group, alert_rule_name=name, parameters=body)


# module equivalent: azure_rm_alertsmanagementsmartdetectoralertrule
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{{ smart_detector_alert_rule_name }}
def update_alerts(cmd, client, body,
                  resource_group,
                  name,
                  state,
                  severity,
                  frequency,
                  detector,
                  scope,
                  action_groups,
                  location=None,
                  tags=None,
                  description=None,
                  throttling=None):
    body = client.get(resource_group_name=resource_group, alert_rule_name=name).as_dict()
    body.location = location  # str
    body.tags = tags  # unknown-primary[object]
    body.description = description  # str
    body.state = state  # str
    body.severity = severity  # str
    body.frequency = frequency  # unknown-primary[timeSpan]
    body.detector = json.loads(detector) if isinstance(detector, str) else detector
    body.scope = json.loads(scope) if isinstance(scope, str) else scope
    body.action_groups = json.loads(action_groups) if isinstance(action_groups, str) else action_groups
    body.throttling = json.loads(throttling) if isinstance(throttling, str) else throttling
    return client.create_or_update(resource_group_name=resource_group, alert_rule_name=name, parameters=body)


# module equivalent: azure_rm_alertsmanagementsmartdetectoralertrule
# URL: /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group }}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{{ smart_detector_alert_rule_name }}
def list_alerts(cmd, client,
                resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list()
