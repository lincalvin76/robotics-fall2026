# Mission 3

## Data To Command

The 2 functions turn a list of LiDAR distances into a move/stop command by first detecting if there's anything in front of the robot using the angles and half-front width view. If our list is empty and there's nothing then we can decide on constantly moving. However if the list is not empty and there is an obstacle in the way, we would check that distance and stop right before it based on the stop_distance, but if we haven't hit that stop_distance range yet and can still move forward than we will continue moving forward with a maximum speed of 0.18 for safety reasons.

## Missing Data Safety

The robot stops when there's no valid front measurement because it does not know if the path is clear or not. It could've received a nan which is just an invalid or unusable number but there could still be an obstacle ahead. Therefore the safest option is to stop moving when its unclear if the path is truly clear or not.

## System Layers

The supplied ROS node, decision functions, and command guard work together by collecting data, making decisions based off that data, and giving it a safety check before running it fully.  In this example it was done through the ROS node collecting the LiDAR data and sending it to the decision functions that determined if there were obstacles or not, and the command guard determining if it can move or not based on certain conditions, like is there an object, do we even have a distance, what should our maximum speed be, etc.
