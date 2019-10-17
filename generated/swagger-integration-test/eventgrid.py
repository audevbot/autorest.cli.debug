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
        output = mgmt_client.event_subscriptions.get(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "WebHook",
              "properties": {
                "endpoint_url": "https://requestb.in/15ksip71"
              }
            },
            "filter": {
              "is_subject_case_sensitive": False
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "WebHook",
              "properties": {
                "endpoint_url": "https://requestb.in/15ksip71"
              }
            },
            "filter": {
              "is_subject_case_sensitive": False,
              "subject_begins_with": "ExamplePrefix",
              "subject_ends_with": "ExampleSuffix"
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "WebHook",
              "properties": {
                "endpoint_url": "https://requestb.in/15ksip71"
              }
            },
            "filter": {
              "is_subject_case_sensitive": False,
              "subject_begins_with": "ExamplePrefix",
              "subject_ends_with": "ExampleSuffix"
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "WebHook",
              "properties": {
                "endpoint_url": "https://contosofunction.azurewebsites.net/api/HttpTriggerCSharp1?code=<HIDDEN>"
              }
            },
            "filter": {
              "is_subject_case_sensitive": False,
              "subject_begins_with": "ExamplePrefix",
              "subject_ends_with": "ExampleSuffix"
            },
            "dead_letter_destination": {
              "endpoint_type": "StorageBlob",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
                "blob_container_name": "contosocontainer"
              }
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "EventHub",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME + ""
              }
            },
            "filter": {
              "is_subject_case_sensitive": False,
              "subject_begins_with": "ExamplePrefix",
              "subject_ends_with": "ExampleSuffix"
            },
            "dead_letter_destination": {
              "endpoint_type": "StorageBlob",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
                "blob_container_name": "contosocontainer"
              }
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "HybridConnection",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Relay/namespaces/" + NAMESPACE_NAME + "/hybridConnections/" + HYBRID_CONNECTION_NAME + ""
              }
            },
            "filter": {
              "is_subject_case_sensitive": False,
              "subject_begins_with": "ExamplePrefix",
              "subject_ends_with": "ExampleSuffix"
            },
            "dead_letter_destination": {
              "endpoint_type": "StorageBlob",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
                "blob_container_name": "contosocontainer"
              }
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "properties": {
            "destination": {
              "endpoint_type": "StorageQueue",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
                "queue_name": "queue1"
              }
            },
            "filter": {
              "is_subject_case_sensitive": False,
              "subject_begins_with": "ExamplePrefix",
              "subject_ends_with": "ExampleSuffix"
            },
            "dead_letter_destination": {
              "endpoint_type": "StorageBlob",
              "properties": {
                "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",
                "blob_container_name": "contosocontainer"
              }
            }
          }
        }
        output = mgmt_client.event_subscriptions.create_or_update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.delete(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.delete(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.delete(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.delete(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "destination": {
            "endpoint_type": "WebHook",
            "properties": {
              "endpoint_url": "https://requestb.in/15ksip71"
            }
          },
          "filter": {
            "is_subject_case_sensitive": True,
            "subject_begins_with": "existingPrefix",
            "subject_ends_with": "newSuffix"
          },
          "labels": [
            "label1",
            "label2"
          ]
        }
        output = mgmt_client.event_subscriptions.update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "destination": {
            "endpoint_type": "EventHub",
            "properties": {
              "resource_id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME + ""
            }
          },
          "filter": {
            "is_subject_case_sensitive": True,
            "subject_begins_with": "existingPrefix",
            "subject_ends_with": "newSuffix"
          },
          "labels": [
            "label1",
            "label2"
          ]
        }
        output = mgmt_client.event_subscriptions.update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "destination": {
            "endpoint_type": "WebHook",
            "properties": {
              "endpoint_url": "https://requestb.in/15ksip71"
            }
          },
          "filter": {
            "is_subject_case_sensitive": True,
            "subject_begins_with": "existingPrefix",
            "subject_ends_with": "newSuffix"
          },
          "labels": [
            "label1",
            "label2"
          ]
        }
        output = mgmt_client.event_subscriptions.update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {
          "destination": {
            "endpoint_type": "WebHook",
            "properties": {
              "endpoint_url": "https://requestb.in/15ksip71"
            }
          },
          "filter": {
            "is_subject_case_sensitive": True,
            "subject_begins_with": "existingPrefix",
            "subject_ends_with": "newSuffix"
          },
          "labels": [
            "label1",
            "label2"
          ]
        }
        output = mgmt_client.event_subscriptions.update(EVENT_SUBSCRIPTION_NAME, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get_full_url(EVENT_SUBSCRIPTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get_full_url(EVENT_SUBSCRIPTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get_full_url(EVENT_SUBSCRIPTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.get_full_url(EVENT_SUBSCRIPTION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_global_by_subscription(, BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_global_by_subscription_for_topic_type(TOPIC_TYPE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_global_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_global_by_resource_group_for_topic_type(RESOURCE_GROUP, TOPIC_TYPE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_regional_by_subscription(LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_regional_by_resource_group(RESOURCE_GROUP, LOCATION_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_regional_by_subscription_for_topic_type(LOCATION_NAME, TOPIC_TYPE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_regional_by_resource_group_for_topic_type(RESOURCE_GROUP, LOCATION_NAME, TOPIC_TYPE_NAME, , BODY)
        BODY = {}
        output = mgmt_client.event_subscriptions.list_by_resource(RESOURCE_GROUP, {RESOURCE_TYPE_NAME}_NAME, , BODY)
        BODY = {}
        output = mgmt_client.operations.list(, BODY)
        BODY = {}
        output = mgmt_client.topics.get(RESOURCE_GROUP, TOPIC_NAME, BODY)
        BODY = {
          "location": "westus2",
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        output = mgmt_client.topics.create_or_update(RESOURCE_GROUP, TOPIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.topics.delete(RESOURCE_GROUP, TOPIC_NAME, BODY)
        BODY = {
          "tags": {
            "tag1": "value1",
            "tag2": "value2"
          }
        }
        output = mgmt_client.topics.update(RESOURCE_GROUP, TOPIC_NAME, BODY)
        BODY = {}
        output = mgmt_client.topics.list_by_subscription(, BODY)
        BODY = {}
        output = mgmt_client.topics.list_by_resource_group(RESOURCE_GROUP, , BODY)
        BODY = {}
        output = mgmt_client.topics.list_shared_access_keys(RESOURCE_GROUP, TOPIC_NAME, , BODY)
        BODY = {
          "key_name": "key1"
        }
        output = mgmt_client.topics.regenerate_key(RESOURCE_GROUP, TOPIC_NAME, , BODY)
        BODY = {}
        output = mgmt_client.topics.list_event_types(RESOURCE_GROUP, {RESOURCE_TYPE_NAME}_NAME, , BODY)
        BODY = {}
        output = mgmt_client.topic_types.list(, BODY)
        BODY = {}
        output = mgmt_client.topic_types.get(TOPIC_TYPE_NAME, BODY)
        BODY = {}
        output = mgmt_client.topic_types.list_event_types(TOPIC_TYPE_NAME, , BODY)


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()