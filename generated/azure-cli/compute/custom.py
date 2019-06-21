# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_compute(cmd, client,
                   resource_group,
                   name,
                   location,
                   tags,
                   properties,
                   description,
                   identifier,
                   provisioning_state,
                   id,
                   type):
    return client.galleries.create()


def delete_compute(cmd, client,
                   resource_group,
                   name):
    return client.galleries.delete()


def list_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.list()


def show_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.show()


def show_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.show()


def list_compute(cmd, client,
                 resource_group,
                 name):
    return client.galleries.list()


def create_compute_image(cmd, client,
                         resource_group,
                         gallery_name,
                         name,
                         location,
                         tags,
                         properties,
                         description,
                         eula,
                         privacy_statement_uri,
                         release_note_uri,
                         os_type,
                         os_state,
                         end_of_life_date,
                         identifier,
                         recommended,
                         disallowed,
                         purchase_plan,
                         provisioning_state,
                         id,
                         type):
    return client.gallery_images.create()


def delete_compute_image(cmd, client,
                         resource_group,
                         gallery_name,
                         name):
    return client.gallery_images.delete()


def list_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.list()


def show_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.show()


def show_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.show()


def list_compute_image(cmd, client,
                       resource_group,
                       gallery_name,
                       name):
    return client.gallery_images.list()


def create_compute_image_version(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 gallery_image_name,
                                 name,
                                 location,
                                 tags,
                                 properties,
                                 publishing_profile,
                                 provisioning_state,
                                 storage_profile,
                                 replication_status,
                                 id,
                                 type):
    return client.gallery_image_versions.create()


def delete_compute_image_version(cmd, client,
                                 resource_group,
                                 gallery_name,
                                 gallery_image_name,
                                 name):
    return client.gallery_image_versions.delete()


def list_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.list()


def show_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.show()


def show_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.show()


def list_compute_image_version(cmd, client,
                               resource_group,
                               gallery_name,
                               gallery_image_name,
                               name):
    return client.gallery_image_versions.list()