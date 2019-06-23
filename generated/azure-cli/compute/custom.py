# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError

# module equivalent: azure_rm_computegallery
def create_compute_gallery(cmd, client,
                           resource_group,
                           name,
                           location=None,
                           tags=None,
                           properties=None,
                           description=None,
                           identifier=None,
                           provisioning_state=None,
                           id=None,
                           type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['description'] = description
    body['identifier'] = identifier
    body['provisioning_state'] = provisioning_state
    return client.galleries.create_or_update(resource_group_name=resource_group, gallery_name=name, gallery=gallery)

# module equivalent: azure_rm_computegallery
def update_compute_gallery(cmd, client,
                           resource_group,
                           name,
                           location=None,
                           tags=None,
                           properties=None,
                           description=None,
                           identifier=None,
                           provisioning_state=None,
                           id=None,
                           type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['description'] = description
    body['identifier'] = identifier
    body['provisioning_state'] = provisioning_state
    return client.galleries.create_or_update(resource_group_name=resource_group, gallery_name=name, gallery=gallery)

# module equivalent: azure_rm_computegallery
def delete_compute_gallery(cmd, client,
                           resource_group,
                           name):
    return client.galleries.delete(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegallery
def list_compute_gallery(cmd, client,
                         resource_group,
                         name):
    return client.galleries.list(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegallery
def show_compute_gallery(cmd, client,
                         resource_group,
                         name):
    return client.galleries.get(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegalleryimage
def create_compute_gallery_image(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 name,
                                 location=None,
                                 tags=None,
                                 properties=None,
                                 description=None,
                                 eula=None,
                                 privacy_statement_uri=None,
                                 release_note_uri=None,
                                 os_type=None,
                                 os_state=None,
                                 end_of_life_date=None,
                                 identifier=None,
                                 recommended=None,
                                 disallowed=None,
                                 purchase_plan=None,
                                 provisioning_state=None,
                                 id=None,
                                 type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['description'] = description
    body['eula'] = eula
    body['privacy_statement_uri'] = privacy_statement_uri
    body['release_note_uri'] = release_note_uri
    body['os_type'] = os_type
    body['os_state'] = os_state
    body['end_of_life_date'] = end_of_life_date
    body['identifier'] = identifier
    body['recommended'] = recommended
    body['disallowed'] = disallowed
    body['purchase_plan'] = purchase_plan
    body['provisioning_state'] = provisioning_state
    return client.gallery_images.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name, galleryImage=galleryImage)

# module equivalent: azure_rm_computegalleryimage
def update_compute_gallery_image(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 name,
                                 location=None,
                                 tags=None,
                                 properties=None,
                                 description=None,
                                 eula=None,
                                 privacy_statement_uri=None,
                                 release_note_uri=None,
                                 os_type=None,
                                 os_state=None,
                                 end_of_life_date=None,
                                 identifier=None,
                                 recommended=None,
                                 disallowed=None,
                                 purchase_plan=None,
                                 provisioning_state=None,
                                 id=None,
                                 type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['description'] = description
    body['eula'] = eula
    body['privacy_statement_uri'] = privacy_statement_uri
    body['release_note_uri'] = release_note_uri
    body['os_type'] = os_type
    body['os_state'] = os_state
    body['end_of_life_date'] = end_of_life_date
    body['identifier'] = identifier
    body['recommended'] = recommended
    body['disallowed'] = disallowed
    body['purchase_plan'] = purchase_plan
    body['provisioning_state'] = provisioning_state
    return client.gallery_images.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name, galleryImage=galleryImage)

# module equivalent: azure_rm_computegalleryimage
def delete_compute_gallery_image(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 name):
    return client.gallery_images.delete(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimage
def list_compute_gallery_image(cmd, client,
                               resource_group,
                               gallery_name,
                               name):
    return client.gallery_images.list_by_gallery(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimage
def show_compute_gallery_image(cmd, client,
                               resource_group,
                               gallery_name,
                               name):
    return client.gallery_images.get(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def create_compute_gallery_image_version(cmd, client,
                                         resource_group,
                                         gallery_name,
                                         gallery_image_name,
                                         name,
                                         location=None,
                                         tags=None,
                                         properties=None,
                                         publishing_profile=None,
                                         provisioning_state=None,
                                         storage_profile=None,
                                         replication_status=None,
                                         id=None,
                                         type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['publishing_profile'] = publishing_profile
    body['provisioning_state'] = provisioning_state
    body['storage_profile'] = storage_profile
    body['replication_status'] = replication_status
    return client.gallery_image_versions.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name, galleryImageVersion=galleryImageVersion)

# module equivalent: azure_rm_computegalleryimageversion
def update_compute_gallery_image_version(cmd, client,
                                         resource_group,
                                         gallery_name,
                                         gallery_image_name,
                                         name,
                                         location=None,
                                         tags=None,
                                         properties=None,
                                         publishing_profile=None,
                                         provisioning_state=None,
                                         storage_profile=None,
                                         replication_status=None,
                                         id=None,
                                         type=None):
    body={}
    body['location'] = location
    body['tags'] = tags
    body['properties'] = properties
    body['publishing_profile'] = publishing_profile
    body['provisioning_state'] = provisioning_state
    body['storage_profile'] = storage_profile
    body['replication_status'] = replication_status
    return client.gallery_image_versions.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name, galleryImageVersion=galleryImageVersion)

# module equivalent: azure_rm_computegalleryimageversion
def delete_compute_gallery_image_version(cmd, client,
                                         resource_group,
                                         gallery_name,
                                         gallery_image_name,
                                         name):
    return client.gallery_image_versions.delete(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def list_compute_gallery_image_version(cmd, client,
                                       resource_group,
                                       gallery_name,
                                       gallery_image_name,
                                       name):
    return client.gallery_image_versions.list_by_gallery_image(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def show_compute_gallery_image_version(cmd, client,
                                       resource_group,
                                       gallery_name,
                                       gallery_image_name,
                                       name):
    return client.gallery_image_versions.get(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)