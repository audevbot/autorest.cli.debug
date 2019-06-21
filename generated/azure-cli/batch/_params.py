# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.)
        c.argument('location', name_arg_type, id_part=None,The region in which to create the account.)
        c.argument('tags', name_arg_type, id_part=None,The user-specified tags associated with the account.)
        c.argument('properties', name_arg_type, id_part=None,The properties of the Batch account.)
        c.argument('auto_storage', name_arg_type, id_part=None,The properties related to the auto-storage account.)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None,The resource ID of the storage account to be used for auto-storage account.)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None,The UTC time at which storage keys were last synchronized with the Batch account.)
        c.argument('pool_allocation_mode', name_arg_type, id_part=None,The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.)
        c.argument('key_vault_reference', name_arg_type, id_part=None,A reference to the Azure key vault associated with the Batch account.)
        c.argument('account_endpoint', name_arg_type, id_part=None,The account endpoint used to interact with the Batch service.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch update') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.)
        c.argument('location', name_arg_type, id_part=None,The region in which to create the account.)
        c.argument('tags', name_arg_type, id_part=None,The user-specified tags associated with the account.)
        c.argument('properties', name_arg_type, id_part=None,The properties of the Batch account.)
        c.argument('auto_storage', name_arg_type, id_part=None,The properties related to the auto-storage account.)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None,The resource ID of the storage account to be used for auto-storage account.)
        c.argument('auto_storage_account_id', name_arg_type, id_part=None,The UTC time at which storage keys were last synchronized with the Batch account.)
        c.argument('pool_allocation_mode', name_arg_type, id_part=None,The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.)
        c.argument('key_vault_reference', name_arg_type, id_part=None,A reference to the Azure key vault associated with the Batch account.)
        c.argument('account_endpoint', name_arg_type, id_part=None,The account endpoint used to interact with the Batch service.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch application version create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('application_name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('name', name_arg_type, id_part=None,The version of the application.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the Application Package.)
        c.argument('state', name_arg_type, id_part=None,The current state of the application package.)
        c.argument('format', name_arg_type, id_part=None,The format of the application package, if the package is active.)
        c.argument('storage_url', name_arg_type, id_part=None,The URL for the application package in Azure Storage.)
        c.argument('storage_url_expiry', name_arg_type, id_part=None,The UTC time at which the Azure Storage URL will expire.)
        c.argument('last_activation_time', name_arg_type, id_part=None,The time at which the package was last activated, if the package is active.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application version delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('application_name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('name', name_arg_type, id_part=None,The version of the application.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('application_name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('name', name_arg_type, id_part=None,The version of the application.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('application_name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('name', name_arg_type, id_part=None,The version of the application.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch application version show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('application_name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('name', name_arg_type, id_part=None,The version of the application.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('application_name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('name', name_arg_type, id_part=None,The version of the application.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch application create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the Application.)
        c.argument('display_name', name_arg_type, id_part=None,The display name for the application.)
        c.argument('allow_updates', name_arg_type, id_part=None,A value indicating whether packages within the application may be overwritten using the same version string.)
        c.argument('default_version', name_arg_type, id_part=None,The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application update') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the Application.)
        c.argument('display_name', name_arg_type, id_part=None,The display name for the application.)
        c.argument('allow_updates', name_arg_type, id_part=None,A value indicating whether packages within the application may be overwritten using the same version string.)
        c.argument('default_version', name_arg_type, id_part=None,The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch application show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The name of the application. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context(' list') as c:
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch certificate create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the certificate.)
        c.argument('thumbprint_algorithm', name_arg_type, id_part=None,This must match the first portion of the certificate name. Currently required to be 'SHA1'.)
        c.argument('thumbprint', name_arg_type, id_part=None,This must match the thumbprint from the name.)
        c.argument('format', name_arg_type, id_part=None,The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.)
        c.argument('data', name_arg_type, id_part=None,The maximum size is 10KB.)
        c.argument('password', name_arg_type, id_part=None,This is required if the certificate format is pfx and must be omitted if the certificate format is cer.)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('previous_provisioning_state', name_arg_type, id_part=None,The previous provisioned state of the resource)
        c.argument('previous_provisioning_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('public_data', name_arg_type, id_part=None,The public key of the certificate.)
        c.argument('delete_certificate_error', name_arg_type, id_part=None,This is only returned when the certificate provisioningState is 'Failed'.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch certificate update') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the certificate.)
        c.argument('thumbprint_algorithm', name_arg_type, id_part=None,This must match the first portion of the certificate name. Currently required to be 'SHA1'.)
        c.argument('thumbprint', name_arg_type, id_part=None,This must match the thumbprint from the name.)
        c.argument('format', name_arg_type, id_part=None,The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.)
        c.argument('data', name_arg_type, id_part=None,The maximum size is 10KB.)
        c.argument('password', name_arg_type, id_part=None,This is required if the certificate format is pfx and must be omitted if the certificate format is cer.)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('previous_provisioning_state', name_arg_type, id_part=None,The previous provisioned state of the resource)
        c.argument('previous_provisioning_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('public_data', name_arg_type, id_part=None,The public key of the certificate.)
        c.argument('delete_certificate_error', name_arg_type, id_part=None,This is only returned when the certificate provisioningState is 'Failed'.)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch certificate delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch certificate show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch pool create') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the pool.)
        c.argument('display_name', name_arg_type, id_part=None,The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.)
        c.argument('vm_size', name_arg_type, id_part=None,For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).)
        c.argument('deployment_configuration', name_arg_type, id_part=None,Using CloudServiceConfiguration specifies that the nodes should be creating using Azure Cloud Services (PaaS), while VirtualMachineConfiguration uses Azure Virtual Machines (IaaS).)
        c.argument('scale_settings', name_arg_type, id_part=None,undefined)
        c.argument('inter_node_communication', name_arg_type, id_part=None,This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to 'Disabled'.)
        c.argument('network_configuration', name_arg_type, id_part=None,undefined)
        c.argument('max_tasks_per_node', name_arg_type, id_part=None,undefined)
        c.argument('task_scheduling_policy', name_arg_type, id_part=None,undefined)
        c.argument('user_accounts', name_arg_type, id_part=None,undefined)
        c.argument('metadata', name_arg_type, id_part=None,The Batch service does not assign any meaning to metadata; it is solely for the use of user code.)
        c.argument('start_task', name_arg_type, id_part=None,In an PATCH (update) operation, this property can be set to an empty object to remove the start task from the pool.)
        c.argument('certificates', name_arg_type, id_part=None,For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory.)
        c.argument('application_packages', name_arg_type, id_part=None,Changes to application packages affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged.)
        c.argument('application_licenses', name_arg_type, id_part=None,The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail.)
        c.argument('last_modified', name_arg_type, id_part=None,This is the last time at which the pool level data, such as the targetDedicatedNodes or autoScaleSettings, changed. It does not factor in node-level changes such as a compute node changing state.)
        c.argument('creation_time', name_arg_type, id_part=None,undefined)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('allocation_state', name_arg_type, id_part=None,undefined)
        c.argument('allocation_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('current_dedicated_nodes', name_arg_type, id_part=None,undefined)
        c.argument('current_low_priority_nodes', name_arg_type, id_part=None,undefined)
        c.argument('auto_scale_run', name_arg_type, id_part=None,This property is set only if the pool automatically scales, i.e. autoScaleSettings are used.)
        c.argument('resize_operation_status', name_arg_type, id_part=None,undefined)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch pool update') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('properties', name_arg_type, id_part=None,The properties associated with the pool.)
        c.argument('display_name', name_arg_type, id_part=None,The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.)
        c.argument('vm_size', name_arg_type, id_part=None,For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).)
        c.argument('deployment_configuration', name_arg_type, id_part=None,Using CloudServiceConfiguration specifies that the nodes should be creating using Azure Cloud Services (PaaS), while VirtualMachineConfiguration uses Azure Virtual Machines (IaaS).)
        c.argument('scale_settings', name_arg_type, id_part=None,undefined)
        c.argument('inter_node_communication', name_arg_type, id_part=None,This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to 'Disabled'.)
        c.argument('network_configuration', name_arg_type, id_part=None,undefined)
        c.argument('max_tasks_per_node', name_arg_type, id_part=None,undefined)
        c.argument('task_scheduling_policy', name_arg_type, id_part=None,undefined)
        c.argument('user_accounts', name_arg_type, id_part=None,undefined)
        c.argument('metadata', name_arg_type, id_part=None,The Batch service does not assign any meaning to metadata; it is solely for the use of user code.)
        c.argument('start_task', name_arg_type, id_part=None,In an PATCH (update) operation, this property can be set to an empty object to remove the start task from the pool.)
        c.argument('certificates', name_arg_type, id_part=None,For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory.)
        c.argument('application_packages', name_arg_type, id_part=None,Changes to application packages affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged.)
        c.argument('application_licenses', name_arg_type, id_part=None,The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail.)
        c.argument('last_modified', name_arg_type, id_part=None,This is the last time at which the pool level data, such as the targetDedicatedNodes or autoScaleSettings, changed. It does not factor in node-level changes such as a compute node changing state.)
        c.argument('creation_time', name_arg_type, id_part=None,undefined)
        c.argument('provisioning_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('allocation_state', name_arg_type, id_part=None,undefined)
        c.argument('allocation_state_transition_time', name_arg_type, id_part=None,undefined)
        c.argument('current_dedicated_nodes', name_arg_type, id_part=None,undefined)
        c.argument('current_low_priority_nodes', name_arg_type, id_part=None,undefined)
        c.argument('auto_scale_run', name_arg_type, id_part=None,This property is set only if the pool automatically scales, i.e. autoScaleSettings are used.)
        c.argument('resize_operation_status', name_arg_type, id_part=None,undefined)
        c.argument('id', name_arg_type, id_part=None,The ID of the resource.)
        c.argument('etag', name_arg_type, id_part=None,The ETag of the resource, used for concurrency statements.)
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch pool delete') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch pool show') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool list') as c:
        c.argument('resource_group', name_arg_type, id_part=None,The name of the resource group that contains the Batch account.)
        c.argument('account_name', name_arg_type, id_part=None,The name of the Batch account.)
        c.argument('name', name_arg_type, id_part=None,The pool name. This must be unique within the account.)
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])