#!/usr/bin/env python3


import sys
import copy
import math

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from tf.transformations import *

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('milestone2',anonymous=True)


robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("Arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planning_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

##########################################
# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print("============ Planning frame: %s" % planning_frame)

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print("============ End effector link: %s" % eef_link)

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print("============ Available Planning Groups:", robot.get_group_names())

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print("============ Printing robot state")
print(robot.get_current_state())
print("")
############################################
q_orig = quaternion_from_euler(0, 0, 0)
q_rot = quaternion_from_euler(2.3, -1.2, 0)
q_new = quaternion_multiply(q_rot, q_orig)
print (q_new)


pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.w = 0.001
pose_goal.position.x = 0.9
pose_goal.position.y = 0.195
pose_goal.position.z = 0.191

group.set_pose_target(pose_goal)
#group.set_named_target("home2")

plan = group.go(wait=True)
group.stop()
group.clear_pose_targets()

display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan)
display_trajectory_publisher.publish(display_trajectory)


group.execute(plan, wait=True)





rospy.sleep(5)
moveit_commander.roscpp_shutdown()
