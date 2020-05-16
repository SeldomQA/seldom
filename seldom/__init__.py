#!/usr/bin/python
#
# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from .running.test_runner import main
from .running.config import Seldom
from .testdata.parameterized import data, data_class
from .testdata.conversion import csv_to_list, excel_to_list, json_to_list
from .webdriver import WebDriver
from .case import TestCase
from .driver import browser
from .skip import skip
from .skip import skip_if
from .skip import skip_unless

__author__ = "bugmaster"

__version__ = "1.5.2"

__description__ = "WebUI automation testing framework based on Selenium."
