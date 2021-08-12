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

from .case import TestCase
from .running.config import Seldom
from .running.next_runner import main
from .running.HTMLTestRunner import SMTP

from .skip import *
from .driver import *
from .logging.log import *
from .testdata.parameterization import *

from .request import HttpRequest

__author__ = "bugmaster"

__version__ = "2.2.2"

__description__ = "WebUI/HTTP automation testing framework based on unittest."
