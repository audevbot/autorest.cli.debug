#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_batchpool_info
version_added: '2.9'
short_description: Get Pool info.
description:
  - Get info of Pool.
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
  account_name:
    description:
      - The name of the Batch account.
    required: true
  maxresults:
    description:
      - The maximum number of items to return in the response.
  name:
    description:
      - The pool name. This must be unique within the account.
  id:
    description:
      - The ID of the resource.
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
  display_name:
    description:
      - >-
        The display name need not be unique and can contain any Unicode
        characters up to a maximum length of 1024.
  last_modified:
    description:
      - >-
        This is the last time at which the pool level data, such as the
        targetDedicatedNodes or autoScaleSettings, changed. It does not factor
        in node-level changes such as a compute node changing state.
  creation_time:
    description:
      - undefined
  provisioning_state_transition_time:
    description:
      - undefined
  allocation_state:
    description:
      - undefined
  allocation_state_transition_time:
    description:
      - undefined
  vm_size:
    description:
      - >-
        For information about available sizes of virtual machines for Cloud
        Services pools (pools created with cloudServiceConfiguration), see Sizes
        for Cloud Services
        (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/).
        Batch supports all Cloud Services VM sizes except ExtraSmall. For
        information about available VM sizes for pools using images from the
        Virtual Machines Marketplace (pools created with
        virtualMachineConfiguration) see Sizes for Virtual Machines (Linux)
        (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/)
        or Sizes for Virtual Machines (Windows)
        (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/).
        Batch supports all Azure VM sizes except STANDARD_A0 and those with
        premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
  deployment_configuration:
    description:
      - >-
        Using CloudServiceConfiguration specifies that the nodes should be
        creating using Azure Cloud Services (PaaS), while
        VirtualMachineConfiguration uses Azure Virtual Machines (IaaS).
    suboptions:
      cloud_service_configuration:
        description:
          - >-
            This property and virtualMachineConfiguration are mutually exclusive
            and one of the properties must be specified. This property cannot be
            specified if the Batch account was created with its
            poolAllocationMode property set to 'UserSubscription'.
        suboptions:
          os_family:
            description:
              - >-
                Possible values are: 2 - OS Family 2, equivalent to Windows
                Server 2008 R2 SP1. 3 - OS Family 3, equivalent to Windows
                Server 2012. 4 - OS Family 4, equivalent to Windows Server 2012
                R2. 5 - OS Family 5, equivalent to Windows Server 2016. For more
                information, see Azure Guest OS Releases
                (https://azure.microsoft.com/documentation/articles/cloud-services-guestos-update-matrix/#releases).
            required: true
          os_version:
            description:
              - >-
                The default value is * which specifies the latest operating
                system version for the specified OS family.
      virtual_machine_configuration:
        description:
          - >-
            This property and cloudServiceConfiguration are mutually exclusive
            and one of the properties must be specified.
        suboptions:
          image_reference:
            description:
              - undefined
            required: true
            suboptions:
              publisher:
                description:
                  - 'For example, Canonical or MicrosoftWindowsServer.'
              offer:
                description:
                  - 'For example, UbuntuServer or WindowsServer.'
              sku:
                description:
                  - 'For example, 14.04.0-LTS or 2012-R2-Datacenter.'
              version:
                description:
                  - >-
                    A value of 'latest' can be specified to select the latest
                    version of an image. If omitted, the default is 'latest'.
              id:
                description:
                  - >-
                    This property is mutually exclusive with other properties.
                    The virtual machine image must be in the same region and
                    subscription as the Azure Batch account. For information
                    about the firewall settings for Batch node agent to
                    communicate with Batch service see
                    https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration
                    .
          node_agent_sku_id:
            description:
              - >-
                The Batch node agent is a program that runs on each node in the
                pool, and provides the command-and-control interface between the
                node and the Batch service. There are different implementations
                of the node agent, known as SKUs, for different operating
                systems. You must specify a node agent SKU which matches the
                selected image reference. To get the list of supported node
                agent SKUs along with their list of verified image references,
                see the 'List supported node agent SKUs' operation.
            required: true
          windows_configuration:
            description:
              - >-
                This property must not be specified if the imageReference
                specifies a Linux OS image.
            suboptions:
              enable_automatic_updates:
                description:
                  - 'If omitted, the default value is true.'
          data_disks:
            description:
              - >-
                This property must be specified if the compute nodes in the pool
                need to have empty data disks attached to them.
            type: list
            suboptions:
              lun:
                description:
                  - >-
                    The lun is used to uniquely identify each data disk. If
                    attaching multiple disks, each should have a distinct lun.
                required: true
              caching:
                description:
                  - >-
                    Values are:<br> none - The caching mode for the disk is not
                    enabled.<br> readOnly - The caching mode for the disk is
                    read only.<br> readWrite - The caching mode for the disk is
                    read and write.<br> The default value for caching is none.
                    For information about the caching options see:
                    https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/.
              disk_size_gb:
                description:
                  - undefined
                required: true
              storage_account_type:
                description:
                  - >-
                    If omitted, the default is "Standard_LRS". Values are:<br>
                    Standard_LRS - The data disk should use standard locally
                    redundant storage.<br> Premium_LRS - The data disk should
                    use premium locally redundant storage.
          license_type:
            description:
              - >-
                This only applies to images that contain the Windows operating
                system, and should only be used when you hold valid on-premises
                licenses for the nodes which will be deployed. If omitted, no
                on-premises licensing discount is applied. Values are:<br>
                Windows_Server - The on-premises license is for Windows
                Server.<br> Windows_Client - The on-premises license is for
                Windows Client.<br>
          container_configuration:
            description:
              - >-
                If specified, setup is performed on each node in the pool to
                allow tasks to run in containers. All regular tasks and job
                manager tasks run on this pool must specify the
                containerSettings property, and all other tasks may specify it.
            suboptions:
              type:
                description:
                  - undefined
                required: true
              container_image_names:
                description:
                  - >-
                    This is the full image reference, as would be specified to
                    "docker pull". An image will be sourced from the default
                    Docker registry unless the image is fully qualified with an
                    alternative registry.
                type: list
              container_registries:
                description:
                  - >-
                    If any images must be downloaded from a private registry
                    which requires credentials, then those credentials must be
                    provided here.
                type: list
  current_dedicated_nodes:
    description:
      - undefined
  current_low_priority_nodes:
    description:
      - undefined
  scale_settings:
    description:
      - undefined
    suboptions:
      fixed_scale:
        description:
          - >-
            This property and autoScale are mutually exclusive and one of the
            properties must be specified.
        suboptions:
          resize_timeout:
            description:
              - >-
                The default value is 15 minutes. Timeout values use ISO 8601
                format. For example, use PT10M for 10 minutes. The minimum value
                is 5 minutes. If you specify a value less than 5 minutes, the
                Batch service rejects the request with an error; if you are
                calling the REST API directly, the HTTP status code is 400 (Bad
                Request).
          target_dedicated_nodes:
            description:
              - >-
                At least one of targetDedicatedNodes, targetLowPriority nodes
                must be set.
          target_low_priority_nodes:
            description:
              - >-
                At least one of targetDedicatedNodes, targetLowPriority nodes
                must be set.
          node_deallocation_option:
            description:
              - 'If omitted, the default value is Requeue.'
      auto_scale:
        description:
          - >-
            This property and fixedScale are mutually exclusive and one of the
            properties must be specified.
        suboptions:
          formula:
            description:
              - undefined
            required: true
          evaluation_interval:
            description:
              - 'If omitted, the default value is 15 minutes (PT15M).'
  auto_scale_run:
    description:
      - >-
        This property is set only if the pool automatically scales, i.e.
        autoScaleSettings are used.
    suboptions:
      evaluation_time:
        description:
          - undefined
        required: true
      results:
        description:
          - >-
            Each variable value is returned in the form $variable=value, and
            variables are separated by semicolons.
      error:
        description:
          - undefined
        suboptions:
          code:
            description:
              - >-
                An identifier for the error. Codes are invariant and are
                intended to be consumed programmatically.
            required: true
          message:
            description:
              - >-
                A message describing the error, intended to be suitable for
                display in a user interface.
            required: true
          details:
            description:
              - undefined
            type: list
            suboptions:
              code:
                description:
                  - >-
                    An identifier for the error. Codes are invariant and are
                    intended to be consumed programmatically.
                required: true
              message:
                description:
                  - >-
                    A message describing the error, intended to be suitable for
                    display in a user interface.
                required: true
              details:
                description:
                  - undefined
                type: list
  inter_node_communication:
    description:
      - >-
        This imposes restrictions on which nodes can be assigned to the pool.
        Enabling this value can reduce the chance of the requested number of
        nodes to be allocated in the pool. If not specified, this value defaults
        to 'Disabled'.
  network_configuration:
    description:
      - undefined
    suboptions:
      subnet_id:
        description:
          - >-
            The virtual network must be in the same region and subscription as
            the Azure Batch account. The specified subnet should have enough
            free IP addresses to accommodate the number of nodes in the pool. If
            the subnet doesn't have enough free IP addresses, the pool will
            partially allocate compute nodes, and a resize error will occur. The
            'MicrosoftAzureBatch' service principal must have the 'Classic
            Virtual Machine Contributor' Role-Based Access Control (RBAC) role
            for the specified VNet. The specified subnet must allow
            communication from the Azure Batch service to be able to schedule
            tasks on the compute nodes. This can be verified by checking if the
            specified VNet has any associated Network Security Groups (NSG). If
            communication to the compute nodes in the specified subnet is denied
            by an NSG, then the Batch service will set the state of the compute
            nodes to unusable. For pools created via virtualMachineConfiguration
            the Batch account must have poolAllocationMode userSubscription in
            order to use a VNet. If the specified VNet has any associated
            Network Security Groups (NSG), then a few reserved system ports must
            be enabled for inbound communication. For pools created with a
            virtual machine configuration, enable ports 29876 and 29877, as well
            as port 22 for Linux and port 3389 for Windows. For pools created
            with a cloud service configuration, enable ports 10100, 20100, and
            30100. Also enable outbound connections to Azure Storage on port
            443. For more details see:
            https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration
      endpoint_configuration:
        description:
          - >-
            Pool endpoint configuration is only supported on pools with the
            virtualMachineConfiguration property.
        suboptions:
          inbound_nat_pools:
            description:
              - >-
                The maximum number of inbound NAT pools per Batch pool is 5. If
                the maximum number of inbound NAT pools is exceeded the request
                fails with HTTP status code 400.
            required: true
            type: list
            suboptions:
              name:
                description:
                  - >-
                    The name must be unique within a Batch pool, can contain
                    letters, numbers, underscores, periods, and hyphens. Names
                    must start with a letter or number, must end with a letter,
                    number, or underscore, and cannot exceed 77 characters.  If
                    any invalid values are provided the request fails with HTTP
                    status code 400.
                required: true
              protocol:
                description:
                  - undefined
                required: true
              backend_port:
                description:
                  - >-
                    This must be unique within a Batch pool. Acceptable values
                    are between 1 and 65535 except for 22, 3389, 29876 and 29877
                    as these are reserved. If any reserved values are provided
                    the request fails with HTTP status code 400.
                required: true
              frontend_port_range_start:
                description:
                  - >-
                    Acceptable values range between 1 and 65534 except ports
                    from 50000 to 55000 which are reserved. All ranges within a
                    pool must be distinct and cannot overlap. If any reserved or
                    overlapping values are provided the request fails with HTTP
                    status code 400.
                required: true
              frontend_port_range_end:
                description:
                  - >-
                    Acceptable values range between 1 and 65534 except ports
                    from 50000 to 55000 which are reserved by the Batch service.
                    All ranges within a pool must be distinct and cannot
                    overlap. If any reserved or overlapping values are provided
                    the request fails with HTTP status code 400.
                required: true
              network_security_group_rules:
                description:
                  - >-
                    The maximum number of rules that can be specified across all
                    the endpoints on a Batch pool is 25. If no network security
                    group rules are specified, a default rule will be created to
                    allow inbound access to the specified backendPort. If the
                    maximum number of network security group rules is exceeded
                    the request fails with HTTP status code 400.
                type: list
  max_tasks_per_node:
    description:
      - undefined
  task_scheduling_policy:
    description:
      - undefined
    suboptions:
      node_fill_type:
        description:
          - undefined
        required: true
  user_accounts:
    description:
      - undefined
    type: list
    suboptions:
      name:
        description:
          - undefined
        required: true
      password:
        description:
          - undefined
        required: true
      elevation_level:
        description:
          - >-
            nonAdmin - The auto user is a standard user without elevated access.
            admin - The auto user is a user with elevated access and operates
            with full Administrator permissions. The default value is nonAdmin.
      linux_user_configuration:
        description:
          - >-
            This property is ignored if specified on a Windows pool. If not
            specified, the user is created with the default options.
        suboptions:
          uid:
            description:
              - >-
                The uid and gid properties must be specified together or not at
                all. If not specified the underlying operating system picks the
                uid.
          gid:
            description:
              - >-
                The uid and gid properties must be specified together or not at
                all. If not specified the underlying operating system picks the
                gid.
          ssh_private_key:
            description:
              - >-
                The private key must not be password protected. The private key
                is used to automatically configure asymmetric-key based
                authentication for SSH between nodes in a Linux pool when the
                pool's enableInterNodeCommunication property is true (it is
                ignored if enableInterNodeCommunication is false). It does this
                by placing the key pair into the user's .ssh directory. If not
                specified, password-less SSH is not configured between nodes (no
                modification of the user's .ssh directory is done).
      windows_user_configuration:
        description:
          - >-
            This property can only be specified if the user is on a Windows
            pool. If not specified and on a Windows pool, the user is created
            with the default options.
        suboptions:
          login_mode:
            description:
              - >-
                Specifies login mode for the user. The default value for
                VirtualMachineConfiguration pools is interactive mode and for
                CloudServiceConfiguration pools is batch mode.
  metadata:
    description:
      - >-
        The Batch service does not assign any meaning to metadata; it is solely
        for the use of user code.
    type: list
    suboptions:
      name:
        description:
          - undefined
        required: true
      value:
        description:
          - undefined
        required: true
  start_task:
    description:
      - >-
        In an PATCH (update) operation, this property can be set to an empty
        object to remove the start task from the pool.
    suboptions:
      command_line:
        description:
          - >-
            The command line does not run under a shell, and therefore cannot
            take advantage of shell features such as environment variable
            expansion. If you want to take advantage of such features, you
            should invoke the shell in the command line, for example using "cmd
            /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux.
            Required if any other properties of the startTask are specified.
      resource_files:
        description:
          - undefined
        type: list
        suboptions:
          auto_storage_container_name:
            description:
              - >-
                The autoStorageContainerName, storageContainerUrl and httpUrl
                properties are mutually exclusive and one of them must be
                specified.
          storage_container_url:
            description:
              - >-
                The autoStorageContainerName, storageContainerUrl and httpUrl
                properties are mutually exclusive and one of them must be
                specified. This URL must be readable and listable using
                anonymous access; that is, the Batch service does not present
                any credentials when downloading the blob. There are two ways to
                get such a URL for a blob in Azure storage: include a Shared
                Access Signature (SAS) granting read and list permissions on the
                blob, or set the ACL for the blob or its container to allow
                public access.
          http_url:
            description:
              - >-
                The autoStorageContainerName, storageContainerUrl and httpUrl
                properties are mutually exclusive and one of them must be
                specified. If the URL is Azure Blob Storage, it must be readable
                using anonymous access; that is, the Batch service does not
                present any credentials when downloading the blob. There are two
                ways to get such a URL for a blob in Azure storage: include a
                Shared Access Signature (SAS) granting read permissions on the
                blob, or set the ACL for the blob or its container to allow
                public access.
          blob_prefix:
            description:
              - >-
                The property is valid only when autoStorageContainerName or
                storageContainerUrl is used. This prefix can be a partial
                filename or a subdirectory. If a prefix is not specified, all
                the files in the container will be downloaded.
          file_path:
            description:
              - >-
                If the httpUrl property is specified, the filePath is required
                and describes the path which the file will be downloaded to,
                including the filename. Otherwise, if the
                autoStorageContainerName or storageContainerUrl property is
                specified, filePath is optional and is the directory to download
                the files to. In the case where filePath is used as a directory,
                any directory structure already associated with the input data
                will be retained in full and appended to the specified filePath
                directory. The specified relative path cannot break out of the
                task's working directory (for example by using '..').
          file_mode:
            description:
              - >-
                This property applies only to files being downloaded to Linux
                compute nodes. It will be ignored if it is specified for a
                resourceFile which will be downloaded to a Windows node. If this
                property is not specified for a Linux node, then a default value
                of 0770 is applied to the file.
      environment_settings:
        description:
          - undefined
        type: list
        suboptions:
          name:
            description:
              - undefined
            required: true
          value:
            description:
              - undefined
      user_identity:
        description:
          - >-
            If omitted, the task runs as a non-administrative user unique to the
            task.
        suboptions:
          user_name:
            description:
              - >-
                The userName and autoUser properties are mutually exclusive; you
                must specify one but not both.
          auto_user:
            description:
              - >-
                The userName and autoUser properties are mutually exclusive; you
                must specify one but not both.
            suboptions:
              scope:
                description:
                  - The default value is task.
              elevation_level:
                description:
                  - >-
                    nonAdmin - The auto user is a standard user without elevated
                    access. admin - The auto user is a user with elevated access
                    and operates with full Administrator permissions. The
                    default value is nonAdmin.
      max_task_retry_count:
        description:
          - >-
            The Batch service retries a task if its exit code is nonzero. Note
            that this value specifically controls the number of retries. The
            Batch service will try the task once, and may then retry up to this
            limit. For example, if the maximum retry count is 3, Batch tries the
            task up to 4 times (one initial try and 3 retries). If the maximum
            retry count is 0, the Batch service does not retry the task. If the
            maximum retry count is -1, the Batch service retries the task
            without limit.
      wait_for_success:
        description:
          - >-
            If true and the start task fails on a compute node, the Batch
            service retries the start task up to its maximum retry count
            (maxTaskRetryCount). If the task has still not completed
            successfully after all retries, then the Batch service marks the
            compute node unusable, and will not schedule tasks to it. This
            condition can be detected via the node state and scheduling error
            detail. If false, the Batch service will not wait for the start task
            to complete. In this case, other tasks can start executing on the
            compute node while the start task is still running; and even if the
            start task fails, new tasks will continue to be scheduled on the
            node. The default is false.
      container_settings:
        description:
          - >-
            When this is specified, all directories recursively below the
            AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the
            node) are mapped into the container, all task environment variables
            are mapped into the container, and the task command line is executed
            in the container.
        suboptions:
          container_run_options:
            description:
              - >-
                These additional options are supplied as arguments to the
                "docker create" command, in addition to those controlled by the
                Batch Service.
          image_name:
            description:
              - >-
                This is the full image reference, as would be specified to
                "docker pull". If no tag is provided as part of the image name,
                the tag ":latest" is used as a default.
            required: true
          registry:
            description:
              - >-
                This setting can be omitted if was already provided at pool
                creation.
            suboptions:
              registry_server:
                description:
                  - 'If omitted, the default is "docker.io".'
              username:
                description:
                  - undefined
                required: true
              password:
                description:
                  - undefined
                required: true
  certificates:
    description:
      - >-
        For Windows compute nodes, the Batch service installs the certificates
        to the specified certificate store and location. For Linux compute
        nodes, the certificates are stored in a directory inside the task
        working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR
        is supplied to the task to query for this location. For certificates
        with visibility of 'remoteUser', a 'certs' directory is created in the
        user's home directory (e.g., /home/{user-name}/certs) and certificates
        are placed in that directory.
    type: list
    suboptions:
      id:
        description:
          - undefined
        required: true
      store_location:
        description:
          - >-
            The default value is currentUser. This property is applicable only
            for pools configured with Windows nodes (that is, created with
            cloudServiceConfiguration, or with virtualMachineConfiguration using
            a Windows image reference). For Linux compute nodes, the
            certificates are stored in a directory inside the task working
            directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is
            supplied to the task to query for this location. For certificates
            with visibility of 'remoteUser', a 'certs' directory is created in
            the user's home directory (e.g., /home/{user-name}/certs) and
            certificates are placed in that directory.
      store_name:
        description:
          - >-
            This property is applicable only for pools configured with Windows
            nodes (that is, created with cloudServiceConfiguration, or with
            virtualMachineConfiguration using a Windows image reference). Common
            store names include: My, Root, CA, Trust, Disallowed, TrustedPeople,
            TrustedPublisher, AuthRoot, AddressBook, but any custom store name
            can also be used. The default value is My.
      visibility:
        description:
          - undefined
        type: list
  application_packages:
    description:
      - >-
        Changes to application packages affect all new compute nodes joining the
        pool, but do not affect compute nodes that are already in the pool until
        they are rebooted or reimaged.
    type: list
    suboptions:
      id:
        description:
          - undefined
        required: true
      version:
        description:
          - >-
            If this is omitted, and no default version is specified for this
            application, the request fails with the error code
            InvalidApplicationPackageReferences. If you are calling the REST API
            directly, the HTTP status code is 409.
  application_licenses:
    description:
      - >-
        The list of application licenses must be a subset of available Batch
        service application licenses. If a license is requested which is not
        supported, pool creation will fail.
    type: list
  resize_operation_status:
    description:
      - undefined
    suboptions:
      target_dedicated_nodes:
        description:
          - undefined
      target_low_priority_nodes:
        description:
          - undefined
      resize_timeout:
        description:
          - >-
            The default value is 15 minutes. The minimum value is 5 minutes. If
            you specify a value less than 5 minutes, the Batch service returns
            an error; if you are calling the REST API directly, the HTTP status
            code is 400 (Bad Request).
      node_deallocation_option:
        description:
          - The default value is requeue.
      start_time:
        description:
          - undefined
      errors:
        description:
          - >-
            This property is set only if an error occurred during the last pool
            resize, and only when the pool allocationState is Steady.
        type: list
        suboptions:
          code:
            description:
              - >-
                An identifier for the error. Codes are invariant and are
                intended to be consumed programmatically.
            required: true
          message:
            description:
              - >-
                A message describing the error, intended to be suitable for
                display in a user interface.
            required: true
          details:
            description:
              - undefined
            type: list
            suboptions:
              code:
                description:
                  - >-
                    An identifier for the error. Codes are invariant and are
                    intended to be consumed programmatically.
                required: true
              message:
                description:
                  - >-
                    A message describing the error, intended to be suitable for
                    display in a user interface.
                required: true
              details:
                description:
                  - undefined
                type: list
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ListPool
  azure_rm_batchpool_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: testpool
