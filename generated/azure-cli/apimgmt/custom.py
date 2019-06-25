# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_apimanagementapi
def create_apimgmt_api(cmd, client,
                       resource_group,
                       name,
                       api_id,
                       parameters=None):
    body={}
    return client.api.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, parameters=body)

# module equivalent: azure_rm_apimanagementapi
def update_apimgmt_api(cmd, client,
                       resource_group,
                       name,
                       api_id,
                       parameters=None):
    body={}
    return client.api.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, parameters=body)

# module equivalent: azure_rm_apimanagementapi
def delete_apimgmt_api(cmd, client,
                       resource_group,
                       name,
                       api_id):
    return client.api.delete(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapi
def list_apimgmt_api(cmd, client,
                     resource_group,
                     name):
    if resource_group is not None and name is not None:
        return client.api.list_by_tags(resource_group_name=resource_group, service_name=name)
    else:
        return client.api.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementapi
def show_apimgmt_api(cmd, client,
                     resource_group,
                     name,
                     api_id):
    return client.api.get(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapirelease
def create_apimgmt_api_release(cmd, client,
                               resource_group,
                               name,
                               api_id,
                               release_id,
                               parameters=None):
    body={}
    return client.api_release.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, release_id=release_id, parameters=body)

# module equivalent: azure_rm_apimanagementapirelease
def update_apimgmt_api_release(cmd, client,
                               resource_group,
                               name,
                               api_id,
                               release_id,
                               parameters=None):
    body={}
    return client.api_release.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, release_id=release_id, parameters=body)

# module equivalent: azure_rm_apimanagementapirelease
def delete_apimgmt_api_release(cmd, client,
                               resource_group,
                               name,
                               api_id,
                               release_id):
    return client.api_release.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, release_id=release_id)

# module equivalent: azure_rm_apimanagementapirelease
def list_apimgmt_api_release(cmd, client,
                             resource_group,
                             name,
                             api_id):
    return client.api_release.list_by_service(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapirelease
def show_apimgmt_api_release(cmd, client,
                             resource_group,
                             name,
                             api_id,
                             release_id):
    return client.api_release.get(resource_group_name=resource_group, service_name=name, api_id=api_id, release_id=release_id)

# module equivalent: azure_rm_apimanagementapioperation
def create_apimgmt_api_operation(cmd, client,
                                 resource_group,
                                 name,
                                 api_id,
                                 operation_id,
                                 parameters=None):
    body={}
    return client.api_operation.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id, parameters=body)

# module equivalent: azure_rm_apimanagementapioperation
def update_apimgmt_api_operation(cmd, client,
                                 resource_group,
                                 name,
                                 api_id,
                                 operation_id,
                                 parameters=None):
    body={}
    return client.api_operation.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id, parameters=body)

# module equivalent: azure_rm_apimanagementapioperation
def delete_apimgmt_api_operation(cmd, client,
                                 resource_group,
                                 name,
                                 api_id,
                                 operation_id):
    return client.api_operation.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id)

# module equivalent: azure_rm_apimanagementapioperation
def list_apimgmt_api_operation(cmd, client,
                               resource_group,
                               name,
                               api_id):
    return client.api_operation.list_by_api(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapioperation
def show_apimgmt_api_operation(cmd, client,
                               resource_group,
                               name,
                               api_id,
                               operation_id):
    return client.api_operation.get(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id)

# module equivalent: azure_rm_apimanagementapioperationpolicy
def create_apimgmt_api_operation_policy(cmd, client,
                                        resource_group,
                                        name,
                                        api_id,
                                        operation_id,
                                        policy_id,
                                        parameters=None):
    body={}
    return client.api_operation_policy.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementapioperationpolicy
def update_apimgmt_api_operation_policy(cmd, client,
                                        resource_group,
                                        name,
                                        api_id,
                                        operation_id,
                                        policy_id,
                                        parameters=None):
    body={}
    return client.api_operation_policy.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementapioperationpolicy
def delete_apimgmt_api_operation_policy(cmd, client,
                                        resource_group,
                                        name,
                                        api_id,
                                        operation_id,
                                        policy_id):
    return client.api_operation_policy.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id, policy_id=policy_id)

# module equivalent: azure_rm_apimanagementapioperationpolicy
def list_apimgmt_api_operation_policy(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      operation_id):
    return client.api_operation_policy.list_by_operation(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id)

# module equivalent: azure_rm_apimanagementapioperationpolicy
def show_apimgmt_api_operation_policy(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      operation_id,
                                      format=None,
                                      policy_id):
    return client.api_operation_policy.get(resource_group_name=resource_group, service_name=name, api_id=api_id, operation_id=operation_id, format=format, policy_id=policy_id)

# module equivalent: azure_rm_apimanagementtag
def create_apimgmt_tag(cmd, client,
                       resource_group,
                       name,
                       tag_id,
                       parameters=None):
    body={}
    return client.tag.create_or_update(resource_group_name=resource_group, service_name=name, tag_id=tag_id, parameters=body)

# module equivalent: azure_rm_apimanagementtag
def update_apimgmt_tag(cmd, client,
                       resource_group,
                       name,
                       tag_id,
                       parameters=None):
    body={}
    return client.tag.create_or_update(resource_group_name=resource_group, service_name=name, tag_id=tag_id, parameters=body)

# module equivalent: azure_rm_apimanagementtag
def delete_apimgmt_tag(cmd, client,
                       resource_group,
                       name,
                       tag_id):
    return client.tag.delete(resource_group_name=resource_group, service_name=name, tag_id=tag_id)

# module equivalent: azure_rm_apimanagementtag
def list_apimgmt_tag(cmd, client,
                     resource_group,
                     name):
    if resource_group is not None and name is not None:
        return client.tag.list_by_operation(resource_group_name=resource_group, service_name=name)
    elif resource_group is not None and name is not None:
        return client.tag.list_by_product(resource_group_name=resource_group, service_name=name)
    elif resource_group is not None and name is not None:
        return client.tag.list_by_api(resource_group_name=resource_group, service_name=name)
    else:
        return client.tag.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementtag
