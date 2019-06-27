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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
    body['description'] = description # str
    body['identifier'] = json.parse(identifier) if isinstance(identifier, str) else identifier
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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
    body['description'] = description # str
    body['identifier'] = json.parse(identifier) if isinstance(identifier, str) else identifier
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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
    body['description'] = description # str
    body['eula'] = eula # str
    body['privacy_statement_uri'] = privacy_statement_uri # str
    body['release_note_uri'] = release_note_uri # str
    body['os_type'] = os_type # str
    body['os_state'] = os_state # str
    body['end_of_life_date'] = end_of_life_date # datetime
    body['identifier'] = json.parse(identifier) if isinstance(identifier, str) else identifier
    body['recommended'] = json.parse(recommended) if isinstance(recommended, str) else recommended
    body['disallowed'] = json.parse(disallowed) if isinstance(disallowed, str) else disallowed
    body['purchase_plan'] = json.parse(purchase_plan) if isinstance(purchase_plan, str) else purchase_plan
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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
    body['description'] = description # str
    body['eula'] = eula # str
    body['privacy_statement_uri'] = privacy_statement_uri # str
    body['release_note_uri'] = release_note_uri # str
    body['os_type'] = os_type # str
    body['os_state'] = os_state # str
    body['end_of_life_date'] = end_of_life_date # datetime
    body['identifier'] = json.parse(identifier) if isinstance(identifier, str) else identifier
    body['recommended'] = json.parse(recommended) if isinstance(recommended, str) else recommended
    body['disallowed'] = json.parse(disallowed) if isinstance(disallowed, str) else disallowed
    body['purchase_plan'] = json.parse(purchase_plan) if isinstance(purchase_plan, str) else purchase_plan
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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
    body['publishing_profile'] = json.parse(publishing_profile) if isinstance(publishing_profile, str) else publishing_profile
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
    body['location'] = location # str
    body['tags'] = tags # unknown[DictionaryType {"$id":"70","$type":"DictionaryType","valueType":{"$id":"71","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"72","fixed":false,"raw":"String"},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"73","fixed":false},"deprecated":false}]
    body['publishing_profile'] = json.parse(publishing_profile) if isinstance(publishing_profile, str) else publishing_profile
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