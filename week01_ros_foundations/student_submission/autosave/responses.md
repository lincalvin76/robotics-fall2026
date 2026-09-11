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

For either curved trial the estimated traveled path and the start-to-end distance describe different measurements because the start-to-end distance will always be shorter than the estimated traveled path. Reasoning for this is because the start-to-end distance is a straight line measurement to the arc so in a way its using the euclidean distance over the curve distance which is shorter.

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

For the very first trial the backup motion results are basically the same with my prediction as I predicted it would move 0.45 forward and stop and even though the backup trial shows it moving 0.41, that's within our range because the backup models have a 9% lower translation which is exactly 0.41. The direction also has 0 change because it was just a forward movement.

## mission_2.prediction_locks

{'straight': '2026-09-09T17:32:12.912810+00:00', 'rotation': '2026-09-11T19:58:22.738983+00:00', 'curve': '2026-09-11T20:01:35.726739+00:00', 'curve_modified': '2026-09-11T20:05:26.162637+00:00'}

## mission_2.predictions

{'rotation': "The robot's position will not change while it's direction will be 1.50 radians to the left", 'straight': 'I predict the robot will be 0.45 meters away from its starting point', 'curve': "I predict a small right curve because it'll be moving forward while turning right ever so slightly by -0.40 radians each second", 'curve_modified': "This curve would be a bit wider as its radius is larger than the previous trial as well as go left instead of right because it's a positive number"}

## mission_2.safety_explanation

The command guard checks if the speed is too high and if it is, it refuses to send the command to the robot, it's our safety check. The final zero command is what calculates when our trial is finished when the forward amount and turning speed are both 0, not including the initial. The timeout is another safety check where if the program crashes or some error happens while the robot is moving, a signal is sent to stop all commands.

## mission_3.data_to_command



## mission_3.missing_data_safety



## mission_3.system_layers



## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
