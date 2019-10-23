# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['healthcareapis'] = """
    type: group
    short-summary: Commands to manage service.
"""

helps['healthcareapis create'] = """
    type: command
    short-summary: create service.
    examples:
      - name: Create or Update a service with all parameters
        text: |-
               az healthcareapis create --resource-group "rg1" --name "service1" --kind "fhir-R4" \\
               --location "westus2" --cosmos-db-offer-throughput "1000" --authentication-authority \\
               "https://login.microsoftonline.com/abfde7b2-df0f-47e6-aabf-2462b07508dc" \\
               --authentication-audience "https://azurehealthcareapis.com" \\
               --authentication-smart-proxy-enabled true --cors-origins "*" --cors-headers "*" \\
               --cors-methods "DELETE,GET,OPTIONS,PATCH,POST,PUT" --cors-max-age "1440" \\
               --cors-allow-credentials false
      - name: Create or Update a service with minimum parameters
        text: |-
               az healthcareapis create --resource-group "rg1" --name "service2" --kind "fhir-R4" \\
               --location "westus2"
"""

helps['healthcareapis update'] = """
    type: command
    short-summary: update service.
    examples:
      - name: Patch service
        text: |-
               az healthcareapis update --resource-group "rg1" --name "service1"
"""

helps['healthcareapis delete'] = """
    type: command
    short-summary: delete service.
    examples:
      - name: Delete service
        text: |-
               az healthcareapis delete --resource-group "rg1" --name "service1"
"""

helps['healthcareapis list'] = """
    type: command
    short-summary: list service.
"""

helps['healthcareapis show'] = """
    type: command
    short-summary: show service.
"""

helps['healthcareapis'] = """
    type: group
    short-summary: Commands to manage operation.
"""

helps['healthcareapis list'] = """
    type: command
    short-summary: list operation.
"""

helps['healthcareapis operationresult'] = """
    type: group
    short-summary: Commands to manage operation result.
"""

helps['healthcareapis operationresult show'] = """
    type: command
    short-summary: show operation result.
"""
