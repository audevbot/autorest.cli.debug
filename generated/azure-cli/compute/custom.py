# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
import json

# module equivalent: azure_rm_computegallery
def create_compute(cmd, client,
                   resource_group,
                   name,
                   location=None,
                   tags=None,
                   description=None,
                   identifier=None):
    body={}
    body['location'] = location # body
    body['tags'] = tags # body
    body['description'] = description # body
    body['identifier'] = identifier # body
    return client.galleries.create_or_update(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegallery
def update_compute(cmd, client,
                   resource_group,
                   name,
                   location=None,
                   tags=None,
                   description=None,
                   identifier=None):
    body={}
    body['location'] = location # body
    body['tags'] = tags # body
    body['description'] = description # body
    body['identifier'] = identifier # body
    return client.galleries.create_or_update(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegallery
def delete_compute(cmd, client,
                   resource_group,
                   name):
    return client.galleries.delete(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegallery
def list_compute(cmd, client,
                 resource_group):
    if resource_group is not None:
        return client.galleries.list_by_resource_group(resource_group_name=resource_group)
    else:
        return client.galleries.list()

# module equivalent: azure_rm_computegallery
def show_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.get(resource_group_name=resource_group, gallery_name=name)

# module equivalent: azure_rm_computegalleryimage
def create_compute_image(cmd, client,
                         resource_group,
                         gallery_name,
                         name,
                         location=None,
                         tags=None,
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
                         purchase_plan=None):
    body={}
    body['location'] = location # body
    body['tags'] = tags # body
    body['description'] = description # body
    body['eula'] = eula # body
    body['privacy_statement_uri'] = privacy_statement_uri # body
    body['release_note_uri'] = release_note_uri # body
    body['os_type'] = os_type # body
    body['os_state'] = os_state # body
    body['end_of_life_date'] = end_of_life_date # body
    body['identifier'] = identifier # body
    body['recommended'] = recommended # body
    body['disallowed'] = disallowed # body
    body['purchase_plan'] = purchase_plan # body
    return client.gallery_images.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimage
def update_compute_image(cmd, client,
                         resource_group,
                         gallery_name,
                         name,
                         location=None,
                         tags=None,
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
                         purchase_plan=None):
    body={}
    body['location'] = location # body
    body['tags'] = tags # body
    body['description'] = description # body
    body['eula'] = eula # body
    body['privacy_statement_uri'] = privacy_statement_uri # body
    body['release_note_uri'] = release_note_uri # body
    body['os_type'] = os_type # body
    body['os_state'] = os_state # body
    body['end_of_life_date'] = end_of_life_date # body
    body['identifier'] = identifier # body
    body['recommended'] = recommended # body
    body['disallowed'] = disallowed # body
    body['purchase_plan'] = purchase_plan # body
    return client.gallery_images.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimage
def delete_compute_image(cmd, client,
                         resource_group,
                         gallery_name,
                         name):
    return client.gallery_images.delete(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimage
def list_compute_image(cmd, client,
                       resource_group,
                       gallery_name):
    return client.gallery_images.list_by_gallery(resource_group_name=resource_group, gallery_name=gallery_name)

# module equivalent: azure_rm_computegalleryimage
def show_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.get(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def create_compute_image_version(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 gallery_image_name,
                                 name,
                                 location=None,
                                 tags=None,
                                 publishing_profile=None):
    body={}
    body['location'] = location # body
    body['tags'] = tags # body
    body['publishing_profile'] = publishing_profile # body
    return client.gallery_image_versions.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def update_compute_image_version(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 gallery_image_name,
                                 name,
                                 location=None,
                                 tags=None,
                                 publishing_profile=None):
    body={}
    body['location'] = location # body
    body['tags'] = tags # body
    body['publishing_profile'] = publishing_profile # body
    return client.gallery_image_versions.create_or_update(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def delete_compute_image_version(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 gallery_image_name,
                                 name):
    return client.gallery_image_versions.delete(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)

# module equivalent: azure_rm_computegalleryimageversion
def list_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name):
    return client.gallery_image_versions.list_by_gallery_image(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name)

# module equivalent: azure_rm_computegalleryimageversion
def show_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.get(resource_group_name=resource_group, gallery_name=gallery_name, gallery_image_name=gallery_image_name, gallery_image_version_name=name)