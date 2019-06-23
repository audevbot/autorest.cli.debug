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
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('name', id_part=None, help='A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.')
        c.argument('location', id_part=None, help='The region in which to create the account.')
        c.argument('tags', id_part=None, help='The user-specified tags associated with the account.')
        c.argument('properties', id_part=None, help='The properties of the Batch account.')
        c.argument('auto_storage', id_part=None, help='The properties related to the auto-storage account.')
        c.argument('auto_storage_account_id', id_part=None, help='The resource ID of the storage account to be used for auto-storage account.')
        c.argument('pool_allocation_mode', id_part=None, help='The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.')
        c.argument('key_vault_reference', id_part=None, help='A reference to the Azure key vault associated with the Batch account.')
        c.argument('account_endpoint', id_part=None, help='The account endpoint used to interact with the Batch service.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch update') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('name', id_part=None, help='A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.')
        c.argument('location', id_part=None, help='The region in which to create the account.')
        c.argument('tags', id_part=None, help='The user-specified tags associated with the account.')
        c.argument('properties', id_part=None, help='The properties of the Batch account.')
        c.argument('auto_storage', id_part=None, help='The properties related to the auto-storage account.')
        c.argument('auto_storage_account_id', id_part=None, help='The resource ID of the storage account to be used for auto-storage account.')
        c.argument('pool_allocation_mode', id_part=None, help='The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.')
        c.argument('key_vault_reference', id_part=None, help='A reference to the Azure key vault associated with the Batch account.')
        c.argument('account_endpoint', id_part=None, help='The account endpoint used to interact with the Batch service.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('name', id_part=None, help='A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('name', id_part=None, help='A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('name', id_part=None, help='A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch application version create') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('application_name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('name', id_part=None, help='The version of the application.')
        c.argument('properties', id_part=None, help='The properties associated with the Application Package.')
        c.argument('state', id_part=None, help='The current state of the application package.')
        c.argument('format', id_part=None, help='The format of the application package, if the package is active.')
        c.argument('storage_url', id_part=None, help='The URL for the application package in Azure Storage.')
        c.argument('storage_url_expiry', id_part=None, help='The UTC time at which the Azure Storage URL will expire.')
        c.argument('last_activation_time', id_part=None, help='The time at which the package was last activated, if the package is active.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application version delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('application_name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('name', id_part=None, help='The version of the application.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('application_name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('name', id_part=None, help='The version of the application.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application version show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('application_name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('name', id_part=None, help='The version of the application.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch application create') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('properties', id_part=None, help='The properties associated with the Application.')
        c.argument('display_name', id_part=None, help='The display name for the application.')
        c.argument('allow_updates', id_part=None, help='A value indicating whether packages within the application may be overwritten using the same version string.')
        c.argument('default_version', id_part=None, help='The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application update') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('properties', id_part=None, help='The properties associated with the Application.')
        c.argument('display_name', id_part=None, help='The display name for the application.')
        c.argument('allow_updates', id_part=None, help='A value indicating whether packages within the application may be overwritten using the same version string.')
        c.argument('default_version', id_part=None, help='The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch application delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch application show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The name of the application. This must be unique within the account.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch certificate create') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.')
        c.argument('properties', id_part=None, help='The properties associated with the certificate.')
        c.argument('thumbprint_algorithm', id_part=None, help='This must match the first portion of the certificate name. Currently required to be \'SHA1\'.')
        c.argument('thumbprint', id_part=None, help='This must match the thumbprint from the name.')
        c.argument('format', id_part=None, help='The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.')
        c.argument('data', id_part=None, help='The maximum size is 10KB.')
        c.argument('password', id_part=None, help='This is required if the certificate format is pfx and must be omitted if the certificate format is cer.')
        c.argument('provisioning_state_transition_time', id_part=None, help='undefined')
        c.argument('previous_provisioning_state', id_part=None, help='The previous provisioned state of the resource')
        c.argument('previous_provisioning_state_transition_time', id_part=None, help='undefined')
        c.argument('public_data', id_part=None, help='The public key of the certificate.')
        c.argument('delete_certificate_error', id_part=None, help='This is only returned when the certificate provisioningState is \'Failed\'.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch certificate update') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.')
        c.argument('properties', id_part=None, help='The properties associated with the certificate.')
        c.argument('thumbprint_algorithm', id_part=None, help='This must match the first portion of the certificate name. Currently required to be \'SHA1\'.')
        c.argument('thumbprint', id_part=None, help='This must match the thumbprint from the name.')
        c.argument('format', id_part=None, help='The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx.')
        c.argument('data', id_part=None, help='The maximum size is 10KB.')
        c.argument('password', id_part=None, help='This is required if the certificate format is pfx and must be omitted if the certificate format is cer.')
        c.argument('provisioning_state_transition_time', id_part=None, help='undefined')
        c.argument('previous_provisioning_state', id_part=None, help='The previous provisioned state of the resource')
        c.argument('previous_provisioning_state_transition_time', id_part=None, help='undefined')
        c.argument('public_data', id_part=None, help='The public key of the certificate.')
        c.argument('delete_certificate_error', id_part=None, help='This is only returned when the certificate provisioningState is \'Failed\'.')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch certificate delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch certificate show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')


    with self.argument_context('batch pool create') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The pool name. This must be unique within the account.')
        c.argument('properties', id_part=None, help='The properties associated with the pool.')
        c.argument('display_name', id_part=None, help='The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.')
        c.argument('vm_size', id_part=None, help='For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).')
        c.argument('deployment_configuration', id_part=None, help='Using CloudServiceConfiguration specifies that the nodes should be creating using Azure Cloud Services (PaaS), while VirtualMachineConfiguration uses Azure Virtual Machines (IaaS).')
        c.argument('scale_settings', id_part=None, help='undefined')
        c.argument('inter_node_communication', id_part=None, help='This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to \'Disabled\'.')
        c.argument('network_configuration', id_part=None, help='undefined')
        c.argument('max_tasks_per_node', id_part=None, help='undefined')
        c.argument('task_scheduling_policy', id_part=None, help='undefined')
        c.argument('user_accounts', id_part=None, help='undefined')
        c.argument('metadata', id_part=None, help='The Batch service does not assign any meaning to metadata; it is solely for the use of user code.')
        c.argument('start_task', id_part=None, help='In an PATCH (update) operation, this property can be set to an empty object to remove the start task from the pool.')
        c.argument('certificates', id_part=None, help='For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of \'remoteUser\', a \'certs\' directory is created in the user\'s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory.')
        c.argument('application_packages', id_part=None, help='Changes to application packages affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged.')
        c.argument('application_licenses', id_part=None, help='The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail.')
        c.argument('last_modified', id_part=None, help='This is the last time at which the pool level data, such as the targetDedicatedNodes or autoScaleSettings, changed. It does not factor in node-level changes such as a compute node changing state.')
        c.argument('creation_time', id_part=None, help='undefined')
        c.argument('provisioning_state_transition_time', id_part=None, help='undefined')
        c.argument('allocation_state', id_part=None, help='undefined')
        c.argument('allocation_state_transition_time', id_part=None, help='undefined')
        c.argument('current_dedicated_nodes', id_part=None, help='undefined')
        c.argument('current_low_priority_nodes', id_part=None, help='undefined')
        c.argument('auto_scale_run', id_part=None, help='This property is set only if the pool automatically scales, i.e. autoScaleSettings are used.')
        c.argument('resize_operation_status', id_part=None, help='undefined')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch pool update') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The pool name. This must be unique within the account.')
        c.argument('properties', id_part=None, help='The properties associated with the pool.')
        c.argument('display_name', id_part=None, help='The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.')
        c.argument('vm_size', id_part=None, help='For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).')
        c.argument('deployment_configuration', id_part=None, help='Using CloudServiceConfiguration specifies that the nodes should be creating using Azure Cloud Services (PaaS), while VirtualMachineConfiguration uses Azure Virtual Machines (IaaS).')
        c.argument('scale_settings', id_part=None, help='undefined')
        c.argument('inter_node_communication', id_part=None, help='This imposes restrictions on which nodes can be assigned to the pool. Enabling this value can reduce the chance of the requested number of nodes to be allocated in the pool. If not specified, this value defaults to \'Disabled\'.')
        c.argument('network_configuration', id_part=None, help='undefined')
        c.argument('max_tasks_per_node', id_part=None, help='undefined')
        c.argument('task_scheduling_policy', id_part=None, help='undefined')
        c.argument('user_accounts', id_part=None, help='undefined')
        c.argument('metadata', id_part=None, help='The Batch service does not assign any meaning to metadata; it is solely for the use of user code.')
        c.argument('start_task', id_part=None, help='In an PATCH (update) operation, this property can be set to an empty object to remove the start task from the pool.')
        c.argument('certificates', id_part=None, help='For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of \'remoteUser\', a \'certs\' directory is created in the user\'s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory.')
        c.argument('application_packages', id_part=None, help='Changes to application packages affect all new compute nodes joining the pool, but do not affect compute nodes that are already in the pool until they are rebooted or reimaged.')
        c.argument('application_licenses', id_part=None, help='The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, pool creation will fail.')
        c.argument('last_modified', id_part=None, help='This is the last time at which the pool level data, such as the targetDedicatedNodes or autoScaleSettings, changed. It does not factor in node-level changes such as a compute node changing state.')
        c.argument('creation_time', id_part=None, help='undefined')
        c.argument('provisioning_state_transition_time', id_part=None, help='undefined')
        c.argument('allocation_state', id_part=None, help='undefined')
        c.argument('allocation_state_transition_time', id_part=None, help='undefined')
        c.argument('current_dedicated_nodes', id_part=None, help='undefined')
        c.argument('current_low_priority_nodes', id_part=None, help='undefined')
        c.argument('auto_scale_run', id_part=None, help='This property is set only if the pool automatically scales, i.e. autoScaleSettings are used.')
        c.argument('resize_operation_status', id_part=None, help='undefined')
        c.argument('id', id_part=None, help='The ID of the resource.')
        c.argument('etag', id_part=None, help='The ETag of the resource, used for concurrency statements.')
        c.argument('resource_id', name_arg_type, id_part=None)

    with self.argument_context('batch pool delete') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The pool name. This must be unique within the account.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool list') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The pool name. This must be unique within the account.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)

    with self.argument_context('batch pool show') as c:
        c.argument('resource_group', id_part=None, help='The name of the resource group that contains the Batch account.')
        c.argument('account_name', id_part=None, help='The name of the Batch account.')
        c.argument('name', id_part=None, help='The pool name. This must be unique within the account.')
        c.argument('resource_id', name_arg_type, id_part=None)
        c.argument('rest_body', name_arg_type, id_part=None)
    apimanagement_name_type = CLIArgumentType(options_list='--apimanagement-name-name', help='Name of the Apimanagement.', id_part='name')

    with self.argument_context('apimanagement') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('apimanagement_name', name_arg_type, options_list=['--name', '-n'])