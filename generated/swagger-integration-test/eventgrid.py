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

        # EventSubscriptions_GetForSubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_GetForResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_GetForResource
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_GetForCustomTopic
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForSubscription
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "WebHook",'
                 '      "properties": {'
                 '        "endpointUrl": "https://requestb.in/15ksip71"'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForResourceGroup
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "WebHook",'
                 '      "properties": {'
                 '        "endpointUrl": "https://requestb.in/15ksip71"'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False,'
                 '      "subjectBeginsWith": "ExamplePrefix",'
                 '      "subjectEndsWith": "ExampleSuffix"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForResource
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "WebHook",'
                 '      "properties": {'
                 '        "endpointUrl": "https://requestb.in/15ksip71"'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False,'
                 '      "subjectBeginsWith": "ExamplePrefix",'
                 '      "subjectEndsWith": "ExampleSuffix"'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForCustomTopic_WebhookDestination
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "WebHook",'
                 '      "properties": {'
                 '        "endpointUrl": "https://contosofunction.azurewebsites.net/api/HttpTriggerCSharp1?code=<HIDDEN>"'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False,'
                 '      "subjectBeginsWith": "ExamplePrefix",'
                 '      "subjectEndsWith": "ExampleSuffix"'
                 '    },'
                 '    "deadLetterDestination": {'
                 '      "endpointType": "StorageBlob",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",'
                 '        "blobContainerName": "contosocontainer"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForCustomTopic_EventHubDestination
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "EventHub",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.EventHub/namespaces/" + NAMESPACE_NAME + "/eventhubs/" + EVENTHUB_NAME + ""'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False,'
                 '      "subjectBeginsWith": "ExamplePrefix",'
                 '      "subjectEndsWith": "ExampleSuffix"'
                 '    },'
                 '    "deadLetterDestination": {'
                 '      "endpointType": "StorageBlob",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",'
                 '        "blobContainerName": "contosocontainer"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForCustomTopic_HybridConnectionDestination
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "HybridConnection",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Relay/namespaces/" + NAMESPACE_NAME + "/hybridConnections/" + HYBRID_CONNECTION_NAME + ""'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False,'
                 '      "subjectBeginsWith": "ExamplePrefix",'
                 '      "subjectEndsWith": "ExampleSuffix"'
                 '    },'
                 '    "deadLetterDestination": {'
                 '      "endpointType": "StorageBlob",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",'
                 '        "blobContainerName": "contosocontainer"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_CreateOrUpdateForCustomTopic_StorageQueueDestination
        body = (
                 '{'
                 '  "properties": {'
                 '    "destination": {'
                 '      "endpointType": "StorageQueue",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",'
                 '        "queueName": "queue1"'
                 '      }'
                 '    },'
                 '    "filter": {'
                 '      "isSubjectCaseSensitive": False,'
                 '      "subjectBeginsWith": "ExamplePrefix",'
                 '      "subjectEndsWith": "ExampleSuffix"'
                 '    },'
                 '    "deadLetterDestination": {'
                 '      "endpointType": "StorageBlob",'
                 '      "properties": {'
                 '        "resourceId": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + RESOURCE_GROUP + "/providers/Microsoft.Storage/storageAccounts/" + STORAGE_ACCOUNT_NAME + "",'
                 '        "blobContainerName": "contosocontainer"'
                 '      }'
                 '    }'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_DeleteForSubscription
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_DeleteForResourceGroup
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_DeleteForResource
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_DeleteForCustomTopic
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_UpdateForSubscription
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_UpdateForResourceGroup
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_UpdateForResource
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_UpdateForCustomTopic
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_GetFullUrlForSubscription
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}/getFullUrl?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_GetFullUrlForResourceGroup
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}/getFullUrl?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_GetFullUrlForResource
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}/getFullUrl?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_GetFullUrlForCustomTopic
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{EVENT_SUBSCRIPTION_NAME}/getFullUrl?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # EventSubscriptions_ListGlobalBySubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListGlobalBySubscriptionForTopicType
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListGlobalByResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListGlobalByResourceGroupForTopicType
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListRegionalBySubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListRegionalByResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListRegionalBySubscriptionForTopicType
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListRegionalByResourceGroupForTopicType
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # EventSubscriptions_ListByResource
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/{providerNamespace}/{resourceTypeName}/{{RESOURCE_TYPE_NAME}_NAME}/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Operations_List
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/operations?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Topics_Get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Topics_CreateOrUpdate
        body = (
                 '{'
                 '  "location": "westus2",'
                 '  "tags": {'
                 '    "tag1": "value1",'
                 '    "tag2": "value2"'
                 '  }'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method put '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Topics_Delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Topics_Update
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Topics_ListBySubscription
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/topics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Topics_ListByResourceGroup
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # Topics_ListSharedAccessKeys
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}/listKeys?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Topics_RegenerateKey
        body = (
                 '{'
                 '  "keyName": "key1"'
                 '}')
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}/regenerateKey?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # Topics_ListEventTypes
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/{providerNamespace}/{resourceTypeName}/{{RESOURCE_TYPE_NAME}_NAME}/providers/Microsoft.EventGrid/eventTypes?api-version=2019-01-01 '
                 , checks=[
                          ])

        # TopicTypes_List
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/topicTypes?api-version=2019-01-01 '
                 , checks=[
                          ])

        # TopicTypes_Get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # TopicTypes_ListEventTypes
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}/eventTypes?api-version=2019-01-01 '
                 , checks=[
                          ])