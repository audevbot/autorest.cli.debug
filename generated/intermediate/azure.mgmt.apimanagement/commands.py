# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.apimanagement._client_factory import cf_apimanagement
def load_command_table(self, _):

    apimanagement_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#ApiManagementOperations.{}',
        client_factory=cf_apimanagement)


    with self.command_group('service apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis')
        g.custom_command('update', 'update_service_apis')
        g.custom_command('delete', 'delete_service_apis')
        g.custom_command('list', 'list_service_apis')
        g.custom_command('show', 'show_service_apis')
    with self.command_group('service apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis')
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apis releases', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_releases')
        g.custom_command('update', 'update_service_apis_releases')
        g.custom_command('delete', 'delete_service_apis_releases')
        g.custom_command('list', 'list_service_apis_releases')
        g.custom_command('show', 'show_service_apis_releases')
    with self.command_group('service apis releases', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_releases')
        g.custom_command('list', 'list_service_apis_releases')
    with self.command_group('service apis operations', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_operations')
        g.custom_command('update', 'update_service_apis_operations')
        g.custom_command('delete', 'delete_service_apis_operations')
        g.custom_command('list', 'list_service_apis_operations')
        g.custom_command('show', 'show_service_apis_operations')
    with self.command_group('service apis operations', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_operations')
        g.custom_command('list', 'list_service_apis_operations')
    with self.command_group('service apis operations policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_operations_policies')
        g.custom_command('delete', 'delete_service_apis_operations_policies')
        g.custom_command('list', 'list_service_apis_operations_policies')
        g.custom_command('show', 'show_service_apis_operations_policies')
    with self.command_group('service apis operations policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_operations_policies')
        g.custom_command('list', 'list_service_apis_operations_policies')
    with self.command_group('service tags', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_tags')
        g.custom_command('update', 'update_service_tags')
        g.custom_command('delete', 'delete_service_tags')
        g.custom_command('list', 'list_service_tags')
        g.custom_command('show', 'show_service_tags')
    with self.command_group('service tags apis products operations', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_tags_apis_products_operations')
        g.custom_command('show', 'show_service_tags_apis_products_operations')
    with self.command_group('service apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apis policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_policies')
        g.custom_command('delete', 'delete_service_apis_policies')
        g.custom_command('list', 'list_service_apis_policies')
        g.custom_command('show', 'show_service_apis_policies')
    with self.command_group('service apis policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_policies')
        g.custom_command('list', 'list_service_apis_policies')
    with self.command_group('service apis schemas', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_schemas')
        g.custom_command('delete', 'delete_service_apis_schemas')
        g.custom_command('list', 'list_service_apis_schemas')
        g.custom_command('show', 'show_service_apis_schemas')
    with self.command_group('service apis schemas', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_schemas')
        g.custom_command('list', 'list_service_apis_schemas')
    with self.command_group('service apis diagnostics', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_diagnostics')
        g.custom_command('update', 'update_service_apis_diagnostics')
        g.custom_command('delete', 'delete_service_apis_diagnostics')
        g.custom_command('list', 'list_service_apis_diagnostics')
        g.custom_command('show', 'show_service_apis_diagnostics')
    with self.command_group('service apis diagnostics', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_diagnostics')
        g.custom_command('list', 'list_service_apis_diagnostics')
    with self.command_group('service apis issues', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_issues')
        g.custom_command('update', 'update_service_apis_issues')
        g.custom_command('delete', 'delete_service_apis_issues')
        g.custom_command('list', 'list_service_apis_issues')
        g.custom_command('show', 'show_service_apis_issues')
    with self.command_group('service apis issues', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_issues')
        g.custom_command('list', 'list_service_apis_issues')
    with self.command_group('service apis issues comments', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_issues_comments')
        g.custom_command('delete', 'delete_service_apis_issues_comments')
        g.custom_command('list', 'list_service_apis_issues_comments')
        g.custom_command('show', 'show_service_apis_issues_comments')
    with self.command_group('service apis issues comments', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_issues_comments')
        g.custom_command('list', 'list_service_apis_issues_comments')
    with self.command_group('service apis issues attachments', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_issues_attachments')
        g.custom_command('delete', 'delete_service_apis_issues_attachments')
        g.custom_command('list', 'list_service_apis_issues_attachments')
        g.custom_command('show', 'show_service_apis_issues_attachments')
    with self.command_group('service apis issues attachments', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_issues_attachments')
        g.custom_command('list', 'list_service_apis_issues_attachments')
    with self.command_group('service apis tagdescriptions', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apis_tagdescriptions')
        g.custom_command('delete', 'delete_service_apis_tagdescriptions')
        g.custom_command('list', 'list_service_apis_tagdescriptions')
        g.custom_command('show', 'show_service_apis_tagdescriptions')
    with self.command_group('service apis tagdescriptions', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis_tagdescriptions')
        g.custom_command('list', 'list_service_apis_tagdescriptions')
    with self.command_group('service apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apiversionsets', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_apiversionsets')
        g.custom_command('update', 'update_service_apiversionsets')
        g.custom_command('delete', 'delete_service_apiversionsets')
        g.custom_command('list', 'list_service_apiversionsets')
        g.custom_command('show', 'show_service_apiversionsets')
    with self.command_group('service apiversionsets', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apiversionsets')
        g.custom_command('list', 'list_service_apiversionsets')
    with self.command_group('service authorizationservers', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_authorizationservers')
        g.custom_command('update', 'update_service_authorizationservers')
        g.custom_command('delete', 'delete_service_authorizationservers')
        g.custom_command('list', 'list_service_authorizationservers')
        g.custom_command('show', 'show_service_authorizationservers')
    with self.command_group('service authorizationservers', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_authorizationservers')
        g.custom_command('list', 'list_service_authorizationservers')
    with self.command_group('service backends', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_backends')
        g.custom_command('update', 'update_service_backends')
        g.custom_command('delete', 'delete_service_backends')
        g.custom_command('list', 'list_service_backends')
        g.custom_command('show', 'show_service_backends')
    with self.command_group('service backends', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_backends')
        g.custom_command('list', 'list_service_backends')
    with self.command_group('service caches', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_caches')
        g.custom_command('update', 'update_service_caches')
        g.custom_command('delete', 'delete_service_caches')
        g.custom_command('list', 'list_service_caches')
        g.custom_command('show', 'show_service_caches')
    with self.command_group('service caches', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_caches')
        g.custom_command('list', 'list_service_caches')
    with self.command_group('service certificates', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_certificates')
        g.custom_command('delete', 'delete_service_certificates')
        g.custom_command('list', 'list_service_certificates')
        g.custom_command('show', 'show_service_certificates')
    with self.command_group('service certificates', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_certificates')
        g.custom_command('list', 'list_service_certificates')
    with self.command_group('', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('delete', 'delete_service')
        g.custom_command('list', 'list_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service')
        g.custom_command('list', 'list_service')
    with self.command_group('service diagnostics', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_diagnostics')
        g.custom_command('update', 'update_service_diagnostics')
        g.custom_command('delete', 'delete_service_diagnostics')
        g.custom_command('list', 'list_service_diagnostics')
        g.custom_command('show', 'show_service_diagnostics')
    with self.command_group('service diagnostics', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_diagnostics')
        g.custom_command('list', 'list_service_diagnostics')
    with self.command_group('service templates', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_templates')
        g.custom_command('update', 'update_service_templates')
        g.custom_command('delete', 'delete_service_templates')
        g.custom_command('list', 'list_service_templates')
        g.custom_command('show', 'show_service_templates')
    with self.command_group('service templates', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_templates')
        g.custom_command('list', 'list_service_templates')
    with self.command_group('service groups', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_groups')
        g.custom_command('update', 'update_service_groups')
        g.custom_command('delete', 'delete_service_groups')
        g.custom_command('list', 'list_service_groups')
        g.custom_command('show', 'show_service_groups')
    with self.command_group('service groups', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_groups')
        g.custom_command('list', 'list_service_groups')
    with self.command_group('service groups users', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_groups_users')
        g.custom_command('delete', 'delete_service_groups_users')
        g.custom_command('list', 'list_service_groups_users')
    with self.command_group('service groups', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_groups')
    with self.command_group('service identityproviders', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_identityproviders')
        g.custom_command('update', 'update_service_identityproviders')
        g.custom_command('delete', 'delete_service_identityproviders')
        g.custom_command('list', 'list_service_identityproviders')
        g.custom_command('show', 'show_service_identityproviders')
    with self.command_group('service identityproviders', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_identityproviders')
        g.custom_command('list', 'list_service_identityproviders')
    with self.command_group('service issues', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_issues')
        g.custom_command('list', 'list_service_issues')
    with self.command_group('service loggers', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_loggers')
        g.custom_command('update', 'update_service_loggers')
        g.custom_command('delete', 'delete_service_loggers')
        g.custom_command('list', 'list_service_loggers')
        g.custom_command('show', 'show_service_loggers')
    with self.command_group('service loggers', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_loggers')
        g.custom_command('list', 'list_service_loggers')
    with self.command_group('service locations', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_locations')
    with self.command_group('service notifications', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_notifications')
        g.custom_command('list', 'list_service_notifications')
        g.custom_command('show', 'show_service_notifications')
    with self.command_group('service notifications', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_notifications')
        g.custom_command('list', 'list_service_notifications')
    with self.command_group('service notifications recipientusers', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_notifications_recipientusers')
        g.custom_command('delete', 'delete_service_notifications_recipientusers')
        g.custom_command('list', 'list_service_notifications_recipientusers')
    with self.command_group('service notifications', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_notifications')
    with self.command_group('service notifications recipientemails', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_notifications_recipientemails')
        g.custom_command('delete', 'delete_service_notifications_recipientemails')
        g.custom_command('list', 'list_service_notifications_recipientemails')
    with self.command_group('service notifications', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_notifications')
    with self.command_group('service openidconnectproviders', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_openidconnectproviders')
        g.custom_command('update', 'update_service_openidconnectproviders')
        g.custom_command('delete', 'delete_service_openidconnectproviders')
        g.custom_command('list', 'list_service_openidconnectproviders')
        g.custom_command('show', 'show_service_openidconnectproviders')
    with self.command_group('service openidconnectproviders', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_openidconnectproviders')
        g.custom_command('list', 'list_service_openidconnectproviders')
    with self.command_group('service policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_policies')
        g.custom_command('delete', 'delete_service_policies')
        g.custom_command('list', 'list_service_policies')
        g.custom_command('show', 'show_service_policies')
    with self.command_group('service policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_policies')
        g.custom_command('list', 'list_service_policies')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service')
    with self.command_group('service products', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_products')
        g.custom_command('update', 'update_service_products')
        g.custom_command('delete', 'delete_service_products')
        g.custom_command('list', 'list_service_products')
        g.custom_command('show', 'show_service_products')
    with self.command_group('service products', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_products')
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_products_apis')
        g.custom_command('delete', 'delete_service_products_apis')
        g.custom_command('list', 'list_service_products_apis')
    with self.command_group('service products', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products groups', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_products_groups')
        g.custom_command('delete', 'delete_service_products_groups')
        g.custom_command('list', 'list_service_products_groups')
    with self.command_group('service products', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_products_policies')
        g.custom_command('delete', 'delete_service_products_policies')
        g.custom_command('list', 'list_service_products_policies')
        g.custom_command('show', 'show_service_products_policies')
    with self.command_group('service products policies', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_products_policies')
        g.custom_command('list', 'list_service_products_policies')
    with self.command_group('service properties', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_properties')
        g.custom_command('update', 'update_service_properties')
        g.custom_command('delete', 'delete_service_properties')
        g.custom_command('list', 'list_service_properties')
        g.custom_command('show', 'show_service_properties')
    with self.command_group('service properties', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_properties')
        g.custom_command('list', 'list_service_properties')
    with self.command_group('service quotas', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_quotas')
    with self.command_group('service quotas periods', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_quotas_periods')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service subscriptions', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_subscriptions')
        g.custom_command('update', 'update_service_subscriptions')
        g.custom_command('delete', 'delete_service_subscriptions')
        g.custom_command('list', 'list_service_subscriptions')
        g.custom_command('show', 'show_service_subscriptions')
    with self.command_group('service subscriptions', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_subscriptions')
        g.custom_command('show', 'show_service_subscriptions')
    with self.command_group('service', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service tenant', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_tenant')
    with self.command_group('service tenant', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_tenant')
    with self.command_group('service tenant', apimanagement_sdk, client_factory=cf_apimanagement) as g:
    with self.command_group('service users', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('create', 'create_service_users')
        g.custom_command('update', 'update_service_users')
        g.custom_command('delete', 'delete_service_users')
        g.custom_command('list', 'list_service_users')
        g.custom_command('show', 'show_service_users')
    with self.command_group('service users', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_users')
        g.custom_command('list', 'list_service_users')
    with self.command_group('service users', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_users')
    with self.command_group('service users', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_users')
    with self.command_group('service users', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('list', 'list_service_users')
    with self.command_group('service apis', apimanagement_sdk, client_factory=cf_apimanagement) as g:
        g.custom_command('show', 'show_service_apis')