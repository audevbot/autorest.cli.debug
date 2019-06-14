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
module: azure_rm_batchpool
version_added: '2.9'
short_description: Manage Azure Pool instance.
description:
  - 'Create, update and delete instance of Azure Pool.'
options:
  resource_group:
    description:
      - The name of the resource group that contains the Batch account.
    required: true
  account_name:
    description:
      - The name of the Batch account.
    required: true
  name:
    description:
      - The pool name. This must be unique within the account.
    required: true
  display_name:
    description:
      - >-
        The display name need not be unique and can contain any Unicode
        characters up to a maximum length of 1024.
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
                  - 'Values are:'
                  - ''
                  - ' none - The caching mode for the disk is not enabled.'
                  - ' readOnly - The caching mode for the disk is read only.'
                  - ' readWrite - The caching mode for the disk is read and write.'
                  - ''
                  - ' The default value for caching is none. For information about the caching options see: https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/.'
              disk_size_gb:
                description:
                  - undefined
                required: true
              storage_account_type:
                description:
                  - 'If omitted, the default is "Standard_LRS". Values are:'
                  - ''
                  - ' Standard_LRS - The data disk should use standard locally redundant storage.'
                  - ' Premium_LRS - The data disk should use premium locally redundant storage.'
          license_type:
            description:
              - >-
                This only applies to images that contain the Windows operating
                system, and should only be used when you hold valid on-premises
                licenses for the nodes which will be deployed. If omitted, no
                on-premises licensing discount is applied. Values are:
              - ''
              - ' Windows_Server - The on-premises license is for Windows Server.'
              - ' Windows_Client - The on-premises license is for Windows Client.'
              - ''
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
  current_dedicated_nodes:
    description:
      - undefined
  current_low_priority_nodes:
    description:
      - undefined
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
  id:
    description:
      - The ID of the resource.
  etag:
    description:
      - 'The ETag of the resource, used for concurrency statements.'
  state:
    description:
      - Assert the state of the Pool.
      - Use C(present) to create or update an Pool and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: CreatePool - Minimal CloudServiceConfiguration
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    vm_size: STANDARD_D4
    deployment_configuration:
      cloud_service_configuration:
        os_family: '5'
    scale_settings:
      fixed_scale:
        target_dedicated_nodes: '3'
- name: CreatePool - Minimal VirtualMachineConfiguration
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    vm_size: STANDARD_D4
    deployment_configuration:
      virtual_machine_configuration:
        image_reference:
          publisher: Canonical
          offer: UbuntuServer
          sku: 14.04.5-LTS
          version: latest
        node_agent_sku_id: batch.node.ubuntu 14.04
    scale_settings:
      auto_scale:
        formula: $TargetDedicatedNodes=1
        evaluation_interval: PT5M
- name: CreatePool - Full Example
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    display_name: my-pool-name
    vm_size: STANDARD_D4
    deployment_configuration:
      cloud_service_configuration:
        os_family: '4'
        os_version: WA-GUEST-OS-4.45_201708-01
    scale_settings:
      fixed_scale:
        resize_timeout: PT8M
        target_dedicated_nodes: '6'
        target_low_priority_nodes: '28'
        node_deallocation_option: TaskCompletion
    inter_node_communication: Enabled
    network_configuration:
      subnet_id: >-
        /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
        }}/providers/Microsoft.Network/virtualNetworks/{{ virtual_network_name
        }}/subnets/{{ subnet_name }}
      endpoint_configuration:
        inbound_nat_pools:
          - name: testnat
            protocol: TCP
            backend_port: '12001'
            frontend_port_range_start: '15000'
            frontend_port_range_end: '15100'
            network_security_group_rules:
              - access: Allow
                sourceAddressPrefix: 192.100.12.45
                priority: '150'
              - access: Deny
                sourceAddressPrefix: '*'
                priority: '3500'
    max_tasks_per_node: '13'
    task_scheduling_policy:
      node_fill_type: Pack
    user_accounts:
      - name: username1
        password: examplepassword
        elevation_level: Admin
        linux_user_configuration:
          uid: '1234'
          gid: '4567'
          ssh_private_key: sshprivatekeyvalue
    metadata:
      - name: metadata-1
        value: value-1
      - name: metadata-2
        value: value-2
    start_task:
      command_line: cmd /c SET
      resource_files:
        - http_url: 'https://testaccount.blob.core.windows.net/example-blob-file'
          file_path: 'c:\temp\gohere'
          file_mode: '777'
      environment_settings:
        - name: MYSET
          value: '1234'
      user_identity:
        auto_user:
          scope: Pool
          elevation_level: Admin
      max_task_retry_count: '6'
      wait_for_success: true
    certificates:
      - id: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Batch/batchAccounts/{{ batch_account_name
          }}/pools/{{ pool_name }}/certificates/{{ certificate_name }}
        store_location: LocalMachine
        store_name: MY
        visibility:
          - RemoteUser
    application_packages:
      - id: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Batch/batchAccounts/{{ batch_account_name
          }}/pools/{{ pool_name }}/applications/{{ application_name }}
        version: asdf
    application_licenses:
      - app-license0
      - app-license1
- name: CreatePool - Custom Image
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    vm_size: STANDARD_D4
    deployment_configuration:
      virtual_machine_configuration:
        image_reference:
          id: >-
            /subscriptions/{{ subscription_id }}/resourceGroups/{{
            resource_group }}/providers/Microsoft.Compute/images/{{ image_name
            }}
        node_agent_sku_id: batch.node.ubuntu 14.04
