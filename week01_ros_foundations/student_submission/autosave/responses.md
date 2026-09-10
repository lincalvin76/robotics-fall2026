# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Calvin Lin
- Email: calvin.lin80@login.cuny.edu

## mission_1.command_path_explanation

/student_cmd_vel and /cmd_vel are separte because when a student proposes a command it needs a safety check in case of any incorrect parameters or issues it may have. So when a commands proposed it travels to the /course_cmd_vel_guard which checks the safety of the proposed command  and if it's good then it sends it to the final /cmd_vel to take action.

## mission_1.graph_explanation

A ROS 2 graph shows how software communicates with nodes from a publisher like some sort of sensor through some message or topic that returns values into a subscriber which is the part that takes action. An example of a node would be /course_cmd_vel_guard which is the entire program that takes in a command and does a safety check on said command (the safety checking section is the topic) which if considered safe then heads to the subscriber.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

.inf which likely represents the sky as /scans shows meters around the robot and the sky is the only way the robot should see .inf

## mission_1.tools_explanation

Gazebo deals with the actual physics of the robot so its motions, sensor readings, walls and wheels, while RViz is responsible for the data part of the robot like its sensor reading data and the robots position. RViz does not deal with any physics

## mission_2.measurement_explanation



## mission_2.motion_comparison



## mission_2.prediction_locks

{'straight': '2026-09-09T17:32:12.912810+00:00'}

## mission_2.predictions

{'straight': 'I predict the robot will be 0.45 meters away from its starting point'}

## mission_2.safety_explanation



## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
