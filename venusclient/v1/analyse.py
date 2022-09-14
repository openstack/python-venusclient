# Copyright 2020 Inspur
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from venusclient.common import utils
from venusclient.v1 import basemodels

CREATION_ATTRIBUTES = basemodels.CREATION_ATTRIBUTES


class LogAnalyse(basemodels.BaseModel):
    model_name = "Analyse"


class AnalyseManager(basemodels.BaseModelManager):
    api_name = "search"
    base_url = "search"
    resource_class = LogAnalyse

    def analyse_log(self):
        url = '/v1/search/analyse/logs'
        url += utils.prepare_query_string()

        try:
            resp, body = self.api.json_request('GET', url)
            return body
        except Exception as e:
            raise RuntimeError(str(e))

    def typical_log(self):
        url = '/v1/search/typical/logs'
        url += utils.prepare_query_string()

        try:
            resp, body = self.api.json_request('GET', url)
            return body
        except Exception as e:
            raise RuntimeError(str(e))
