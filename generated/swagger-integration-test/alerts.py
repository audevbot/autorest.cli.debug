# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.alertsmanagement
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtRecoveryServicesTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtRecoveryServicesTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.alertsmanagement.RecoveryServices
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_alerts(self, resource_group):

SERVICE_NAME = "myapimrndxyz"
        BODY = {}
        azure_operation_poller = self.mgmt_client.alerts.meta_data(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.alerts.get_all(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.alerts.get_by_id(ALERT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "comments": "Acknowledging alert"
        }
        azure_operation_poller = self.mgmt_client.alerts.change_state(ALERT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "comments": "Acknowledging alert"
        }
        azure_operation_poller = self.mgmt_client.alerts.change_state(ALERT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.alerts.get_summary(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.smart_groups.get_all(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.smart_groups.get_by_id(SMART_GROUP_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "comments": "Acknowledging smart group"
        }
        azure_operation_poller = self.mgmt_client.smart_groups.change_state(SMART_GROUP_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "comments": "Acknowledging alert"
        }
        azure_operation_poller = self.mgmt_client.alerts.change_state(ALERT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.action_rules.list_by_subscription(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.action_rules.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.action_rules.get_by_name(resource_group.name, ACTION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
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
        azure_operation_poller = self.mgmt_client.action_rules.create_update(resource_group.name, ACTION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.action_rules.delete(resource_group.name, ACTION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "key1": "value1",
            "key2": "value2"
          },
          "properties": {
            "status": "Disabled"
          }
        }
        azure_operation_poller = self.mgmt_client.action_rules.update(resource_group.name, ACTION_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.smart_detector_alert_rules.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.smart_detector_alert_rules.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.smart_detector_alert_rules.get(resource_group.name, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
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
        azure_operation_poller = self.mgmt_client.smart_detector_alert_rules.create_or_update(resource_group.name, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "tags": {
            "new_key": "newVal"
          },
          "properties": {
            "description": "New description for patching",
            "frequency": "PT1M"
          }
        }
        azure_operation_poller = self.mgmt_client.smart_detector_alert_rules.patch(resource_group.name, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.smart_detector_alert_rules.delete(resource_group.name, SMART_DETECTOR_ALERT_RULE_NAME, BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()