# Mission 1

## Command Path Explanation

/student_cmd_vel and /cmd_vel are separte because when a student proposes a command it needs a safety check in case of any incorrect parameters or issues it may have. So when a commands proposed it travels to the /course_cmd_vel_guard which checks the safety of the proposed command  and if it's good then it sends it to the final /cmd_vel to take action.

## Graph Explanation

A ROS 2 graph shows how software communicates with nodes from a publisher like some sort of sensor through some message or topic that returns values into a subscriber which is the part that takes action. An example of a node would be /course_cmd_vel_guard which is the entire program that takes in a command and does a safety check on said command (the safety checking section is the topic) which if considered safe then heads to the subscriber.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

.inf which likely represents the sky as /scans shows meters around the robot and the sky is the only way the robot should see .inf

## Tools Explanation

Gazebo deals with the actual physics of the robot so its motions, sensor readings, walls and wheels, while RViz is responsible for the data part of the robot like its sensor reading data and the robots position. RViz does not deal with any physics
