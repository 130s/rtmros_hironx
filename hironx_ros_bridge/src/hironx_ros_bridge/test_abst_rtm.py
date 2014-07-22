# -*- coding: utf-8 -*-
# Software License Agreement (BSD License)
#
# Copyright (c) 2014, Tokyo Opensource Robotics Kyokai Association
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Tokyo Opensource Robotics Kyokai Association. nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Isaac Isao Saito

import argparse
import unittest

from hrpsys import rtm


class AbstractTestRtm(unittest.TestCase):
    '''
    Test cases of OpenRTM-based classes can take advantage of this class
    by extending this.
    '''

    @classmethod
    def setUpClass(cls):
        '''
        This method needs to be called in the derived class BEFORE they tries
        to connect omniorb name server to properly read in the arguments.
        '''
        cls._parse_arg_rtm()

    @classmethod
    def _parse_arg_rtm(self):
        '''
        Read from argument (can be from command line / 'arg' in .launch files)
        then pass them to rtm.
        '''
        parser = argparse.ArgumentParser(description='hiro command line interpreters')
        parser.add_argument('--host', help='corba name server hostname')
        parser.add_argument('--modelfile', help='robot model file nmae')
        parser.add_argument('--port', help='corba name server port number')
        parser.add_argument('--robot', help='robot modlule name (RobotHardware0 for real robot, Robot()')
        args, unknown = parser.parse_known_args()
        if args.host:
            rtm.nshost = args.host
        if args.port:
            rtm.nsport = args.port
