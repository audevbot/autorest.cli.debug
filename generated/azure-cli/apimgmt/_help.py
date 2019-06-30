# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import



helps['apimgmt api'] = """
    type: group
    short-summary: Commands to manage Api.
"""

helps['apimgmt api create'] = """
    type: command
    short-summary: create a apimgmt api.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiUsingOai3Import
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApiUsingWadlImport
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApi
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApiClone
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementUpdateApi
        text: apimgmt api create  --xxx yyy
      - name: ApiManagementDeleteApi
        text: apimgmt api create  --xxx yyy
"""

helps['apimgmt api update'] = """
    type: command
    short-summary: update a apimgmt api.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiUsingOai3Import
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApiUsingWadlImport
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApi
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApiClone
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementUpdateApi
        text: apimgmt api update  --xxx yyy
      - name: ApiManagementDeleteApi
        text: apimgmt api update  --xxx yyy
"""

helps['apimgmt api delete'] = """
    type: command
    short-summary: delete a apimgmt api.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiUsingOai3Import
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApiUsingWadlImport
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApi
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApiClone
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementUpdateApi
        text: apimgmt api delete  --xxx yyy
      - name: ApiManagementDeleteApi
        text: apimgmt api delete  --xxx yyy
"""

helps['apimgmt api list'] = """
    type: command
    short-summary: list a apimgmt api.
    examples:
# list_by_tags -- list
      - name: ApiManagementCreateApiUsingOai3Import
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiUsingWadlImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiClone
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementUpdateApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementDeleteApi
        text: apimgmt api list  --xxx yyy
# list_by_service -- list
      - name: ApiManagementCreateApiUsingOai3Import
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiUsingWadlImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiClone
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementUpdateApi
        text: apimgmt api list  --xxx yyy
      - name: ApiManagementDeleteApi
        text: apimgmt api list  --xxx yyy
"""

helps['apimgmt api show'] = """
    type: command
    short-summary: show a apimgmt api.
    examples:
# get -- show
      - name: ApiManagementCreateApiUsingOai3Import
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApiUsingSwaggerImport
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApiUsingWadlImport
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateSoapToRestApiUsingWsdlImport
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateSoapPassThroughApiUsingWsdlImport
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApi
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApiRevisionFromExistingApi
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApiNewVersionUsingExistingApi
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApiClone
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementCreateApiWithOpenIdConnect
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementUpdateApi
        text: apimgmt api show  --xxx yyy
      - name: ApiManagementDeleteApi
        text: apimgmt api show  --xxx yyy
"""

helps['apimgmt api release'] = """
    type: group
    short-summary: Commands to manage ApiRelease.
"""

helps['apimgmt api release create'] = """
    type: command
    short-summary: create a apimgmt api release.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiRelease
        text: apimgmt api release create  --xxx yyy
      - name: ApiManagementUpdateApiRelease
        text: apimgmt api release create  --xxx yyy
      - name: ApiManagementDeleteApiRelease
        text: apimgmt api release create  --xxx yyy
"""

helps['apimgmt api release update'] = """
    type: command
    short-summary: update a apimgmt api release.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiRelease
        text: apimgmt api release update  --xxx yyy
      - name: ApiManagementUpdateApiRelease
        text: apimgmt api release update  --xxx yyy
      - name: ApiManagementDeleteApiRelease
        text: apimgmt api release update  --xxx yyy
"""

helps['apimgmt api release delete'] = """
    type: command
    short-summary: delete a apimgmt api release.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiRelease
        text: apimgmt api release delete  --xxx yyy
      - name: ApiManagementUpdateApiRelease
        text: apimgmt api release delete  --xxx yyy
      - name: ApiManagementDeleteApiRelease
        text: apimgmt api release delete  --xxx yyy
"""

helps['apimgmt api release list'] = """
    type: command
    short-summary: list a apimgmt api release.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiRelease
        text: apimgmt api release list  --xxx yyy
      - name: ApiManagementUpdateApiRelease
        text: apimgmt api release list  --xxx yyy
      - name: ApiManagementDeleteApiRelease
        text: apimgmt api release list  --xxx yyy
"""

helps['apimgmt api release show'] = """
    type: command
    short-summary: show a apimgmt api release.
    examples:
# get -- show
      - name: ApiManagementCreateApiRelease
        text: apimgmt api release show  --xxx yyy
      - name: ApiManagementUpdateApiRelease
        text: apimgmt api release show  --xxx yyy
      - name: ApiManagementDeleteApiRelease
        text: apimgmt api release show  --xxx yyy
"""

helps['apimgmt api operation'] = """
    type: group
    short-summary: Commands to manage ApiOperation.
"""

helps['apimgmt api operation create'] = """
    type: command
    short-summary: create a apimgmt api operation.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiOperation
        text: apimgmt api operation create  --xxx yyy
      - name: ApiManagementUpdateApiOperation
        text: apimgmt api operation create  --xxx yyy
      - name: ApiManagementDeleteApiOperation
        text: apimgmt api operation create  --xxx yyy
"""

helps['apimgmt api operation update'] = """
    type: command
    short-summary: update a apimgmt api operation.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiOperation
        text: apimgmt api operation update  --xxx yyy
      - name: ApiManagementUpdateApiOperation
        text: apimgmt api operation update  --xxx yyy
      - name: ApiManagementDeleteApiOperation
        text: apimgmt api operation update  --xxx yyy
"""

helps['apimgmt api operation delete'] = """
    type: command
    short-summary: delete a apimgmt api operation.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiOperation
        text: apimgmt api operation delete  --xxx yyy
      - name: ApiManagementUpdateApiOperation
        text: apimgmt api operation delete  --xxx yyy
      - name: ApiManagementDeleteApiOperation
        text: apimgmt api operation delete  --xxx yyy
"""

helps['apimgmt api operation list'] = """
    type: command
    short-summary: list a apimgmt api operation.
    examples:
# list_by_api -- list
      - name: ApiManagementCreateApiOperation
        text: apimgmt api operation list  --xxx yyy
      - name: ApiManagementUpdateApiOperation
        text: apimgmt api operation list  --xxx yyy
      - name: ApiManagementDeleteApiOperation
        text: apimgmt api operation list  --xxx yyy
"""

helps['apimgmt api operation show'] = """
    type: command
    short-summary: show a apimgmt api operation.
    examples:
# get -- show
      - name: ApiManagementCreateApiOperation
        text: apimgmt api operation show  --xxx yyy
      - name: ApiManagementUpdateApiOperation
        text: apimgmt api operation show  --xxx yyy
      - name: ApiManagementDeleteApiOperation
        text: apimgmt api operation show  --xxx yyy
"""

helps['apimgmt api operation policy'] = """
    type: group
    short-summary: Commands to manage ApiOperationPolicy.
"""

helps['apimgmt api operation policy create'] = """
    type: command
    short-summary: create a apimgmt api operation policy.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiOperationPolicy
        text: apimgmt api operation policy create  --xxx yyy
      - name: ApiManagementDeleteApiOperationPolicy
        text: apimgmt api operation policy create  --xxx yyy
"""

helps['apimgmt api operation policy update'] = """
    type: command
    short-summary: update a apimgmt api operation policy.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiOperationPolicy
        text: apimgmt api operation policy update  --xxx yyy
      - name: ApiManagementDeleteApiOperationPolicy
        text: apimgmt api operation policy update  --xxx yyy
"""

helps['apimgmt api operation policy delete'] = """
    type: command
    short-summary: delete a apimgmt api operation policy.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiOperationPolicy
        text: apimgmt api operation policy delete  --xxx yyy
      - name: ApiManagementDeleteApiOperationPolicy
        text: apimgmt api operation policy delete  --xxx yyy
"""

helps['apimgmt api operation policy list'] = """
    type: command
    short-summary: list a apimgmt api operation policy.
    examples:
# list_by_operation -- list
      - name: ApiManagementCreateApiOperationPolicy
        text: apimgmt api operation policy list  --xxx yyy
      - name: ApiManagementDeleteApiOperationPolicy
        text: apimgmt api operation policy list  --xxx yyy
"""

helps['apimgmt api operation policy show'] = """
    type: command
    short-summary: show a apimgmt api operation policy.
    examples:
# get -- show
      - name: ApiManagementCreateApiOperationPolicy
        text: apimgmt api operation policy show  --xxx yyy
      - name: ApiManagementDeleteApiOperationPolicy
        text: apimgmt api operation policy show  --xxx yyy
"""

helps['apimgmt tag'] = """
    type: group
    short-summary: Commands to manage Tag.
"""

helps['apimgmt tag create'] = """
    type: command
    short-summary: create a apimgmt tag.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateTag
        text: apimgmt tag create  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag create  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag create  --xxx yyy
"""

helps['apimgmt tag update'] = """
    type: command
    short-summary: update a apimgmt tag.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateTag
        text: apimgmt tag update  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag update  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag update  --xxx yyy
"""

helps['apimgmt tag delete'] = """
    type: command
    short-summary: delete a apimgmt tag.
    examples:
# delete -- delete
      - name: ApiManagementCreateTag
        text: apimgmt tag delete  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag delete  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag delete  --xxx yyy
"""

