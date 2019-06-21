# 
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_compute(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.galleries.create()


def delete_compute(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.galleries.delete()


def list_compute(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.galleries.list()


def show_compute(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.galleries.show()


def show_compute(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.galleries.show()


def list_compute(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.galleries.list()


def create_compute_images(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_images.create()


def delete_compute_images(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_images.delete()


def list_compute_images(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_images.list()


def show_compute_images(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_images.show()


def show_compute_images(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_images.show()


def list_compute_images(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_images.list()


def create_compute_images_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_image_versions.create()


def delete_compute_images_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_image_versions.delete()


def list_compute_images_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_image_versions.list()


def show_compute_images_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_image_versions.show()


def show_compute_images_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_image_versions.show()


def list_compute_images_versions(cmd, client, resource_group_name, apimanagement_name, location=None, tags=None):
    return client.gallery_image_versions.list()