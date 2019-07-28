# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['alerts'] = """
    type: group
    short-summary: Commands to manage smart detector alert rule.
"""

helps['alerts create'] = """
    type: command
    short-summary: create smart detector alert rule.
    examples:
      - name: Create or update a Smart Detector alert rule
        text: |-
               az alerts create --resource-group "MyAlertRules" --name "MyAlertRule" --description \\
               "Sample smart detector alert rule description" --state "Enabled" --severity "Sev3" \\
               --frequency "PT5M"
"""

helps['alerts update'] = """
    type: command
    short-summary: update smart detector alert rule.
"""

helps['alerts delete'] = """
    type: command
    short-summary: delete smart detector alert rule.
    examples:
      - name: Delete a Smart Detector alert rule
        text: |-
               az alerts delete --resource-group "MyAlertRules" --name "MyAlertRule"
"""

helps['alerts list'] = """
    type: command
    short-summary: list smart detector alert rule.
"""

helps['alerts show'] = """
    type: command
    short-summary: show smart detector alert rule.
"""
