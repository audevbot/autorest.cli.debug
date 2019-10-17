# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.xxxx
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

class MgmtXxxTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtXxxTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.xxxx.XxxMgmtClient
        )
    
    def test_xxx(self):

        BODY = {}
        output = mgmt_client.alerts.meta_data(, BODY)
        BODY = {}
        output = mgmt_client.alerts.get_all(, BODY)
        BODY = {}
        output = mgmt_client.alerts.get_by_id(ALERT_NAME, BODY)
        BODY = {
          "comments": "Acknowledging alert"
        }
        output = mgmt_client.alerts.change_state(ALERT_NAME, , BODY)
        BODY = {
          "comments": "Acknowledging alert"
        }
        output = mgmt_client.alerts.change_state(ALERT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.alerts.get_summary(, BODY)
        BODY = {}
        output = mgmt_client.smart_groups.get_all(, BODY)
        BODY = {}
        output = mgmt_client.smart_groups.get_by_id(SMART_GROUP_NAME, BODY)
        BODY = {
          "comments": "Acknowledging smart group"
        }
        output = mgmt_client.smart_groups.change_state(SMART_GROUP_NAME, , BODY)
        BODY = {
          "comments": "Acknowledging alert"
        }
        output = mgmt_client.alerts.change_state(ALERT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.action_rules.list_by_subscription(, BODY)
        BODY = {}
        output = mgmt_client.action_rules.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.action_rules.get_by_name(RESOURCE_GROUP, ACTION_RULE_NAME, BODY)
        BODY = {
          "location": "Global",
          "properties": {
            "scope": {
              "scope_type": "ResourceGroup",
              "values": [
                "/subscriptions/1e3ff1c0-771a-4119-a03b-be82a51e232d/resourceGroups/alertscorrelationrg"
              ]
            },
            "conditions": {
              "severity": {
                "operator": "Equals",
                "values": [
                  "Sev0",
                  "Sev2"
                ]
              },
              "monitor_service": {
                "operator": "Equals",
                "values": [
                  "Platform",
                  "Application Insights"
                ]
              },
              "monitor_condition": {
                "operator": "Equals",
                "values": [
                  "Fired"
                ]
              },
              "target_resource_type": {
                "operator": "NotEquals",
                "values": [
                  "Microsoft.Compute/VirtualMachines"
                ]
              }
            },
            "type": "Suppression",
            "suppression_config": {
              "recurrence_type": "Daily",
              "schedule": {
                "start_date": "12/09/2018",
                "end_date": "12/18/2018",
                "start_time": "06:00:00",
                "end_time": "14:00:00"
              }
            },
            "description": "Action rule on resource group for daily suppression",
            "status": "Enabled"
          }
        }
        output = mgmt_client.action_rules.create_update(RESOURCE_GROUP, ACTION_RULE_NAME, BODY)
        BODY = {}
        output = mgmt_client.action_rules.delete(RESOURCE_GROUP, ACTION_RULE_NAME, BODY)
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          },
          "properties": {
            "status": "Disabled"
          }
        }
        output = mgmt_client.action_rules.update(RESOURCE_GROUP, ACTION_RULE_NAME, BODY)
        BODY = {}
        output = mgmt_client.smart_detector_alert_rules.list(, BODY)
        BODY = {}
        output = mgmt_client.smart_detector_alert_rules.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.smart_detector_alert_rules.get(RESOURCE_GROUP, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        BODY = {
          "properties": {
            "description": "Sample smart detector alert rule description",
            "state": "Enabled",
            "severity": "Sev3",
            "frequency": "PT5M",
            "detector": {
              "id": "VMMemoryLeak"
            },
            "scope": [
              "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/MyVms/providers/Microsoft.Compute/virtualMachines/vm1"
            ],
            "action_groups": {
              "custom_email_subject": "My custom email subject",
              "custom_webhook_payload": "{\"AlertRuleName\":\"#alertrulename\"}",
              "group_ids": [
                "/subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourcegroups/actionGroups/providers/microsoft.insights/actiongroups/MyActionGroup"
              ]
            },
            "throttling": {
              "duration": "PT20M"
            }
          }
        }
        output = mgmt_client.smart_detector_alert_rules.create_or_update(RESOURCE_GROUP, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        BODY = {
          "tags": {
            "new_key": "newVal"
          },
          "properties": {
            "description": "New description for patching",
            "frequency": "PT1M"
          }
        }
        output = mgmt_client.smart_detector_alert_rules.patch(RESOURCE_GROUP, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        BODY = {}
        output = mgmt_client.smart_detector_alert_rules.delete(RESOURCE_GROUP, SMART_DETECTOR_ALERT_RULE_NAME, BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()