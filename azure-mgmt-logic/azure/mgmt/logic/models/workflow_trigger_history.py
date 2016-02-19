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

from .sub_resource import SubResource


class WorkflowTriggerHistory(SubResource):
    """WorkflowTriggerHistory

    :param str id: Gets or sets the resource id.
    :param str name: Gets the workflow trigger history name.
    :param str type: Gets the workflow trigger history type.
    :param datetime start_time: Gets the start time.
    :param datetime end_time: Gets the end time.
    :param str status: Gets the status. Possible values include:
     'NotSpecified', 'Paused', 'Running', 'Waiting', 'Succeeded', 'Skipped',
     'Suspended', 'Cancelled', 'Failed'
    :param str code: Gets the code.
    :param object error: Gets the error.
    :param str tracking_id: Gets the tracking id.
    :param ContentLink inputs_link: Gets the link to input parameters.
    :param ContentLink outputs_link: Gets the link to output parameters.
    :param bool fired: Gets a value indicating whether trigger was fired.
    :param ResourceReference run: Gets the reference to workflow run.
    """

    _required = []

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601', 'flatten': True},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601', 'flatten': True},
        'status': {'key': 'properties.status', 'type': 'WorkflowStatus', 'flatten': True},
        'code': {'key': 'properties.code', 'type': 'str', 'flatten': True},
        'error': {'key': 'properties.error', 'type': 'object', 'flatten': True},
        'tracking_id': {'key': 'properties.trackingId', 'type': 'str', 'flatten': True},
        'inputs_link': {'key': 'properties.inputsLink', 'type': 'ContentLink', 'flatten': True},
        'outputs_link': {'key': 'properties.outputsLink', 'type': 'ContentLink', 'flatten': True},
        'fired': {'key': 'properties.fired', 'type': 'bool', 'flatten': True},
        'run': {'key': 'properties.run', 'type': 'ResourceReference', 'flatten': True},
    }

    def __init__(self, id=None, name=None, type=None, start_time=None, end_time=None, status=None, code=None, error=None, tracking_id=None, inputs_link=None, outputs_link=None, fired=None, run=None):
        super(WorkflowTriggerHistory, self).__init__(id=id)
        self.name = name
        self.type = type
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.code = code
        self.error = error
        self.tracking_id = tracking_id
        self.inputs_link = inputs_link
        self.outputs_link = outputs_link
        self.fired = fired
        self.run = run
