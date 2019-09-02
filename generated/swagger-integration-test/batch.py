# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os
import time
import mock
import unittest

from azure_devtools.scenario_tests.const import MOCKED_SUBSCRIPTION_ID
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest, LiveScenarioTest, ResourceGroupPreparer, create_random_name, live_only, record_only
from azure.cli.core.util import get_file_json


class ResourceGroupScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_rg_scenario')
    def test_resource_group(self, resource_group):

        self.cmd('group create -n {rg} -l westus --tag a=b c', checks=[
            self.check('name', '{rg}'),
            self.check('tags', {'a': 'b', 'c': ''})
        ])

        self.kwargs['sub'] = self.get_subscription_id()
        self.kwargs['name'] = 'zimsxyzname'

        # batch_batchaccounts_put
        body = (
                 '{'
                 '  "location": "japaneast",'
                 '  "properties": {'
                 '    "autoStorage": {'
                 '      "storageAccountId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_put_1
        body = (
                 '{'
                 '  "location": "japaneast",'
                 '  "properties": {'
                 '    "autoStorage": {'
                 '      "storageAccountId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""'
                 '    },'
                 '    "poolAllocationMode": "UserSubscription",'
                 '    "keyVaultReference": {'
                 '      "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.KeyVault/vaults/" + VAULT_NAME + "",'
                 '      "url": "http://sample.vault.azure.net/"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Batch/batchAccounts?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_syncautostoragekeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/syncAutoStorageKeys?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_regeneratekeys_post
        body = (
                 '{'
                 '  "keyName": "Primary"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/regenerateKeys?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/listKeys?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_applications_versions_activate_post
        body = (
                 '{'
                 '  "format": "zip"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}/versions/{VERSION_NAME}/activate?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_applications_versions_put
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}/versions/{VERSION_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_applications_versions_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}/versions/{VERSION_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_applications_versions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}/versions/{VERSION_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_applications_versions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}/versions?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_applications_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "allowUpdates": False,'
                 '    "displayName": "myAppName"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_applications_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_applications_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_applications_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications/{APPLICATION_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_applications_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/applications?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_locations_quotas_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Batch/locations/{LOCATION_NAME}/quotas?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_locations_checknameavailability_post
        body = (
                 '{'
                 '  "name": "newaccountname",'
                 '  "type": "Microsoft.Batch/batchAccounts"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Batch/locations/{LOCATION_NAME}/checkNameAvailability?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_locations_checknameavailability_post_1
        body = (
                 '{'
                 '  "name": "existingaccountname",'
                 '  "type": "Microsoft.Batch/batchAccounts"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/providers/Microsoft.Batch/locations/{LOCATION_NAME}/checkNameAvailability?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",'
                 '    "password": "KG0UY40e..."'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_put_1
        body = (
                 '{'
                 '  "properties": {'
                 '    "data": "MIICrjCCAZagAwI...",'
                 '    "format": "Cer"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_put_2
        body = (
                 '{'
                 '  "properties": {'
                 '    "thumbprintAlgorithm": "SHA1",'
                 '    "thumbprint": "0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E",'
                 '    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",'
                 '    "password": "KG0UY40e...",'
                 '    "format": "Pfx"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_certificates_canceldelete_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/certificates/{CERTIFICATE_NAME}/cancelDelete?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_put
        body = (
                 '{'
                 '  "properties": {'
                 '    "vmSize": "STANDARD_D4",'
                 '    "deploymentConfiguration": {'
                 '      "cloudServiceConfiguration": {'
                 '        "osFamily": "5"'
                 '      }'
                 '    },'
                 '    "scaleSettings": {'
                 '      "fixedScale": {'
                 '        "targetDedicatedNodes": "3"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_put_1
        body = (
                 '{'
                 '  "properties": {'
                 '    "vmSize": "STANDARD_D4",'
                 '    "deploymentConfiguration": {'
                 '      "virtualMachineConfiguration": {'
                 '        "imageReference": {'
                 '          "publisher": "Canonical",'
                 '          "offer": "UbuntuServer",'
                 '          "sku": "14.04.5-LTS",'
                 '          "version": "latest"'
                 '        },'
                 '        "nodeAgentSkuId": "batch.node.ubuntu 14.04"'
                 '      }'
                 '    },'
                 '    "scaleSettings": {'
                 '      "autoScale": {'
                 '        "formula": "$TargetDedicatedNodes=1",'
                 '        "evaluationInterval": "PT5M"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_put_2
        body = (
                 '{'
                 '  "properties": {'
                 '    "displayName": "my-pool-name",'
                 '    "vmSize": "STANDARD_D4",'
                 '    "interNodeCommunication": "Enabled",'
                 '    "maxTasksPerNode": "13",'
                 '    "taskSchedulingPolicy": {'
                 '      "nodeFillType": "Pack"'
                 '    },'
                 '    "deploymentConfiguration": {'
                 '      "cloudServiceConfiguration": {'
                 '        "osFamily": "4",'
                 '        "osVersion": "WA-GUEST-OS-4.45_201708-01"'
                 '      }'
                 '    },'
                 '    "networkConfiguration": {'
                 '      "subnetId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",'
                 '      "endpointConfiguration": {'
                 '        "inboundNatPools": ['
                 '          {'
                 '            "name": "testnat",'
                 '            "protocol": "TCP",'
                 '            "backendPort": "12001",'
                 '            "frontendPortRangeStart": "15000",'
                 '            "frontendPortRangeEnd": "15100",'
                 '            "networkSecurityGroupRules": ['
                 '              {'
                 '                "access": "Allow",'
                 '                "sourceAddressPrefix": "192.100.12.45",'
                 '                "priority": "150"'
                 '              },'
                 '              {'
                 '                "access": "Deny",'
                 '                "sourceAddressPrefix": "*",'
                 '                "priority": "3500"'
                 '              }'
                 '            ]'
                 '          }'
                 '        ]'
                 '      }'
                 '    },'
                 '    "scaleSettings": {'
                 '      "fixedScale": {'
                 '        "targetDedicatedNodes": "6",'
                 '        "targetLowPriorityNodes": "28",'
                 '        "resizeTimeout": "PT8M",'
                 '        "nodeDeallocationOption": "TaskCompletion"'
                 '      }'
                 '    },'
                 '    "metadata": ['
                 '      {'
                 '        "name": "metadata-1",'
                 '        "value": "value-1"'
                 '      },'
                 '      {'
                 '        "name": "metadata-2",'
                 '        "value": "value-2"'
                 '      }'
                 '    ],'
                 '    "startTask": {'
                 '      "commandLine": "cmd /c SET",'
                 '      "resourceFiles": ['
                 '        {'
                 '          "httpUrl": "https://testaccount.blob.core.windows.net/example-blob-file",'
                 '          "filePath": "c:\\temp\\gohere",'
                 '          "fileMode": "777"'
                 '        }'
                 '      ],'
                 '      "environmentSettings": ['
                 '        {'
                 '          "name": "MYSET",'
                 '          "value": "1234"'
                 '        }'
                 '      ],'
                 '      "userIdentity": {'
                 '        "autoUser": {'
                 '          "scope": "Pool",'
                 '          "elevationLevel": "Admin"'
                 '        }'
                 '      },'
                 '      "maxTaskRetryCount": "6",'
                 '      "waitForSuccess": True'
                 '    },'
                 '    "userAccounts": ['
                 '      {'
                 '        "name": "username1",'
                 '        "password": "examplepassword",'
                 '        "elevationLevel": "Admin",'
                 '        "linuxUserConfiguration": {'
                 '          "sshPrivateKey": "sshprivatekeyvalue",'
                 '          "uid": "1234",'
                 '          "gid": "4567"'
                 '        }'
                 '      }'
                 '    ],'
                 '    "applicationPackages": ['
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/applications/" + APPLICATION_NAME + "",'
                 '        "version": "asdf"'
                 '      }'
                 '    ],'
                 '    "certificates": ['
                 '      {'
                 '        "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/certificates/" + CERTIFICATE_NAME + "",'
                 '        "storeLocation": "LocalMachine",'
                 '        "storeName": "MY",'
                 '        "visibility": ['
                 '          "RemoteUser"'
                 '        ]'
                 '      }'
                 '    ],'
                 '    "applicationLicenses": ['
                 '      "app-license0",'
                 '      "app-license1"'
                 '    ]'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_put_3
        body = (
                 '{'
                 '  "properties": {'
                 '    "vmSize": "STANDARD_D4",'
                 '    "deploymentConfiguration": {'
                 '      "virtualMachineConfiguration": {'
                 '        "imageReference": {'
                 '          "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/images/" + IMAGE_NAME + ""'
                 '        },'
                 '        "nodeAgentSkuId": "batch.node.ubuntu 14.04"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_put_4
        body = (
                 '{'
                 '  "properties": {'
                 '    "vmSize": "STANDARD_D4",'
                 '    "deploymentConfiguration": {'
                 '      "virtualMachineConfiguration": {'
                 '        "imageReference": {'
                 '          "publisher": "MicrosoftWindowsServer",'
                 '          "offer": "WindowsServer",'
                 '          "sku": "2016-Datacenter-SmallDisk",'
                 '          "version": "latest"'
                 '        },'
                 '        "nodeAgentSkuId": "batch.node.windows amd64",'
                 '        "windowsConfiguration": {'
                 '          "enableAutomaticUpdates": False'
                 '        },'
                 '        "licenseType": "Windows_Server",'
                 '        "dataDisks": ['
                 '          {'
                 '            "lun": "0",'
                 '            "caching": "ReadWrite",'
                 '            "diskSizeGB": "30",'
                 '            "storageAccountType": "Premium_LRS"'
                 '          },'
                 '          {'
                 '            "lun": "1",'
                 '            "caching": "None",'
                 '            "diskSizeGB": "200",'
                 '            "storageAccountType": "Standard_LRS"'
                 '          }'
                 '        ]'
                 '      }'
                 '    },'
                 '    "networkConfiguration": {'
                 '      "endpointConfiguration": {'
                 '        "inboundNatPools": ['
                 '          {'
                 '            "name": "testnat",'
                 '            "protocol": "TCP",'
                 '            "backendPort": "12001",'
                 '            "frontendPortRangeStart": "15000",'
                 '            "frontendPortRangeEnd": "15100",'
                 '            "networkSecurityGroupRules": ['
                 '              {'
                 '                "access": "Allow",'
                 '                "sourceAddressPrefix": "192.100.12.45",'
                 '                "priority": "150"'
                 '              },'
                 '              {'
                 '                "access": "Deny",'
                 '                "sourceAddressPrefix": "*",'
                 '                "priority": "3500"'
                 '              }'
                 '            ]'
                 '          }'
                 '        ]'
                 '      }'
                 '    },'
                 '    "scaleSettings": {'
                 '      "autoScale": {'
                 '        "formula": "$TargetDedicatedNodes=1",'
                 '        "evaluationInterval": "PT5M"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_patch_1
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_patch_2
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_patch_3
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}?api-version=2018-12-01 '
                 , checks=[
                          ])

        # batch_batchaccounts_pools_disableautoscale_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}/disableAutoScale?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # batch_batchaccounts_pools_stopresize_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Batch/batchAccounts/{BATCH_ACCOUNT_NAME}/pools/{POOL_NAME}/stopResize?api-version=2018-12-01 '
                 '--body "{body}"'
                 , checks=[
                          ])