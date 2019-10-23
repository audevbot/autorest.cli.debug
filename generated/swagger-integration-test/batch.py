# coding: utf-8

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import unittest

import azure.mgmt.batch
from devtools_testutils import AzureMgmtTestCase, ResourceGroupPreparer

AZURE_LOCATION = 'eastus'

class MgmtBatchManagementTest(AzureMgmtTestCase):

    def setUp(self):
        super(MgmtBatchManagementTest, self).setUp()
        self.mgmt_client = self.create_mgmt_client(
            azure.mgmt.batch.BatchManagement
        )
    
    @ResourceGroupPreparer(location=AZURE_LOCATION)
    def test_batch(self, resource_group):

        SERVICE_NAME = "myapimrndxyz"
        BODY = {
          "location": "japaneast",
          "properties": {
            "auto_storage": {
              "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
            }
          }
        }
        azure_operation_poller = self.mgmt_client.batch_account.create(resource_group.name, BATCH_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "location": "japaneast",
          "properties": {
            "auto_storage": {
              "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
            },
            "pool_allocation_mode": "UserSubscription",
            "key_vault_reference": {
              "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.KeyVault/vaults/" + VAULT_NAME + "",
              "url": "http://sample.vault.azure.net/"
            }
          }
        }
        azure_operation_poller = self.mgmt_client.batch_account.create(resource_group.name, BATCH_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "auto_storage": {
              "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
            }
          }
        }
        azure_operation_poller = self.mgmt_client.batch_account.update(resource_group.name, BATCH_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.batch_account.delete(resource_group.name, BATCH_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.batch_account.get(resource_group.name, BATCH_ACCOUNT_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.batch_account.list(, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.batch_account.list_by_resource_group(resource_group.name, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.batch_account.synchronize_auto_storage_keys(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "key_name": "Primary"
        }
        azure_operation_poller = self.mgmt_client.batch_account.regenerate_key(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.batch_account.get_keys(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "format": "zip"
        }
        azure_operation_poller = self.mgmt_client.application_package.activate(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application_package.create(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application_package.delete(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application_package.get(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application_package.list(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "allow_updates": False,
            "display_name": "myAppName"
          }
        }
        azure_operation_poller = self.mgmt_client.application.create(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application.delete(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application.get(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "allow_updates": True,
            "display_name": "myAppName",
            "default_version": "2"
          }
        }
        azure_operation_poller = self.mgmt_client.application.update(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.application_package.list(resource_group.name, BATCH_ACCOUNT_NAME, APPLICATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.location.get_quotas(LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "newaccountname",
          "type": "Microsoft.Batch/batchAccounts"
        }
        azure_operation_poller = self.mgmt_client.location.check_name_availability(LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "name": "existingaccountname",
          "type": "Microsoft.Batch/batchAccounts"
        }
        azure_operation_poller = self.mgmt_client.location.check_name_availability(LOCATION_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.list_by_batch_account(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.list_by_batch_account(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
            "password": "KG0UY40e..."
          }
        }
        azure_operation_poller = self.mgmt_client.certificate.create(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "data": "MIICrjCCAZagAwI...",
            "format": "Cer"
          }
        }
        azure_operation_poller = self.mgmt_client.certificate.create(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "thumbprint_algorithm": "SHA1",
            "thumbprint": "0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E",
            "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
            "password": "KG0UY40e...",
            "format": "Pfx"
          }
        }
        azure_operation_poller = self.mgmt_client.certificate.create(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
            "password": "KG0UY40e..."
          }
        }
        azure_operation_poller = self.mgmt_client.certificate.update(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.delete(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.get(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.get(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.certificate.cancel_deletion(resource_group.name, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.pool.list_by_batch_account(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.pool.list_by_batch_account(resource_group.name, BATCH_ACCOUNT_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "vm_size": "STANDARD_D4",
            "deployment_configuration": {
              "cloud_service_configuration": {
                "os_family": "5"
              }
            },
            "scale_settings": {
              "fixed_scale": {
                "target_dedicated_nodes": "3"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.pool.create(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "vm_size": "STANDARD_D4",
            "deployment_configuration": {
              "virtual_machine_configuration": {
                "image_reference": {
                  "publisher": "Canonical",
                  "offer": "UbuntuServer",
                  "sku": "14.04.5-LTS",
                  "version": "latest"
                },
                "node_agent_sku_id": "batch.node.ubuntu 14.04"
              }
            },
            "scale_settings": {
              "auto_scale": {
                "formula": "$TargetDedicatedNodes=1",
                "evaluation_interval": "PT5M"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.pool.create(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "display_name": "my-pool-name",
            "vm_size": "STANDARD_D4",
            "inter_node_communication": "Enabled",
            "max_tasks_per_node": "13",
            "task_scheduling_policy": {
              "node_fill_type": "Pack"
            },
            "deployment_configuration": {
              "cloud_service_configuration": {
                "os_family": "4",
                "os_version": "WA-GUEST-OS-4.45_201708-01"
              }
            },
            "network_configuration": {
              "subnet_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Network/virtualNetworks/" + VIRTUAL_NETWORK_NAME + "/subnets/" + SUBNET_NAME + "",
              "endpoint_configuration": {
                "inbound_nat_pools": [
                  {
                    "name": "testnat",
                    "protocol": "TCP",
                    "backend_port": "12001",
                    "frontend_port_range_start": "15000",
                    "frontend_port_range_end": "15100",
                    "network_security_group_rules": [
                      {
                        "access": "Allow",
                        "source_address_prefix": "192.100.12.45",
                        "priority": "150"
                      },
                      {
                        "access": "Deny",
                        "source_address_prefix": "*",
                        "priority": "3500"
                      }
                    ]
                  }
                ]
              }
            },
            "scale_settings": {
              "fixed_scale": {
                "target_dedicated_nodes": "6",
                "target_low_priority_nodes": "28",
                "resize_timeout": "PT8M",
                "node_deallocation_option": "TaskCompletion"
              }
            },
            "metadata": [
              {
                "name": "metadata-1",
                "value": "value-1"
              },
              {
                "name": "metadata-2",
                "value": "value-2"
              }
            ],
            "start_task": {
              "command_line": "cmd /c SET",
              "resource_files": [
                {
                  "http_url": "https://testaccount.blob.core.windows.net/example-blob-file",
                  "file_path": "c:\\temp\\gohere",
                  "file_mode": "777"
                }
              ],
              "environment_settings": [
                {
                  "name": "MYSET",
                  "value": "1234"
                }
              ],
              "user_identity": {
                "auto_user": {
                  "scope": "Pool",
                  "elevation_level": "Admin"
                }
              },
              "max_task_retry_count": "6",
              "wait_for_success": True
            },
            "user_accounts": [
              {
                "name": "username1",
                "password": "examplepassword",
                "elevation_level": "Admin",
                "linux_user_configuration": {
                  "ssh_private_key": "sshprivatekeyvalue",
                  "uid": "1234",
                  "gid": "4567"
                }
              }
            ],
            "application_packages": [
              {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/applications/" + APPLICATION_NAME + "",
                "version": "asdf"
              }
            ],
            "certificates": [
              {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/certificates/" + CERTIFICATE_NAME + "",
                "store_location": "LocalMachine",
                "store_name": "MY",
                "visibility": [
                  "RemoteUser"
                ]
              }
            ],
            "application_licenses": [
              "app-license0",
              "app-license1"
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.pool.create(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "vm_size": "STANDARD_D4",
            "deployment_configuration": {
              "virtual_machine_configuration": {
                "image_reference": {
                  "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Compute/images/" + IMAGE_NAME + ""
                },
                "node_agent_sku_id": "batch.node.ubuntu 14.04"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.pool.create(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "vm_size": "STANDARD_D4",
            "deployment_configuration": {
              "virtual_machine_configuration": {
                "image_reference": {
                  "publisher": "MicrosoftWindowsServer",
                  "offer": "WindowsServer",
                  "sku": "2016-Datacenter-SmallDisk",
                  "version": "latest"
                },
                "node_agent_sku_id": "batch.node.windows amd64",
                "windows_configuration": {
                  "enable_automatic_updates": False
                },
                "license_type": "Windows_Server",
                "data_disks": [
                  {
                    "lun": "0",
                    "caching": "ReadWrite",
                    "disk_size_gb": "30",
                    "storage_account_type": "Premium_LRS"
                  },
                  {
                    "lun": "1",
                    "caching": "None",
                    "disk_size_gb": "200",
                    "storage_account_type": "Standard_LRS"
                  }
                ]
              }
            },
            "network_configuration": {
              "endpoint_configuration": {
                "inbound_nat_pools": [
                  {
                    "name": "testnat",
                    "protocol": "TCP",
                    "backend_port": "12001",
                    "frontend_port_range_start": "15000",
                    "frontend_port_range_end": "15100",
                    "network_security_group_rules": [
                      {
                        "access": "Allow",
                        "source_address_prefix": "192.100.12.45",
                        "priority": "150"
                      },
                      {
                        "access": "Deny",
                        "source_address_prefix": "*",
                        "priority": "3500"
                      }
                    ]
                  }
                ]
              }
            },
            "scale_settings": {
              "auto_scale": {
                "formula": "$TargetDedicatedNodes=1",
                "evaluation_interval": "PT5M"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.pool.create(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "scale_settings": {
              "fixed_scale": {
                "target_dedicated_nodes": "5",
                "target_low_priority_nodes": "0",
                "resize_timeout": "PT8M",
                "node_deallocation_option": "TaskCompletion"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.pool.update(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "scale_settings": {
              "auto_scale": {
                "formula": "$TargetDedicatedNodes=34"
              }
            }
          }
        }
        azure_operation_poller = self.mgmt_client.pool.update(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {}
        }
        azure_operation_poller = self.mgmt_client.pool.update(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {
          "properties": {
            "metadata": [
              {
                "name": "key1",
                "value": "value1"
              }
            ],
            "application_packages": [
              {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/applications/" + APPLICATION_NAME + ""
              },
              {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/applications/" + APPLICATION_NAME + "",
                "version": "1.0"
              }
            ],
            "certificates": [
              {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Batch/batchAccounts/" + BATCH_ACCOUNT_NAME + "/pools/" + POOL_NAME + "/certificates/" + CERTIFICATE_NAME + "",
                "store_location": "LocalMachine",
                "store_name": "MY"
              }
            ]
          }
        }
        azure_operation_poller = self.mgmt_client.pool.update(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.pool.delete(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.pool.get(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.pool.disable_auto_scale(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, , BODY)
        result_create = azure_operation_poller.result()
        BODY = {}
        azure_operation_poller = self.mgmt_client.pool.stop_resize(resource_group.name, BATCH_ACCOUNT_NAME, POOL_NAME, , BODY)
        result_create = azure_operation_poller.result()


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()