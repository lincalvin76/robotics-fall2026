# Mission 2

## Measurement Explanation

For either curved trial the estimated traveled path and the start-to-end distance describe different measurements because the start-to-end distance will always be shorter than the estimated traveled path. Reasoning for this is because the start-to-end distance is a straight line measurement to the arc so in a way its using the euclidean distance over the curve distance which is shorter.

## Motion Comparison

For the very first trial the backup motion results are basically the same with my prediction as I predicted it would move 0.45 forward and stop and even though the backup trial shows it moving 0.41, that's within our range because the backup models have a 9% lower translation which is exactly 0.41. The direction also has 0 change because it was just a forward movement.

## Prediction Locks

{'straight': '2026-09-09T17:32:12.912810+00:00', 'rotation': '2026-09-11T19:58:22.738983+00:00', 'curve': '2026-09-11T20:01:35.726739+00:00', 'curve_modified': '2026-09-11T20:05:26.162637+00:00'}

## Predictions

{'rotation': "The robot's position will not change while it's direction will be 1.50 radians to the left", 'straight': 'I predict the robot will be 0.45 meters away from its starting point', 'curve': "I predict a small right curve because it'll be moving forward while turning right ever so slightly by -0.40 radians each second", 'curve_modified': "This curve would be a bit wider as its radius is larger than the previous trial as well as go left instead of right because it's a positive number"}

## Safety Explanation

The command guard checks if the speed is too high and if it is, it refuses to send the command to the robot, it's our safety check. The final zero command is what calculates when our trial is finished when the forward amount and turning speed are both 0, not including the initial. The timeout is another safety check where if the program crashes or some error happens while the robot is moving, a signal is sent to stop all commands.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
