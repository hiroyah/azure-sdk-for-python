# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OSDisk(Model):
    """
    Describes an Operating System disk.

    :param str os_type: Gets or sets the Operating System type. Possible
     values include: 'Windows', 'Linux'
    :param DiskEncryptionSettings encryption_settings: Gets or sets the disk
     encryption settings.
    :param str name: Gets or sets the disk name.
    :param VirtualHardDisk vhd: Gets or sets the Virtual Hard Disk.
    :param VirtualHardDisk image: Gets or sets the Source User Image
     VirtualHardDisk. This VirtualHardDisk will be copied before using it to
     attach to the Virtual Machine.If SourceImage is provided, the
     destination VirtualHardDisk should not exist.
    :param str caching: Gets or sets the caching type. Possible values
     include: 'None', 'ReadOnly', 'ReadWrite'
    :param str create_option: Gets or sets the create option. Possible values
     include: 'fromImage', 'empty', 'attach'
    :param int disk_size_gb: Gets or sets the initial disk size in GB for
     blank data disks, and the new desired size for existing OS and Data
     disks.
    """

    _required = ['name', 'vhd', 'create_option']

    _attribute_map = {
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'encryption_settings': {'key': 'encryptionSettings', 'type': 'DiskEncryptionSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'vhd': {'key': 'vhd', 'type': 'VirtualHardDisk'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'create_option': {'key': 'createOption', 'type': 'DiskCreateOptionTypes'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
    }

    def __init__(self, name, vhd, create_option, os_type=None, encryption_settings=None, image=None, caching=None, disk_size_gb=None):
        self.os_type = os_type
        self.encryption_settings = encryption_settings
        self.name = name
        self.vhd = vhd
        self.image = image
        self.caching = caching
        self.create_option = create_option
        self.disk_size_gb = disk_size_gb
