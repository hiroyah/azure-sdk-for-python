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


class StorageQueueMessage(Model):
    """StorageQueueMessage

    :param str storage_account: Gets or sets the storage account name.
    :param str queue_name: Gets or sets the queue name.
    :param str sas_token: Gets or sets the SAS key.
    :param str message: Gets or sets the message.
    """

    _required = []

    _attribute_map = {
        'storage_account': {'key': 'storageAccount', 'type': 'str'},
        'queue_name': {'key': 'queueName', 'type': 'str'},
        'sas_token': {'key': 'sasToken', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, storage_account=None, queue_name=None, sas_token=None, message=None):
        self.storage_account = storage_account
        self.queue_name = queue_name
        self.sas_token = sas_token
        self.message = message