- name: CreatePool - Full VirtualMachineConfiguration
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    vm_size: STANDARD_D4
    deployment_configuration:
      virtual_machine_configuration:
        image_reference:
          publisher: MicrosoftWindowsServer
          offer: WindowsServer
          sku: 2016-Datacenter-SmallDisk
          version: latest
        node_agent_sku_id: batch.node.windows amd64
        windows_configuration:
          enable_automatic_updates: false
        data_disks:
          - lun: '0'
            caching: ReadWrite
            disk_size_gb: '30'
            storage_account_type: Premium_LRS
          - lun: '1'
            caching: None
            disk_size_gb: '200'
            storage_account_type: Standard_LRS
        license_type: Windows_Server
    scale_settings:
      auto_scale:
        formula: $TargetDedicatedNodes=1
        evaluation_interval: PT5M
    network_configuration:
      endpoint_configuration:
        inbound_nat_pools:
          - name: testnat
            protocol: TCP
            backend_port: '12001'
            frontend_port_range_start: '15000'
            frontend_port_range_end: '15100'
            network_security_group_rules:
              - access: Allow
                sourceAddressPrefix: 192.100.12.45
                priority: '150'
              - access: Deny
                sourceAddressPrefix: '*'
                priority: '3500'
- name: UpdatePool - Resize Pool
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    scale_settings:
      fixed_scale:
        resize_timeout: PT8M
        target_dedicated_nodes: '5'
        target_low_priority_nodes: '0'
        node_deallocation_option: TaskCompletion
- name: UpdatePool - Enable Autoscale
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    scale_settings:
      auto_scale:
        formula: $TargetDedicatedNodes=34
- name: UpdatePool - Remove Start Task
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    start_task: {}
- name: UpdatePool - Other Properties
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    metadata:
      - name: key1
        value: value1
    certificates:
      - id: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Batch/batchAccounts/{{ batch_account_name
          }}/pools/{{ pool_name }}/certificates/{{ certificate_name }}
        store_location: LocalMachine
        store_name: MY
    application_packages:
      - id: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Batch/batchAccounts/{{ batch_account_name
          }}/pools/{{ pool_name }}/applications/{{ application_name }}
      - id: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Batch/batchAccounts/{{ batch_account_name
          }}/pools/{{ pool_name }}/applications/{{ application_name }}
        version: '1.0'
- name: DeletePool
  azure_rm_batchpool:
    resource_group: myResourceGroup
    account_name: myBatchAccount
    name: myPool
    state: absent