def show_apimgmt_tag(cmd, client,
                     resource_group,
                     name,
                     tag_id):
    return client.tag.get(resource_group_name=resource_group, service_name=name, tag_id=tag_id)

# module equivalent: azure_rm_apimanagementapipolicy
def create_apimgmt_api_policy(cmd, client,
                              resource_group,
                              name,
                              api_id,
                              policy_id,
                              parameters=None):
    body={}
    return client.api_policy.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementapipolicy
def update_apimgmt_api_policy(cmd, client,
                              resource_group,
                              name,
                              api_id,
                              policy_id,
                              parameters=None):
    body={}
    return client.api_policy.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementapipolicy
def delete_apimgmt_api_policy(cmd, client,
                              resource_group,
                              name,
                              api_id,
                              policy_id):
    return client.api_policy.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, policy_id=policy_id)

# module equivalent: azure_rm_apimanagementapipolicy
def list_apimgmt_api_policy(cmd, client,
                            resource_group,
                            name,
                            api_id):
    return client.api_policy.list_by_api(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapipolicy
def show_apimgmt_api_policy(cmd, client,
                            resource_group,
                            name,
                            api_id,
                            policy_id,
                            format=None):
    return client.api_policy.get(resource_group_name=resource_group, service_name=name, api_id=api_id, policy_id=policy_id, format=format)

# module equivalent: azure_rm_apimanagementapischema
def create_apimgmt_api_schema(cmd, client,
                              resource_group,
                              name,
                              api_id,
                              schema_id,
                              parameters=None):
    body={}
    return client.api_schema.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, schema_id=schema_id, parameters=body)

# module equivalent: azure_rm_apimanagementapischema
def update_apimgmt_api_schema(cmd, client,
                              resource_group,
                              name,
                              api_id,
                              schema_id,
                              parameters=None):
    body={}
    return client.api_schema.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, schema_id=schema_id, parameters=body)

# module equivalent: azure_rm_apimanagementapischema
def delete_apimgmt_api_schema(cmd, client,
                              resource_group,
                              name,
                              api_id,
                              schema_id):
    return client.api_schema.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, schema_id=schema_id)

# module equivalent: azure_rm_apimanagementapischema
def list_apimgmt_api_schema(cmd, client,
                            resource_group,
                            name,
                            api_id):
    return client.api_schema.list_by_api(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapischema
def show_apimgmt_api_schema(cmd, client,
                            resource_group,
                            name,
                            api_id,
                            schema_id):
    return client.api_schema.get(resource_group_name=resource_group, service_name=name, api_id=api_id, schema_id=schema_id)

# module equivalent: azure_rm_apimanagementapidiagnostic
def create_apimgmt_api_diagnostic(cmd, client,
                                  resource_group,
                                  name,
                                  api_id,
                                  diagnostic_id,
                                  parameters=None):
    body={}
    return client.api_diagnostic.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, diagnostic_id=diagnostic_id, parameters=body)

# module equivalent: azure_rm_apimanagementapidiagnostic
def update_apimgmt_api_diagnostic(cmd, client,
                                  resource_group,
                                  name,
                                  api_id,
                                  diagnostic_id,
                                  parameters=None):
    body={}
    return client.api_diagnostic.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, diagnostic_id=diagnostic_id, parameters=body)

# module equivalent: azure_rm_apimanagementapidiagnostic
def delete_apimgmt_api_diagnostic(cmd, client,
                                  resource_group,
                                  name,
                                  api_id,
                                  diagnostic_id):
    return client.api_diagnostic.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, diagnostic_id=diagnostic_id)

# module equivalent: azure_rm_apimanagementapidiagnostic
def list_apimgmt_api_diagnostic(cmd, client,
                                resource_group,
                                name,
                                api_id):
    return client.api_diagnostic.list_by_service(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapidiagnostic
def show_apimgmt_api_diagnostic(cmd, client,
                                resource_group,
                                name,
                                api_id,
                                diagnostic_id):
    return client.api_diagnostic.get(resource_group_name=resource_group, service_name=name, api_id=api_id, diagnostic_id=diagnostic_id)

# module equivalent: azure_rm_apimanagementapiissue
def create_apimgmt_api_issue(cmd, client,
                             resource_group,
                             name,
                             api_id,
                             issue_id,
                             parameters=None):
    body={}
    return client.api_issue.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiissue
def update_apimgmt_api_issue(cmd, client,
                             resource_group,
                             name,
                             api_id,
                             issue_id,
                             parameters=None):
    body={}
    return client.api_issue.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiissue
def delete_apimgmt_api_issue(cmd, client,
                             resource_group,
                             name,
                             api_id,
                             issue_id):
    return client.api_issue.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id)

# module equivalent: azure_rm_apimanagementapiissue
def list_apimgmt_api_issue(cmd, client,
                           resource_group,
                           name,
                           api_id):
    return client.api_issue.list_by_service(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapiissue
def show_apimgmt_api_issue(cmd, client,
                           resource_group,
                           name,
                           api_id,
                           issue_id):
    return client.api_issue.get(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id)

# module equivalent: azure_rm_apimanagementapiissuecomment
def create_apimgmt_api_issue_comment(cmd, client,
                                     resource_group,
                                     name,
                                     api_id,
                                     issue_id,
                                     comment_id,
                                     parameters=None):
    body={}
    return client.api_issue_comment.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, comment_id=comment_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiissuecomment
def update_apimgmt_api_issue_comment(cmd, client,
                                     resource_group,
                                     name,
                                     api_id,
                                     issue_id,
                                     comment_id,
                                     parameters=None):
    body={}
    return client.api_issue_comment.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, comment_id=comment_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiissuecomment
def delete_apimgmt_api_issue_comment(cmd, client,
                                     resource_group,
                                     name,
                                     api_id,
                                     issue_id,
                                     comment_id):
    return client.api_issue_comment.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, comment_id=comment_id)

