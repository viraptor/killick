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

from __future__ import absolute_import

import logging
import sys

import paste
from paste import translogger  # noqa
import pecan

from anchor import jsonloader

logger = logging.getLogger(__name__)

def setup_app(config):
    # initial logging, will be re-configured later
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    app_conf = dict(config.app)
    app = pecan.make_app(
        app_conf.pop('root'),
        logging=config.logging,
        **app_conf
    )

    jsonloader.conf.load_file_data("config.json") # todo tidy conf loading
    jsonloader.conf.load_extensions()

    return paste.translogger.TransLogger(app, setup_console_handler=False)
