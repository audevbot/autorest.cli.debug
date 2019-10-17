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
  "location": "japaneast",
  "properties": {
    "auto_storage": {
      "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
    }
  }
}
        output = mgmt_client.batch_account.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, BODY)
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
        output = mgmt_client.batch_account.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, BODY)
BODY = {
  "properties": {
    "auto_storage": {
      "storage_account_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + ""
    }
  }
}
        output = mgmt_client.batch_account.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, BODY)
BODY = {}
        output = mgmt_client.batch_account.delete(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, BODY)
BODY = {}
        output = mgmt_client.batch_account.get(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, BODY)
BODY = {}
        output = mgmt_client.batch_account.list(, BODY)
BODY = {}
        output = mgmt_client.batch_account.list_by_resource_group(RESOURCE_GROUP, , BODY)
BODY = {}
        output = mgmt_client.batch_account.synchronize_auto_storage_keys(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {
  "key_name": "Primary"
}
        output = mgmt_client.batch_account.regenerate_key(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {}
        output = mgmt_client.batch_account.get_keys(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {
  "format": "zip"
}
        output = mgmt_client.application_package.activate(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, , BODY)
BODY = {}
        output = mgmt_client.application_package.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, BODY)
BODY = {}
        output = mgmt_client.application_package.delete(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, BODY)
BODY = {}
        output = mgmt_client.application_package.get(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, VERSION_NAME, BODY)
BODY = {}
        output = mgmt_client.application_package.list(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, , BODY)
BODY = {
  "properties": {
    "allow_updates": False,
    "display_name": "myAppName"
  }
}
        output = mgmt_client.application.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
BODY = {}
        output = mgmt_client.application.delete(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
BODY = {}
        output = mgmt_client.application.get(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
BODY = {
  "properties": {
    "allow_updates": True,
    "display_name": "myAppName",
    "default_version": "2"
  }
}
        output = mgmt_client.application.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, APPLICATION_NAME, BODY)
BODY = {}
        output = mgmt_client.application.list(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {}
        output = mgmt_client.location.get_quotas(LOCATION_NAME, , BODY)
BODY = {
  "name": "newaccountname",
  "type": "Microsoft.Batch/batchAccounts"
}
        output = mgmt_client.location.check_name_availability(LOCATION_NAME, , BODY)
BODY = {
  "name": "existingaccountname",
  "type": "Microsoft.Batch/batchAccounts"
}
        output = mgmt_client.location.check_name_availability(LOCATION_NAME, , BODY)
BODY = {}
        output = mgmt_client.certificate.list_by_batch_account(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {}
        output = mgmt_client.certificate.list_by_batch_account(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {
  "properties": {
    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
    "password": "KG0UY40e..."
  }
}
        output = mgmt_client.certificate.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {
  "properties": {
    "data": "MIICrjCCAZagAwI...",
    "format": "Cer"
  }
}
        output = mgmt_client.certificate.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {
  "properties": {
    "thumbprint_algorithm": "SHA1",
    "thumbprint": "0A0E4F50D51BEADEAC1D35AFC5116098E7902E6E",
    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
    "password": "KG0UY40e...",
    "format": "Pfx"
  }
}
        output = mgmt_client.certificate.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {
  "properties": {
    "data": "MIIJsgIBAzCCCW4GCSqGSIb3DQE...",
    "password": "KG0UY40e..."
  }
}
        output = mgmt_client.certificate.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {}
        output = mgmt_client.certificate.delete(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {}
        output = mgmt_client.certificate.get(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {}
        output = mgmt_client.certificate.get(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, BODY)
BODY = {}
        output = mgmt_client.certificate.cancel_deletion(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, CERTIFICATE_NAME, , BODY)
BODY = {}
        output = mgmt_client.pool.list_by_batch_account(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
BODY = {}
        output = mgmt_client.pool.list_by_batch_account(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, , BODY)
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
        output = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
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
        output = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
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
        output = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
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
        output = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
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
        output = mgmt_client.pool.create(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
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
        output = mgmt_client.pool.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
BODY = {
  "properties": {
    "scale_settings": {
      "auto_scale": {
        "formula": "$TargetDedicatedNodes=34"
      }
    }
  }
}
        output = mgmt_client.pool.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
BODY = {
  "properties": {}
}
        output = mgmt_client.pool.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
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
        output = mgmt_client.pool.update(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
BODY = {}
        output = mgmt_client.pool.delete(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
BODY = {}
        output = mgmt_client.pool.get(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, BODY)
BODY = {}
        output = mgmt_client.pool.disable_auto_scale(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, , BODY)
BODY = {}
        output = mgmt_client.pool.stop_resize(RESOURCE_GROUP, BATCH_ACCOUNT_NAME, POOL_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()