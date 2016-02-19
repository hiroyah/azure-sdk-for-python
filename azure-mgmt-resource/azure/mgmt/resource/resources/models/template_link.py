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


class TemplateLink(Model):
    """
    Entity representing the reference to the template.

    :param str uri: URI referencing the template.
    :param str content_version: If included it must match the ContentVersion
     in the template.
    """

    _required = ['uri']

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'content_version': {'key': 'contentVersion', 'type': 'str'},
    }

    def __init__(self, uri, content_version=None):
        self.uri = uri
        self.content_version = content_version
