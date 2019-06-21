# Create software update configuration
RESOURCE_GROUP="myresourcegroup"
AUTOMATION_ACCOUNT_NAME="myautomationaccount"
SOFTWARE_UPDATE_CONFIGURATION_NAME="mysoftwareupdateconfiguration"

az resource create --id /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.Automation/automationAccounts/$AUTOMATION_ACCOUNT_NAME/softwareUpdateConfigurations/$SOFTWARE_UPDATE_CONFIGURATION_NAME --api-version 2017-05-15-preview --is-full-object --properties '
{
  "properties": {
    "updateConfiguration": {
      "operatingSystem": "Windows",
      "duration": "PT2H0M",
      "windows": {
        "excludedKbNumbers": [
          "168934",
          "168973"
        ],
        "includedUpdateClassifications": "Critical",
        "rebootSetting": "IfRequired"
      },
      "azureVirtualMachines": [
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-01",
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-02",
        "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-03"
      ],
      "nonAzureComputerNames": [
        "box1.contoso.com",
        "box2.contoso.com"
      ],
      "targets": {
        "azureQueries": [
          {
            "scope": [
              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources",
              "/subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067"
            ],
            "tagSettings": {
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
              "filterOperator": "All"
            },
            "locations": [
              "Japan East",
              "UK South"
            ]
          }
        ],
        "nonAzureQueries": [
          {
            "functionAlias": "SavedSearch1",
            "workspaceId": "WorkspaceId1"
          },
          {
            "functionAlias": "SavedSearch2",
            "workspaceId": "WorkspaceId2"
          }
        ]
      }
    },
    "scheduleInfo": {
      "frequency": "Hour",
      "startTime": "2017-10-19T12:22:57+00:00",
      "timeZone": "America/Los_Angeles",
      "interval": "1",
      "expiryTime": "2018-11-09T11:22:57+00:00",
      "advancedSchedule": {
        "weekDays": [
          "Monday",
          "Thursday"
        ]
      }
    },
    "tasks": {
      "preTask": {
        "source": "HelloWorld",
        "parameters": {
          "COMPUTERNAME": "Computer1"
        }
      },
      "postTask": {
        "source": "GetCache",
        "parameters": null
      }
    }
  }
}
'