# module equivalent: azure_rm_apimanagementapiissuecomment
def list_apimgmt_api_issue_comment(cmd, client,
                                   resource_group,
                                   name,
                                   api_id,
                                   issue_id):
    return client.api_issue_comment.list_by_service(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id)

# module equivalent: azure_rm_apimanagementapiissuecomment
def show_apimgmt_api_issue_comment(cmd, client,
                                   resource_group,
                                   name,
                                   api_id,
                                   issue_id,
                                   comment_id):
    return client.api_issue_comment.get(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, comment_id=comment_id)

# module equivalent: azure_rm_apimanagementapiissueattachment
def create_apimgmt_api_issue_attachment(cmd, client,
                                        resource_group,
                                        name,
                                        api_id,
                                        issue_id,
                                        attachment_id,
                                        parameters=None):
    body={}
    return client.api_issue_attachment.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, attachment_id=attachment_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiissueattachment
def update_apimgmt_api_issue_attachment(cmd, client,
                                        resource_group,
                                        name,
                                        api_id,
                                        issue_id,
                                        attachment_id,
                                        parameters=None):
    body={}
    return client.api_issue_attachment.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, attachment_id=attachment_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiissueattachment
def delete_apimgmt_api_issue_attachment(cmd, client,
                                        resource_group,
                                        name,
                                        api_id,
                                        issue_id,
                                        attachment_id):
    return client.api_issue_attachment.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, attachment_id=attachment_id)

# module equivalent: azure_rm_apimanagementapiissueattachment
def list_apimgmt_api_issue_attachment(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      issue_id):
    return client.api_issue_attachment.list_by_service(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id)

# module equivalent: azure_rm_apimanagementapiissueattachment
def show_apimgmt_api_issue_attachment(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      issue_id,
                                      attachment_id):
    return client.api_issue_attachment.get(resource_group_name=resource_group, service_name=name, api_id=api_id, issue_id=issue_id, attachment_id=attachment_id)

# module equivalent: azure_rm_apimanagementapitagdescription
def create_apimgmt_api_tagdescription(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      tag_id,
                                      parameters=None):
    body={}
    return client.api_tag_description.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, tag_id=tag_id, parameters=body)

# module equivalent: azure_rm_apimanagementapitagdescription
def update_apimgmt_api_tagdescription(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      tag_id,
                                      parameters=None):
    body={}
    return client.api_tag_description.create_or_update(resource_group_name=resource_group, service_name=name, api_id=api_id, tag_id=tag_id, parameters=body)

# module equivalent: azure_rm_apimanagementapitagdescription
def delete_apimgmt_api_tagdescription(cmd, client,
                                      resource_group,
                                      name,
                                      api_id,
                                      tag_id):
    return client.api_tag_description.delete(resource_group_name=resource_group, service_name=name, api_id=api_id, tag_id=tag_id)

# module equivalent: azure_rm_apimanagementapitagdescription
def list_apimgmt_api_tagdescription(cmd, client,
                                    resource_group,
                                    name,
                                    api_id):
    return client.api_tag_description.list_by_service(resource_group_name=resource_group, service_name=name, api_id=api_id)

# module equivalent: azure_rm_apimanagementapitagdescription
def show_apimgmt_api_tagdescription(cmd, client,
                                    resource_group,
                                    name,
                                    api_id,
                                    tag_id):
    return client.api_tag_description.get(resource_group_name=resource_group, service_name=name, api_id=api_id, tag_id=tag_id)

