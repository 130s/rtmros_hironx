#!/usr/bin/env python
# -*- coding: utf-8 -*-

import actionlib
import hironx_ros_bridge.msg as hironxoaction
from hironx_ros_bridge.rmi import HironxRMI
from hironx_ros_bridge.sample_rmi import SampleHironxRMI
from test_hironx_ros_bridge import *


class TestHiroROSBridgeRMI(TestHiroROSBridge):

    @classmethod
    def setUpClass(cls):
        '''
        Overriding because we need to instantiate ROS action server using
        hironx_ros_bridge.rmi.HironxRMI class.
        '''
        # Start an action server that handles various ROS Actions.
        cls.rmi_sampleclass = SampleHironxRMI(robot="HiroNX(Robot)0")

    def tearDown(self):
        True  # TODO Run practical teardown.

    def test_rmi_goInitial(self):
        aclient = actionlib.SimpleActionClient('goInitial', hironxoaction.GoInitialAction)
        aclient.wait_for_server()
        goal = hironxoaction.GoInitialGoal(tm=7)
        aclient.send_goal(goal)
        aclient.wait_for_result()
        self.assertTrue(aclient.get_result())  # A GoInitialResult

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'hironx_rmi', TestHiroROSBridgeRMI)