helps['apimgmt tag list'] = """
    type: command
    short-summary: list a apimgmt tag.
    examples:
# list_by_operation -- list
      - name: ApiManagementCreateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag list  --xxx yyy
# list_by_product -- list
      - name: ApiManagementCreateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag list  --xxx yyy
# list_by_api -- list
      - name: ApiManagementCreateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag list  --xxx yyy
# list_by_service -- list
      - name: ApiManagementCreateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag list  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag list  --xxx yyy
"""

helps['apimgmt tag show'] = """
    type: command
    short-summary: show a apimgmt tag.
    examples:
# get -- show
      - name: ApiManagementCreateTag
        text: apimgmt tag show  --xxx yyy
      - name: ApiManagementUpdateTag
        text: apimgmt tag show  --xxx yyy
      - name: ApiManagementDeleteTag
        text: apimgmt tag show  --xxx yyy
"""

helps['apimgmt api policy'] = """
    type: group
    short-summary: Commands to manage ApiPolicy.
"""

helps['apimgmt api policy create'] = """
    type: command
    short-summary: create a apimgmt api policy.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiPolicy
        text: apimgmt api policy create  --xxx yyy
      - name: ApiManagementCreateApiPolicyNonXmlEncoded
        text: apimgmt api policy create  --xxx yyy
      - name: ApiManagementDeleteApiPolicy
        text: apimgmt api policy create  --xxx yyy
"""

helps['apimgmt api policy update'] = """
    type: command
    short-summary: update a apimgmt api policy.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiPolicy
        text: apimgmt api policy update  --xxx yyy
      - name: ApiManagementCreateApiPolicyNonXmlEncoded
        text: apimgmt api policy update  --xxx yyy
      - name: ApiManagementDeleteApiPolicy
        text: apimgmt api policy update  --xxx yyy
"""

helps['apimgmt api policy delete'] = """
    type: command
    short-summary: delete a apimgmt api policy.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiPolicy
        text: apimgmt api policy delete  --xxx yyy
      - name: ApiManagementCreateApiPolicyNonXmlEncoded
        text: apimgmt api policy delete  --xxx yyy
      - name: ApiManagementDeleteApiPolicy
        text: apimgmt api policy delete  --xxx yyy
"""

helps['apimgmt api policy list'] = """
    type: command
    short-summary: list a apimgmt api policy.
    examples:
# list_by_api -- list
      - name: ApiManagementCreateApiPolicy
        text: apimgmt api policy list  --xxx yyy
      - name: ApiManagementCreateApiPolicyNonXmlEncoded
        text: apimgmt api policy list  --xxx yyy
      - name: ApiManagementDeleteApiPolicy
        text: apimgmt api policy list  --xxx yyy
"""

helps['apimgmt api policy show'] = """
    type: command
    short-summary: show a apimgmt api policy.
    examples:
# get -- show
      - name: ApiManagementCreateApiPolicy
        text: apimgmt api policy show  --xxx yyy
      - name: ApiManagementCreateApiPolicyNonXmlEncoded
        text: apimgmt api policy show  --xxx yyy
      - name: ApiManagementDeleteApiPolicy
        text: apimgmt api policy show  --xxx yyy
"""

helps['apimgmt api schema'] = """
    type: group
    short-summary: Commands to manage ApiSchema.
"""

helps['apimgmt api schema create'] = """
    type: command
    short-summary: create a apimgmt api schema.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiSchema
        text: apimgmt api schema create  --xxx yyy
      - name: ApiManagementDeleteApiSchema
        text: apimgmt api schema create  --xxx yyy
"""

helps['apimgmt api schema update'] = """
    type: command
    short-summary: update a apimgmt api schema.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiSchema
        text: apimgmt api schema update  --xxx yyy
      - name: ApiManagementDeleteApiSchema
        text: apimgmt api schema update  --xxx yyy
"""

helps['apimgmt api schema delete'] = """
    type: command
    short-summary: delete a apimgmt api schema.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiSchema
        text: apimgmt api schema delete  --xxx yyy
      - name: ApiManagementDeleteApiSchema
        text: apimgmt api schema delete  --xxx yyy
"""

helps['apimgmt api schema list'] = """
    type: command
    short-summary: list a apimgmt api schema.
    examples:
# list_by_api -- list
      - name: ApiManagementCreateApiSchema
        text: apimgmt api schema list  --xxx yyy
      - name: ApiManagementDeleteApiSchema
        text: apimgmt api schema list  --xxx yyy
"""

helps['apimgmt api schema show'] = """
    type: command
    short-summary: show a apimgmt api schema.
    examples:
# get -- show
      - name: ApiManagementCreateApiSchema
        text: apimgmt api schema show  --xxx yyy
      - name: ApiManagementDeleteApiSchema
        text: apimgmt api schema show  --xxx yyy
"""

helps['apimgmt api diagnostic'] = """
    type: group
    short-summary: Commands to manage ApiDiagnostic.
"""

helps['apimgmt api diagnostic create'] = """
    type: command
    short-summary: create a apimgmt api diagnostic.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiDiagnostic
        text: apimgmt api diagnostic create  --xxx yyy
      - name: ApiManagementUpdateApiDiagnostic
        text: apimgmt api diagnostic create  --xxx yyy
      - name: ApiManagementDeleteApiDiagnostic
        text: apimgmt api diagnostic create  --xxx yyy
"""

helps['apimgmt api diagnostic update'] = """
    type: command
    short-summary: update a apimgmt api diagnostic.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiDiagnostic
        text: apimgmt api diagnostic update  --xxx yyy
      - name: ApiManagementUpdateApiDiagnostic
        text: apimgmt api diagnostic update  --xxx yyy
      - name: ApiManagementDeleteApiDiagnostic
        text: apimgmt api diagnostic update  --xxx yyy
"""

helps['apimgmt api diagnostic delete'] = """
    type: command
    short-summary: delete a apimgmt api diagnostic.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiDiagnostic
        text: apimgmt api diagnostic delete  --xxx yyy
      - name: ApiManagementUpdateApiDiagnostic
        text: apimgmt api diagnostic delete  --xxx yyy
      - name: ApiManagementDeleteApiDiagnostic
        text: apimgmt api diagnostic delete  --xxx yyy
"""

helps['apimgmt api diagnostic list'] = """
    type: command
    short-summary: list a apimgmt api diagnostic.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiDiagnostic
        text: apimgmt api diagnostic list  --xxx yyy
      - name: ApiManagementUpdateApiDiagnostic
        text: apimgmt api diagnostic list  --xxx yyy
      - name: ApiManagementDeleteApiDiagnostic
        text: apimgmt api diagnostic list  --xxx yyy
"""

helps['apimgmt api diagnostic show'] = """
    type: command
    short-summary: show a apimgmt api diagnostic.
    examples:
# get -- show
      - name: ApiManagementCreateApiDiagnostic
        text: apimgmt api diagnostic show  --xxx yyy
      - name: ApiManagementUpdateApiDiagnostic
        text: apimgmt api diagnostic show  --xxx yyy
      - name: ApiManagementDeleteApiDiagnostic
        text: apimgmt api diagnostic show  --xxx yyy
"""

helps['apimgmt api issue'] = """
    type: group
    short-summary: Commands to manage ApiIssue.
"""

helps['apimgmt api issue create'] = """
    type: command
    short-summary: create a apimgmt api issue.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiIssue
        text: apimgmt api issue create  --xxx yyy
      - name: ApiManagementUpdateApiIssue
        text: apimgmt api issue create  --xxx yyy
      - name: ApiManagementDeleteApiIssue
        text: apimgmt api issue create  --xxx yyy
"""

helps['apimgmt api issue update'] = """
    type: command
    short-summary: update a apimgmt api issue.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiIssue
        text: apimgmt api issue update  --xxx yyy
      - name: ApiManagementUpdateApiIssue
        text: apimgmt api issue update  --xxx yyy
      - name: ApiManagementDeleteApiIssue
        text: apimgmt api issue update  --xxx yyy
"""

helps['apimgmt api issue delete'] = """
    type: command
    short-summary: delete a apimgmt api issue.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiIssue
        text: apimgmt api issue delete  --xxx yyy
      - name: ApiManagementUpdateApiIssue
        text: apimgmt api issue delete  --xxx yyy
      - name: ApiManagementDeleteApiIssue
        text: apimgmt api issue delete  --xxx yyy
"""

helps['apimgmt api issue list'] = """
    type: command
    short-summary: list a apimgmt api issue.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiIssue
        text: apimgmt api issue list  --xxx yyy
      - name: ApiManagementUpdateApiIssue
        text: apimgmt api issue list  --xxx yyy
      - name: ApiManagementDeleteApiIssue
        text: apimgmt api issue list  --xxx yyy
"""

helps['apimgmt api issue show'] = """
    type: command
    short-summary: show a apimgmt api issue.
    examples:
# get -- show
      - name: ApiManagementCreateApiIssue
        text: apimgmt api issue show  --xxx yyy
      - name: ApiManagementUpdateApiIssue
        text: apimgmt api issue show  --xxx yyy
      - name: ApiManagementDeleteApiIssue
        text: apimgmt api issue show  --xxx yyy
"""

helps['apimgmt api issue comment'] = """
    type: group
    short-summary: Commands to manage ApiIssueComment.
"""

helps['apimgmt api issue comment create'] = """
    type: command
    short-summary: create a apimgmt api issue comment.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiIssueComment
        text: apimgmt api issue comment create  --xxx yyy
      - name: ApiManagementDeleteApiIssueComment
        text: apimgmt api issue comment create  --xxx yyy
"""

