# Copyright 2016 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import inspect
import logging

# dashboard
from dashboard.services.consume.restclient import RestClient


__all__ = ['BaseManager']


class BaseManager(object):
    """
    Base Manager: create app context, process view request object
    """

    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):

        for attrib, value in kwargs.items():
            if value:
                setattr(self, str(attrib), value)

    @staticmethod
    def rest_client(engine_name, base_url, resource, *args, **kwargs):
        """
        Instantiate RestClient
        :param engine_name: API Config: str
        :param base_url: API Server: str
        :param resource: API URI: str
        :param args: arguments: tuple
        :param kwargs: keyword args: dict
        :return: RestClient
        """
        response_dict = {}
        if engine_name and base_url and resource:
            rest_handle = RestClient(engine_name, base_url)
            response_dict = rest_handle.process_request(resource, *args, **kwargs)
        return response_dict

    def app_logger(self, log_level, log_msg):
        """
        Custom application logger
        """
        level_map = {
            'DEBUG': 10, 'INFO': 20, 'WARNING': 30,
            'ERROR': 40, 'CRITICAL': 50
        }

        func = inspect.currentframe().f_back.f_code
        log_message = "%s in %s:%i %s" % (func.co_name, func.co_filename,
                                          func.co_firstlineno, log_msg)
        self.logger.log(level_map.get(log_level, 10), log_message)
