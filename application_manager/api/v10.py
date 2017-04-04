# Copyright (c) 2017 LSD - UFCG.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import httplib

from application_manager.utils import api as u
from application_manager.service.api import v10 as api

rest = u.Rest('v10', __name__)


@rest.post('/manager/application_started/<app_id>')
def application_started(app_id, data):
    return u.render(api.application_started(app_id, data))


@rest.post('/manager/application_stopped/<app_id>')
def application_stopped(app_id, data):
    api.application_stopped(app_id)
    return httplib.ACCEPTED