helps['apimgmt api issue comment update'] = """
    type: command
    short-summary: update a apimgmt api issue comment.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiIssueComment
        text: apimgmt api issue comment update  --xxx yyy
      - name: ApiManagementDeleteApiIssueComment
        text: apimgmt api issue comment update  --xxx yyy
"""

helps['apimgmt api issue comment delete'] = """
    type: command
    short-summary: delete a apimgmt api issue comment.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiIssueComment
        text: apimgmt api issue comment delete  --xxx yyy
      - name: ApiManagementDeleteApiIssueComment
        text: apimgmt api issue comment delete  --xxx yyy
"""

helps['apimgmt api issue comment list'] = """
    type: command
    short-summary: list a apimgmt api issue comment.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiIssueComment
        text: apimgmt api issue comment list  --xxx yyy
      - name: ApiManagementDeleteApiIssueComment
        text: apimgmt api issue comment list  --xxx yyy
"""

helps['apimgmt api issue comment show'] = """
    type: command
    short-summary: show a apimgmt api issue comment.
    examples:
# get -- show
      - name: ApiManagementCreateApiIssueComment
        text: apimgmt api issue comment show  --xxx yyy
      - name: ApiManagementDeleteApiIssueComment
        text: apimgmt api issue comment show  --xxx yyy
"""

helps['apimgmt api issue attachment'] = """
    type: group
    short-summary: Commands to manage ApiIssueAttachment.
"""

helps['apimgmt api issue attachment create'] = """
    type: command
    short-summary: create a apimgmt api issue attachment.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiIssueAttachment
        text: apimgmt api issue attachment create  --xxx yyy
      - name: ApiManagementDeleteApiIssueAttachment
        text: apimgmt api issue attachment create  --xxx yyy
"""

helps['apimgmt api issue attachment update'] = """
    type: command
    short-summary: update a apimgmt api issue attachment.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiIssueAttachment
        text: apimgmt api issue attachment update  --xxx yyy
      - name: ApiManagementDeleteApiIssueAttachment
        text: apimgmt api issue attachment update  --xxx yyy
"""

helps['apimgmt api issue attachment delete'] = """
    type: command
    short-summary: delete a apimgmt api issue attachment.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiIssueAttachment
        text: apimgmt api issue attachment delete  --xxx yyy
      - name: ApiManagementDeleteApiIssueAttachment
        text: apimgmt api issue attachment delete  --xxx yyy
"""

helps['apimgmt api issue attachment list'] = """
    type: command
    short-summary: list a apimgmt api issue attachment.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiIssueAttachment
        text: apimgmt api issue attachment list  --xxx yyy
      - name: ApiManagementDeleteApiIssueAttachment
        text: apimgmt api issue attachment list  --xxx yyy
"""

helps['apimgmt api issue attachment show'] = """
    type: command
    short-summary: show a apimgmt api issue attachment.
    examples:
# get -- show
      - name: ApiManagementCreateApiIssueAttachment
        text: apimgmt api issue attachment show  --xxx yyy
      - name: ApiManagementDeleteApiIssueAttachment
        text: apimgmt api issue attachment show  --xxx yyy
"""

helps['apimgmt api tagdescription'] = """
    type: group
    short-summary: Commands to manage ApiTagDescription.
"""

helps['apimgmt api tagdescription create'] = """
    type: command
    short-summary: create a apimgmt api tagdescription.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiTagDescription
        text: apimgmt api tagdescription create  --xxx yyy
      - name: ApiManagementDeleteApiTagDescription
        text: apimgmt api tagdescription create  --xxx yyy
"""

helps['apimgmt api tagdescription update'] = """
    type: command
    short-summary: update a apimgmt api tagdescription.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiTagDescription
        text: apimgmt api tagdescription update  --xxx yyy
      - name: ApiManagementDeleteApiTagDescription
        text: apimgmt api tagdescription update  --xxx yyy
"""

helps['apimgmt api tagdescription delete'] = """
    type: command
    short-summary: delete a apimgmt api tagdescription.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiTagDescription
        text: apimgmt api tagdescription delete  --xxx yyy
      - name: ApiManagementDeleteApiTagDescription
        text: apimgmt api tagdescription delete  --xxx yyy
"""

helps['apimgmt api tagdescription list'] = """
    type: command
    short-summary: list a apimgmt api tagdescription.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiTagDescription
        text: apimgmt api tagdescription list  --xxx yyy
      - name: ApiManagementDeleteApiTagDescription
        text: apimgmt api tagdescription list  --xxx yyy
"""

helps['apimgmt api tagdescription show'] = """
    type: command
    short-summary: show a apimgmt api tagdescription.
    examples:
# get -- show
      - name: ApiManagementCreateApiTagDescription
        text: apimgmt api tagdescription show  --xxx yyy
      - name: ApiManagementDeleteApiTagDescription
        text: apimgmt api tagdescription show  --xxx yyy
"""

helps['apimgmt apiversionset'] = """
    type: group
    short-summary: Commands to manage ApiVersionSet.
"""

helps['apimgmt apiversionset create'] = """
    type: command
    short-summary: create a apimgmt apiversionset.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateApiVersionSet
        text: apimgmt apiversionset create  --xxx yyy
      - name: ApiManagementUpdateApiVersionSet
        text: apimgmt apiversionset create  --xxx yyy
      - name: ApiManagementDeleteApiVersionSet
        text: apimgmt apiversionset create  --xxx yyy
"""

helps['apimgmt apiversionset update'] = """
    type: command
    short-summary: update a apimgmt apiversionset.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateApiVersionSet
        text: apimgmt apiversionset update  --xxx yyy
      - name: ApiManagementUpdateApiVersionSet
        text: apimgmt apiversionset update  --xxx yyy
      - name: ApiManagementDeleteApiVersionSet
        text: apimgmt apiversionset update  --xxx yyy
"""

helps['apimgmt apiversionset delete'] = """
    type: command
    short-summary: delete a apimgmt apiversionset.
    examples:
# delete -- delete
      - name: ApiManagementCreateApiVersionSet
        text: apimgmt apiversionset delete  --xxx yyy
      - name: ApiManagementUpdateApiVersionSet
        text: apimgmt apiversionset delete  --xxx yyy
      - name: ApiManagementDeleteApiVersionSet
        text: apimgmt apiversionset delete  --xxx yyy
"""

helps['apimgmt apiversionset list'] = """
    type: command
    short-summary: list a apimgmt apiversionset.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateApiVersionSet
        text: apimgmt apiversionset list  --xxx yyy
      - name: ApiManagementUpdateApiVersionSet
        text: apimgmt apiversionset list  --xxx yyy
      - name: ApiManagementDeleteApiVersionSet
        text: apimgmt apiversionset list  --xxx yyy
"""

helps['apimgmt apiversionset show'] = """
    type: command
    short-summary: show a apimgmt apiversionset.
    examples:
# get -- show
      - name: ApiManagementCreateApiVersionSet
        text: apimgmt apiversionset show  --xxx yyy
      - name: ApiManagementUpdateApiVersionSet
        text: apimgmt apiversionset show  --xxx yyy
      - name: ApiManagementDeleteApiVersionSet
        text: apimgmt apiversionset show  --xxx yyy
"""

helps['apimgmt authorizationserver'] = """
    type: group
    short-summary: Commands to manage AuthorizationServer.
"""

helps['apimgmt authorizationserver create'] = """
    type: command
    short-summary: create a apimgmt authorizationserver.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateAuthorizationServer
        text: apimgmt authorizationserver create  --xxx yyy
      - name: ApiManagementUpdateAuthorizationServer
        text: apimgmt authorizationserver create  --xxx yyy
      - name: ApiManagementDeleteAuthorizationServer
        text: apimgmt authorizationserver create  --xxx yyy
"""

helps['apimgmt authorizationserver update'] = """
    type: command
    short-summary: update a apimgmt authorizationserver.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateAuthorizationServer
        text: apimgmt authorizationserver update  --xxx yyy
      - name: ApiManagementUpdateAuthorizationServer
        text: apimgmt authorizationserver update  --xxx yyy
      - name: ApiManagementDeleteAuthorizationServer
        text: apimgmt authorizationserver update  --xxx yyy
"""

helps['apimgmt authorizationserver delete'] = """
    type: command
    short-summary: delete a apimgmt authorizationserver.
    examples:
# delete -- delete
      - name: ApiManagementCreateAuthorizationServer
        text: apimgmt authorizationserver delete  --xxx yyy
      - name: ApiManagementUpdateAuthorizationServer
        text: apimgmt authorizationserver delete  --xxx yyy
      - name: ApiManagementDeleteAuthorizationServer
        text: apimgmt authorizationserver delete  --xxx yyy
"""

helps['apimgmt authorizationserver list'] = """
    type: command
    short-summary: list a apimgmt authorizationserver.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateAuthorizationServer
        text: apimgmt authorizationserver list  --xxx yyy
      - name: ApiManagementUpdateAuthorizationServer
        text: apimgmt authorizationserver list  --xxx yyy
      - name: ApiManagementDeleteAuthorizationServer
        text: apimgmt authorizationserver list  --xxx yyy
"""

