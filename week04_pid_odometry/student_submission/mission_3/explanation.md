# mission_3 Submission

- Name: Calvin Lin
- Section: (not provided)

## Explanations

### technical_analysis

I predicted that increasing speed would make overshoots a lot and that's exactly what happened, it overshot the line i drew and charged straight into pedestrians, The next route point becomes a heading command because the robot constantly checks its own position and compares it's heading position to where the next route point is, based on where the route point is relative to the robot, it would turn to face that route point. PID changes steering by adjusting speed based on the error from waypoint and fixes overshooting with a high enough Kd value, inaccurate wheel radius can make a well-tuned controller follow the wrong physical path because the odometry would think it's in a different spot meaning all the controller movements could be done way later or way earlier than it should because the sensor is either ahead or behind.

### human_centered_analysis

The most consequential failure for a pedestrian would be the robot failing to stop or slow then when getting near a pedestrian, A clearance and speed trade off could be as speed get's higher we increase the clearance range, so the range around pedestrians so we stop way earlier, and as we slow down we can also decrease the clearance range.  Usually the safety testers should be the one's responsible for verifying that decision before deployment because they want to make sure that the robot doesn't run into any accidents and that the code values should be safe.