# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['aro'] = """
    type: group
    short-summary: Commands to manage open shift managed cluster.
"""

helps['aro create'] = """
    type: command
    short-summary: create open shift managed cluster.
    examples:
      - name: Create/Update OpenShift Managed Cluster
        text: |-
               az aro create --resource-group "rg1" --name "clustername1" --location "location1" \\
               --open-shift-version "v3.11"
"""

helps['aro update'] = """
    type: command
    short-summary: update open shift managed cluster.
"""

helps['aro delete'] = """
    type: command
    short-summary: delete open shift managed cluster.
    examples:
      - name: Delete OpenShift Managed Cluster
        text: |-
               az aro delete --resource-group "rg1" --name "clustername1"
"""

helps['aro list'] = """
    type: command
    short-summary: list open shift managed cluster.
"""

helps['aro show'] = """
    type: command
    short-summary: show open shift managed cluster.
"""