helps['apimgmt authorizationserver show'] = """
    type: command
    short-summary: show a apimgmt authorizationserver.
    examples:
# get -- show
      - name: ApiManagementCreateAuthorizationServer
        text: apimgmt authorizationserver show  --xxx yyy
      - name: ApiManagementUpdateAuthorizationServer
        text: apimgmt authorizationserver show  --xxx yyy
      - name: ApiManagementDeleteAuthorizationServer
        text: apimgmt authorizationserver show  --xxx yyy
"""

helps['apimgmt backend'] = """
    type: group
    short-summary: Commands to manage Backend.
"""

helps['apimgmt backend create'] = """
    type: command
    short-summary: create a apimgmt backend.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateBackendServiceFabric
        text: apimgmt backend create  --xxx yyy
      - name: ApiManagementCreateBackendProxyBackend
        text: apimgmt backend create  --xxx yyy
      - name: ApiManagementUpdateBackend
        text: apimgmt backend create  --xxx yyy
      - name: ApiManagementDeleteBackend
        text: apimgmt backend create  --xxx yyy
"""

helps['apimgmt backend update'] = """
    type: command
    short-summary: update a apimgmt backend.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateBackendServiceFabric
        text: apimgmt backend update  --xxx yyy
      - name: ApiManagementCreateBackendProxyBackend
        text: apimgmt backend update  --xxx yyy
      - name: ApiManagementUpdateBackend
        text: apimgmt backend update  --xxx yyy
      - name: ApiManagementDeleteBackend
        text: apimgmt backend update  --xxx yyy
"""

helps['apimgmt backend delete'] = """
    type: command
    short-summary: delete a apimgmt backend.
    examples:
# delete -- delete
      - name: ApiManagementCreateBackendServiceFabric
        text: apimgmt backend delete  --xxx yyy
      - name: ApiManagementCreateBackendProxyBackend
        text: apimgmt backend delete  --xxx yyy
      - name: ApiManagementUpdateBackend
        text: apimgmt backend delete  --xxx yyy
      - name: ApiManagementDeleteBackend
        text: apimgmt backend delete  --xxx yyy
"""

helps['apimgmt backend list'] = """
    type: command
    short-summary: list a apimgmt backend.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateBackendServiceFabric
        text: apimgmt backend list  --xxx yyy
      - name: ApiManagementCreateBackendProxyBackend
        text: apimgmt backend list  --xxx yyy
      - name: ApiManagementUpdateBackend
        text: apimgmt backend list  --xxx yyy
      - name: ApiManagementDeleteBackend
        text: apimgmt backend list  --xxx yyy
"""

helps['apimgmt backend show'] = """
    type: command
    short-summary: show a apimgmt backend.
    examples:
# get -- show
      - name: ApiManagementCreateBackendServiceFabric
        text: apimgmt backend show  --xxx yyy
      - name: ApiManagementCreateBackendProxyBackend
        text: apimgmt backend show  --xxx yyy
      - name: ApiManagementUpdateBackend
        text: apimgmt backend show  --xxx yyy
      - name: ApiManagementDeleteBackend
        text: apimgmt backend show  --xxx yyy
"""

helps['apimgmt cache'] = """
    type: group
    short-summary: Commands to manage Cache.
"""

helps['apimgmt cache create'] = """
    type: command
    short-summary: create a apimgmt cache.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateCache
        text: apimgmt cache create  --xxx yyy
      - name: ApiManagementUpdateCache
        text: apimgmt cache create  --xxx yyy
      - name: ApiManagementDeleteCache
        text: apimgmt cache create  --xxx yyy
"""

helps['apimgmt cache update'] = """
    type: command
    short-summary: update a apimgmt cache.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateCache
        text: apimgmt cache update  --xxx yyy
      - name: ApiManagementUpdateCache
        text: apimgmt cache update  --xxx yyy
      - name: ApiManagementDeleteCache
        text: apimgmt cache update  --xxx yyy
"""

helps['apimgmt cache delete'] = """
    type: command
    short-summary: delete a apimgmt cache.
    examples:
# delete -- delete
      - name: ApiManagementCreateCache
        text: apimgmt cache delete  --xxx yyy
      - name: ApiManagementUpdateCache
        text: apimgmt cache delete  --xxx yyy
      - name: ApiManagementDeleteCache
        text: apimgmt cache delete  --xxx yyy
"""

helps['apimgmt cache list'] = """
    type: command
    short-summary: list a apimgmt cache.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateCache
        text: apimgmt cache list  --xxx yyy
      - name: ApiManagementUpdateCache
        text: apimgmt cache list  --xxx yyy
      - name: ApiManagementDeleteCache
        text: apimgmt cache list  --xxx yyy
"""

helps['apimgmt cache show'] = """
    type: command
    short-summary: show a apimgmt cache.
    examples:
# get -- show
      - name: ApiManagementCreateCache
        text: apimgmt cache show  --xxx yyy
      - name: ApiManagementUpdateCache
        text: apimgmt cache show  --xxx yyy
      - name: ApiManagementDeleteCache
        text: apimgmt cache show  --xxx yyy
"""

helps['apimgmt certificate'] = """
    type: group
    short-summary: Commands to manage Certificate.
"""

helps['apimgmt certificate create'] = """
    type: command
    short-summary: create a apimgmt certificate.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateCertificate
        text: apimgmt certificate create  --xxx yyy
      - name: ApiManagementDeleteCertificate
        text: apimgmt certificate create  --xxx yyy
"""

helps['apimgmt certificate update'] = """
    type: command
    short-summary: update a apimgmt certificate.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateCertificate
        text: apimgmt certificate update  --xxx yyy
      - name: ApiManagementDeleteCertificate
        text: apimgmt certificate update  --xxx yyy
"""

helps['apimgmt certificate delete'] = """
    type: command
    short-summary: delete a apimgmt certificate.
    examples:
# delete -- delete
      - name: ApiManagementCreateCertificate
        text: apimgmt certificate delete  --xxx yyy
      - name: ApiManagementDeleteCertificate
        text: apimgmt certificate delete  --xxx yyy
"""

helps['apimgmt certificate list'] = """
    type: command
    short-summary: list a apimgmt certificate.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateCertificate
        text: apimgmt certificate list  --xxx yyy
      - name: ApiManagementDeleteCertificate
        text: apimgmt certificate list  --xxx yyy
"""

helps['apimgmt certificate show'] = """
    type: command
    short-summary: show a apimgmt certificate.
    examples:
# get -- show
      - name: ApiManagementCreateCertificate
        text: apimgmt certificate show  --xxx yyy
      - name: ApiManagementDeleteCertificate
        text: apimgmt certificate show  --xxx yyy
"""

helps['apimgmt'] = """
    type: group
    short-summary: Commands to manage ApiManagementService.
"""

helps['apimgmt create'] = """
    type: command
    short-summary: create a apimgmt.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateService
        text: apimgmt create  --xxx yyy
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: apimgmt create  --xxx yyy
      - name: ApiManagementCreateServiceHavingMsi
        text: apimgmt create  --xxx yyy
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: apimgmt create  --xxx yyy
      - name: ApiManagementUpdateServiceDisableTls10
        text: apimgmt create  --xxx yyy
      - name: ApiManagementUpdateServicePublisherDetails
        text: apimgmt create  --xxx yyy
      - name: ApiManagementServiceDeleteService
        text: apimgmt create  --xxx yyy
"""

helps['apimgmt update'] = """
    type: command
    short-summary: update a apimgmt.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateService
        text: apimgmt update  --xxx yyy
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: apimgmt update  --xxx yyy
      - name: ApiManagementCreateServiceHavingMsi
        text: apimgmt update  --xxx yyy
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: apimgmt update  --xxx yyy
      - name: ApiManagementUpdateServiceDisableTls10
        text: apimgmt update  --xxx yyy
      - name: ApiManagementUpdateServicePublisherDetails
        text: apimgmt update  --xxx yyy
      - name: ApiManagementServiceDeleteService
        text: apimgmt update  --xxx yyy
"""

helps['apimgmt delete'] = """
    type: command
    short-summary: delete a apimgmt.
    examples:
# delete -- delete
      - name: ApiManagementCreateService
        text: apimgmt delete  --xxx yyy
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: apimgmt delete  --xxx yyy
      - name: ApiManagementCreateServiceHavingMsi
        text: apimgmt delete  --xxx yyy
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: apimgmt delete  --xxx yyy
      - name: ApiManagementUpdateServiceDisableTls10
        text: apimgmt delete  --xxx yyy
      - name: ApiManagementUpdateServicePublisherDetails
        text: apimgmt delete  --xxx yyy
      - name: ApiManagementServiceDeleteService
        text: apimgmt delete  --xxx yyy
"""

helps['apimgmt list'] = """
    type: command
    short-summary: list a apimgmt.
    examples:
# list_by_resource_group -- list
      - name: ApiManagementCreateService
        text: apimgmt list  --xxx yyy
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: apimgmt list  --xxx yyy
      - name: ApiManagementCreateServiceHavingMsi
        text: apimgmt list  --xxx yyy
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: apimgmt list  --xxx yyy
      - name: ApiManagementUpdateServiceDisableTls10
        text: apimgmt list  --xxx yyy
      - name: ApiManagementUpdateServicePublisherDetails
        text: apimgmt list  --xxx yyy
      - name: ApiManagementServiceDeleteService
        text: apimgmt list  --xxx yyy
# list -- list
      - name: ApiManagementCreateService
        text: apimgmt list  --xxx yyy
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: apimgmt list  --xxx yyy
      - name: ApiManagementCreateServiceHavingMsi
        text: apimgmt list  --xxx yyy
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: apimgmt list  --xxx yyy
      - name: ApiManagementUpdateServiceDisableTls10
        text: apimgmt list  --xxx yyy
      - name: ApiManagementUpdateServicePublisherDetails
        text: apimgmt list  --xxx yyy
      - name: ApiManagementServiceDeleteService
        text: apimgmt list  --xxx yyy
"""

