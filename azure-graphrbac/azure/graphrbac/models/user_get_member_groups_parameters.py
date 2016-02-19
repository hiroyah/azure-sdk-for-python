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


class UserGetMemberGroupsParameters(Model):
    """
    Request parameters for GetMemberGroups API call

    :param bool security_enabled_only: If true only membership in security
     enabled groups should be checked. Otherwise membership in all groups
     should be checked
    """

    _required = ['security_enabled_only']

    _attribute_map = {
        'security_enabled_only': {'key': 'securityEnabledOnly', 'type': 'bool'},
    }

    def __init__(self, security_enabled_only):
        self.security_enabled_only = security_enabled_only
