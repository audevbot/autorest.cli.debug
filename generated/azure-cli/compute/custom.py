# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_compute(cmd, client,
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
    return client.galleries.create(resource_group, name, gallery)


def delete_compute(cmd, client,
                   resource_group,
                   name):
    return client.galleries.delete(resource_group, name)


def list_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.list(resource_group, name)


def show_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.show(resource_group, name)


def show_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.show(resource_group, name)


def list_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.list(resource_group, name)


def create_compute_image(cmd, client,
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
    return client.gallery_images.create(resource_group, gallery_name, name, galleryImage)


def delete_compute_image(cmd, client,
                         resource_group,
                         gallery_name,
                         name):
    return client.gallery_images.delete(resource_group, gallery_name, name)


def list_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.list(resource_group, gallery_name, name)


def show_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.show(resource_group, gallery_name, name)


def show_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.show(resource_group, gallery_name, name)


def list_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.list(resource_group, gallery_name, name)


def create_compute_image_version(cmd, client,
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
    return client.gallery_image_versions.create(resource_group, gallery_name, gallery_image_name, name, galleryImageVersion)


def delete_compute_image_version(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 gallery_image_name,
                                 name):
    return client.gallery_image_versions.delete(resource_group, gallery_name, gallery_image_name, name)


def list_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.list(resource_group, gallery_name, gallery_image_name, name)


def show_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.show(resource_group, gallery_name, gallery_image_name, name)


def show_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.show(resource_group, gallery_name, gallery_image_name, name)


def list_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.list(resource_group, gallery_name, gallery_image_name, name)