'''

RETURN = '''
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
  contains:
    display_name:
      description:
        - >-
          The display name need not be unique and can contain any Unicode
          characters up to a maximum length of 1024.
      returned: always
      type: str
      sample: null
    last_modified:
      description:
        - >-
          This is the last time at which the pool level data, such as the
          targetDedicatedNodes or autoScaleSettings, changed. It does not factor
          in node-level changes such as a compute node changing state.
      returned: always
      type: datetime
      sample: null
    creation_time:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: datetime
      sample: null
    provisioning_state:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: str
      sample: null
    provisioning_state_transition_time:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: datetime
      sample: null
    allocation_state:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: str
      sample: null
    allocation_state_transition_time:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: datetime
      sample: null
    vm_size:
      description:
        - >-
          For information about available sizes of virtual machines for Cloud
          Services pools (pools created with cloudServiceConfiguration), see
          Sizes for Cloud Services
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
      returned: always
      type: str
      sample: null
    deployment_configuration:
      description:
        - >-
          Using CloudServiceConfiguration specifies that the nodes should be
          creating using Azure Cloud Services (PaaS), while
          VirtualMachineConfiguration uses Azure Virtual Machines (IaaS).
      returned: always
      type: dict
      sample: null
      contains:
        cloud_service_configuration:
          description:
            - >-
              This property and virtualMachineConfiguration are mutually
              exclusive and one of the properties must be specified. This
              property cannot be specified if the Batch account was created with
              its poolAllocationMode property set to 'UserSubscription'.
          returned: always
          type: dict
          sample: null
          contains:
            os_family:
              description:
                - >-
                  Possible values are: 2 - OS Family 2, equivalent to Windows
                  Server 2008 R2 SP1. 3 - OS Family 3, equivalent to Windows
                  Server 2012. 4 - OS Family 4, equivalent to Windows Server
                  2012 R2. 5 - OS Family 5, equivalent to Windows Server 2016.
                  For more information, see Azure Guest OS Releases
                  (https://azure.microsoft.com/documentation/articles/cloud-services-guestos-update-matrix/#releases).
              returned: always
              type: str
              sample: null
            os_version:
              description:
                - >-
                  The default value is * which specifies the latest operating
                  system version for the specified OS family.
              returned: always
              type: str
              sample: null
        virtual_machine_configuration:
          description:
            - >-
              This property and cloudServiceConfiguration are mutually exclusive
              and one of the properties must be specified.
          returned: always
          type: dict
          sample: null
          contains:
            image_reference:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: dict
              sample: null
              contains:
                publisher:
                  description:
                    - 'For example, Canonical or MicrosoftWindowsServer.'
                  returned: always
                  type: str
                  sample: null
                offer:
                  description:
                    - 'For example, UbuntuServer or WindowsServer.'
                  returned: always
                  type: str
                  sample: null
                sku:
                  description:
                    - 'For example, 14.04.0-LTS or 2012-R2-Datacenter.'
                  returned: always
                  type: str
                  sample: null
                version:
                  description:
                    - >-
                      A value of 'latest' can be specified to select the latest
                      version of an image. If omitted, the default is 'latest'.
                  returned: always
                  type: str
                  sample: null
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
                  returned: always
                  type: str
                  sample: null
            node_agent_sku_id:
              description:
                - >-
                  The Batch node agent is a program that runs on each node in
                  the pool, and provides the command-and-control interface
                  between the node and the Batch service. There are different
                  implementations of the node agent, known as SKUs, for
                  different operating systems. You must specify a node agent SKU
                  which matches the selected image reference. To get the list of
                  supported node agent SKUs along with their list of verified
                  image references, see the 'List supported node agent SKUs'
                  operation.
              returned: always
              type: str
              sample: null
            windows_configuration:
              description:
                - >-
                  This property must not be specified if the imageReference
                  specifies a Linux OS image.
              returned: always
              type: dict
              sample: null
              contains:
                enable_automatic_updates:
                  description:
                    - 'If omitted, the default value is true.'
                  returned: always
                  type: boolean
                  sample: null
            data_disks:
              description:
                - >-
                  This property must be specified if the compute nodes in the
                  pool need to have empty data disks attached to them.
              returned: always
              type: dict
              sample: null
              contains:
                lun:
                  description:
                    - >-
                      The lun is used to uniquely identify each data disk. If
                      attaching multiple disks, each should have a distinct lun.
                  returned: always
                  type: number
                  sample: null
                caching:
                  description:
                    - |-
                      Values are:

                       none - The caching mode for the disk is not enabled.
                       readOnly - The caching mode for the disk is read only.
                       readWrite - The caching mode for the disk is read and write.

                       The default value for caching is none. For information about the caching options see: https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/.
                  returned: always
                  type: str
                  sample: null
                disk_size_gb:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: number
                  sample: null
                storage_account_type:
                  description:
                    - |-
                      If omitted, the default is "Standard_LRS". Values are:

                       Standard_LRS - The data disk should use standard locally redundant storage.
                       Premium_LRS - The data disk should use premium locally redundant storage.
                  returned: always
                  type: str
                  sample: null
            license_type:
              description:
                - >
                  This only applies to images that contain the Windows operating
                  system, and should only be used when you hold valid
                  on-premises licenses for the nodes which will be deployed. If
                  omitted, no on-premises licensing discount is applied. Values
                  are:

                   Windows_Server - The on-premises license is for Windows Server.
                   Windows_Client - The on-premises license is for Windows Client.
              returned: always
              type: str
              sample: null
            container_configuration:
              description:
                - >-
                  If specified, setup is performed on each node in the pool to
                  allow tasks to run in containers. All regular tasks and job
                  manager tasks run on this pool must specify the
                  containerSettings property, and all other tasks may specify
                  it.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: str
                  sample: null
                container_image_names:
                  description:
                    - >-
                      This is the full image reference, as would be specified to
                      "docker pull". An image will be sourced from the default
                      Docker registry unless the image is fully qualified with
                      an alternative registry.
                  returned: always
                  type: str
                  sample: null
                container_registries:
                  description:
                    - >-
                      If any images must be downloaded from a private registry
                      which requires credentials, then those credentials must be
                      provided here.
                  returned: always
                  type: dict
                  sample: null
    current_dedicated_nodes:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: number
      sample: null
    current_low_priority_nodes:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: number
      sample: null
    scale_settings:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        fixed_scale:
          description:
            - >-
              This property and autoScale are mutually exclusive and one of the
              properties must be specified.
          returned: always
          type: dict
          sample: null
          contains:
            resize_timeout:
              description:
                - >-
                  The default value is 15 minutes. Timeout values use ISO 8601
                  format. For example, use PT10M for 10 minutes. The minimum
                  value is 5 minutes. If you specify a value less than 5
                  minutes, the Batch service rejects the request with an error;
                  if you are calling the REST API directly, the HTTP status code
                  is 400 (Bad Request).
              returned: always
              type: 'unknown-primary[timeSpan]'
              sample: null
            target_dedicated_nodes:
              description:
                - >-
                  At least one of targetDedicatedNodes, targetLowPriority nodes
                  must be set.
              returned: always
              type: number
              sample: null
            target_low_priority_nodes:
              description:
                - >-
                  At least one of targetDedicatedNodes, targetLowPriority nodes
                  must be set.
              returned: always
              type: number
              sample: null
            node_deallocation_option:
              description:
                - 'If omitted, the default value is Requeue.'
              returned: always
              type: str
              sample: null
        auto_scale:
          description:
            - >-
              This property and fixedScale are mutually exclusive and one of the
              properties must be specified.
          returned: always
          type: dict
          sample: null
          contains:
            formula:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: str
              sample: null
            evaluation_interval:
              description:
                - 'If omitted, the default value is 15 minutes (PT15M).'
              returned: always
              type: 'unknown-primary[timeSpan]'
              sample: null
    auto_scale_run:
      description:
        - >-
          This property is set only if the pool automatically scales, i.e.
          autoScaleSettings are used.
      returned: always
      type: dict
      sample: null
      contains:
        evaluation_time:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: datetime
          sample: null
        results:
          description:
            - >-
              Each variable value is returned in the form $variable=value, and
              variables are separated by semicolons.
          returned: always
          type: str
          sample: null
        error:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - >-
                  An identifier for the error. Codes are invariant and are
                  intended to be consumed programmatically.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  A message describing the error, intended to be suitable for
                  display in a user interface.
              returned: always
              type: str
              sample: null
            details:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: dict
              sample: null
              contains:
                code:
                  description:
                    - >-
                      An identifier for the error. Codes are invariant and are
                      intended to be consumed programmatically.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      A message describing the error, intended to be suitable
                      for display in a user interface.
                  returned: always
                  type: str
                  sample: null
                details:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: dict
                  sample: null
    inter_node_communication:
      description:
        - >-
          This imposes restrictions on which nodes can be assigned to the pool.
          Enabling this value can reduce the chance of the requested number of
          nodes to be allocated in the pool. If not specified, this value
          defaults to 'Disabled'.
      returned: always
      type: str
      sample: null
    network_configuration:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        subnet_id:
          description:
            - >-
              The virtual network must be in the same region and subscription as
              the Azure Batch account. The specified subnet should have enough
              free IP addresses to accommodate the number of nodes in the pool.
              If the subnet doesn't have enough free IP addresses, the pool will
              partially allocate compute nodes, and a resize error will occur.
              The 'MicrosoftAzureBatch' service principal must have the 'Classic
              Virtual Machine Contributor' Role-Based Access Control (RBAC) role
              for the specified VNet. The specified subnet must allow
              communication from the Azure Batch service to be able to schedule
              tasks on the compute nodes. This can be verified by checking if
              the specified VNet has any associated Network Security Groups
              (NSG). If communication to the compute nodes in the specified
              subnet is denied by an NSG, then the Batch service will set the
              state of the compute nodes to unusable. For pools created via
              virtualMachineConfiguration the Batch account must have
              poolAllocationMode userSubscription in order to use a VNet. If the
              specified VNet has any associated Network Security Groups (NSG),
              then a few reserved system ports must be enabled for inbound
              communication. For pools created with a virtual machine
              configuration, enable ports 29876 and 29877, as well as port 22
              for Linux and port 3389 for Windows. For pools created with a
              cloud service configuration, enable ports 10100, 20100, and 30100.
              Also enable outbound connections to Azure Storage on port 443. For
              more details see:
              https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration
          returned: always
          type: str
          sample: null
        endpoint_configuration:
          description:
            - >-
              Pool endpoint configuration is only supported on pools with the
              virtualMachineConfiguration property.
          returned: always
          type: dict
          sample: null
          contains:
            inbound_nat_pools:
              description:
                - >-
                  The maximum number of inbound NAT pools per Batch pool is 5.
                  If the maximum number of inbound NAT pools is exceeded the
                  request fails with HTTP status code 400.
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - >-
                      The name must be unique within a Batch pool, can contain
                      letters, numbers, underscores, periods, and hyphens. Names
                      must start with a letter or number, must end with a
                      letter, number, or underscore, and cannot exceed 77
                      characters.  If any invalid values are provided the
                      request fails with HTTP status code 400.
                  returned: always
                  type: str
                  sample: null
                protocol:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: str
                  sample: null
                backend_port:
                  description:
                    - >-
                      This must be unique within a Batch pool. Acceptable values
                      are between 1 and 65535 except for 22, 3389, 29876 and
                      29877 as these are reserved. If any reserved values are
                      provided the request fails with HTTP status code 400.
                  returned: always
                  type: number
                  sample: null
                frontend_port_range_start:
                  description:
                    - >-
                      Acceptable values range between 1 and 65534 except ports
                      from 50000 to 55000 which are reserved. All ranges within
                      a pool must be distinct and cannot overlap. If any
                      reserved or overlapping values are provided the request
                      fails with HTTP status code 400.
                  returned: always
                  type: number
                  sample: null
                frontend_port_range_end:
                  description:
                    - >-
                      Acceptable values range between 1 and 65534 except ports
                      from 50000 to 55000 which are reserved by the Batch
                      service. All ranges within a pool must be distinct and
                      cannot overlap. If any reserved or overlapping values are
                      provided the request fails with HTTP status code 400.
                  returned: always
                  type: number
                  sample: null
                network_security_group_rules:
                  description:
                    - >-
                      The maximum number of rules that can be specified across
                      all the endpoints on a Batch pool is 25. If no network
                      security group rules are specified, a default rule will be
                      created to allow inbound access to the specified
                      backendPort. If the maximum number of network security
                      group rules is exceeded the request fails with HTTP status
                      code 400.
                  returned: always
                  type: dict
                  sample: null
    max_tasks_per_node:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: number
      sample: null
    task_scheduling_policy:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        node_fill_type:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
    user_accounts:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        password:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        elevation_level:
          description:
            - >-
              nonAdmin - The auto user is a standard user without elevated
              access. admin - The auto user is a user with elevated access and
              operates with full Administrator permissions. The default value is
              nonAdmin.
          returned: always
          type: str
          sample: null
        linux_user_configuration:
          description:
            - >-
              This property is ignored if specified on a Windows pool. If not
              specified, the user is created with the default options.
          returned: always
          type: dict
          sample: null
          contains:
            uid:
              description:
                - >-
                  The uid and gid properties must be specified together or not
                  at all. If not specified the underlying operating system picks
                  the uid.
              returned: always
              type: number
              sample: null
            gid:
              description:
                - >-
                  The uid and gid properties must be specified together or not
                  at all. If not specified the underlying operating system picks
                  the gid.
              returned: always
              type: number
              sample: null
            ssh_private_key:
              description:
                - >-
                  The private key must not be password protected. The private
                  key is used to automatically configure asymmetric-key based
                  authentication for SSH between nodes in a Linux pool when the
                  pool's enableInterNodeCommunication property is true (it is
                  ignored if enableInterNodeCommunication is false). It does
                  this by placing the key pair into the user's .ssh directory.
                  If not specified, password-less SSH is not configured between
                  nodes (no modification of the user's .ssh directory is done).
              returned: always
              type: str
              sample: null
        windows_user_configuration:
          description:
            - >-
              This property can only be specified if the user is on a Windows
              pool. If not specified and on a Windows pool, the user is created
              with the default options.
          returned: always
          type: dict
          sample: null
          contains:
            login_mode:
              description:
                - >-
                  Specifies login mode for the user. The default value for
                  VirtualMachineConfiguration pools is interactive mode and for
                  CloudServiceConfiguration pools is batch mode.
              returned: always
              type: str
              sample: null
    metadata:
      description:
        - >-
          The Batch service does not assign any meaning to metadata; it is
          solely for the use of user code.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        value:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
    start_task:
      description:
        - >-
          In an PATCH (update) operation, this property can be set to an empty
          object to remove the start task from the pool.
      returned: always
      type: dict
      sample: null
      contains:
        command_line:
          description:
            - >-
              The command line does not run under a shell, and therefore cannot
              take advantage of shell features such as environment variable
              expansion. If you want to take advantage of such features, you
              should invoke the shell in the command line, for example using
              "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux.
              Required if any other properties of the startTask are specified.
          returned: always
          type: str
          sample: null
        resource_files:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: dict
          sample: null
          contains:
            auto_storage_container_name:
              description:
                - >-
                  The autoStorageContainerName, storageContainerUrl and httpUrl
                  properties are mutually exclusive and one of them must be
                  specified.
              returned: always
              type: str
              sample: null
            storage_container_url:
              description:
                - >-
                  The autoStorageContainerName, storageContainerUrl and httpUrl
                  properties are mutually exclusive and one of them must be
                  specified. This URL must be readable and listable using
                  anonymous access; that is, the Batch service does not present
                  any credentials when downloading the blob. There are two ways
                  to get such a URL for a blob in Azure storage: include a
                  Shared Access Signature (SAS) granting read and list
                  permissions on the blob, or set the ACL for the blob or its
                  container to allow public access.
              returned: always
              type: str
              sample: null
            http_url:
              description:
                - >-
                  The autoStorageContainerName, storageContainerUrl and httpUrl
                  properties are mutually exclusive and one of them must be
                  specified. If the URL is Azure Blob Storage, it must be
                  readable using anonymous access; that is, the Batch service
                  does not present any credentials when downloading the blob.
                  There are two ways to get such a URL for a blob in Azure
                  storage: include a Shared Access Signature (SAS) granting read
                  permissions on the blob, or set the ACL for the blob or its
                  container to allow public access.
              returned: always
              type: str
              sample: null
            blob_prefix:
              description:
                - >-
                  The property is valid only when autoStorageContainerName or
                  storageContainerUrl is used. This prefix can be a partial
                  filename or a subdirectory. If a prefix is not specified, all
                  the files in the container will be downloaded.
              returned: always
              type: str
              sample: null
            file_path:
              description:
                - >-
                  If the httpUrl property is specified, the filePath is required
                  and describes the path which the file will be downloaded to,
                  including the filename. Otherwise, if the
                  autoStorageContainerName or storageContainerUrl property is
                  specified, filePath is optional and is the directory to
                  download the files to. In the case where filePath is used as a
                  directory, any directory structure already associated with the
                  input data will be retained in full and appended to the
                  specified filePath directory. The specified relative path
                  cannot break out of the task's working directory (for example
                  by using '..').
              returned: always
              type: str
              sample: null
            file_mode:
              description:
                - >-
                  This property applies only to files being downloaded to Linux
                  compute nodes. It will be ignored if it is specified for a
                  resourceFile which will be downloaded to a Windows node. If
                  this property is not specified for a Linux node, then a
                  default value of 0770 is applied to the file.
              returned: always
              type: str
              sample: null
        environment_settings:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: str
              sample: null
            value:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: str
              sample: null
        user_identity:
          description:
            - >-
              If omitted, the task runs as a non-administrative user unique to
              the task.
          returned: always
          type: dict
          sample: null
          contains:
            user_name:
              description:
                - >-
                  The userName and autoUser properties are mutually exclusive;
                  you must specify one but not both.
              returned: always
              type: str
              sample: null
            auto_user:
              description:
                - >-
                  The userName and autoUser properties are mutually exclusive;
                  you must specify one but not both.
              returned: always
              type: dict
              sample: null
              contains:
                scope:
                  description:
                    - The default value is task.
                  returned: always
                  type: str
                  sample: null
                elevation_level:
                  description:
                    - >-
                      nonAdmin - The auto user is a standard user without
                      elevated access. admin - The auto user is a user with
                      elevated access and operates with full Administrator
                      permissions. The default value is nonAdmin.
                  returned: always
                  type: str
                  sample: null
        max_task_retry_count:
          description:
            - >-
              The Batch service retries a task if its exit code is nonzero. Note
              that this value specifically controls the number of retries. The
              Batch service will try the task once, and may then retry up to
              this limit. For example, if the maximum retry count is 3, Batch
              tries the task up to 4 times (one initial try and 3 retries). If
              the maximum retry count is 0, the Batch service does not retry the
              task. If the maximum retry count is -1, the Batch service retries
              the task without limit.
          returned: always
          type: number
          sample: null
        wait_for_success:
          description:
            - >-
              If true and the start task fails on a compute node, the Batch
              service retries the start task up to its maximum retry count
              (maxTaskRetryCount). If the task has still not completed
              successfully after all retries, then the Batch service marks the
              compute node unusable, and will not schedule tasks to it. This
              condition can be detected via the node state and scheduling error
              detail. If false, the Batch service will not wait for the start
              task to complete. In this case, other tasks can start executing on
              the compute node while the start task is still running; and even
              if the start task fails, new tasks will continue to be scheduled
              on the node. The default is false.
          returned: always
          type: boolean
          sample: null
        container_settings:
          description:
            - >-
              When this is specified, all directories recursively below the
              AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the
              node) are mapped into the container, all task environment
              variables are mapped into the container, and the task command line
              is executed in the container.
          returned: always
          type: dict
          sample: null
          contains:
            container_run_options:
              description:
                - >-
                  These additional options are supplied as arguments to the
                  "docker create" command, in addition to those controlled by
                  the Batch Service.
              returned: always
              type: str
              sample: null
            image_name:
              description:
                - >-
                  This is the full image reference, as would be specified to
                  "docker pull". If no tag is provided as part of the image
                  name, the tag ":latest" is used as a default.
              returned: always
              type: str
              sample: null
            registry:
              description:
                - >-
                  This setting can be omitted if was already provided at pool
                  creation.
              returned: always
              type: dict
              sample: null
              contains:
                registry_server:
                  description:
                    - 'If omitted, the default is "docker.io".'
                  returned: always
                  type: str
                  sample: null
                username:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: str
                  sample: null
                password:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: str
                  sample: null
    certificates:
      description:
        - >-
          For Windows compute nodes, the Batch service installs the certificates
          to the specified certificate store and location. For Linux compute
          nodes, the certificates are stored in a directory inside the task
          working directory and an environment variable
          AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this
          location. For certificates with visibility of 'remoteUser', a 'certs'
          directory is created in the user's home directory (e.g.,
          /home/{user-name}/certs) and certificates are placed in that
          directory.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        store_location:
          description:
            - >-
              The default value is currentUser. This property is applicable only
              for pools configured with Windows nodes (that is, created with
              cloudServiceConfiguration, or with virtualMachineConfiguration
              using a Windows image reference). For Linux compute nodes, the
              certificates are stored in a directory inside the task working
              directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is
              supplied to the task to query for this location. For certificates
              with visibility of 'remoteUser', a 'certs' directory is created in
              the user's home directory (e.g., /home/{user-name}/certs) and
              certificates are placed in that directory.
          returned: always
          type: str
          sample: null
        store_name:
          description:
            - >-
              This property is applicable only for pools configured with Windows
              nodes (that is, created with cloudServiceConfiguration, or with
              virtualMachineConfiguration using a Windows image reference).
              Common store names include: My, Root, CA, Trust, Disallowed,
              TrustedPeople, TrustedPublisher, AuthRoot, AddressBook, but any
              custom store name can also be used. The default value is My.
          returned: always
          type: str
          sample: null
        visibility:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
    application_packages:
      description:
        - >-
          Changes to application packages affect all new compute nodes joining
          the pool, but do not affect compute nodes that are already in the pool
          until they are rebooted or reimaged.
      returned: always
      type: dict
      sample: null
      contains:
        id:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: str
          sample: null
        version:
          description:
            - >-
              If this is omitted, and no default version is specified for this
              application, the request fails with the error code
              InvalidApplicationPackageReferences. If you are calling the REST
              API directly, the HTTP status code is 409.
          returned: always
          type: str
          sample: null
    application_licenses:
      description:
        - >-
          The list of application licenses must be a subset of available Batch
          service application licenses. If a license is requested which is not
          supported, pool creation will fail.
      returned: always
      type: str
      sample: null
    resize_operation_status:
      description:
        - !<tag:yaml.org,2002:js/undefined> ''
      returned: always
      type: dict
      sample: null
      contains:
        target_dedicated_nodes:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: number
          sample: null
        target_low_priority_nodes:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: number
          sample: null
        resize_timeout:
          description:
            - >-
              The default value is 15 minutes. The minimum value is 5 minutes.
              If you specify a value less than 5 minutes, the Batch service
              returns an error; if you are calling the REST API directly, the
              HTTP status code is 400 (Bad Request).
          returned: always
          type: 'unknown-primary[timeSpan]'
          sample: null
        node_deallocation_option:
          description:
            - The default value is requeue.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - !<tag:yaml.org,2002:js/undefined> ''
          returned: always
          type: datetime
          sample: null
        errors:
          description:
            - >-
              This property is set only if an error occurred during the last
              pool resize, and only when the pool allocationState is Steady.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - >-
                  An identifier for the error. Codes are invariant and are
                  intended to be consumed programmatically.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  A message describing the error, intended to be suitable for
                  display in a user interface.
              returned: always
              type: str
              sample: null
            details:
              description:
                - !<tag:yaml.org,2002:js/undefined> ''
              returned: always
              type: dict
              sample: null
              contains:
                code:
                  description:
                    - >-
                      An identifier for the error. Codes are invariant and are
                      intended to be consumed programmatically.
                  returned: always
                  type: str
                  sample: null
                message:
                  description:
                    - >-
                      A message describing the error, intended to be suitable
                      for display in a user interface.
                  returned: always
                  type: str
                  sample: null
                details:
                  description:
                    - !<tag:yaml.org,2002:js/undefined> ''
                  returned: always
                  type: dict
                  sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from copy import deepcopy
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.batch import BatchManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMPool(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resource_group_name',
                required=true
            ),
            account_name=dict(
                type='str',
                updatable=False,
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='pool_name',
                required=true
            ),
            display_name=dict(
                type='str',
                disposition='/'
            ),
            vm_size=dict(
                type='str',
                disposition='/'
            ),
            deployment_configuration=dict(
                type='dict',
                disposition='/',
                options=dict(
                    cloud_service_configuration=dict(
                        type='dict',
                        options=dict(
                            os_family=dict(
                                type='str',
                                required=true
                            ),
                            os_version=dict(
                                type='str'
                            )
                        )
                    ),
                    virtual_machine_configuration=dict(
                        type='dict',
                        options=dict(
                            image_reference=dict(
                                type='dict',
                                required=true,
                                options=dict(
                                    publisher=dict(
                                        type='str'
                                    ),
                                    offer=dict(
                                        type='str'
                                    ),
                                    sku=dict(
                                        type='str'
                                    ),
                                    version=dict(
                                        type='str'
                                    ),
                                    id=dict(
                                        type='raw',
                                        pattern=('//subscriptions/{{ subscription_id }}'
                                                 '/resourceGroups/{{ resource_group }}'
                                                 '/providers/Microsoft.Compute/images'
                                                 '/{{ name }}')
                                    )
                                )
                            ),
                            node_agent_sku_id=dict(
                                type='str',
                                required=true
                            ),
                            windows_configuration=dict(
                                type='dict',
                                options=dict(
                                    enable_automatic_updates=dict(
                                        type='boolean'
                                    )
                                )
                            ),
                            data_disks=dict(
                                type='list',
                                options=dict(
                                    lun=dict(
                                        type='number',
                                        required=true
                                    ),
                                    caching=dict(
                                        type='str',
                                        choices=['None',
                                                 'ReadOnly',
                                                 'ReadWrite']
                                    ),
                                    disk_size_gb=dict(
                                        type='number',
                                        required=true
                                    ),
                                    storage_account_type=dict(
                                        type='str',
                                        choices=['Standard_LRS',
                                                 'Premium_LRS']
                                    )
                                )
                            ),
                            license_type=dict(
                                type='str'
                            ),
                            container_configuration=dict(
                                type='dict',
                                options=dict(
                                    type=dict(
                                        type='str',
                                        required=true
                                    ),
                                    container_image_names=dict(
                                        type='list'
                                    ),
                                    container_registries=dict(
                                        type='list'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            scale_settings=dict(
                type='dict',
                disposition='/',
                options=dict(
                    fixed_scale=dict(
                        type='dict',
                        options=dict(
                            resize_timeout=dict(
                                type='unknown-primary[timeSpan]'
                            ),
                            target_dedicated_nodes=dict(
                                type='number'
                            ),
                            target_low_priority_nodes=dict(
                                type='number'
                            ),
                            node_deallocation_option=dict(
                                type='str',
                                choices=['Requeue',
                                         'Terminate',
                                         'TaskCompletion',
                                         'RetainedData']
                            )
                        )
                    ),
                    auto_scale=dict(
                        type='dict',
                        options=dict(
                            formula=dict(
                                type='str',
                                required=true
                            ),
                            evaluation_interval=dict(
                                type='unknown-primary[timeSpan]'
                            )
                        )
                    )
                )
            ),
            inter_node_communication=dict(
                type='str',
                disposition='/',
                choices=['Enabled',
                         'Disabled']
            ),
            network_configuration=dict(
                type='dict',
                disposition='/',
                options=dict(
                    subnet_id=dict(
                        type='raw',
                        pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                                 '/{{ resource_group }}/providers/Microsoft.Network'
                                 '/virtualNetworks/{{ virtual_network_name }}/subnets'
                                 '/{{ name }}')
                    ),
                    endpoint_configuration=dict(
                        type='dict',
                        options=dict(
                            inbound_nat_pools=dict(
                                type='list',
                                required=true,
                                options=dict(
                                    name=dict(
                                        type='str',
                                        required=true
                                    ),
                                    protocol=dict(
                                        type='str',
                                        choices=['TCP',
                                                 'UDP'],
                                        required=true
                                    ),
                                    backend_port=dict(
                                        type='number',
                                        required=true
                                    ),
                                    frontend_port_range_start=dict(
                                        type='number',
                                        required=true
                                    ),
                                    frontend_port_range_end=dict(
                                        type='number',
                                        required=true
                                    ),
                                    network_security_group_rules=dict(
                                        type='list'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            max_tasks_per_node=dict(
                type='number',
                disposition='/'
            ),
            task_scheduling_policy=dict(
                type='dict',
                disposition='/',
                options=dict(
                    node_fill_type=dict(
                        type='str',
                        choices=['Spread',
                                 'Pack'],
                        required=true
                    )
                )
            ),
            user_accounts=dict(
                type='list',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str',
                        required=true
                    ),
                    password=dict(
                        type='str',
                        no_log=True,
                        required=true
                    ),
                    elevation_level=dict(
                        type='str',
                        choices=['NonAdmin',
                                 'Admin']
                    ),
                    linux_user_configuration=dict(
                        type='dict',
                        options=dict(
                            uid=dict(
                                type='number'
                            ),
                            gid=dict(
                                type='number'
                            ),
                            ssh_private_key=dict(
                                type='str'
                            )
                        )
                    ),
                    windows_user_configuration=dict(
                        type='dict',
                        options=dict(
                            login_mode=dict(
                                type='str',
                                choices=['Batch',
                                         'Interactive']
                            )
                        )
                    )
                )
            ),
            metadata=dict(
                type='list',
                disposition='/',
                options=dict(
                    name=dict(
                        type='str',
                        required=true
                    ),
                    value=dict(
                        type='str',
                        required=true
                    )
                )
            ),
            start_task=dict(
                type='dict',
                disposition='/',
                options=dict(
                    command_line=dict(
                        type='str'
                    ),
                    resource_files=dict(
                        type='list',
                        options=dict(
                            auto_storage_container_name=dict(
                                type='str'
                            ),
                            storage_container_url=dict(
                                type='str'
                            ),
                            http_url=dict(
                                type='str'
                            ),
                            blob_prefix=dict(
                                type='str'
                            ),
                            file_path=dict(
                                type='str'
                            ),
                            file_mode=dict(
                                type='str'
                            )
                        )
                    ),
                    environment_settings=dict(
                        type='list',
                        options=dict(
                            name=dict(
                                type='str',
                                required=true
                            ),
                            value=dict(
                                type='str'
                            )
                        )
                    ),
                    user_identity=dict(
                        type='dict',
                        options=dict(
                            user_name=dict(
                                type='str'
                            ),
                            auto_user=dict(
                                type='dict',
                                options=dict(
                                    scope=dict(
                                        type='str',
                                        choices=['Task',
                                                 'Pool']
                                    ),
                                    elevation_level=dict(
                                        type='str',
                                        choices=['NonAdmin',
                                                 'Admin']
                                    )
                                )
                            )
                        )
                    ),
                    max_task_retry_count=dict(
                        type='number'
                    ),
                    wait_for_success=dict(
                        type='boolean'
                    ),
                    container_settings=dict(
                        type='dict',
                        options=dict(
                            container_run_options=dict(
                                type='str'
                            ),
                            image_name=dict(
                                type='str',
                                required=true
                            ),
                            registry=dict(
                                type='dict',
                                options=dict(
                                    registry_server=dict(
                                        type='str'
                                    ),
                                    username=dict(
                                        type='str',
                                        required=true
                                    ),
                                    password=dict(
                                        type='str',
                                        no_log=True,
                                        required=true
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            certificates=dict(
                type='list',
                disposition='/',
                options=dict(
                    id=dict(
                        type='raw',
                        required=true,
                        pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                                 '/{{ resource_group }}/providers/Microsoft.Batch'
                                 '/batchAccounts/{{ batch_account_name }}/pools'
                                 '/{{ pool_name }}/certificates/{{ name }}')
                    ),
                    store_location=dict(
                        type='str',
                        choices=['CurrentUser',
                                 'LocalMachine']
                    ),
                    store_name=dict(
                        type='str'
                    ),
                    visibility=dict(
                        type='list'
                    )
                )
            ),
            application_packages=dict(
                type='list',
                disposition='/',
                options=dict(
                    id=dict(
                        type='raw',
                        required=true,
                        pattern=('//subscriptions/{{ subscription_id }}/resourceGroups'
                                 '/{{ resource_group }}/providers/Microsoft.Batch'
                                 '/batchAccounts/{{ batch_account_name }}/pools'
                                 '/{{ pool_name }}/applications/{{ name }}')
                    ),
                    version=dict(
                        type='str'
                    )
                )
            ),
            application_licenses=dict(
                type='list',
                disposition='/'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.account_name = None
        self.name = None
        self.id = None
        self.etag = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMPool, self).__init__(derived_arg_spec=self.module_arg_spec,
                                          supports_check_mode=True,
                                          supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(BatchManagement,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if self.location is None:
            self.location = resource_group.location

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["etag"] = response["etag"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.pool.create(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        pool_name=self.name,
                                                        parameters=self.body)
            else:
                response = self.mgmt_client.pool.update(resource_group_name=self.resource_group,
                                                        account_name=self.account_name,
                                                        pool_name=self.name,
                                                        parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Pool instance.')
            self.fail('Error creating the Pool instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        # self.log('Deleting the Pool instance {0}'.format(self.))
        try:
            response = self.mgmt_client.pool.delete(resource_group_name=self.resource_group,
                                                    account_name=self.account_name,
                                                    pool_name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Pool instance.')
            self.fail('Error deleting the Pool instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Pool instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.pool.get(resource_group_name=self.resource_group,
                                                 account_name=self.account_name,
                                                 pool_name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMPool()


if __name__ == '__main__':
    main()