helps['apimgmt show'] = """
    type: command
    short-summary: show a apimgmt.
    examples:
# get -- show
      - name: ApiManagementCreateService
        text: apimgmt show  --xxx yyy
      - name: ApiManagementCreateMultiRegionServiceWithCustomHostname
        text: apimgmt show  --xxx yyy
      - name: ApiManagementCreateServiceHavingMsi
        text: apimgmt show  --xxx yyy
      - name: ApiManagementCreateServiceWithSystemCertificates
        text: apimgmt show  --xxx yyy
      - name: ApiManagementUpdateServiceDisableTls10
        text: apimgmt show  --xxx yyy
      - name: ApiManagementUpdateServicePublisherDetails
        text: apimgmt show  --xxx yyy
      - name: ApiManagementServiceDeleteService
        text: apimgmt show  --xxx yyy
"""

helps['apimgmt diagnostic'] = """
    type: group
    short-summary: Commands to manage Diagnostic.
"""

helps['apimgmt diagnostic create'] = """
    type: command
    short-summary: create a apimgmt diagnostic.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateDiagnostic
        text: apimgmt diagnostic create  --xxx yyy
      - name: ApiManagementUpdateDiagnostic
        text: apimgmt diagnostic create  --xxx yyy
      - name: ApiManagementDeleteDiagnostic
        text: apimgmt diagnostic create  --xxx yyy
"""

helps['apimgmt diagnostic update'] = """
    type: command
    short-summary: update a apimgmt diagnostic.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateDiagnostic
        text: apimgmt diagnostic update  --xxx yyy
      - name: ApiManagementUpdateDiagnostic
        text: apimgmt diagnostic update  --xxx yyy
      - name: ApiManagementDeleteDiagnostic
        text: apimgmt diagnostic update  --xxx yyy
"""

helps['apimgmt diagnostic delete'] = """
    type: command
    short-summary: delete a apimgmt diagnostic.
    examples:
# delete -- delete
      - name: ApiManagementCreateDiagnostic
        text: apimgmt diagnostic delete  --xxx yyy
      - name: ApiManagementUpdateDiagnostic
        text: apimgmt diagnostic delete  --xxx yyy
      - name: ApiManagementDeleteDiagnostic
        text: apimgmt diagnostic delete  --xxx yyy
"""

helps['apimgmt diagnostic list'] = """
    type: command
    short-summary: list a apimgmt diagnostic.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateDiagnostic
        text: apimgmt diagnostic list  --xxx yyy
      - name: ApiManagementUpdateDiagnostic
        text: apimgmt diagnostic list  --xxx yyy
      - name: ApiManagementDeleteDiagnostic
        text: apimgmt diagnostic list  --xxx yyy
"""

helps['apimgmt diagnostic show'] = """
    type: command
    short-summary: show a apimgmt diagnostic.
    examples:
# get -- show
      - name: ApiManagementCreateDiagnostic
        text: apimgmt diagnostic show  --xxx yyy
      - name: ApiManagementUpdateDiagnostic
        text: apimgmt diagnostic show  --xxx yyy
      - name: ApiManagementDeleteDiagnostic
        text: apimgmt diagnostic show  --xxx yyy
"""

helps['apimgmt template'] = """
    type: group
    short-summary: Commands to manage EmailTemplate.
"""

helps['apimgmt template create'] = """
    type: command
    short-summary: create a apimgmt template.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateEmailTemplate
        text: apimgmt template create  --xxx yyy
      - name: ApiManagementUpdateEmailTemplate
        text: apimgmt template create  --xxx yyy
      - name: ApiManagementDeleteEmailTemplate
        text: apimgmt template create  --xxx yyy
"""

helps['apimgmt template update'] = """
    type: command
    short-summary: update a apimgmt template.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateEmailTemplate
        text: apimgmt template update  --xxx yyy
      - name: ApiManagementUpdateEmailTemplate
        text: apimgmt template update  --xxx yyy
      - name: ApiManagementDeleteEmailTemplate
        text: apimgmt template update  --xxx yyy
"""

helps['apimgmt template delete'] = """
    type: command
    short-summary: delete a apimgmt template.
    examples:
# delete -- delete
      - name: ApiManagementCreateEmailTemplate
        text: apimgmt template delete  --xxx yyy
      - name: ApiManagementUpdateEmailTemplate
        text: apimgmt template delete  --xxx yyy
      - name: ApiManagementDeleteEmailTemplate
        text: apimgmt template delete  --xxx yyy
"""

helps['apimgmt template list'] = """
    type: command
    short-summary: list a apimgmt template.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateEmailTemplate
        text: apimgmt template list  --xxx yyy
      - name: ApiManagementUpdateEmailTemplate
        text: apimgmt template list  --xxx yyy
      - name: ApiManagementDeleteEmailTemplate
        text: apimgmt template list  --xxx yyy
"""

helps['apimgmt template show'] = """
    type: command
    short-summary: show a apimgmt template.
    examples:
# get -- show
      - name: ApiManagementCreateEmailTemplate
        text: apimgmt template show  --xxx yyy
      - name: ApiManagementUpdateEmailTemplate
        text: apimgmt template show  --xxx yyy
      - name: ApiManagementDeleteEmailTemplate
        text: apimgmt template show  --xxx yyy
"""

helps['apimgmt group'] = """
    type: group
    short-summary: Commands to manage Group.
"""

helps['apimgmt group create'] = """
    type: command
    short-summary: create a apimgmt group.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateGroup
        text: apimgmt group create  --xxx yyy
      - name: ApiManagementCreateGroupExternal
        text: apimgmt group create  --xxx yyy
      - name: ApiManagementUpdateGroup
        text: apimgmt group create  --xxx yyy
      - name: ApiManagementDeleteGroup
        text: apimgmt group create  --xxx yyy
"""

helps['apimgmt group update'] = """
    type: command
    short-summary: update a apimgmt group.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateGroup
        text: apimgmt group update  --xxx yyy
      - name: ApiManagementCreateGroupExternal
        text: apimgmt group update  --xxx yyy
      - name: ApiManagementUpdateGroup
        text: apimgmt group update  --xxx yyy
      - name: ApiManagementDeleteGroup
        text: apimgmt group update  --xxx yyy
"""

helps['apimgmt group delete'] = """
    type: command
    short-summary: delete a apimgmt group.
    examples:
# delete -- delete
      - name: ApiManagementCreateGroup
        text: apimgmt group delete  --xxx yyy
      - name: ApiManagementCreateGroupExternal
        text: apimgmt group delete  --xxx yyy
      - name: ApiManagementUpdateGroup
        text: apimgmt group delete  --xxx yyy
      - name: ApiManagementDeleteGroup
        text: apimgmt group delete  --xxx yyy
"""

helps['apimgmt group list'] = """
    type: command
    short-summary: list a apimgmt group.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateGroup
        text: apimgmt group list  --xxx yyy
      - name: ApiManagementCreateGroupExternal
        text: apimgmt group list  --xxx yyy
      - name: ApiManagementUpdateGroup
        text: apimgmt group list  --xxx yyy
      - name: ApiManagementDeleteGroup
        text: apimgmt group list  --xxx yyy
"""

helps['apimgmt group show'] = """
    type: command
    short-summary: show a apimgmt group.
    examples:
# get -- show
      - name: ApiManagementCreateGroup
        text: apimgmt group show  --xxx yyy
      - name: ApiManagementCreateGroupExternal
        text: apimgmt group show  --xxx yyy
      - name: ApiManagementUpdateGroup
        text: apimgmt group show  --xxx yyy
      - name: ApiManagementDeleteGroup
        text: apimgmt group show  --xxx yyy
"""

helps['apimgmt group user'] = """
    type: group
    short-summary: Commands to manage GroupUser.
"""

helps['apimgmt group user create'] = """
    type: command
    short-summary: create a apimgmt group user.
    examples:
# create -- create
      - name: ApiManagementCreateGroupUser
        text: apimgmt group user create  --xxx yyy
      - name: ApiManagementDeleteGroupUser
        text: apimgmt group user create  --xxx yyy
"""

helps['apimgmt group user delete'] = """
    type: command
    short-summary: delete a apimgmt group user.
    examples:
# delete -- delete
      - name: ApiManagementCreateGroupUser
        text: apimgmt group user delete  --xxx yyy
      - name: ApiManagementDeleteGroupUser
        text: apimgmt group user delete  --xxx yyy
"""

helps['apimgmt group user list'] = """
    type: command
    short-summary: list a apimgmt group user.
    examples:
# list -- list
      - name: ApiManagementCreateGroupUser
        text: apimgmt group user list  --xxx yyy
      - name: ApiManagementDeleteGroupUser
        text: apimgmt group user list  --xxx yyy
"""

helps['apimgmt identityprovider'] = """
    type: group
    short-summary: Commands to manage IdentityProvider.
"""

