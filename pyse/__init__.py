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

from .running.test_runner import TestRunner
from .pyse_api import WebDriver
from .case import TestCase
from .driver import Pyse 

__author__ = "bugmaster"

__version__ = "0.0.9"

'''
0.0.2 version update:
* all the elements of the operation selector xpath replaced by css, css syntax because more concise.
* when you run the test case no longer need to specify the directory, the default directory for the current test.
* modify the examples under demo.

0.0.3 version update:
* With the nose instead of unittest.
* Discard HTMLTestRunner,Integrated nose-html-reporting.
* modify the examples under demo.

0.0.3.1 version update:
* Repair part bug.

0.0.4
Method to add default to wait.
Modify the realization of the individual methods

0.0.5
Increase the support of multiple positioning methods

0.0.6
add setup.py file, Specification of the installation process, a time to install all dependencies.
Delete unnecessary files

0.0.7
Re based on unittest.

0.0.8
add parameterized
Beautification test report

0.0.9
Simplifying API calls
'''