- name: ListPoolWithFilter
  azure_rm_batchpool_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: testpool
- name: GetPool
  azure_rm_batchpool_info:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool

'''

RETURN = '''
pool:
  description: >-
    A list of dict results where the key is the name of the Pool and the values
    are the facts for that Pool.
  returned: always
  type: complex
  contains:
    pool_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - The ID of the resource.
          returned: always
          type: str
          sample: null
        name:
          description:
            - The name of the resource.
          returned: always
          type: str
          sample: null
        type:
          description:
            - The type of the resource.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - 'The ETag of the resource, used for concurrency statements.'
          returned: always
          type: str
          sample: null
        properties:
          description:
            - The properties associated with the pool.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMPoolInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=true
            ),
            account_name=dict(
                type='str',
                required=true
            ),
            maxresults=dict(
                type='number'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.account_name = None
        self.maxresults = None
        self.name = None
        self.id = None
        self.etag = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMPoolInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.account_name is not None and
            self.name is not None):
            self.results['pool'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.account_name is not None):
            self.results['pool'] = self.format_item(self.listbybatchaccount())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/batchAccounts' +
                    '/{{ batch_account_name }}' +
                    '/pools' +
                    '/{{ pool_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ batch_account_name }}', self.batch_account_name)
        self.url = self.url.replace('{{ pool_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbybatchaccount(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.Batch' +
                    '/batchAccounts' +
                    '/{{ batch_account_name }}' +
                    '/pools')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ batch_account_name }}', self.batch_account_name)
        self.url = self.url.replace('{{ pool_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMPoolInfo()


if __name__ == '__main__':
    main()
