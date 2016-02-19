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


class HostNameSslState(Model):
    """
    Object that represents a SSL-enabled host name.

    :param str name: Host name
    :param str ssl_state: SSL type. Possible values include: 'Disabled',
     'SniEnabled', 'IpBasedEnabled'
    :param str virtual_ip: Virtual IP address assigned to the host name if IP
     based SSL is enabled
    :param str thumbprint: SSL cert thumbprint
    :param bool to_update: Set this flag to update existing host name
    """

    _required = ['ssl_state']

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'ssl_state': {'key': 'sslState', 'type': 'SslState'},
        'virtual_ip': {'key': 'virtualIP', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'to_update': {'key': 'toUpdate', 'type': 'bool'},
    }

    def __init__(self, ssl_state, name=None, virtual_ip=None, thumbprint=None, to_update=None):
        self.name = name
        self.ssl_state = ssl_state
        self.virtual_ip = virtual_ip
        self.thumbprint = thumbprint
        self.to_update = to_update
