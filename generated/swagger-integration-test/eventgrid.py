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

        # eventgrid_get
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_get_3
        self.cmd('rest '
                 '--method get '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_put
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_put_1
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_put_2
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_put_3
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_put_4
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_put_5
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_put_6
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
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_delete_1
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_delete_2
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_delete_3
        self.cmd('rest '
                 '--method delete '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_patch_1
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_patch_2
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_patch_3
        self.cmd('rest '
                 '--method patch '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}/{{EVENT_SUBSCRIPTION_NAME}_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_post_1
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}/{{EVENT_SUBSCRIPTION_NAME}_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_post_2
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}/{{EVENT_SUBSCRIPTION_NAME}_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_post_3
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /{scope}/{{SCOPE}_NAME}/Microsoft.EventGrid/{MICROSOFT.EVENT_GRID_NAME}/{eventSubscriptionName}/{{EVENT_SUBSCRIPTION_NAME}_NAME}?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_eventsubscriptions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topictypes_eventsubscriptions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_eventsubscriptions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topictypes_eventsubscriptions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_locations_eventsubscriptions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_locations_eventsubscriptions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_locations_topictypes_eventsubscriptions_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_locations_topictypes_eventsubscriptions_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/locations/{LOCATION_NAME}/topicTypes/{TOPIC_TYPE_NAME}/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_eventsubscriptions_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/{providerNamespace}/{resourceTypeName}/{{RESOURCE_TYPE_NAME}_NAME}/providers/Microsoft.EventGrid/eventSubscriptions?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_operations_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/operations?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topics_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topics_put
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

        # eventgrid_topics_delete
        self.cmd('rest '
                 '--method delete '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topics_patch
        self.cmd('rest '
                 '--method patch '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topics_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/providers/Microsoft.EventGrid/topics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topics_get_2
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topics_listkeys_post
        body = (
                 '{}'
        self.kwargs['body'] = body.replace('"', '\\"')
        self.cmd('rest '
                 '--method post '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.EventGrid/topics/{TOPIC_NAME}/listKeys?api-version=2019-01-01 '
                 '--body "{body}"'
                 , checks=[
                          ])

        # eventgrid_topics_regeneratekey_post
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

        # eventgrid_eventtypes_get
        self.cmd('rest '
                 '--method get '
                 '--uri /subscriptions/{sub}/resourceGroups/{rg}/providers/{providerNamespace}/{resourceTypeName}/{{RESOURCE_TYPE_NAME}_NAME}/providers/Microsoft.EventGrid/eventTypes?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topictypes_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/topicTypes?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topictypes_get_1
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}?api-version=2019-01-01 '
                 , checks=[
                          ])

        # eventgrid_topictypes_eventtypes_get
        self.cmd('rest '
                 '--method get '
                 '--uri /providers/Microsoft.EventGrid/topicTypes/{TOPIC_TYPE_NAME}/eventTypes?api-version=2019-01-01 '
                 , checks=[
                          ])