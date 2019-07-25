#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_softwareupdateconfiguration
version_added: '2.9'
short_description: Manage Azure SoftwareUpdateConfiguration instance.
description:
  - 'Create, update and delete instance of Azure SoftwareUpdateConfiguration.'
options:
  resource_group:
    description:
      - Name of an Azure Resource group.
    required: true
    type: str
  automation_account_name:
    description:
      - The name of the automation account.
    required: true
    type: str
  name:
    description:
      - Resource name.
    type: str
  client_request_id:
    description:
      - Identifies this specific client request.
    type: str
  update_configuration:
    description:
      - update specific properties for the Software update configuration
    required: true
    type: dict
    suboptions:
      operating_system:
        description:
          - operating system of target machines
        required: true
        type: str
      windows:
        description:
          - Windows specific update configuration.
        type: dict
        suboptions:
          included_update_classifications:
            description:
              - >-
                Update classification included in the software update
                configuration. A comma separated string with required values
            type: str
          excluded_kb_numbers:
            description:
              - KB numbers excluded from the software update configuration.
            type: list
          included_kb_numbers:
            description:
              - KB numbers included from the software update configuration.
            type: list
          reboot_setting:
            description:
              - Reboot setting for the software update configuration.
            type: str
      linux:
        description:
          - Linux specific update configuration.
        type: dict
        suboptions:
          included_package_classifications:
            description:
              - >-
                Update classifications included in the software update
                configuration.
            type: str
          excluded_package_name_masks:
            description:
              - packages excluded from the software update configuration.
            type: list
          included_package_name_masks:
            description:
              - packages included from the software update configuration.
            type: list
          reboot_setting:
            description:
              - Reboot setting for the software update configuration.
            type: str
      duration:
        description:
          - >-
            Maximum time allowed for the software update configuration run.
            Duration needs to be specified using the format PT[n]H[n]M[n]S as
            per ISO8601
        type: 'unknown-primary[timeSpan]'
      azure_virtual_machines:
        description:
          - >-
            List of azure resource Ids for azure virtual machines targeted by
            the software update configuration.
        type: list
      non_azure_computer_names:
        description:
          - >-
            List of names of non-azure machines targeted by the software update
            configuration.
        type: list
      targets:
        description:
          - Group targets for the software update configuration.
        type: dict
        suboptions:
          azure_queries:
            description:
              - List of Azure queries in the software update configuration.
            type: list
            suboptions:
              scope:
                description:
                  - List of Subscription or Resource Group ARM Ids.
                type: list
              locations:
                description:
                  - List of locations to scope the query to.
                type: list
              tag_settings:
                description:
                  - Tag settings for the VM.
                type: dict
          non_azure_queries:
            description:
              - List of non Azure queries in the software update configuration.
            type: list
            suboptions:
              function_alias:
                description:
                  - Log Analytics Saved Search name.
                type: str
              workspace_id:
                description:
                  - >-
                    Workspace Id for Log Analytics in which the saved Search is
                    resided.
                type: str
  schedule_info:
    description:
      - Schedule information for the Software update configuration
    required: true
    type: dict
    suboptions:
      start_time:
        description:
          - Gets or sets the start time of the schedule.
        type: datetime
      expiry_time:
        description:
          - Gets or sets the end time of the schedule.
        type: datetime
      expiry_time_offset_minutes:
        description:
          - Gets or sets the expiry time's offset in minutes.
        type: number
      is_enabled:
        description:
          - Gets or sets a value indicating whether this schedule is enabled.
        type: boolean
      next_run:
        description:
          - Gets or sets the next run time of the schedule.
        type: datetime
      next_run_offset_minutes:
        description:
          - Gets or sets the next run time's offset in minutes.
        type: number
      interval:
        description:
          - Gets or sets the interval of the schedule.
        type: number
      frequency:
        description:
          - Gets or sets the frequency of the schedule.
        type: str
      time_zone:
        description:
          - Gets or sets the time zone of the schedule.
        type: str
      advanced_schedule:
        description:
          - Gets or sets the advanced schedule.
        type: dict
        suboptions:
          week_days:
            description:
              - Days of the week that the job should execute on.
            type: list
          month_days:
            description:
              - >-
                Days of the month that the job should execute on. Must be
                between 1 and 31.
            type: list
          monthly_occurrences:
            description:
              - Occurrences of days within a month.
            type: list
            suboptions:
              occurrence:
                description:
                  - >-
                    Occurrence of the week within the month. Must be between 1
                    and 5
                type: number
              day:
                description:
                  - >-
                    Day of the occurrence. Must be one of monday, tuesday,
                    wednesday, thursday, friday, saturday, sunday.
                type: str
      creation_time:
        description:
          - Gets or sets the creation time.
        type: datetime
      last_modified_time:
        description:
          - Gets or sets the last modified time.
        type: datetime
      description:
        description:
          - Gets or sets the description.
        type: str
      start_time_offset_minutes:
        description:
          - Gets the start time's offset in minutes.
        type: number
  error:
    description:
      - Details of provisioning error
    type: dict
    suboptions:
      code:
        description:
          - Error code
        type: str
      message:
        description:
          - Error message indicating why the operation failed.
        type: str
  tasks:
    description:
      - Tasks information for the Software update configuration.
    type: dict
    suboptions:
      pre_task:
        description:
          - Pre task properties.
        type: dict
        suboptions:
          parameters:
            description:
              - Gets or sets the parameters of the task.
            type: >-
              unknown[DictionaryType
              {"$id":"355","$type":"DictionaryType","valueType":{"$id":"356","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"357","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"358","fixed":false},"deprecated":false}]
          source:
            description:
              - Gets or sets the name of the runbook.
            type: str
      post_task:
        description:
          - Post task properties.
        type: dict
        suboptions:
          parameters:
            description:
              - Gets or sets the parameters of the task.
            type: >-
              unknown[DictionaryType
              {"$id":"355","$type":"DictionaryType","valueType":{"$id":"356","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"357","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"358","fixed":false},"deprecated":false}]
          source:
            description:
              - Gets or sets the name of the runbook.
            type: str
  provisioning_state:
    description:
      - >-
        Provisioning state for the software update configuration, which only
        appears in the response.
    type: str
  creation_time:
    description:
      - 'Creation time of the resource, which only appears in the response.'
    type: datetime
  created_by:
    description:
      - 'CreatedBy property, which only appears in the response.'
    type: str
  last_modified_time:
    description:
      - 'Last time resource was modified, which only appears in the response.'
    type: datetime
  last_modified_by:
    description:
      - 'LastModifiedBy property, which only appears in the response.'
    type: str
  id:
    description:
      - Resource Id.
    type: str
  type:
    description:
      - Resource type
    type: str
  state:
    description:
      - Assert the state of the SoftwareUpdateConfiguration.
      - >-
        Use C(present) to create or update an SoftwareUpdateConfiguration and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Create software update configuration
  azure_rm_softwareupdateconfiguration:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: mySoftwareUpdateConfiguration
    update_configuration:
      operating_system: Windows
      windows:
        included_update_classifications: Critical
        excluded_kb_numbers:
          - '168934'
          - '168973'
        reboot_setting: IfRequired
      duration: PT2H0M
      azure_virtual_machines:
        - >-
          /subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-01
        - >-
          /subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-02
        - >-
          /subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources/providers/Microsoft.Compute/virtualMachines/vm-03
      non_azure_computer_names:
        - box1.contoso.com
        - box2.contoso.com
      targets:
        azure_queries:
          - scope:
              - >-
                /subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067/resourceGroups/myresources
              - /subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067
            locations:
              - Japan East
              - UK South
            tag_settings:
              tags:
                - tag1:
                    - tag1Value1
                    - tag1Value2
                    - tag1Value3
                - tag2:
                    - tag2Value1
                    - tag2Value2
                    - tag2Value3
              filterOperator: All
        non_azure_queries:
          - function_alias: SavedSearch1
            workspace_id: WorkspaceId1
          - function_alias: SavedSearch2
            workspace_id: WorkspaceId2
    schedule_info:
      start_time: '2017-10-19T12:22:57+00:00'
      expiry_time: '2018-11-09T11:22:57+00:00'
      interval: '1'
      frequency: Hour
      time_zone: America/Los_Angeles
      advanced_schedule:
        week_days:
          - Monday
          - Thursday
    tasks:
      pre_task:
        source: HelloWorld
      post_task:
        source: GetCache