# module equivalent: azure_rm_apimanagementapiversionset
def create_apimgmt_apiversionset(cmd, client,
                                 resource_group,
                                 name,
                                 version_set_id,
                                 parameters=None):
    body={}
    return client.api_version_set.create_or_update(resource_group_name=resource_group, service_name=name, version_set_id=version_set_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiversionset
def update_apimgmt_apiversionset(cmd, client,
                                 resource_group,
                                 name,
                                 version_set_id,
                                 parameters=None):
    body={}
    return client.api_version_set.create_or_update(resource_group_name=resource_group, service_name=name, version_set_id=version_set_id, parameters=body)

# module equivalent: azure_rm_apimanagementapiversionset
def delete_apimgmt_apiversionset(cmd, client,
                                 resource_group,
                                 name,
                                 version_set_id):
    return client.api_version_set.delete(resource_group_name=resource_group, service_name=name, version_set_id=version_set_id)

# module equivalent: azure_rm_apimanagementapiversionset
def list_apimgmt_apiversionset(cmd, client,
                               resource_group,
                               name):
    return client.api_version_set.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementapiversionset
def show_apimgmt_apiversionset(cmd, client,
                               resource_group,
                               name,
                               version_set_id):
    return client.api_version_set.get(resource_group_name=resource_group, service_name=name, version_set_id=version_set_id)

# module equivalent: azure_rm_apimanagementauthorizationserver
def create_apimgmt_authorizationserver(cmd, client,
                                       resource_group,
                                       name,
                                       authsid,
                                       parameters=None):
    body={}
    return client.authorization_server.create_or_update(resource_group_name=resource_group, service_name=name, authsid=authsid, parameters=body)

# module equivalent: azure_rm_apimanagementauthorizationserver
def update_apimgmt_authorizationserver(cmd, client,
                                       resource_group,
                                       name,
                                       authsid,
                                       parameters=None):
    body={}
    return client.authorization_server.create_or_update(resource_group_name=resource_group, service_name=name, authsid=authsid, parameters=body)

# module equivalent: azure_rm_apimanagementauthorizationserver
def delete_apimgmt_authorizationserver(cmd, client,
                                       resource_group,
                                       name,
                                       authsid):
    return client.authorization_server.delete(resource_group_name=resource_group, service_name=name, authsid=authsid)

# module equivalent: azure_rm_apimanagementauthorizationserver
def list_apimgmt_authorizationserver(cmd, client,
                                     resource_group,
                                     name):
    return client.authorization_server.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementauthorizationserver
def show_apimgmt_authorizationserver(cmd, client,
                                     resource_group,
                                     name,
                                     authsid):
    return client.authorization_server.get(resource_group_name=resource_group, service_name=name, authsid=authsid)

# module equivalent: azure_rm_apimanagementbackend
def create_apimgmt_backend(cmd, client,
                           resource_group,
                           name,
                           backend_id,
                           parameters=None):
    body={}
    return client.backend.create_or_update(resource_group_name=resource_group, service_name=name, backend_id=backend_id, parameters=body)

# module equivalent: azure_rm_apimanagementbackend
def update_apimgmt_backend(cmd, client,
                           resource_group,
                           name,
                           backend_id,
                           parameters=None):
    body={}
    return client.backend.create_or_update(resource_group_name=resource_group, service_name=name, backend_id=backend_id, parameters=body)

# module equivalent: azure_rm_apimanagementbackend
def delete_apimgmt_backend(cmd, client,
                           resource_group,
                           name,
                           backend_id):
    return client.backend.delete(resource_group_name=resource_group, service_name=name, backend_id=backend_id)

# module equivalent: azure_rm_apimanagementbackend
def list_apimgmt_backend(cmd, client,
                         resource_group,
                         name):
    return client.backend.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementbackend
def show_apimgmt_backend(cmd, client,
                         resource_group,
                         name,
                         backend_id):
    return client.backend.get(resource_group_name=resource_group, service_name=name, backend_id=backend_id)

# module equivalent: azure_rm_apimanagementcache
def create_apimgmt_cache(cmd, client,
                         resource_group,
                         name,
                         cache_id,
                         parameters=None):
    body={}
    return client.cache.create_or_update(resource_group_name=resource_group, service_name=name, cache_id=cache_id, parameters=body)

# module equivalent: azure_rm_apimanagementcache
def update_apimgmt_cache(cmd, client,
                         resource_group,
                         name,
                         cache_id,
                         parameters=None):
    body={}
    return client.cache.create_or_update(resource_group_name=resource_group, service_name=name, cache_id=cache_id, parameters=body)

# module equivalent: azure_rm_apimanagementcache
def delete_apimgmt_cache(cmd, client,
                         resource_group,
                         name,
                         cache_id):
    return client.cache.delete(resource_group_name=resource_group, service_name=name, cache_id=cache_id)

# module equivalent: azure_rm_apimanagementcache
def list_apimgmt_cache(cmd, client,
                       resource_group,
                       name):
    return client.cache.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementcache
def show_apimgmt_cache(cmd, client,
                       resource_group,
                       name,
                       cache_id):
    return client.cache.get(resource_group_name=resource_group, service_name=name, cache_id=cache_id)

# module equivalent: azure_rm_apimanagementcertificate
def create_apimgmt_certificate(cmd, client,
                               resource_group,
                               name,
                               certificate_id,
                               parameters=None):
    body={}
    return client.certificate.create_or_update(resource_group_name=resource_group, service_name=name, certificate_id=certificate_id, parameters=body)

# module equivalent: azure_rm_apimanagementcertificate
def update_apimgmt_certificate(cmd, client,
                               resource_group,
                               name,
                               certificate_id,
                               parameters=None):
    body={}
    return client.certificate.create_or_update(resource_group_name=resource_group, service_name=name, certificate_id=certificate_id, parameters=body)

# module equivalent: azure_rm_apimanagementcertificate
def delete_apimgmt_certificate(cmd, client,
                               resource_group,
                               name,
                               certificate_id):
    return client.certificate.delete(resource_group_name=resource_group, service_name=name, certificate_id=certificate_id)

# module equivalent: azure_rm_apimanagementcertificate
def list_apimgmt_certificate(cmd, client,
                             resource_group,
                             name):
    return client.certificate.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementcertificate
def show_apimgmt_certificate(cmd, client,
                             resource_group,
                             name,
                             certificate_id):
    return client.certificate.get(resource_group_name=resource_group, service_name=name, certificate_id=certificate_id)

# module equivalent: azure_rm_apimanagementservice
def create_apimgmt(cmd, client,
                   resource_group,
                   name,
                   parameters=None):
    body={}
    return client.api_management_service.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementservice
def update_apimgmt(cmd, client,
                   resource_group,
                   name,
                   parameters=None):
    body={}
    return client.api_management_service.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementservice
def delete_apimgmt(cmd, client,
                   resource_group,
                   name):
    return client.api_management_service.delete(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementservice
def list_apimgmt(cmd, client,
                 resource_group):
    if resource_group is not None:
        return client.api_management_service.list_by_resource_group(resource_group_name=resource_group)
    else:
        return client.api_management_service.list()

# module equivalent: azure_rm_apimanagementservice
def show_apimgmt(cmd, client,
                 resource_group,
                 name):
    return client.api_management_service.get(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementdiagnostic
def create_apimgmt_diagnostic(cmd, client,
                              resource_group,
                              name,
                              diagnostic_id,
                              parameters=None):
    body={}
    return client.diagnostic.create_or_update(resource_group_name=resource_group, service_name=name, diagnostic_id=diagnostic_id, parameters=body)

# module equivalent: azure_rm_apimanagementdiagnostic
def update_apimgmt_diagnostic(cmd, client,
                              resource_group,
                              name,
                              diagnostic_id,
                              parameters=None):
    body={}
    return client.diagnostic.create_or_update(resource_group_name=resource_group, service_name=name, diagnostic_id=diagnostic_id, parameters=body)

# module equivalent: azure_rm_apimanagementdiagnostic
def delete_apimgmt_diagnostic(cmd, client,
                              resource_group,
                              name,
                              diagnostic_id):
    return client.diagnostic.delete(resource_group_name=resource_group, service_name=name, diagnostic_id=diagnostic_id)

# module equivalent: azure_rm_apimanagementdiagnostic
def list_apimgmt_diagnostic(cmd, client,
                            resource_group,
                            name):
    return client.diagnostic.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementdiagnostic
def show_apimgmt_diagnostic(cmd, client,
                            resource_group,
                            name,
                            diagnostic_id):
    return client.diagnostic.get(resource_group_name=resource_group, service_name=name, diagnostic_id=diagnostic_id)

# module equivalent: azure_rm_apimanagementemailtemplate
def create_apimgmt_template(cmd, client,
                            resource_group,
                            service_name,
                            name,
                            parameters=None):
    body={}
    body['parameters'] = parameters
    return client.email_template.create_or_update(resource_group_name=resource_group, service_name=service_name, template_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementemailtemplate
def update_apimgmt_template(cmd, client,
                            resource_group,
                            service_name,
                            name,
                            parameters=None):
    body={}
    body['parameters'] = parameters
    return client.email_template.create_or_update(resource_group_name=resource_group, service_name=service_name, template_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementemailtemplate
def delete_apimgmt_template(cmd, client,
                            resource_group,
                            service_name,
                            name):
    return client.email_template.delete(resource_group_name=resource_group, service_name=service_name, template_name=name)

# module equivalent: azure_rm_apimanagementemailtemplate
def list_apimgmt_template(cmd, client,
                          resource_group,
                          service_name):
    return client.email_template.list_by_service(resource_group_name=resource_group, service_name=service_name)

# module equivalent: azure_rm_apimanagementemailtemplate
def show_apimgmt_template(cmd, client,
                          resource_group,
                          service_name,
                          name):
    return client.email_template.get(resource_group_name=resource_group, service_name=service_name, template_name=name)

# module equivalent: azure_rm_apimanagementgroup
def create_apimgmt_group(cmd, client,
                         resource_group,
                         name,
                         group_id,
                         parameters=None):
    body={}
    return client.group.create_or_update(resource_group_name=resource_group, service_name=name, group_id=group_id, parameters=body)

# module equivalent: azure_rm_apimanagementgroup
def update_apimgmt_group(cmd, client,
                         resource_group,
                         name,
                         group_id,
                         parameters=None):
    body={}
    return client.group.create_or_update(resource_group_name=resource_group, service_name=name, group_id=group_id, parameters=body)

# module equivalent: azure_rm_apimanagementgroup
def delete_apimgmt_group(cmd, client,
                         resource_group,
                         name,
                         group_id):
    return client.group.delete(resource_group_name=resource_group, service_name=name, group_id=group_id)

# module equivalent: azure_rm_apimanagementgroup
def list_apimgmt_group(cmd, client,
                       resource_group,
                       name):
    return client.group.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementgroup
def show_apimgmt_group(cmd, client,
                       resource_group,
                       name,
                       group_id):
    return client.group.get(resource_group_name=resource_group, service_name=name, group_id=group_id)

# module equivalent: azure_rm_apimanagementgroupuser
def create_apimgmt_group_user(cmd, client,
                              resource_group,
                              name,
                              group_id,
                              user_id):
    body={}
    return client.group_user.create(resource_group_name=resource_group, service_name=name, group_id=group_id, user_id=user_id)

# module equivalent: azure_rm_apimanagementgroupuser
def delete_apimgmt_group_user(cmd, client,
                              resource_group,
                              name,
                              group_id,
                              user_id):
    return client.group_user.delete(resource_group_name=resource_group, service_name=name, group_id=group_id, user_id=user_id)

# module equivalent: azure_rm_apimanagementgroupuser
def list_apimgmt_group_user(cmd, client,
                            resource_group,
                            name,
                            group_id):
    return client.group_user.list(resource_group_name=resource_group, service_name=name, group_id=group_id)

# module equivalent: azure_rm_apimanagementidentityprovider
def create_apimgmt_identityprovider(cmd, client,
                                    resource_group,
                                    service_name,
                                    name,
                                    parameters=None):
    body={}
    return client.identity_provider.create_or_update(resource_group_name=resource_group, service_name=service_name, identity_provider_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementidentityprovider
def update_apimgmt_identityprovider(cmd, client,
                                    resource_group,
                                    service_name,
                                    name,
                                    parameters=None):
    body={}
    return client.identity_provider.create_or_update(resource_group_name=resource_group, service_name=service_name, identity_provider_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementidentityprovider
def delete_apimgmt_identityprovider(cmd, client,
                                    resource_group,
                                    service_name,
                                    name):
    return client.identity_provider.delete(resource_group_name=resource_group, service_name=service_name, identity_provider_name=name)

# module equivalent: azure_rm_apimanagementidentityprovider
def list_apimgmt_identityprovider(cmd, client,
                                  resource_group,
                                  service_name):
    return client.identity_provider.list_by_service(resource_group_name=resource_group, service_name=service_name)

# module equivalent: azure_rm_apimanagementidentityprovider
def show_apimgmt_identityprovider(cmd, client,
                                  resource_group,
                                  service_name,
                                  name):
    return client.identity_provider.get(resource_group_name=resource_group, service_name=service_name, identity_provider_name=name)

# module equivalent: azure_rm_apimanagementlogger
def create_apimgmt_logger(cmd, client,
                          resource_group,
                          name,
                          logger_id,
                          parameters=None):
    body={}
    return client.logger.create_or_update(resource_group_name=resource_group, service_name=name, logger_id=logger_id, parameters=body)

# module equivalent: azure_rm_apimanagementlogger
def update_apimgmt_logger(cmd, client,
                          resource_group,
                          name,
                          logger_id,
                          parameters=None):
    body={}
    return client.logger.create_or_update(resource_group_name=resource_group, service_name=name, logger_id=logger_id, parameters=body)

# module equivalent: azure_rm_apimanagementlogger
def delete_apimgmt_logger(cmd, client,
                          resource_group,
                          name,
                          logger_id):
    return client.logger.delete(resource_group_name=resource_group, service_name=name, logger_id=logger_id)

# module equivalent: azure_rm_apimanagementlogger
def list_apimgmt_logger(cmd, client,
                        resource_group,
                        name):
    return client.logger.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementlogger
def show_apimgmt_logger(cmd, client,
                        resource_group,
                        name,
                        logger_id):
    return client.logger.get(resource_group_name=resource_group, service_name=name, logger_id=logger_id)

# module equivalent: azure_rm_apimanagementnotification
def create_apimgmt_notification(cmd, client,
                                resource_group,
                                service_name,
                                name):
    body={}
    return client.notification.create_or_update(resource_group_name=resource_group, service_name=service_name, notification_name=name)

# module equivalent: azure_rm_apimanagementnotification
def update_apimgmt_notification(cmd, client,
                                resource_group,
                                service_name,
                                name):
    body={}
    return client.notification.create_or_update(resource_group_name=resource_group, service_name=service_name, notification_name=name)

# module equivalent: azure_rm_apimanagementnotification
def list_apimgmt_notification(cmd, client,
                              resource_group,
                              service_name):
    return client.notification.list_by_service(resource_group_name=resource_group, service_name=service_name)

# module equivalent: azure_rm_apimanagementnotification
def show_apimgmt_notification(cmd, client,
                              resource_group,
                              service_name,
                              name):
    return client.notification.get(resource_group_name=resource_group, service_name=service_name, notification_name=name)

# module equivalent: azure_rm_apimanagementnotificationrecipientuser
def create_apimgmt_notification_recipientuser(cmd, client,
                                              resource_group,
                                              service_name,
                                              name,
                                              user_id):
    body={}
    return client.notification_recipient_user.create_or_update(resource_group_name=resource_group, service_name=service_name, notification_name=name, user_id=user_id)

# module equivalent: azure_rm_apimanagementnotificationrecipientuser
def update_apimgmt_notification_recipientuser(cmd, client,
                                              resource_group,
                                              service_name,
                                              name,
                                              user_id):
    body={}
    return client.notification_recipient_user.create_or_update(resource_group_name=resource_group, service_name=service_name, notification_name=name, user_id=user_id)

# module equivalent: azure_rm_apimanagementnotificationrecipientuser
def delete_apimgmt_notification_recipientuser(cmd, client,
                                              resource_group,
                                              service_name,
                                              name,
                                              user_id):
    return client.notification_recipient_user.delete(resource_group_name=resource_group, service_name=service_name, notification_name=name, user_id=user_id)

# module equivalent: azure_rm_apimanagementnotificationrecipientuser
def list_apimgmt_notification_recipientuser(cmd, client,
                                            resource_group,
                                            service_name,
                                            name):
    return client.notification_recipient_user.list_by_notification(resource_group_name=resource_group, service_name=service_name, notification_name=name)

# module equivalent: azure_rm_apimanagementnotificationrecipientemail
def create_apimgmt_notification_recipientemail(cmd, client,
                                               resource_group,
                                               service_name,
                                               name,
                                               email):
    body={}
    return client.notification_recipient_email.create_or_update(resource_group_name=resource_group, service_name=service_name, notification_name=name, email=email)

# module equivalent: azure_rm_apimanagementnotificationrecipientemail
def update_apimgmt_notification_recipientemail(cmd, client,
                                               resource_group,
                                               service_name,
                                               name,
                                               email):
    body={}
    return client.notification_recipient_email.create_or_update(resource_group_name=resource_group, service_name=service_name, notification_name=name, email=email)

# module equivalent: azure_rm_apimanagementnotificationrecipientemail
def delete_apimgmt_notification_recipientemail(cmd, client,
                                               resource_group,
                                               service_name,
                                               name,
                                               email):
    return client.notification_recipient_email.delete(resource_group_name=resource_group, service_name=service_name, notification_name=name, email=email)

# module equivalent: azure_rm_apimanagementnotificationrecipientemail
def list_apimgmt_notification_recipientemail(cmd, client,
                                             resource_group,
                                             service_name,
                                             name):
    return client.notification_recipient_email.list_by_notification(resource_group_name=resource_group, service_name=service_name, notification_name=name)

# module equivalent: azure_rm_apimanagementopenidconnectprovider
def create_apimgmt_openidconnectprovider(cmd, client,
                                         resource_group,
                                         name,
                                         opid,
                                         parameters=None):
    body={}
    return client.open_id_connect_provider.create_or_update(resource_group_name=resource_group, service_name=name, opid=opid, parameters=body)

# module equivalent: azure_rm_apimanagementopenidconnectprovider
def update_apimgmt_openidconnectprovider(cmd, client,
                                         resource_group,
                                         name,
                                         opid,
                                         parameters=None):
    body={}
    return client.open_id_connect_provider.create_or_update(resource_group_name=resource_group, service_name=name, opid=opid, parameters=body)

# module equivalent: azure_rm_apimanagementopenidconnectprovider
def delete_apimgmt_openidconnectprovider(cmd, client,
                                         resource_group,
                                         name,
                                         opid):
    return client.open_id_connect_provider.delete(resource_group_name=resource_group, service_name=name, opid=opid)

# module equivalent: azure_rm_apimanagementopenidconnectprovider
def list_apimgmt_openidconnectprovider(cmd, client,
                                       resource_group,
                                       name):
    return client.open_id_connect_provider.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementopenidconnectprovider
def show_apimgmt_openidconnectprovider(cmd, client,
                                       resource_group,
                                       name,
                                       opid):
    return client.open_id_connect_provider.get(resource_group_name=resource_group, service_name=name, opid=opid)

# module equivalent: azure_rm_apimanagementpolicy
def create_apimgmt_policy(cmd, client,
                          resource_group,
                          name,
                          policy_id,
                          parameters=None):
    body={}
    return client.policy.create_or_update(resource_group_name=resource_group, service_name=name, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementpolicy
def update_apimgmt_policy(cmd, client,
                          resource_group,
                          name,
                          policy_id,
                          parameters=None):
    body={}
    return client.policy.create_or_update(resource_group_name=resource_group, service_name=name, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementpolicy
def delete_apimgmt_policy(cmd, client,
                          resource_group,
                          name,
                          policy_id):
    return client.policy.delete(resource_group_name=resource_group, service_name=name, policy_id=policy_id)

# module equivalent: azure_rm_apimanagementpolicy
def list_apimgmt_policy(cmd, client,
                        resource_group,
                        name):
    return client.policy.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementpolicy
def show_apimgmt_policy(cmd, client,
                        resource_group,
                        name,
                        policy_id,
                        format=None):
    return client.policy.get(resource_group_name=resource_group, service_name=name, policy_id=policy_id, format=format)

# module equivalent: azure_rm_apimanagementsigninsetting
def create_apimgmt_portalsetting(cmd, client,
                                 resource_group,
                                 name,
                                 parameters=None):
    body={}
    return client.sign_in_settings.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementsigninsetting
def update_apimgmt_portalsetting(cmd, client,
                                 resource_group,
                                 name,
                                 parameters=None):
    body={}
    return client.sign_in_settings.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementsigninsetting
def show_apimgmt_portalsetting(cmd, client,
                               resource_group,
                               name):
    return client.sign_in_settings.get(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementsignupsetting
def create_apimgmt_portalsetting(cmd, client,
                                 resource_group,
                                 name,
                                 parameters=None):
    body={}
    return client.sign_up_settings.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementsignupsetting
def update_apimgmt_portalsetting(cmd, client,
                                 resource_group,
                                 name,
                                 parameters=None):
    body={}
    return client.sign_up_settings.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementsignupsetting
def show_apimgmt_portalsetting(cmd, client,
                               resource_group,
                               name):
    return client.sign_up_settings.get(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementdelegationsetting
def create_apimgmt_portalsetting(cmd, client,
                                 resource_group,
                                 name,
                                 parameters=None):
    body={}
    return client.delegation_settings.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementdelegationsetting
def update_apimgmt_portalsetting(cmd, client,
                                 resource_group,
                                 name,
                                 parameters=None):
    body={}
    return client.delegation_settings.create_or_update(resource_group_name=resource_group, service_name=name, parameters=body)

# module equivalent: azure_rm_apimanagementdelegationsetting
def show_apimgmt_portalsetting(cmd, client,
                               resource_group,
                               name):
    return client.delegation_settings.get(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementproduct
def create_apimgmt_product(cmd, client,
                           resource_group,
                           name,
                           product_id,
                           parameters=None):
    body={}
    return client.product.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, parameters=body)

# module equivalent: azure_rm_apimanagementproduct
def update_apimgmt_product(cmd, client,
                           resource_group,
                           name,
                           product_id,
                           parameters=None):
    body={}
    return client.product.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, parameters=body)

# module equivalent: azure_rm_apimanagementproduct
def delete_apimgmt_product(cmd, client,
                           resource_group,
                           name,
                           product_id):
    return client.product.delete(resource_group_name=resource_group, service_name=name, product_id=product_id)

# module equivalent: azure_rm_apimanagementproduct
def list_apimgmt_product(cmd, client,
                         resource_group,
                         name):
    if resource_group is not None and name is not None:
        return client.product.list_by_tags(resource_group_name=resource_group, service_name=name)
    else:
        return client.product.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementproduct
def show_apimgmt_product(cmd, client,
                         resource_group,
                         name,
                         product_id):
    return client.product.get(resource_group_name=resource_group, service_name=name, product_id=product_id)

# module equivalent: azure_rm_apimanagementproductapi
def create_apimgmt_product_api(cmd, client,
                               resource_group,
                               name,
                               product_id,
                               api_id):
    body={}
    return client.product_api.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, api_id=api_id)

# module equivalent: azure_rm_apimanagementproductapi
def update_apimgmt_product_api(cmd, client,
                               resource_group,
                               name,
                               product_id,
                               api_id):
    body={}
    return client.product_api.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, api_id=api_id)

# module equivalent: azure_rm_apimanagementproductapi
def delete_apimgmt_product_api(cmd, client,
                               resource_group,
                               name,
                               product_id,
                               api_id):
    return client.product_api.delete(resource_group_name=resource_group, service_name=name, product_id=product_id, api_id=api_id)

# module equivalent: azure_rm_apimanagementproductapi
def list_apimgmt_product_api(cmd, client,
                             resource_group,
                             name,
                             product_id):
    return client.product_api.list_by_product(resource_group_name=resource_group, service_name=name, product_id=product_id)

# module equivalent: azure_rm_apimanagementproductgroup
def create_apimgmt_product_group(cmd, client,
                                 resource_group,
                                 name,
                                 product_id,
                                 group_id):
    body={}
    return client.product_group.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, group_id=group_id)

# module equivalent: azure_rm_apimanagementproductgroup
def update_apimgmt_product_group(cmd, client,
                                 resource_group,
                                 name,
                                 product_id,
                                 group_id):
    body={}
    return client.product_group.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, group_id=group_id)

# module equivalent: azure_rm_apimanagementproductgroup
def delete_apimgmt_product_group(cmd, client,
                                 resource_group,
                                 name,
                                 product_id,
                                 group_id):
    return client.product_group.delete(resource_group_name=resource_group, service_name=name, product_id=product_id, group_id=group_id)

# module equivalent: azure_rm_apimanagementproductgroup
def list_apimgmt_product_group(cmd, client,
                               resource_group,
                               name,
                               product_id):
    return client.product_group.list_by_product(resource_group_name=resource_group, service_name=name, product_id=product_id)

# module equivalent: azure_rm_apimanagementproductpolicy
def create_apimgmt_product_policy(cmd, client,
                                  resource_group,
                                  name,
                                  product_id,
                                  policy_id,
                                  parameters=None):
    body={}
    return client.product_policy.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementproductpolicy
def update_apimgmt_product_policy(cmd, client,
                                  resource_group,
                                  name,
                                  product_id,
                                  policy_id,
                                  parameters=None):
    body={}
    return client.product_policy.create_or_update(resource_group_name=resource_group, service_name=name, product_id=product_id, policy_id=policy_id, parameters=body)

# module equivalent: azure_rm_apimanagementproductpolicy
def delete_apimgmt_product_policy(cmd, client,
                                  resource_group,
                                  name,
                                  product_id,
                                  policy_id):
    return client.product_policy.delete(resource_group_name=resource_group, service_name=name, product_id=product_id, policy_id=policy_id)

# module equivalent: azure_rm_apimanagementproductpolicy
def list_apimgmt_product_policy(cmd, client,
                                resource_group,
                                name,
                                product_id):
    return client.product_policy.list_by_product(resource_group_name=resource_group, service_name=name, product_id=product_id)

# module equivalent: azure_rm_apimanagementproductpolicy
def show_apimgmt_product_policy(cmd, client,
                                resource_group,
                                name,
                                product_id,
                                policy_id,
                                format=None):
    return client.product_policy.get(resource_group_name=resource_group, service_name=name, product_id=product_id, policy_id=policy_id, format=format)

# module equivalent: azure_rm_apimanagementproperty
def create_apimgmt_property(cmd, client,
                            resource_group,
                            name,
                            prop_id,
                            parameters=None):
    body={}
    return client.property.create_or_update(resource_group_name=resource_group, service_name=name, prop_id=prop_id, parameters=body)

# module equivalent: azure_rm_apimanagementproperty
def update_apimgmt_property(cmd, client,
                            resource_group,
                            name,
                            prop_id,
                            parameters=None):
    body={}
    return client.property.create_or_update(resource_group_name=resource_group, service_name=name, prop_id=prop_id, parameters=body)

# module equivalent: azure_rm_apimanagementproperty
def delete_apimgmt_property(cmd, client,
                            resource_group,
                            name,
                            prop_id):
    return client.property.delete(resource_group_name=resource_group, service_name=name, prop_id=prop_id)

# module equivalent: azure_rm_apimanagementproperty
def list_apimgmt_property(cmd, client,
                          resource_group,
                          name):
    return client.property.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementproperty
def show_apimgmt_property(cmd, client,
                          resource_group,
                          name,
                          prop_id):
    return client.property.get(resource_group_name=resource_group, service_name=name, prop_id=prop_id)

# module equivalent: azure_rm_apimanagementsubscription
def create_apimgmt_subscription(cmd, client,
                                resource_group,
                                name,
                                sid,
                                parameters=None,
                                notify=None):
    body={}
    return client.subscription.create_or_update(resource_group_name=resource_group, service_name=name, sid=sid, parameters=body, notify=notify)

# module equivalent: azure_rm_apimanagementsubscription
def update_apimgmt_subscription(cmd, client,
                                resource_group,
                                name,
                                sid,
                                parameters=None,
                                notify=None):
    body={}
    return client.subscription.create_or_update(resource_group_name=resource_group, service_name=name, sid=sid, parameters=body, notify=notify)

# module equivalent: azure_rm_apimanagementsubscription
def delete_apimgmt_subscription(cmd, client,
                                resource_group,
                                name,
                                sid):
    return client.subscription.delete(resource_group_name=resource_group, service_name=name, sid=sid)

# module equivalent: azure_rm_apimanagementsubscription
def list_apimgmt_subscription(cmd, client,
                              resource_group,
                              name):
    return client.subscription.list(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementsubscription
def show_apimgmt_subscription(cmd, client,
                              resource_group,
                              name,
                              sid):
    return client.subscription.get(resource_group_name=resource_group, service_name=name, sid=sid)

# module equivalent: azure_rm_apimanagementuser
def create_apimgmt_user(cmd, client,
                        resource_group,
                        name,
                        user_id,
                        parameters=None):
    body={}
    return client.user.create_or_update(resource_group_name=resource_group, service_name=name, user_id=user_id, parameters=body)

# module equivalent: azure_rm_apimanagementuser
def update_apimgmt_user(cmd, client,
                        resource_group,
                        name,
                        user_id,
                        parameters=None):
    body={}
    return client.user.create_or_update(resource_group_name=resource_group, service_name=name, user_id=user_id, parameters=body)

# module equivalent: azure_rm_apimanagementuser
def delete_apimgmt_user(cmd, client,
                        resource_group,
                        name,
                        user_id):
    return client.user.delete(resource_group_name=resource_group, service_name=name, user_id=user_id)

# module equivalent: azure_rm_apimanagementuser
def list_apimgmt_user(cmd, client,
                      resource_group,
                      name):
    return client.user.list_by_service(resource_group_name=resource_group, service_name=name)

# module equivalent: azure_rm_apimanagementuser
def show_apimgmt_user(cmd, client,
                      resource_group,
                      name,
                      user_id):
    return client.user.get(resource_group_name=resource_group, service_name=name, user_id=user_id)