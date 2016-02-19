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

from .http_authentication import HttpAuthentication


class BasicAuthentication(HttpAuthentication):
    """BasicAuthentication

    :param str type: Gets or sets the http authentication type. Possible
     values include: 'NotSpecified', 'ClientCertificate',
     'ActiveDirectoryOAuth', 'Basic'
    :param str username: Gets or sets the username.
    :param str password: Gets or sets the password.
    """

    _required = []

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, type=None, username=None, password=None):
        super(BasicAuthentication, self).__init__(type=type)
        self.username = username
        self.password = password
