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


class SearchManager(basemodels.BaseModelManager):
    api_name = "search"
    base_url = "search"

    def get_logs(self, start_time=0, end_time=20, page_size=15, page_num=1):
        url = '/v1/search/logs'

        params = {
            'start_time': start_time,
            'end_time': end_time,
            'page_size': page_size,
            'page_num': page_num
        }
        url += utils.prepare_query_string(params)

        print('123123123')
        print(url)

        try:
            resp, body = self.api.json_request('GET', url)
            return body
        except Exception as e:
            raise RuntimeError(str(e))
