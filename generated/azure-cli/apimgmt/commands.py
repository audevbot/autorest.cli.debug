# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.apimgmt._client_factory import cf_apimgmt
def load_command_table(self, _):

    apimgmt_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimgmt.operations#ApiManagementOperations.{}',
        client_factory=cf_apimgmt)


    with self.command_group('apimgmt service api', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api')
        g.custom_command('update', 'update_apimgmt_service_api')
        g.custom_command('delete', 'delete_apimgmt_service_api')
        g.custom_command('list', 'list_apimgmt_service_api')
        g.custom_command('show', 'show_apimgmt_service_api')
    with self.command_group('apimgmt service api release', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_release')
        g.custom_command('update', 'update_apimgmt_service_api_release')
        g.custom_command('delete', 'delete_apimgmt_service_api_release')
        g.custom_command('list', 'list_apimgmt_service_api_release')
        g.custom_command('show', 'show_apimgmt_service_api_release')
    with self.command_group('apimgmt service api operation', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_operation')
        g.custom_command('update', 'update_apimgmt_service_api_operation')
        g.custom_command('delete', 'delete_apimgmt_service_api_operation')
        g.custom_command('list', 'list_apimgmt_service_api_operation')
        g.custom_command('show', 'show_apimgmt_service_api_operation')
    with self.command_group('apimgmt service api operation policy', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_operation_policy')
        g.custom_command('update', 'update_apimgmt_service_api_operation_policy')
        g.custom_command('delete', 'delete_apimgmt_service_api_operation_policy')
        g.custom_command('list', 'list_apimgmt_service_api_operation_policy')
        g.custom_command('show', 'show_apimgmt_service_api_operation_policy')
    with self.command_group('apimgmt service tag', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_tag')
        g.custom_command('update', 'update_apimgmt_service_tag')
        g.custom_command('delete', 'delete_apimgmt_service_tag')
        g.custom_command('list', 'list_apimgmt_service_tag')
        g.custom_command('show', 'show_apimgmt_service_tag')
    with self.command_group('apimgmt service api policy', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_policy')
        g.custom_command('update', 'update_apimgmt_service_api_policy')
        g.custom_command('delete', 'delete_apimgmt_service_api_policy')
        g.custom_command('list', 'list_apimgmt_service_api_policy')
        g.custom_command('show', 'show_apimgmt_service_api_policy')
    with self.command_group('apimgmt service api schema', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_schema')
        g.custom_command('update', 'update_apimgmt_service_api_schema')
        g.custom_command('delete', 'delete_apimgmt_service_api_schema')
        g.custom_command('list', 'list_apimgmt_service_api_schema')
        g.custom_command('show', 'show_apimgmt_service_api_schema')
    with self.command_group('apimgmt service api diagnostic', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_diagnostic')
        g.custom_command('update', 'update_apimgmt_service_api_diagnostic')
        g.custom_command('delete', 'delete_apimgmt_service_api_diagnostic')
        g.custom_command('list', 'list_apimgmt_service_api_diagnostic')
        g.custom_command('show', 'show_apimgmt_service_api_diagnostic')
    with self.command_group('apimgmt service api issue', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_issue')
        g.custom_command('update', 'update_apimgmt_service_api_issue')
        g.custom_command('delete', 'delete_apimgmt_service_api_issue')
        g.custom_command('list', 'list_apimgmt_service_api_issue')
        g.custom_command('show', 'show_apimgmt_service_api_issue')
    with self.command_group('apimgmt service api issue comment', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_issue_comment')
        g.custom_command('update', 'update_apimgmt_service_api_issue_comment')
        g.custom_command('delete', 'delete_apimgmt_service_api_issue_comment')
        g.custom_command('list', 'list_apimgmt_service_api_issue_comment')
        g.custom_command('show', 'show_apimgmt_service_api_issue_comment')
    with self.command_group('apimgmt service api issue attachment', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_issue_attachment')
        g.custom_command('update', 'update_apimgmt_service_api_issue_attachment')
        g.custom_command('delete', 'delete_apimgmt_service_api_issue_attachment')
        g.custom_command('list', 'list_apimgmt_service_api_issue_attachment')
        g.custom_command('show', 'show_apimgmt_service_api_issue_attachment')
    with self.command_group('apimgmt service api tagdescription', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_api_tagdescription')
        g.custom_command('update', 'update_apimgmt_service_api_tagdescription')
        g.custom_command('delete', 'delete_apimgmt_service_api_tagdescription')
        g.custom_command('list', 'list_apimgmt_service_api_tagdescription')
        g.custom_command('show', 'show_apimgmt_service_api_tagdescription')
    with self.command_group('apimgmt service apiversionset', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_apiversionset')
        g.custom_command('update', 'update_apimgmt_service_apiversionset')
        g.custom_command('delete', 'delete_apimgmt_service_apiversionset')
        g.custom_command('list', 'list_apimgmt_service_apiversionset')
        g.custom_command('show', 'show_apimgmt_service_apiversionset')
    with self.command_group('apimgmt service authorizationserver', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_authorizationserver')
        g.custom_command('update', 'update_apimgmt_service_authorizationserver')
        g.custom_command('delete', 'delete_apimgmt_service_authorizationserver')
        g.custom_command('list', 'list_apimgmt_service_authorizationserver')
        g.custom_command('show', 'show_apimgmt_service_authorizationserver')
    with self.command_group('apimgmt service backend', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_backend')
        g.custom_command('update', 'update_apimgmt_service_backend')
        g.custom_command('delete', 'delete_apimgmt_service_backend')
        g.custom_command('list', 'list_apimgmt_service_backend')
        g.custom_command('show', 'show_apimgmt_service_backend')
    with self.command_group('apimgmt service cache', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_cache')
        g.custom_command('update', 'update_apimgmt_service_cache')
        g.custom_command('delete', 'delete_apimgmt_service_cache')
        g.custom_command('list', 'list_apimgmt_service_cache')
        g.custom_command('show', 'show_apimgmt_service_cache')
    with self.command_group('apimgmt service certificate', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_certificate')
        g.custom_command('update', 'update_apimgmt_service_certificate')
        g.custom_command('delete', 'delete_apimgmt_service_certificate')
        g.custom_command('list', 'list_apimgmt_service_certificate')
        g.custom_command('show', 'show_apimgmt_service_certificate')
    with self.command_group('apimgmt service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service')
        g.custom_command('update', 'update_apimgmt_service')
        g.custom_command('delete', 'delete_apimgmt_service')
        g.custom_command('list', 'list_apimgmt_service')
        g.custom_command('show', 'show_apimgmt_service')
    with self.command_group('apimgmt service diagnostic', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_diagnostic')
        g.custom_command('update', 'update_apimgmt_service_diagnostic')
        g.custom_command('delete', 'delete_apimgmt_service_diagnostic')
        g.custom_command('list', 'list_apimgmt_service_diagnostic')
        g.custom_command('show', 'show_apimgmt_service_diagnostic')
    with self.command_group('apimgmt service template', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_template')
        g.custom_command('update', 'update_apimgmt_service_template')
        g.custom_command('delete', 'delete_apimgmt_service_template')
        g.custom_command('list', 'list_apimgmt_service_template')
        g.custom_command('show', 'show_apimgmt_service_template')
    with self.command_group('apimgmt service group', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_group')
        g.custom_command('update', 'update_apimgmt_service_group')
        g.custom_command('delete', 'delete_apimgmt_service_group')
        g.custom_command('list', 'list_apimgmt_service_group')
        g.custom_command('show', 'show_apimgmt_service_group')
    with self.command_group('apimgmt service group user', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_group_user')
        g.custom_command('delete', 'delete_apimgmt_service_group_user')
        g.custom_command('list', 'list_apimgmt_service_group_user')
    with self.command_group('apimgmt service identityprovider', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_identityprovider')
        g.custom_command('update', 'update_apimgmt_service_identityprovider')
        g.custom_command('delete', 'delete_apimgmt_service_identityprovider')
        g.custom_command('list', 'list_apimgmt_service_identityprovider')
        g.custom_command('show', 'show_apimgmt_service_identityprovider')
    with self.command_group('apimgmt service logger', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_logger')
        g.custom_command('update', 'update_apimgmt_service_logger')
        g.custom_command('delete', 'delete_apimgmt_service_logger')
        g.custom_command('list', 'list_apimgmt_service_logger')
        g.custom_command('show', 'show_apimgmt_service_logger')
    with self.command_group('apimgmt service notification', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_notification')
        g.custom_command('update', 'update_apimgmt_service_notification')
        g.custom_command('list', 'list_apimgmt_service_notification')
        g.custom_command('show', 'show_apimgmt_service_notification')
    with self.command_group('apimgmt service notification recipientuser', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_notification_recipientuser')
        g.custom_command('update', 'update_apimgmt_service_notification_recipientuser')
        g.custom_command('delete', 'delete_apimgmt_service_notification_recipientuser')
        g.custom_command('list', 'list_apimgmt_service_notification_recipientuser')
    with self.command_group('apimgmt service notification recipientemail', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_notification_recipientemail')
        g.custom_command('update', 'update_apimgmt_service_notification_recipientemail')
        g.custom_command('delete', 'delete_apimgmt_service_notification_recipientemail')
        g.custom_command('list', 'list_apimgmt_service_notification_recipientemail')
    with self.command_group('apimgmt service openidconnectprovider', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_openidconnectprovider')
        g.custom_command('update', 'update_apimgmt_service_openidconnectprovider')
        g.custom_command('delete', 'delete_apimgmt_service_openidconnectprovider')
        g.custom_command('list', 'list_apimgmt_service_openidconnectprovider')
        g.custom_command('show', 'show_apimgmt_service_openidconnectprovider')
    with self.command_group('apimgmt service policy', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_policy')
        g.custom_command('update', 'update_apimgmt_service_policy')
        g.custom_command('delete', 'delete_apimgmt_service_policy')
        g.custom_command('list', 'list_apimgmt_service_policy')
        g.custom_command('show', 'show_apimgmt_service_policy')
    with self.command_group('apimgmt service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service')
        g.custom_command('update', 'update_apimgmt_service')
        g.custom_command('show', 'show_apimgmt_service')
    with self.command_group('apimgmt service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service')
        g.custom_command('update', 'update_apimgmt_service')
        g.custom_command('show', 'show_apimgmt_service')
    with self.command_group('apimgmt service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service')
        g.custom_command('update', 'update_apimgmt_service')
        g.custom_command('show', 'show_apimgmt_service')
    with self.command_group('apimgmt service product', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_product')
        g.custom_command('update', 'update_apimgmt_service_product')
        g.custom_command('delete', 'delete_apimgmt_service_product')
        g.custom_command('list', 'list_apimgmt_service_product')
        g.custom_command('show', 'show_apimgmt_service_product')
    with self.command_group('apimgmt service product api', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_product_api')
        g.custom_command('update', 'update_apimgmt_service_product_api')
        g.custom_command('delete', 'delete_apimgmt_service_product_api')
        g.custom_command('list', 'list_apimgmt_service_product_api')
    with self.command_group('apimgmt service product group', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_product_group')
        g.custom_command('update', 'update_apimgmt_service_product_group')
        g.custom_command('delete', 'delete_apimgmt_service_product_group')
        g.custom_command('list', 'list_apimgmt_service_product_group')
    with self.command_group('apimgmt service product policy', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_product_policy')
        g.custom_command('update', 'update_apimgmt_service_product_policy')
        g.custom_command('delete', 'delete_apimgmt_service_product_policy')
        g.custom_command('list', 'list_apimgmt_service_product_policy')
        g.custom_command('show', 'show_apimgmt_service_product_policy')
    with self.command_group('apimgmt service property', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_property')
        g.custom_command('update', 'update_apimgmt_service_property')
        g.custom_command('delete', 'delete_apimgmt_service_property')
        g.custom_command('list', 'list_apimgmt_service_property')
        g.custom_command('show', 'show_apimgmt_service_property')
    with self.command_group('apimgmt service subscription', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_subscription')
        g.custom_command('update', 'update_apimgmt_service_subscription')
        g.custom_command('delete', 'delete_apimgmt_service_subscription')
        g.custom_command('list', 'list_apimgmt_service_subscription')
        g.custom_command('show', 'show_apimgmt_service_subscription')
    with self.command_group('apimgmt service user', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_apimgmt_service_user')
        g.custom_command('update', 'update_apimgmt_service_user')
        g.custom_command('delete', 'delete_apimgmt_service_user')
        g.custom_command('list', 'list_apimgmt_service_user')
        g.custom_command('show', 'show_apimgmt_service_user')