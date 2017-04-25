#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Software License Agreement (BSD License)
#
# Copyright (c) 2017, TORK
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials provided
# with the distribution.
# * Neither the name of TORK (Tokyo Opensource Robotics Kyokai Association). 
# nor the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
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

from hironx_ros_bridge.hironx_client import HIRONX
from test_hironx import TestHiro

PKG = 'hironx_ros_bridge'


class TestHiroClient(TestHiro):

    _RTC_LIST = [
            ['seq', "SequencePlayer"],
            ['sh', "StateHolder"],
            ['fk', "ForwardKinematics"],
            ['ic', "ImpedanceController"],
            ['el', "SoftErrorLimiter"],
            # ['co', "CollisionDetector"],
            ['sc', "ServoController"],
            ['log', "DataLogger"],
        ]

    _RTC_LIST_CUSTOM = [
            ['seq', "SequencePlayer"],
            ['sh', "StateHolder"],
            ['fk', "ForwardKinematics"],
            ['el', "SoftErrorLimiter"],
            ['co', "CollisionDetector"],
            ['log', "DataLogger"],
        ]

    def test_getRTCList(self):
        self.assertListEqual(self.robot.getRTCList(), self._RTC_LIST)

    def test_getRTCList_customrtcs(self):
        '''
        Test when the RTC list was passed from the client.

        Because this uses HIRONX.init(), which is already done in the
        superclass, HIRONX class instance is re-generated within this method,
        which is not elegant but as of now I can't think of a better way.
        '''
        self.robot = HIRONX()
        self.robot.init(rtcs=self._RTC_LIST_CUSTOM)

        self.assertListEqual(self.robot.getRTCList(), self._RTC_LIST_CUSTOM)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_hronx_client', TestHiroClient)
