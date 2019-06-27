# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import json

# module equivalent: azure_rm_recoveryservicesreplicationalertsetting
def create_recoveryservices_resourcegroup_vault_replicationalertsetting(cmd, client,
                                                                        resource_name,
                                                                        resource_group,
                                                                        name,
                                                                        send_to_owners=None,
                                                                        custom_email_addresses=None,
                                                                        locale=None):
    body={}
    body['send_to_owners'] = send_to_owners # str
    body['custom_email_addresses'] = json.loads(custom_email_addresses) if isinstance(custom_email_addresses, str) else custom_email_addresses
    body['locale'] = locale # str
    return client.replication_alert_settings.create(resource_name=resource_name, resource_group_name=resource_group, alert_setting_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationalertsetting
def list_recoveryservices_resourcegroup_vault_replicationalertsetting(cmd, client,
                                                                      resource_name,
                                                                      resource_group):
    return client.replication_alert_settings.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationalertsetting
def show_recoveryservices_resourcegroup_vault_replicationalertsetting(cmd, client,
                                                                      resource_name,
                                                                      resource_group,
                                                                      name):
    return client.replication_alert_settings.get(resource_name=resource_name, resource_group_name=resource_group, alert_setting_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationfabric
def create_recoveryservices_resourcegroup_vault_replicationfabric(cmd, client,
                                                                  resource_name,
                                                                  resource_group,
                                                                  name):
    body={}
    return client.replication_fabrics.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationfabric
def delete_recoveryservices_resourcegroup_vault_replicationfabric(cmd, client,
                                                                  resource_name,
                                                                  resource_group,
                                                                  name):
    return client.replication_fabrics.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationfabric
def list_recoveryservices_resourcegroup_vault_replicationfabric(cmd, client,
                                                                resource_name,
                                                                resource_group):
    return client.replication_fabrics.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationfabric
def show_recoveryservices_resourcegroup_vault_replicationfabric(cmd, client,
                                                                resource_name,
                                                                resource_group,
                                                                name):
    return client.replication_fabrics.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationnetworkmapping
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping(cmd, client,
                                                                                                               resource_name,
                                                                                                               resource_group,
                                                                                                               fabric_name,
                                                                                                               network_name,
                                                                                                               name,
                                                                                                               recovery_fabric_name=None,
                                                                                                               recovery_network_id=None):
    body={}
    body['recovery_fabric_name'] = recovery_fabric_name # str
    body['recovery_network_id'] = recovery_network_id # str
    return client.replication_network_mappings.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, network_name=network_name, network_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationnetworkmapping
def update_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping(cmd, client,
                                                                                                               resource_name,
                                                                                                               resource_group,
                                                                                                               fabric_name,
                                                                                                               network_name,
                                                                                                               name,
                                                                                                               recovery_fabric_name=None,
                                                                                                               recovery_network_id=None):
    body={}
    body['recovery_fabric_name'] = recovery_fabric_name # str
    body['recovery_network_id'] = recovery_network_id # str
    return client.replication_network_mappings.update(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, network_name=network_name, network_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationnetworkmapping
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping(cmd, client,
                                                                                                               resource_name,
                                                                                                               resource_group,
                                                                                                               fabric_name,
                                                                                                               network_name,
                                                                                                               name):
    return client.replication_network_mappings.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, network_name=network_name, network_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationnetworkmapping
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping(cmd, client,
                                                                                                             resource_name,
                                                                                                             resource_group,
                                                                                                             fabric_name,
                                                                                                             network_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None and network_name is not None:
        return client.replication_network_mappings.list_by_replication_networks(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, network_name=network_name)
    else:
        return client.replication_network_mappings.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationnetworkmapping
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationnetwork_replicationnetworkmapping(cmd, client,
                                                                                                             resource_name,
                                                                                                             resource_group,
                                                                                                             fabric_name,
                                                                                                             network_name,
                                                                                                             name):
    return client.replication_network_mappings.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, network_name=network_name, network_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainer
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer(cmd, client,
                                                                                                 resource_name,
                                                                                                 resource_group,
                                                                                                 fabric_name,
                                                                                                 name):
    body={}
    return client.replication_protection_containers.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainer
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer(cmd, client,
                                                                                                 resource_name,
                                                                                                 resource_group,
                                                                                                 fabric_name,
                                                                                                 name):
    return client.replication_protection_containers.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainer
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer(cmd, client,
                                                                                               resource_name,
                                                                                               resource_group,
                                                                                               fabric_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None:
        return client.replication_protection_containers.list_by_replication_fabrics(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name)
    else:
        return client.replication_protection_containers.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainer
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer(cmd, client,
                                                                                               resource_name,
                                                                                               resource_group,
                                                                                               fabric_name,
                                                                                               name):
    return client.replication_protection_containers.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationmigrationitem
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem(cmd, client,
                                                                                                                          resource_name,
                                                                                                                          resource_group,
                                                                                                                          fabric_name,
                                                                                                                          protection_container_name,
                                                                                                                          name,
                                                                                                                          policy_id=None):
    body={}
    body['policy_id'] = policy_id # str
    return client.replication_migration_items.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, migration_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationmigrationitem
def update_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem(cmd, client,
                                                                                                                          resource_name,
                                                                                                                          resource_group,
                                                                                                                          fabric_name,
                                                                                                                          protection_container_name,
                                                                                                                          name,
                                                                                                                          policy_id=None):
    body={}
    body['policy_id'] = policy_id # str
    return client.replication_migration_items.update(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, migration_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationmigrationitem
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem(cmd, client,
                                                                                                                          resource_name,
                                                                                                                          resource_group,
                                                                                                                          fabric_name,
                                                                                                                          protection_container_name,
                                                                                                                          name):
    return client.replication_migration_items.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, migration_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationmigrationitem
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem(cmd, client,
                                                                                                                        resource_name,
                                                                                                                        resource_group,
                                                                                                                        fabric_name,
                                                                                                                        protection_container_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None and protection_container_name is not None:
        return client.replication_migration_items.list_by_replication_protection_containers(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name)
    else:
        return client.replication_migration_items.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationmigrationitem
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationmigrationitem(cmd, client,
                                                                                                                        resource_name,
                                                                                                                        resource_group,
                                                                                                                        fabric_name,
                                                                                                                        protection_container_name,
                                                                                                                        name):
    return client.replication_migration_items.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, migration_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotecteditem
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem(cmd, client,
                                                                                                                          resource_name,
                                                                                                                          resource_group,
                                                                                                                          fabric_name,
                                                                                                                          protection_container_name,
                                                                                                                          name,
                                                                                                                          policy_id=None,
                                                                                                                          protectable_item_id=None):
    body={}
    body['policy_id'] = policy_id # str
    body['protectable_item_id'] = protectable_item_id # str
    return client.replication_protected_items.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, replicated_protected_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotecteditem
def update_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem(cmd, client,
                                                                                                                          resource_name,
                                                                                                                          resource_group,
                                                                                                                          fabric_name,
                                                                                                                          protection_container_name,
                                                                                                                          name,
                                                                                                                          policy_id=None,
                                                                                                                          protectable_item_id=None):
    body={}
    body['policy_id'] = policy_id # str
    body['protectable_item_id'] = protectable_item_id # str
    return client.replication_protected_items.update(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, replicated_protected_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotecteditem
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem(cmd, client,
                                                                                                                          resource_name,
                                                                                                                          resource_group,
                                                                                                                          fabric_name,
                                                                                                                          protection_container_name,
                                                                                                                          name):
    return client.replication_protected_items.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, replicated_protected_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotecteditem
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem(cmd, client,
                                                                                                                        resource_name,
                                                                                                                        resource_group,
                                                                                                                        fabric_name,
                                                                                                                        protection_container_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None and protection_container_name is not None:
        return client.replication_protected_items.list_by_replication_protection_containers(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name)
    else:
        return client.replication_protected_items.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationprotecteditem
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotecteditem(cmd, client,
                                                                                                                        resource_name,
                                                                                                                        resource_group,
                                                                                                                        fabric_name,
                                                                                                                        protection_container_name,
                                                                                                                        name):
    return client.replication_protected_items.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, replicated_protected_item_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainermapping
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping(cmd, client,
                                                                                                                                       resource_name,
                                                                                                                                       resource_group,
                                                                                                                                       fabric_name,
                                                                                                                                       protection_container_name,
                                                                                                                                       name,
                                                                                                                                       target_protection_container_id=None,
                                                                                                                                       policy_id=None):
    body={}
    body['target_protection_container_id'] = target_protection_container_id # str
    body['policy_id'] = policy_id # str
    return client.replication_protection_container_mappings.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainermapping
def update_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping(cmd, client,
                                                                                                                                       resource_name,
                                                                                                                                       resource_group,
                                                                                                                                       fabric_name,
                                                                                                                                       protection_container_name,
                                                                                                                                       name,
                                                                                                                                       target_protection_container_id=None,
                                                                                                                                       policy_id=None):
    body={}
    body['target_protection_container_id'] = target_protection_container_id # str
    body['policy_id'] = policy_id # str
    return client.replication_protection_container_mappings.update(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainermapping
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping(cmd, client,
                                                                                                                                       resource_name,
                                                                                                                                       resource_group,
                                                                                                                                       fabric_name,
                                                                                                                                       protection_container_name,
                                                                                                                                       name):
    return client.replication_protection_container_mappings.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainermapping
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping(cmd, client,
                                                                                                                                     resource_name,
                                                                                                                                     resource_group,
                                                                                                                                     fabric_name,
                                                                                                                                     protection_container_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None and protection_container_name is not None:
        return client.replication_protection_container_mappings.list_by_replication_protection_containers(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name)
    else:
        return client.replication_protection_container_mappings.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationprotectioncontainermapping
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationprotectioncontainer_replicationprotectioncontainermapping(cmd, client,
                                                                                                                                     resource_name,
                                                                                                                                     resource_group,
                                                                                                                                     fabric_name,
                                                                                                                                     protection_container_name,
                                                                                                                                     name):
    return client.replication_protection_container_mappings.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, protection_container_name=protection_container_name, mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryservicesprovider
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider(cmd, client,
                                                                                                      resource_name,
                                                                                                      resource_group,
                                                                                                      fabric_name,
                                                                                                      name,
                                                                                                      machine_name=None,
                                                                                                      authentication_identity_input=None,
                                                                                                      resource_access_identity_input=None):
    body={}
    body['machine_name'] = machine_name # str
    body['authentication_identity_input'] = json.loads(authentication_identity_input) if isinstance(authentication_identity_input, str) else authentication_identity_input
    body['resource_access_identity_input'] = json.loads(resource_access_identity_input) if isinstance(resource_access_identity_input, str) else resource_access_identity_input
    return client.replication_recovery_services_providers.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, provider_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryservicesprovider
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider(cmd, client,
                                                                                                      resource_name,
                                                                                                      resource_group,
                                                                                                      fabric_name,
                                                                                                      name):
    return client.replication_recovery_services_providers.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, provider_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryservicesprovider
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider(cmd, client,
                                                                                                    resource_name,
                                                                                                    resource_group,
                                                                                                    fabric_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None:
        return client.replication_recovery_services_providers.list_by_replication_fabrics(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name)
    else:
        return client.replication_recovery_services_providers.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryservicesprovider
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationrecoveryservicesprovider(cmd, client,
                                                                                                    resource_name,
                                                                                                    resource_group,
                                                                                                    fabric_name,
                                                                                                    name):
    return client.replication_recovery_services_providers.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, provider_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationstorageclassificationmapping
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping(cmd, client,
                                                                                                                                           resource_name,
                                                                                                                                           resource_group,
                                                                                                                                           fabric_name,
                                                                                                                                           storage_classification_name,
                                                                                                                                           name,
                                                                                                                                           target_storage_classification_id=None):
    body={}
    body['target_storage_classification_id'] = target_storage_classification_id # str
    return client.replication_storage_classification_mappings.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, storage_classification_name=storage_classification_name, storage_classification_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationstorageclassificationmapping
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping(cmd, client,
                                                                                                                                           resource_name,
                                                                                                                                           resource_group,
                                                                                                                                           fabric_name,
                                                                                                                                           storage_classification_name,
                                                                                                                                           name):
    return client.replication_storage_classification_mappings.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, storage_classification_name=storage_classification_name, storage_classification_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationstorageclassificationmapping
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping(cmd, client,
                                                                                                                                         resource_name,
                                                                                                                                         resource_group,
                                                                                                                                         fabric_name,
                                                                                                                                         storage_classification_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None and storage_classification_name is not None:
        return client.replication_storage_classification_mappings.list_by_replication_storage_classifications(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, storage_classification_name=storage_classification_name)
    else:
        return client.replication_storage_classification_mappings.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationstorageclassificationmapping
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationstorageclassification_replicationstorageclassificationmapping(cmd, client,
                                                                                                                                         resource_name,
                                                                                                                                         resource_group,
                                                                                                                                         fabric_name,
                                                                                                                                         storage_classification_name,
                                                                                                                                         name):
    return client.replication_storage_classification_mappings.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, storage_classification_name=storage_classification_name, storage_classification_mapping_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationvcenter
def create_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter(cmd, client,
                                                                                     resource_name,
                                                                                     resource_group,
                                                                                     fabric_name,
                                                                                     name,
                                                                                     friendly_name=None,
                                                                                     ip_address=None,
                                                                                     process_server_id=None,
                                                                                     port=None,
                                                                                     run_as_account_id=None):
    body={}
    body['friendly_name'] = friendly_name # str
    body['ip_address'] = ip_address # str
    body['process_server_id'] = process_server_id # str
    body['port'] = port # str
    body['run_as_account_id'] = run_as_account_id # str
    return client.replicationv_centers.create(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, v_center_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationvcenter
def update_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter(cmd, client,
                                                                                     resource_name,
                                                                                     resource_group,
                                                                                     fabric_name,
                                                                                     name,
                                                                                     friendly_name=None,
                                                                                     ip_address=None,
                                                                                     process_server_id=None,
                                                                                     port=None,
                                                                                     run_as_account_id=None):
    body={}
    body['friendly_name'] = friendly_name # str
    body['ip_address'] = ip_address # str
    body['process_server_id'] = process_server_id # str
    body['port'] = port # str
    body['run_as_account_id'] = run_as_account_id # str
    return client.replicationv_centers.update(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, v_center_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationvcenter
def delete_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter(cmd, client,
                                                                                     resource_name,
                                                                                     resource_group,
                                                                                     fabric_name,
                                                                                     name):
    return client.replicationv_centers.delete(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, v_center_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationvcenter
def list_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter(cmd, client,
                                                                                   resource_name,
                                                                                   resource_group,
                                                                                   fabric_name):
    if resource_name is not None and resource_group is not None and fabric_name is not None:
        return client.replicationv_centers.list_by_replication_fabrics(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name)
    else:
        return client.replicationv_centers.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationvcenter
def show_recoveryservices_resourcegroup_vault_replicationfabric_replicationvcenter(cmd, client,
                                                                                   resource_name,
                                                                                   resource_group,
                                                                                   fabric_name,
                                                                                   name):
    return client.replicationv_centers.get(resource_name=resource_name, resource_group_name=resource_group, fabric_name=fabric_name, v_center_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationpolicy
def create_recoveryservices_resourcegroup_vault_replicationpolicy(cmd, client,
                                                                  resource_name,
                                                                  resource_group,
                                                                  name):
    body={}
    return client.replication_policies.create(resource_name=resource_name, resource_group_name=resource_group, policy_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationpolicy
def update_recoveryservices_resourcegroup_vault_replicationpolicy(cmd, client,
                                                                  resource_name,
                                                                  resource_group,
                                                                  name):
    body={}
    return client.replication_policies.update(resource_name=resource_name, resource_group_name=resource_group, policy_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationpolicy
def delete_recoveryservices_resourcegroup_vault_replicationpolicy(cmd, client,
                                                                  resource_name,
                                                                  resource_group,
                                                                  name):
    return client.replication_policies.delete(resource_name=resource_name, resource_group_name=resource_group, policy_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationpolicy
def list_recoveryservices_resourcegroup_vault_replicationpolicy(cmd, client,
                                                                resource_name,
                                                                resource_group):
    return client.replication_policies.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationpolicy
def show_recoveryservices_resourcegroup_vault_replicationpolicy(cmd, client,
                                                                resource_name,
                                                                resource_group,
                                                                name):
    return client.replication_policies.get(resource_name=resource_name, resource_group_name=resource_group, policy_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryplan
def create_recoveryservices_resourcegroup_vault_replicationrecoveryplan(cmd, client,
                                                                        resource_name,
                                                                        resource_group,
                                                                        name,
                                                                        primary_fabric_id=None,
                                                                        recovery_fabric_id=None,
                                                                        failover_deployment_model=None,
                                                                        groups=None):
    body={}
    body['primary_fabric_id'] = primary_fabric_id # str
    body['recovery_fabric_id'] = recovery_fabric_id # str
    body['failover_deployment_model'] = failover_deployment_model # str
    body['groups'] = json.loads(groups) if isinstance(groups, str) else groups
    return client.replication_recovery_plans.create(resource_name=resource_name, resource_group_name=resource_group, recovery_plan_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryplan
def update_recoveryservices_resourcegroup_vault_replicationrecoveryplan(cmd, client,
                                                                        resource_name,
                                                                        resource_group,
                                                                        name,
                                                                        primary_fabric_id=None,
                                                                        recovery_fabric_id=None,
                                                                        failover_deployment_model=None,
                                                                        groups=None):
    body={}
    body['primary_fabric_id'] = primary_fabric_id # str
    body['recovery_fabric_id'] = recovery_fabric_id # str
    body['failover_deployment_model'] = failover_deployment_model # str
    body['groups'] = json.loads(groups) if isinstance(groups, str) else groups
    return client.replication_recovery_plans.update(resource_name=resource_name, resource_group_name=resource_group, recovery_plan_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryplan
def delete_recoveryservices_resourcegroup_vault_replicationrecoveryplan(cmd, client,
                                                                        resource_name,
                                                                        resource_group,
                                                                        name):
    return client.replication_recovery_plans.delete(resource_name=resource_name, resource_group_name=resource_group, recovery_plan_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryplan
def list_recoveryservices_resourcegroup_vault_replicationrecoveryplan(cmd, client,
                                                                      resource_name,
                                                                      resource_group):
    return client.replication_recovery_plans.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationrecoveryplan
def show_recoveryservices_resourcegroup_vault_replicationrecoveryplan(cmd, client,
                                                                      resource_name,
                                                                      resource_group,
                                                                      name):
    return client.replication_recovery_plans.get(resource_name=resource_name, resource_group_name=resource_group, recovery_plan_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationvaultsetting
def create_recoveryservices_resourcegroup_vault_replicationvaultsetting(cmd, client,
                                                                        resource_name,
                                                                        resource_group,
                                                                        name,
                                                                        migration_solution_id=None):
    body={}
    body['migration_solution_id'] = migration_solution_id # str
    return client.replication_vault_setting.create(resource_name=resource_name, resource_group_name=resource_group, vault_setting_name=name)

# module equivalent: azure_rm_recoveryservicesreplicationvaultsetting
def list_recoveryservices_resourcegroup_vault_replicationvaultsetting(cmd, client,
                                                                      resource_name,
                                                                      resource_group):
    return client.replication_vault_setting.list(resource_name=resource_name, resource_group_name=resource_group)

# module equivalent: azure_rm_recoveryservicesreplicationvaultsetting
def show_recoveryservices_resourcegroup_vault_replicationvaultsetting(cmd, client,
                                                                      resource_name,
                                                                      resource_group,
                                                                      name):
    return client.replication_vault_setting.get(resource_name=resource_name, resource_group_name=resource_group, vault_setting_name=name)