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

        BODY = {
          "properties": {
            "update_configuration": {
              "operating_system": "Windows",
              "duration": "PT2H0M",
              "windows": {
                "excluded_kb_numbers": [
                  "168934",
                  "168973"
                ],
                "included_update_classifications": "Critical",
                "reboot_setting": "IfRequired"
              },
              "azure_virtual_machines": [
                "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-01",
                "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-02",
                "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-03"
              ],
              "non_azure_computer_names": [
                "box1.contoso.com",
                "box2.contoso.com"
              ],
              "targets": {
                "azure_queries": [
                  {
                    "scope": [
                      "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources",
                      "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067"
                    ],
                    "tag_settings": {
                      "tags": [
                        {
                          "tag1": [
                            "tag1Value1",
                            "tag1Value2",
                            "tag1Value3"
                          ]
                        },
                        {
                          "tag2": [
                            "tag2Value1",
                            "tag2Value2",
                            "tag2Value3"
                          ]
                        }
                      ],
                      "filter_operator": "All"
                    },
                    "locations": [
                      "Japan East",
                      "UK South"
                    ]
                  }
                ],
                "non_azure_queries": [
                  {
                    "function_alias": "SavedSearch1",
                    "workspace_id": "WorkspaceId1"
                  },
                  {
                    "function_alias": "SavedSearch2",
                    "workspace_id": "WorkspaceId2"
                  }
                ]
              }
            },
            "schedule_info": {
              "frequency": "Hour",
              "start_time": "2017-10-19T12:22:57+00:00",
              "time_zone": "America/Los_Angeles",
              "interval": "1",
              "expiry_time": "2018-11-09T11:22:57+00:00",
              "advanced_schedule": {
                "week_days": [
                  "Monday",
                  "Thursday"
                ]
              }
            },
            "tasks": {
              "pre_task": {
                "source": "HelloWorld",
                "parameters": {
                  "computername": "Computer1"
                }
              },
              "post_task": {
                "source": "GetCache"
              }
            }
          }
        }
        output = mgmt_client.software_update_configurations.create(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, SOFTWARE_UPDATE_CONFIGURATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.software_update_configurations.get_by_name(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, SOFTWARE_UPDATE_CONFIGURATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.software_update_configurations.delete(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, SOFTWARE_UPDATE_CONFIGURATION_NAME, BODY)
        BODY = {}
        output = mgmt_client.software_update_configurations.list(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, , BODY)
        BODY = {}
        output = mgmt_client.software_update_configurations.list(RESOURCE_GROUP, AUTOMATION_ACCOUNT_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()