helps['apimgmt identityprovider create'] = """
    type: command
    short-summary: create a apimgmt identityprovider.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateIdentityProvider
        text: apimgmt identityprovider create  --xxx yyy
      - name: ApiManagementUpdateIdentityProvider
        text: apimgmt identityprovider create  --xxx yyy
      - name: ApiManagementDeleteIdentityProvider
        text: apimgmt identityprovider create  --xxx yyy
"""

helps['apimgmt identityprovider update'] = """
    type: command
    short-summary: update a apimgmt identityprovider.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateIdentityProvider
        text: apimgmt identityprovider update  --xxx yyy
      - name: ApiManagementUpdateIdentityProvider
        text: apimgmt identityprovider update  --xxx yyy
      - name: ApiManagementDeleteIdentityProvider
        text: apimgmt identityprovider update  --xxx yyy
"""

helps['apimgmt identityprovider delete'] = """
    type: command
    short-summary: delete a apimgmt identityprovider.
    examples:
# delete -- delete
      - name: ApiManagementCreateIdentityProvider
        text: apimgmt identityprovider delete  --xxx yyy
      - name: ApiManagementUpdateIdentityProvider
        text: apimgmt identityprovider delete  --xxx yyy
      - name: ApiManagementDeleteIdentityProvider
        text: apimgmt identityprovider delete  --xxx yyy
"""

helps['apimgmt identityprovider list'] = """
    type: command
    short-summary: list a apimgmt identityprovider.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateIdentityProvider
        text: apimgmt identityprovider list  --xxx yyy
      - name: ApiManagementUpdateIdentityProvider
        text: apimgmt identityprovider list  --xxx yyy
      - name: ApiManagementDeleteIdentityProvider
        text: apimgmt identityprovider list  --xxx yyy
"""

helps['apimgmt identityprovider show'] = """
    type: command
    short-summary: show a apimgmt identityprovider.
    examples:
# get -- show
      - name: ApiManagementCreateIdentityProvider
        text: apimgmt identityprovider show  --xxx yyy
      - name: ApiManagementUpdateIdentityProvider
        text: apimgmt identityprovider show  --xxx yyy
      - name: ApiManagementDeleteIdentityProvider
        text: apimgmt identityprovider show  --xxx yyy
"""

helps['apimgmt logger'] = """
    type: group
    short-summary: Commands to manage Logger.
"""

helps['apimgmt logger create'] = """
    type: command
    short-summary: create a apimgmt logger.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateEHLogger
        text: apimgmt logger create  --xxx yyy
      - name: ApiManagementCreateAILogger
        text: apimgmt logger create  --xxx yyy
      - name: ApiManagementUpdateLogger
        text: apimgmt logger create  --xxx yyy
      - name: ApiManagementDeleteLogger
        text: apimgmt logger create  --xxx yyy
"""

helps['apimgmt logger update'] = """
    type: command
    short-summary: update a apimgmt logger.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateEHLogger
        text: apimgmt logger update  --xxx yyy
      - name: ApiManagementCreateAILogger
        text: apimgmt logger update  --xxx yyy
      - name: ApiManagementUpdateLogger
        text: apimgmt logger update  --xxx yyy
      - name: ApiManagementDeleteLogger
        text: apimgmt logger update  --xxx yyy
"""

helps['apimgmt logger delete'] = """
    type: command
    short-summary: delete a apimgmt logger.
    examples:
# delete -- delete
      - name: ApiManagementCreateEHLogger
        text: apimgmt logger delete  --xxx yyy
      - name: ApiManagementCreateAILogger
        text: apimgmt logger delete  --xxx yyy
      - name: ApiManagementUpdateLogger
        text: apimgmt logger delete  --xxx yyy
      - name: ApiManagementDeleteLogger
        text: apimgmt logger delete  --xxx yyy
"""

helps['apimgmt logger list'] = """
    type: command
    short-summary: list a apimgmt logger.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateEHLogger
        text: apimgmt logger list  --xxx yyy
      - name: ApiManagementCreateAILogger
        text: apimgmt logger list  --xxx yyy
      - name: ApiManagementUpdateLogger
        text: apimgmt logger list  --xxx yyy
      - name: ApiManagementDeleteLogger
        text: apimgmt logger list  --xxx yyy
"""

helps['apimgmt logger show'] = """
    type: command
    short-summary: show a apimgmt logger.
    examples:
# get -- show
      - name: ApiManagementCreateEHLogger
        text: apimgmt logger show  --xxx yyy
      - name: ApiManagementCreateAILogger
        text: apimgmt logger show  --xxx yyy
      - name: ApiManagementUpdateLogger
        text: apimgmt logger show  --xxx yyy
      - name: ApiManagementDeleteLogger
        text: apimgmt logger show  --xxx yyy
"""

helps['apimgmt notification'] = """
    type: group
    short-summary: Commands to manage Notification.
"""

helps['apimgmt notification create'] = """
    type: command
    short-summary: create a apimgmt notification.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateNotification
        text: apimgmt notification create  --xxx yyy
"""

helps['apimgmt notification update'] = """
    type: command
    short-summary: update a apimgmt notification.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateNotification
        text: apimgmt notification update  --xxx yyy
"""

helps['apimgmt notification list'] = """
    type: command
    short-summary: list a apimgmt notification.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateNotification
        text: apimgmt notification list  --xxx yyy
"""

helps['apimgmt notification show'] = """
    type: command
    short-summary: show a apimgmt notification.
    examples:
# get -- show
      - name: ApiManagementCreateNotification
        text: apimgmt notification show  --xxx yyy
"""

helps['apimgmt notification recipientuser'] = """
    type: group
    short-summary: Commands to manage NotificationRecipientUser.
"""

helps['apimgmt notification recipientuser create'] = """
    type: command
    short-summary: create a apimgmt notification recipientuser.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateNotificationRecipientUser
        text: apimgmt notification recipientuser create  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientUser
        text: apimgmt notification recipientuser create  --xxx yyy
"""

helps['apimgmt notification recipientuser update'] = """
    type: command
    short-summary: update a apimgmt notification recipientuser.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateNotificationRecipientUser
        text: apimgmt notification recipientuser update  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientUser
        text: apimgmt notification recipientuser update  --xxx yyy
"""

helps['apimgmt notification recipientuser delete'] = """
    type: command
    short-summary: delete a apimgmt notification recipientuser.
    examples:
# delete -- delete
      - name: ApiManagementCreateNotificationRecipientUser
        text: apimgmt notification recipientuser delete  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientUser
        text: apimgmt notification recipientuser delete  --xxx yyy
"""

helps['apimgmt notification recipientuser list'] = """
    type: command
    short-summary: list a apimgmt notification recipientuser.
    examples:
# list_by_notification -- list
      - name: ApiManagementCreateNotificationRecipientUser
        text: apimgmt notification recipientuser list  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientUser
        text: apimgmt notification recipientuser list  --xxx yyy
"""

helps['apimgmt notification recipientemail'] = """
    type: group
    short-summary: Commands to manage NotificationRecipientEmail.
"""

helps['apimgmt notification recipientemail create'] = """
    type: command
    short-summary: create a apimgmt notification recipientemail.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateNotificationRecipientEmail
        text: apimgmt notification recipientemail create  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientEmail
        text: apimgmt notification recipientemail create  --xxx yyy
"""

helps['apimgmt notification recipientemail update'] = """
    type: command
    short-summary: update a apimgmt notification recipientemail.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateNotificationRecipientEmail
        text: apimgmt notification recipientemail update  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientEmail
        text: apimgmt notification recipientemail update  --xxx yyy
"""

helps['apimgmt notification recipientemail delete'] = """
    type: command
    short-summary: delete a apimgmt notification recipientemail.
    examples:
# delete -- delete
      - name: ApiManagementCreateNotificationRecipientEmail
        text: apimgmt notification recipientemail delete  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientEmail
        text: apimgmt notification recipientemail delete  --xxx yyy
"""

helps['apimgmt notification recipientemail list'] = """
    type: command
    short-summary: list a apimgmt notification recipientemail.
    examples:
# list_by_notification -- list
      - name: ApiManagementCreateNotificationRecipientEmail
        text: apimgmt notification recipientemail list  --xxx yyy
      - name: ApiManagementDeleteNotificationRecipientEmail
        text: apimgmt notification recipientemail list  --xxx yyy
"""

helps['apimgmt openidconnectprovider'] = """
    type: group
    short-summary: Commands to manage OpenIdConnectProvider.
"""

helps['apimgmt openidconnectprovider create'] = """
    type: command
    short-summary: create a apimgmt openidconnectprovider.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateOpenIdConnectProvider
        text: apimgmt openidconnectprovider create  --xxx yyy
      - name: ApiManagementUpdateOpenIdConnectProvider
        text: apimgmt openidconnectprovider create  --xxx yyy
      - name: ApiManagementDeleteOpenIdConnectProvider
        text: apimgmt openidconnectprovider create  --xxx yyy
"""

helps['apimgmt openidconnectprovider update'] = """
    type: command
    short-summary: update a apimgmt openidconnectprovider.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateOpenIdConnectProvider
        text: apimgmt openidconnectprovider update  --xxx yyy
      - name: ApiManagementUpdateOpenIdConnectProvider
        text: apimgmt openidconnectprovider update  --xxx yyy
      - name: ApiManagementDeleteOpenIdConnectProvider
        text: apimgmt openidconnectprovider update  --xxx yyy
"""