- name: Delete software update configuration
  azure_rm_softwareupdateconfiguration:
    resource_group: myResourceGroup
    automation_account_name: myAutomationAccount
    name: mySoftwareUpdateConfiguration
    state: absent

'''

RETURN = '''
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
id:
  description:
    - Resource Id.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
properties:
  description:
    - Software update configuration properties.
  returned: always
  type: dict
  sample: null
  contains:
    update_configuration:
      description:
        - update specific properties for the Software update configuration
      returned: always
      type: dict
      sample: null
      contains:
        operating_system:
          description:
            - operating system of target machines
          returned: always
          type: str
          sample: null
        windows:
          description:
            - Windows specific update configuration.
          returned: always
          type: dict
          sample: null
          contains:
            included_update_classifications:
              description:
                - >-
                  Update classification included in the software update
                  configuration. A comma separated string with required values
              returned: always
              type: str
              sample: null
            excluded_kb_numbers:
              description:
                - KB numbers excluded from the software update configuration.
              returned: always
              type: str
              sample: null
            included_kb_numbers:
              description:
                - KB numbers included from the software update configuration.
              returned: always
              type: str
              sample: null
            reboot_setting:
              description:
                - Reboot setting for the software update configuration.
              returned: always
              type: str
              sample: null
        linux:
          description:
            - Linux specific update configuration.
          returned: always
          type: dict
          sample: null
          contains:
            included_package_classifications:
              description:
                - >-
                  Update classifications included in the software update
                  configuration.
              returned: always
              type: str
              sample: null
            excluded_package_name_masks:
              description:
                - packages excluded from the software update configuration.
              returned: always
              type: str
              sample: null
            included_package_name_masks:
              description:
                - packages included from the software update configuration.
              returned: always
              type: str
              sample: null
            reboot_setting:
              description:
                - Reboot setting for the software update configuration.
              returned: always
              type: str
              sample: null
        duration:
          description:
            - >-
              Maximum time allowed for the software update configuration run.
              Duration needs to be specified using the format PT[n]H[n]M[n]S as
              per ISO8601
          returned: always
          type: 'unknown-primary[timeSpan]'
          sample: null
        azure_virtual_machines:
          description:
            - >-
              List of azure resource Ids for azure virtual machines targeted by
              the software update configuration.
          returned: always
          type: str
          sample: null
        non_azure_computer_names:
          description:
            - >-
              List of names of non-azure machines targeted by the software
              update configuration.
          returned: always
          type: str
          sample: null
        targets:
          description:
            - Group targets for the software update configuration.
          returned: always
          type: dict
          sample: null
          contains:
            azure_queries:
              description:
                - List of Azure queries in the software update configuration.
              returned: always
              type: dict
              sample: null
              contains:
                scope:
                  description:
                    - List of Subscription or Resource Group ARM Ids.
                  returned: always
                  type: str
                  sample: null
                locations:
                  description:
                    - List of locations to scope the query to.
                  returned: always
                  type: str
                  sample: null
                tag_settings:
                  description:
                    - Tag settings for the VM.
                  returned: always
                  type: dict
                  sample: null
            non_azure_queries:
              description:
                - >-
                  List of non Azure queries in the software update
                  configuration.
              returned: always
              type: dict
              sample: null
              contains:
                function_alias:
                  description:
                    - Log Analytics Saved Search name.
                  returned: always
                  type: str
                  sample: null
                workspace_id:
                  description:
                    - >-
                      Workspace Id for Log Analytics in which the saved Search
                      is resided.
                  returned: always
                  type: str
                  sample: null
    schedule_info:
      description:
        - Schedule information for the Software update configuration
      returned: always
      type: dict
      sample: null
      contains:
        start_time:
          description:
            - Gets or sets the start time of the schedule.
          returned: always
          type: datetime
          sample: null
        start_time_offset_minutes:
          description:
            - Gets the start time's offset in minutes.
          returned: always
          type: number
          sample: null
        expiry_time:
          description:
            - Gets or sets the end time of the schedule.
          returned: always
          type: datetime
          sample: null
        expiry_time_offset_minutes:
          description:
            - Gets or sets the expiry time's offset in minutes.
          returned: always
          type: number
          sample: null
        is_enabled:
          description:
            - Gets or sets a value indicating whether this schedule is enabled.
          returned: always
          type: boolean
          sample: null
        next_run:
          description:
            - Gets or sets the next run time of the schedule.
          returned: always
          type: datetime
          sample: null
        next_run_offset_minutes:
          description:
            - Gets or sets the next run time's offset in minutes.
          returned: always
          type: number
          sample: null
        interval:
          description:
            - Gets or sets the interval of the schedule.
          returned: always
          type: number
          sample: null
        frequency:
          description:
            - Gets or sets the frequency of the schedule.
          returned: always
          type: str
          sample: null
        time_zone:
          description:
            - Gets or sets the time zone of the schedule.
          returned: always
          type: str
          sample: null
        advanced_schedule:
          description:
            - Gets or sets the advanced schedule.
          returned: always
          type: dict
          sample: null
          contains:
            week_days:
              description:
                - Days of the week that the job should execute on.
              returned: always
              type: str
              sample: null
            month_days:
              description:
                - >-
                  Days of the month that the job should execute on. Must be
                  between 1 and 31.
              returned: always
              type: number
              sample: null
            monthly_occurrences:
              description:
                - Occurrences of days within a month.
              returned: always
              type: dict
              sample: null
              contains:
                occurrence:
                  description:
                    - >-
                      Occurrence of the week within the month. Must be between 1
                      and 5
                  returned: always
                  type: number
                  sample: null
                day:
                  description:
                    - >-
                      Day of the occurrence. Must be one of monday, tuesday,
                      wednesday, thursday, friday, saturday, sunday.
                  returned: always
                  type: str
                  sample: null
        creation_time:
          description:
            - Gets or sets the creation time.
          returned: always
          type: datetime
          sample: null
        last_modified_time:
          description:
            - Gets or sets the last modified time.
          returned: always
          type: datetime
          sample: null
        description:
          description:
            - Gets or sets the description.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - >-
          Provisioning state for the software update configuration, which only
          appears in the response.
      returned: always
      type: str
      sample: null
    error:
      description:
        - Details of provisioning error
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - Error code
          returned: always
          type: str
          sample: null
        message:
          description:
            - Error message indicating why the operation failed.
          returned: always
          type: str
          sample: null
    creation_time:
      description:
        - 'Creation time of the resource, which only appears in the response.'
      returned: always
      type: datetime
      sample: null
    created_by:
      description:
        - 'CreatedBy property, which only appears in the response.'
      returned: always
      type: str
      sample: null
    last_modified_time:
      description:
        - 'Last time resource was modified, which only appears in the response.'
      returned: always
      type: datetime
      sample: null
    last_modified_by:
      description:
        - 'LastModifiedBy property, which only appears in the response.'
      returned: always
      type: str
      sample: null
    tasks:
      description:
        - Tasks information for the Software update configuration.
      returned: always
      type: dict
      sample: null
      contains:
        pre_task:
          description:
            - Pre task properties.
          returned: always
          type: dict
          sample: null
          contains:
            parameters:
              description:
                - Gets or sets the parameters of the task.
              returned: always
              type: >-
                unknown[DictionaryType
                {"$id":"355","$type":"DictionaryType","valueType":{"$id":"356","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"357","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"358","fixed":false},"deprecated":false}]
              sample: null
            source:
              description:
                - Gets or sets the name of the runbook.
              returned: always
              type: str
              sample: null
        post_task:
          description:
            - Post task properties.
          returned: always
          type: dict
          sample: null
          contains:
            parameters:
              description:
                - Gets or sets the parameters of the task.
              returned: always
              type: >-
                unknown[DictionaryType
                {"$id":"355","$type":"DictionaryType","valueType":{"$id":"356","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"357","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"358","fixed":false},"deprecated":false}]
              sample: null
            source:
              description:
                - Gets or sets the name of the runbook.
              returned: always
              type: str
              sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSoftwareUpdateConfigurations(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            automation_account_name=dict(
                type='str',
                updatable=False,
                disposition='automationAccountName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='softwareUpdateConfigurationName',
                required=true
            ),
            client_request_id=dict(
                type='str',
                updatable=False,
                disposition='clientRequestId'
            ),
            update_configuration=dict(
                type='dict',
                disposition='/properties/updateConfiguration',
                required=true,
                options=dict(
                    operating_system=dict(
                        type='str',
                        disposition='operatingSystem',
                        choices=['Windows',
                                 'Linux'],
                        required=true
                    ),
                    windows=dict(
                        type='dict',
                        options=dict(
                            included_update_classifications=dict(
                                type='str',
                                disposition='includedUpdateClassifications',
                                choices=['Unclassified',
                                         'Critical',
                                         'Security',
                                         'UpdateRollup',
                                         'FeaturePack',
                                         'ServicePack',
                                         'Definition',
                                         'Tools',
                                         'Updates']
                            ),
                            excluded_kb_numbers=dict(
                                type='list',
                                disposition='excludedKbNumbers'
                            ),
                            included_kb_numbers=dict(
                                type='list',
                                disposition='includedKbNumbers'
                            ),
                            reboot_setting=dict(
                                type='str',
                                disposition='rebootSetting'
                            )
                        )
                    ),
                    linux=dict(
                        type='dict',
                        options=dict(
                            included_package_classifications=dict(
                                type='str',
                                disposition='includedPackageClassifications',
                                choices=['Unclassified',
                                         'Critical',
                                         'Security',
                                         'Other']
                            ),
                            excluded_package_name_masks=dict(
                                type='list',
                                disposition='excludedPackageNameMasks'
                            ),
                            included_package_name_masks=dict(
                                type='list',
                                disposition='includedPackageNameMasks'
                            ),
                            reboot_setting=dict(
                                type='str',
                                disposition='rebootSetting'
                            )
                        )
                    ),
                    duration=dict(
                        type='unknown-primary[timeSpan]'
                    ),
                    azure_virtual_machines=dict(
                        type='raw',
                        disposition='azureVirtualMachines',
                        pattern=('//subscriptions/5ae68d89-69a4-454f-b5ce-e443cc4e0067'
                                 '/resourceGroups/myresources/providers/Microsoft.Compute'
                                 '/virtualMachines/vm-03')
                    ),
                    non_azure_computer_names=dict(
                        type='list',
                        disposition='nonAzureComputerNames'
                    ),
                    targets=dict(
                        type='dict',
                        options=dict(
                            azure_queries=dict(
                                type='list',
                                disposition='azureQueries',
                                options=dict(
                                    scope=dict(
                                        type='raw',
                                        pattern=('//subscriptions'
                                                 '/5ae68d89-69a4-454f-b5ce-e443cc4e0067')
                                    ),
                                    locations=dict(
                                        type='list'
                                    ),
                                    tag_settings=dict(
                                        type='dict',
                                        disposition='tagSettings'
                                    )
                                )
                            ),
                            non_azure_queries=dict(
                                type='list',
                                disposition='nonAzureQueries',
                                options=dict(
                                    function_alias=dict(
                                        type='str',
                                        disposition='functionAlias'
                                    ),
                                    workspace_id=dict(
                                        type='str',
                                        disposition='workspaceId'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            schedule_info=dict(
                type='dict',
                disposition='/properties/scheduleInfo',
                required=true,
                options=dict(
                    start_time=dict(
                        type='datetime',
                        disposition='startTime'
                    ),
                    expiry_time=dict(
                        type='datetime',
                        disposition='expiryTime'
                    ),
                    expiry_time_offset_minutes=dict(
                        type='number',
                        disposition='expiryTimeOffsetMinutes'
                    ),
                    is_enabled=dict(
                        type='boolean',
                        disposition='isEnabled'
                    ),
                    next_run=dict(
                        type='datetime',
                        disposition='nextRun'
                    ),
                    next_run_offset_minutes=dict(
                        type='number',
                        disposition='nextRunOffsetMinutes'
                    ),
                    interval=dict(
                        type='number'
                    ),
                    frequency=dict(
                        type='str',
                        choices=['OneTime',
                                 'Day',
                                 'Hour',
                                 'Week',
                                 'Month',
                                 'Minute']
                    ),
                    time_zone=dict(
                        type='str',
                        disposition='timeZone'
                    ),
                    advanced_schedule=dict(
                        type='dict',
                        disposition='advancedSchedule',
                        options=dict(
                            week_days=dict(
                                type='list',
                                disposition='weekDays'
                            ),
                            month_days=dict(
                                type='list',
                                disposition='monthDays'
                            ),
                            monthly_occurrences=dict(
                                type='list',
                                disposition='monthlyOccurrences',
                                options=dict(
                                    occurrence=dict(
                                        type='number'
                                    ),
                                    day=dict(
                                        type='str',
                                        choices=['Monday',
                                                 'Tuesday',
                                                 'Wednesday',
                                                 'Thursday',
                                                 'Friday',
                                                 'Saturday',
                                                 'Sunday']
                                    )
                                )
                            )
                        )
                    ),
                    creation_time=dict(
                        type='datetime',
                        disposition='creationTime'
                    ),
                    last_modified_time=dict(
                        type='datetime',
                        disposition='lastModifiedTime'
                    ),
                    description=dict(
                        type='str'
                    )
                )
            ),
            error=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    code=dict(
                        type='str'
                    ),
                    message=dict(
                        type='str'
                    )
                )
            ),
            tasks=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    pre_task=dict(
                        type='dict',
                        disposition='preTask',
                        options=dict(
                            parameters=dict(
                                type='unknown[DictionaryType {"$id":"355","$type":"DictionaryType","valueType":{"$id":"356","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"357","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"358","fixed":false},"deprecated":false}]'
                            ),
                            source=dict(
                                type='str'
                            )
                        )
                    ),
                    post_task=dict(
                        type='dict',
                        disposition='postTask',
                        options=dict(
                            parameters=dict(
                                type='unknown[DictionaryType {"$id":"355","$type":"DictionaryType","valueType":{"$id":"356","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"357","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"358","fixed":false},"deprecated":false}]'
                            ),
                            source=dict(
                                type='str'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.automation_account_name = None
        self.name = None
        self.client_request_id = None
        self.name = None
        self.id = None
        self.type = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-05-15-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMSoftwareUpdateConfigurations, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                  supports_check_mode=True,
                                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Automation' +
                    '/automationAccounts' +
                    '/{{ automation_account_name }}' +
                    '/softwareUpdateConfigurations' +
                    '/{{ software_update_configuration_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ automation_account_name }}', self.automation_account_name)
        self.url = self.url.replace('{{ software_update_configuration_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("SoftwareUpdateConfiguration instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('SoftwareUpdateConfiguration instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the SoftwareUpdateConfiguration instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('SoftwareUpdateConfiguration instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('SoftwareUpdateConfiguration instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["name"] = response["name"]
           self.results["id"] = response["id"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the SoftwareUpdateConfiguration instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the SoftwareUpdateConfiguration instance.')
            self.fail('Error creating the SoftwareUpdateConfiguration instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the SoftwareUpdateConfiguration instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the SoftwareUpdateConfiguration instance.')
            self.fail('Error deleting the SoftwareUpdateConfiguration instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the SoftwareUpdateConfiguration instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("SoftwareUpdateConfiguration instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the SoftwareUpdateConfiguration instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMSoftwareUpdateConfigurations()


if __name__ == '__main__':
    main()
