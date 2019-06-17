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


    with self.command_group('service apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis')
        g.custom_command('update', 'update_service_apis')
        g.custom_command('delete', 'delete_service_apis')
        g.custom_command('list', 'list_service_apis')
        g.custom_command('show', 'show_service_apis')
    with self.command_group('service apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis')
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apis releases', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_releases')
        g.custom_command('update', 'update_service_apis_releases')
        g.custom_command('delete', 'delete_service_apis_releases')
        g.custom_command('list', 'list_service_apis_releases')
        g.custom_command('show', 'show_service_apis_releases')
    with self.command_group('service apis releases', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_releases')
        g.custom_command('list', 'list_service_apis_releases')
    with self.command_group('service apis operations', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_operations')
        g.custom_command('update', 'update_service_apis_operations')
        g.custom_command('delete', 'delete_service_apis_operations')
        g.custom_command('list', 'list_service_apis_operations')
        g.custom_command('show', 'show_service_apis_operations')
    with self.command_group('service apis operations', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_operations')
        g.custom_command('list', 'list_service_apis_operations')
    with self.command_group('service apis operations policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_operations_policies')
        g.custom_command('delete', 'delete_service_apis_operations_policies')
        g.custom_command('list', 'list_service_apis_operations_policies')
        g.custom_command('show', 'show_service_apis_operations_policies')
    with self.command_group('service apis operations policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_operations_policies')
        g.custom_command('list', 'list_service_apis_operations_policies')
    with self.command_group('service tags', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_tags')
        g.custom_command('update', 'update_service_tags')
        g.custom_command('delete', 'delete_service_tags')
        g.custom_command('list', 'list_service_tags')
        g.custom_command('show', 'show_service_tags')
    with self.command_group('service tags apis products operations', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_tags_apis_products_operations')
        g.custom_command('show', 'show_service_tags_apis_products_operations')
    with self.command_group('service apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apis policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_policies')
        g.custom_command('delete', 'delete_service_apis_policies')
        g.custom_command('list', 'list_service_apis_policies')
        g.custom_command('show', 'show_service_apis_policies')
    with self.command_group('service apis policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_policies')
        g.custom_command('list', 'list_service_apis_policies')
    with self.command_group('service apis schemas', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_schemas')
        g.custom_command('delete', 'delete_service_apis_schemas')
        g.custom_command('list', 'list_service_apis_schemas')
        g.custom_command('show', 'show_service_apis_schemas')
    with self.command_group('service apis schemas', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_schemas')
        g.custom_command('list', 'list_service_apis_schemas')
    with self.command_group('service apis diagnostics', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_diagnostics')
        g.custom_command('update', 'update_service_apis_diagnostics')
        g.custom_command('delete', 'delete_service_apis_diagnostics')
        g.custom_command('list', 'list_service_apis_diagnostics')
        g.custom_command('show', 'show_service_apis_diagnostics')
    with self.command_group('service apis diagnostics', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_diagnostics')
        g.custom_command('list', 'list_service_apis_diagnostics')
    with self.command_group('service apis issues', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_issues')
        g.custom_command('update', 'update_service_apis_issues')
        g.custom_command('delete', 'delete_service_apis_issues')
        g.custom_command('list', 'list_service_apis_issues')
        g.custom_command('show', 'show_service_apis_issues')
    with self.command_group('service apis issues', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_issues')
        g.custom_command('list', 'list_service_apis_issues')
    with self.command_group('service apis issues comments', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_issues_comments')
        g.custom_command('delete', 'delete_service_apis_issues_comments')
        g.custom_command('list', 'list_service_apis_issues_comments')
        g.custom_command('show', 'show_service_apis_issues_comments')
    with self.command_group('service apis issues comments', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_issues_comments')
        g.custom_command('list', 'list_service_apis_issues_comments')
    with self.command_group('service apis issues attachments', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_issues_attachments')
        g.custom_command('delete', 'delete_service_apis_issues_attachments')
        g.custom_command('list', 'list_service_apis_issues_attachments')
        g.custom_command('show', 'show_service_apis_issues_attachments')
    with self.command_group('service apis issues attachments', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_issues_attachments')
        g.custom_command('list', 'list_service_apis_issues_attachments')
    with self.command_group('service apis tagdescriptions', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apis_tagdescriptions')
        g.custom_command('delete', 'delete_service_apis_tagdescriptions')
        g.custom_command('list', 'list_service_apis_tagdescriptions')
        g.custom_command('show', 'show_service_apis_tagdescriptions')
    with self.command_group('service apis tagdescriptions', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis_tagdescriptions')
        g.custom_command('list', 'list_service_apis_tagdescriptions')
    with self.command_group('service apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_apis')
    with self.command_group('service apiversionsets', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_apiversionsets')
        g.custom_command('update', 'update_service_apiversionsets')
        g.custom_command('delete', 'delete_service_apiversionsets')
        g.custom_command('list', 'list_service_apiversionsets')
        g.custom_command('show', 'show_service_apiversionsets')
    with self.command_group('service apiversionsets', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apiversionsets')
        g.custom_command('list', 'list_service_apiversionsets')
    with self.command_group('service authorizationservers', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_authorizationservers')
        g.custom_command('update', 'update_service_authorizationservers')
        g.custom_command('delete', 'delete_service_authorizationservers')
        g.custom_command('list', 'list_service_authorizationservers')
        g.custom_command('show', 'show_service_authorizationservers')
    with self.command_group('service authorizationservers', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_authorizationservers')
        g.custom_command('list', 'list_service_authorizationservers')
    with self.command_group('service backends', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_backends')
        g.custom_command('update', 'update_service_backends')
        g.custom_command('delete', 'delete_service_backends')
        g.custom_command('list', 'list_service_backends')
        g.custom_command('show', 'show_service_backends')
    with self.command_group('service backends', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_backends')
        g.custom_command('list', 'list_service_backends')
    with self.command_group('service caches', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_caches')
        g.custom_command('update', 'update_service_caches')
        g.custom_command('delete', 'delete_service_caches')
        g.custom_command('list', 'list_service_caches')
        g.custom_command('show', 'show_service_caches')
    with self.command_group('service caches', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_caches')
        g.custom_command('list', 'list_service_caches')
    with self.command_group('service certificates', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_certificates')
        g.custom_command('delete', 'delete_service_certificates')
        g.custom_command('list', 'list_service_certificates')
        g.custom_command('show', 'show_service_certificates')
    with self.command_group('service certificates', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_certificates')
        g.custom_command('list', 'list_service_certificates')
    with self.command_group('', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('delete', 'delete_service')
        g.custom_command('list', 'list_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service')
        g.custom_command('list', 'list_service')
    with self.command_group('service diagnostics', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_diagnostics')
        g.custom_command('update', 'update_service_diagnostics')
        g.custom_command('delete', 'delete_service_diagnostics')
        g.custom_command('list', 'list_service_diagnostics')
        g.custom_command('show', 'show_service_diagnostics')
    with self.command_group('service diagnostics', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_diagnostics')
        g.custom_command('list', 'list_service_diagnostics')
    with self.command_group('service templates', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_templates')
        g.custom_command('update', 'update_service_templates')
        g.custom_command('delete', 'delete_service_templates')
        g.custom_command('list', 'list_service_templates')
        g.custom_command('show', 'show_service_templates')
    with self.command_group('service templates', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_templates')
        g.custom_command('list', 'list_service_templates')
    with self.command_group('service groups', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_groups')
        g.custom_command('update', 'update_service_groups')
        g.custom_command('delete', 'delete_service_groups')
        g.custom_command('list', 'list_service_groups')
        g.custom_command('show', 'show_service_groups')
    with self.command_group('service groups', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_groups')
        g.custom_command('list', 'list_service_groups')
    with self.command_group('service groups users', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_groups_users')
        g.custom_command('delete', 'delete_service_groups_users')
        g.custom_command('list', 'list_service_groups_users')
    with self.command_group('service groups', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_groups')
    with self.command_group('service identityproviders', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_identityproviders')
        g.custom_command('update', 'update_service_identityproviders')
        g.custom_command('delete', 'delete_service_identityproviders')
        g.custom_command('list', 'list_service_identityproviders')
        g.custom_command('show', 'show_service_identityproviders')
    with self.command_group('service identityproviders', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_identityproviders')
        g.custom_command('list', 'list_service_identityproviders')
    with self.command_group('service issues', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_issues')
        g.custom_command('list', 'list_service_issues')
    with self.command_group('service loggers', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_loggers')
        g.custom_command('update', 'update_service_loggers')
        g.custom_command('delete', 'delete_service_loggers')
        g.custom_command('list', 'list_service_loggers')
        g.custom_command('show', 'show_service_loggers')
    with self.command_group('service loggers', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_loggers')
        g.custom_command('list', 'list_service_loggers')
    with self.command_group('service locations', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_locations')
    with self.command_group('service notifications', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_notifications')
        g.custom_command('list', 'list_service_notifications')
        g.custom_command('show', 'show_service_notifications')
    with self.command_group('service notifications', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_notifications')
        g.custom_command('list', 'list_service_notifications')
    with self.command_group('service notifications recipientusers', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_notifications_recipientusers')
        g.custom_command('delete', 'delete_service_notifications_recipientusers')
        g.custom_command('list', 'list_service_notifications_recipientusers')
    with self.command_group('service notifications', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_notifications')
    with self.command_group('service notifications recipientemails', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_notifications_recipientemails')
        g.custom_command('delete', 'delete_service_notifications_recipientemails')
        g.custom_command('list', 'list_service_notifications_recipientemails')
    with self.command_group('service notifications', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_notifications')
    with self.command_group('service openidconnectproviders', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_openidconnectproviders')
        g.custom_command('update', 'update_service_openidconnectproviders')
        g.custom_command('delete', 'delete_service_openidconnectproviders')
        g.custom_command('list', 'list_service_openidconnectproviders')
        g.custom_command('show', 'show_service_openidconnectproviders')
    with self.command_group('service openidconnectproviders', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_openidconnectproviders')
        g.custom_command('list', 'list_service_openidconnectproviders')
    with self.command_group('service policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_policies')
        g.custom_command('delete', 'delete_service_policies')
        g.custom_command('list', 'list_service_policies')
        g.custom_command('show', 'show_service_policies')
    with self.command_group('service policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_policies')
        g.custom_command('list', 'list_service_policies')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service')
        g.custom_command('update', 'update_service')
        g.custom_command('show', 'show_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service')
    with self.command_group('service products', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_products')
        g.custom_command('update', 'update_service_products')
        g.custom_command('delete', 'delete_service_products')
        g.custom_command('list', 'list_service_products')
        g.custom_command('show', 'show_service_products')
    with self.command_group('service products', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_products')
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_products_apis')
        g.custom_command('delete', 'delete_service_products_apis')
        g.custom_command('list', 'list_service_products_apis')
    with self.command_group('service products', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products groups', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_products_groups')
        g.custom_command('delete', 'delete_service_products_groups')
        g.custom_command('list', 'list_service_products_groups')
    with self.command_group('service products', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_products')
    with self.command_group('service products policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_products_policies')
        g.custom_command('delete', 'delete_service_products_policies')
        g.custom_command('list', 'list_service_products_policies')
        g.custom_command('show', 'show_service_products_policies')
    with self.command_group('service products policies', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_products_policies')
        g.custom_command('list', 'list_service_products_policies')
    with self.command_group('service properties', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_properties')
        g.custom_command('update', 'update_service_properties')
        g.custom_command('delete', 'delete_service_properties')
        g.custom_command('list', 'list_service_properties')
        g.custom_command('show', 'show_service_properties')
    with self.command_group('service properties', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_properties')
        g.custom_command('list', 'list_service_properties')
    with self.command_group('service quotas', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_quotas')
    with self.command_group('service quotas periods', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_quotas_periods')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service subscriptions', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_subscriptions')
        g.custom_command('update', 'update_service_subscriptions')
        g.custom_command('delete', 'delete_service_subscriptions')
        g.custom_command('list', 'list_service_subscriptions')
        g.custom_command('show', 'show_service_subscriptions')
    with self.command_group('service subscriptions', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_subscriptions')
        g.custom_command('show', 'show_service_subscriptions')
    with self.command_group('service', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service')
    with self.command_group('service tenant', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_tenant')
    with self.command_group('service tenant', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_tenant')
    with self.command_group('service tenant', apimgmt_sdk, client_factory=cf_apimgmt) as g:
    with self.command_group('service users', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('create', 'create_service_users')
        g.custom_command('update', 'update_service_users')
        g.custom_command('delete', 'delete_service_users')
        g.custom_command('list', 'list_service_users')
        g.custom_command('show', 'show_service_users')
    with self.command_group('service users', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_users')
        g.custom_command('list', 'list_service_users')
    with self.command_group('service users', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_users')
    with self.command_group('service users', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_users')
    with self.command_group('service users', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('list', 'list_service_users')
    with self.command_group('service apis', apimgmt_sdk, client_factory=cf_apimgmt) as g:
        g.custom_command('show', 'show_service_apis')