helps['apimgmt openidconnectprovider delete'] = """
    type: command
    short-summary: delete a apimgmt openidconnectprovider.
    examples:
# delete -- delete
      - name: ApiManagementCreateOpenIdConnectProvider
        text: apimgmt openidconnectprovider delete  --xxx yyy
      - name: ApiManagementUpdateOpenIdConnectProvider
        text: apimgmt openidconnectprovider delete  --xxx yyy
      - name: ApiManagementDeleteOpenIdConnectProvider
        text: apimgmt openidconnectprovider delete  --xxx yyy
"""

helps['apimgmt openidconnectprovider list'] = """
    type: command
    short-summary: list a apimgmt openidconnectprovider.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateOpenIdConnectProvider
        text: apimgmt openidconnectprovider list  --xxx yyy
      - name: ApiManagementUpdateOpenIdConnectProvider
        text: apimgmt openidconnectprovider list  --xxx yyy
      - name: ApiManagementDeleteOpenIdConnectProvider
        text: apimgmt openidconnectprovider list  --xxx yyy
"""

helps['apimgmt openidconnectprovider show'] = """
    type: command
    short-summary: show a apimgmt openidconnectprovider.
    examples:
# get -- show
      - name: ApiManagementCreateOpenIdConnectProvider
        text: apimgmt openidconnectprovider show  --xxx yyy
      - name: ApiManagementUpdateOpenIdConnectProvider
        text: apimgmt openidconnectprovider show  --xxx yyy
      - name: ApiManagementDeleteOpenIdConnectProvider
        text: apimgmt openidconnectprovider show  --xxx yyy
"""

helps['apimgmt policy'] = """
    type: group
    short-summary: Commands to manage Policy.
"""

helps['apimgmt policy create'] = """
    type: command
    short-summary: create a apimgmt policy.
    examples:
# create_or_update -- create
      - name: ApiManagementCreatePolicy
        text: apimgmt policy create  --xxx yyy
      - name: ApiManagementDeletePolicy
        text: apimgmt policy create  --xxx yyy
"""

helps['apimgmt policy update'] = """
    type: command
    short-summary: update a apimgmt policy.
    examples:
# create_or_update -- update
      - name: ApiManagementCreatePolicy
        text: apimgmt policy update  --xxx yyy
      - name: ApiManagementDeletePolicy
        text: apimgmt policy update  --xxx yyy
"""

helps['apimgmt policy delete'] = """
    type: command
    short-summary: delete a apimgmt policy.
    examples:
# delete -- delete
      - name: ApiManagementCreatePolicy
        text: apimgmt policy delete  --xxx yyy
      - name: ApiManagementDeletePolicy
        text: apimgmt policy delete  --xxx yyy
"""

helps['apimgmt policy list'] = """
    type: command
    short-summary: list a apimgmt policy.
    examples:
# list_by_service -- list
      - name: ApiManagementCreatePolicy
        text: apimgmt policy list  --xxx yyy
      - name: ApiManagementDeletePolicy
        text: apimgmt policy list  --xxx yyy
"""

helps['apimgmt policy show'] = """
    type: command
    short-summary: show a apimgmt policy.
    examples:
# get -- show
      - name: ApiManagementCreatePolicy
        text: apimgmt policy show  --xxx yyy
      - name: ApiManagementDeletePolicy
        text: apimgmt policy show  --xxx yyy
"""

helps['apimgmt portalsetting'] = """
    type: group
    short-summary: Commands to manage SignInSetting.
"""

helps['apimgmt portalsetting create'] = """
    type: command
    short-summary: create a apimgmt portalsetting.
    examples:
# create_or_update -- create
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: apimgmt portalsetting create  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: apimgmt portalsetting create  --xxx yyy
"""

helps['apimgmt portalsetting update'] = """
    type: command
    short-summary: update a apimgmt portalsetting.
    examples:
# create_or_update -- update
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: apimgmt portalsetting update  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: apimgmt portalsetting update  --xxx yyy
"""

helps['apimgmt portalsetting show'] = """
    type: command
    short-summary: show a apimgmt portalsetting.
    examples:
# get -- show
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: apimgmt portalsetting show  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateSignIn
        text: apimgmt portalsetting show  --xxx yyy
"""

helps['apimgmt portalsetting'] = """
    type: group
    short-summary: Commands to manage SignUpSetting.
"""

helps['apimgmt portalsetting create'] = """
    type: command
    short-summary: create a apimgmt portalsetting.
    examples:
# create_or_update -- create
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: apimgmt portalsetting create  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: apimgmt portalsetting create  --xxx yyy
"""

helps['apimgmt portalsetting update'] = """
    type: command
    short-summary: update a apimgmt portalsetting.
    examples:
# create_or_update -- update
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: apimgmt portalsetting update  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: apimgmt portalsetting update  --xxx yyy
"""

helps['apimgmt portalsetting show'] = """
    type: command
    short-summary: show a apimgmt portalsetting.
    examples:
# get -- show
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: apimgmt portalsetting show  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateSignUp
        text: apimgmt portalsetting show  --xxx yyy
"""

helps['apimgmt portalsetting'] = """
    type: group
    short-summary: Commands to manage DelegationSetting.
"""

helps['apimgmt portalsetting create'] = """
    type: command
    short-summary: create a apimgmt portalsetting.
    examples:
# create_or_update -- create
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: apimgmt portalsetting create  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: apimgmt portalsetting create  --xxx yyy
"""

helps['apimgmt portalsetting update'] = """
    type: command
    short-summary: update a apimgmt portalsetting.
    examples:
# create_or_update -- update
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: apimgmt portalsetting update  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: apimgmt portalsetting update  --xxx yyy
"""

helps['apimgmt portalsetting show'] = """
    type: command
    short-summary: show a apimgmt portalsetting.
    examples:
# get -- show
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: apimgmt portalsetting show  --xxx yyy
      - name: ApiManagementPortalSettingsUpdateDelegation
        text: apimgmt portalsetting show  --xxx yyy
"""

helps['apimgmt product'] = """
    type: group
    short-summary: Commands to manage Product.
"""

helps['apimgmt product create'] = """
    type: command
    short-summary: create a apimgmt product.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateProduct
        text: apimgmt product create  --xxx yyy
      - name: ApiManagementUpdateProduct
        text: apimgmt product create  --xxx yyy
      - name: ApiManagementDeleteProduct
        text: apimgmt product create  --xxx yyy
"""

helps['apimgmt product update'] = """
    type: command
    short-summary: update a apimgmt product.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateProduct
        text: apimgmt product update  --xxx yyy
      - name: ApiManagementUpdateProduct
        text: apimgmt product update  --xxx yyy
      - name: ApiManagementDeleteProduct
        text: apimgmt product update  --xxx yyy
"""

helps['apimgmt product delete'] = """
    type: command
    short-summary: delete a apimgmt product.
    examples:
# delete -- delete
      - name: ApiManagementCreateProduct
        text: apimgmt product delete  --xxx yyy
      - name: ApiManagementUpdateProduct
        text: apimgmt product delete  --xxx yyy
      - name: ApiManagementDeleteProduct
        text: apimgmt product delete  --xxx yyy
"""

helps['apimgmt product list'] = """
    type: command
    short-summary: list a apimgmt product.
    examples:
# list_by_tags -- list
      - name: ApiManagementCreateProduct
        text: apimgmt product list  --xxx yyy
      - name: ApiManagementUpdateProduct
        text: apimgmt product list  --xxx yyy
      - name: ApiManagementDeleteProduct
        text: apimgmt product list  --xxx yyy
# list_by_service -- list
      - name: ApiManagementCreateProduct
        text: apimgmt product list  --xxx yyy
      - name: ApiManagementUpdateProduct
        text: apimgmt product list  --xxx yyy
      - name: ApiManagementDeleteProduct
        text: apimgmt product list  --xxx yyy
"""

helps['apimgmt product show'] = """
    type: command
    short-summary: show a apimgmt product.
    examples:
# get -- show
      - name: ApiManagementCreateProduct
        text: apimgmt product show  --xxx yyy
      - name: ApiManagementUpdateProduct
        text: apimgmt product show  --xxx yyy
      - name: ApiManagementDeleteProduct
        text: apimgmt product show  --xxx yyy
"""

helps['apimgmt product api'] = """
    type: group
    short-summary: Commands to manage ProductApi.
"""

helps['apimgmt product api create'] = """
    type: command
    short-summary: create a apimgmt product api.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateProductApi
        text: apimgmt product api create  --xxx yyy
      - name: ApiManagementDeleteProductApi
        text: apimgmt product api create  --xxx yyy
"""

helps['apimgmt product api update'] = """
    type: command
    short-summary: update a apimgmt product api.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateProductApi
        text: apimgmt product api update  --xxx yyy
      - name: ApiManagementDeleteProductApi
        text: apimgmt product api update  --xxx yyy
"""

helps['apimgmt product api delete'] = """
    type: command
    short-summary: delete a apimgmt product api.
    examples:
# delete -- delete
      - name: ApiManagementCreateProductApi
        text: apimgmt product api delete  --xxx yyy
      - name: ApiManagementDeleteProductApi
        text: apimgmt product api delete  --xxx yyy
"""

helps['apimgmt product api list'] = """
    type: command
    short-summary: list a apimgmt product api.
    examples:
# list_by_product -- list
      - name: ApiManagementCreateProductApi
        text: apimgmt product api list  --xxx yyy
      - name: ApiManagementDeleteProductApi
        text: apimgmt product api list  --xxx yyy
"""

helps['apimgmt product group'] = """
    type: group
    short-summary: Commands to manage ProductGroup.
"""

helps['apimgmt product group create'] = """
    type: command
    short-summary: create a apimgmt product group.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateProductGroup
        text: apimgmt product group create  --xxx yyy
      - name: ApiManagementDeleteProductGroup
        text: apimgmt product group create  --xxx yyy
"""

helps['apimgmt product group update'] = """
    type: command
    short-summary: update a apimgmt product group.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateProductGroup
        text: apimgmt product group update  --xxx yyy
      - name: ApiManagementDeleteProductGroup
        text: apimgmt product group update  --xxx yyy
"""

helps['apimgmt product group delete'] = """
    type: command
    short-summary: delete a apimgmt product group.
    examples:
# delete -- delete
      - name: ApiManagementCreateProductGroup
        text: apimgmt product group delete  --xxx yyy
      - name: ApiManagementDeleteProductGroup
        text: apimgmt product group delete  --xxx yyy
"""

helps['apimgmt product group list'] = """
    type: command
    short-summary: list a apimgmt product group.
    examples:
# list_by_product -- list
      - name: ApiManagementCreateProductGroup
        text: apimgmt product group list  --xxx yyy
      - name: ApiManagementDeleteProductGroup
        text: apimgmt product group list  --xxx yyy
"""

helps['apimgmt product policy'] = """
    type: group
    short-summary: Commands to manage ProductPolicy.
"""

helps['apimgmt product policy create'] = """
    type: command
    short-summary: create a apimgmt product policy.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateProductPolicy
        text: apimgmt product policy create  --xxx yyy
      - name: ApiManagementDeleteProductPolicy
        text: apimgmt product policy create  --xxx yyy
"""

helps['apimgmt product policy update'] = """
    type: command
    short-summary: update a apimgmt product policy.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateProductPolicy
        text: apimgmt product policy update  --xxx yyy
      - name: ApiManagementDeleteProductPolicy
        text: apimgmt product policy update  --xxx yyy
"""

helps['apimgmt product policy delete'] = """
    type: command
    short-summary: delete a apimgmt product policy.
    examples:
# delete -- delete
      - name: ApiManagementCreateProductPolicy
        text: apimgmt product policy delete  --xxx yyy
      - name: ApiManagementDeleteProductPolicy
        text: apimgmt product policy delete  --xxx yyy
"""

helps['apimgmt product policy list'] = """
    type: command
    short-summary: list a apimgmt product policy.
    examples:
# list_by_product -- list
      - name: ApiManagementCreateProductPolicy
        text: apimgmt product policy list  --xxx yyy
      - name: ApiManagementDeleteProductPolicy
        text: apimgmt product policy list  --xxx yyy
"""

helps['apimgmt product policy show'] = """
    type: command
    short-summary: show a apimgmt product policy.
    examples:
# get -- show
      - name: ApiManagementCreateProductPolicy
        text: apimgmt product policy show  --xxx yyy
      - name: ApiManagementDeleteProductPolicy
        text: apimgmt product policy show  --xxx yyy
"""

helps['apimgmt property'] = """
    type: group
    short-summary: Commands to manage Property.
"""

helps['apimgmt property create'] = """
    type: command
    short-summary: create a apimgmt property.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateProperty
        text: apimgmt property create  --xxx yyy
      - name: ApiManagementUpdateProperty
        text: apimgmt property create  --xxx yyy
      - name: ApiManagementDeleteProperty
        text: apimgmt property create  --xxx yyy
"""

helps['apimgmt property update'] = """
    type: command
    short-summary: update a apimgmt property.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateProperty
        text: apimgmt property update  --xxx yyy
      - name: ApiManagementUpdateProperty
        text: apimgmt property update  --xxx yyy
      - name: ApiManagementDeleteProperty
        text: apimgmt property update  --xxx yyy
"""

helps['apimgmt property delete'] = """
    type: command
    short-summary: delete a apimgmt property.
    examples:
# delete -- delete
      - name: ApiManagementCreateProperty
        text: apimgmt property delete  --xxx yyy
      - name: ApiManagementUpdateProperty
        text: apimgmt property delete  --xxx yyy
      - name: ApiManagementDeleteProperty
        text: apimgmt property delete  --xxx yyy
"""

helps['apimgmt property list'] = """
    type: command
    short-summary: list a apimgmt property.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateProperty
        text: apimgmt property list  --xxx yyy
      - name: ApiManagementUpdateProperty
        text: apimgmt property list  --xxx yyy
      - name: ApiManagementDeleteProperty
        text: apimgmt property list  --xxx yyy
"""

helps['apimgmt property show'] = """
    type: command
    short-summary: show a apimgmt property.
    examples:
# get -- show
      - name: ApiManagementCreateProperty
        text: apimgmt property show  --xxx yyy
      - name: ApiManagementUpdateProperty
        text: apimgmt property show  --xxx yyy
      - name: ApiManagementDeleteProperty
        text: apimgmt property show  --xxx yyy
"""

helps['apimgmt subscription'] = """
    type: group
    short-summary: Commands to manage Subscription.
"""

helps['apimgmt subscription create'] = """
    type: command
    short-summary: create a apimgmt subscription.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateSubscription
        text: apimgmt subscription create  --xxx yyy
      - name: ApiManagementUpdateSubscription
        text: apimgmt subscription create  --xxx yyy
      - name: ApiManagementDeleteSubscription
        text: apimgmt subscription create  --xxx yyy
"""

helps['apimgmt subscription update'] = """
    type: command
    short-summary: update a apimgmt subscription.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateSubscription
        text: apimgmt subscription update  --xxx yyy
      - name: ApiManagementUpdateSubscription
        text: apimgmt subscription update  --xxx yyy
      - name: ApiManagementDeleteSubscription
        text: apimgmt subscription update  --xxx yyy
"""

helps['apimgmt subscription delete'] = """
    type: command
    short-summary: delete a apimgmt subscription.
    examples:
# delete -- delete
      - name: ApiManagementCreateSubscription
        text: apimgmt subscription delete  --xxx yyy
      - name: ApiManagementUpdateSubscription
        text: apimgmt subscription delete  --xxx yyy
      - name: ApiManagementDeleteSubscription
        text: apimgmt subscription delete  --xxx yyy
"""

helps['apimgmt subscription list'] = """
    type: command
    short-summary: list a apimgmt subscription.
    examples:
# list -- list
      - name: ApiManagementCreateSubscription
        text: apimgmt subscription list  --xxx yyy
      - name: ApiManagementUpdateSubscription
        text: apimgmt subscription list  --xxx yyy
      - name: ApiManagementDeleteSubscription
        text: apimgmt subscription list  --xxx yyy
"""

helps['apimgmt subscription show'] = """
    type: command
    short-summary: show a apimgmt subscription.
    examples:
# get -- show
      - name: ApiManagementCreateSubscription
        text: apimgmt subscription show  --xxx yyy
      - name: ApiManagementUpdateSubscription
        text: apimgmt subscription show  --xxx yyy
      - name: ApiManagementDeleteSubscription
        text: apimgmt subscription show  --xxx yyy
"""

helps['apimgmt user'] = """
    type: group
    short-summary: Commands to manage User.
"""

helps['apimgmt user create'] = """
    type: command
    short-summary: create a apimgmt user.
    examples:
# create_or_update -- create
      - name: ApiManagementCreateUser
        text: apimgmt user create  --xxx yyy
      - name: ApiManagementUpdateUser
        text: apimgmt user create  --xxx yyy
      - name: ApiManagementDeleteUser
        text: apimgmt user create  --xxx yyy
"""

helps['apimgmt user update'] = """
    type: command
    short-summary: update a apimgmt user.
    examples:
# create_or_update -- update
      - name: ApiManagementCreateUser
        text: apimgmt user update  --xxx yyy
      - name: ApiManagementUpdateUser
        text: apimgmt user update  --xxx yyy
      - name: ApiManagementDeleteUser
        text: apimgmt user update  --xxx yyy
"""

helps['apimgmt user delete'] = """
    type: command
    short-summary: delete a apimgmt user.
    examples:
# delete -- delete
      - name: ApiManagementCreateUser
        text: apimgmt user delete  --xxx yyy
      - name: ApiManagementUpdateUser
        text: apimgmt user delete  --xxx yyy
      - name: ApiManagementDeleteUser
        text: apimgmt user delete  --xxx yyy
"""

helps['apimgmt user list'] = """
    type: command
    short-summary: list a apimgmt user.
    examples:
# list_by_service -- list
      - name: ApiManagementCreateUser
        text: apimgmt user list  --xxx yyy
      - name: ApiManagementUpdateUser
        text: apimgmt user list  --xxx yyy
      - name: ApiManagementDeleteUser
        text: apimgmt user list  --xxx yyy
"""

helps['apimgmt user show'] = """
    type: command
    short-summary: show a apimgmt user.
    examples:
# get -- show
      - name: ApiManagementCreateUser
        text: apimgmt user show  --xxx yyy
      - name: ApiManagementUpdateUser
        text: apimgmt user show  --xxx yyy
      - name: ApiManagementDeleteUser
        text: apimgmt user show  --xxx yyy
"""