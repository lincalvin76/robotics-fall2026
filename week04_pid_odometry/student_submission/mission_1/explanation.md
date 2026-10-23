# mission_1 Submission

- Name: Calvin Lin
- Section: (not provided)

## Explanations

### prediction

Having too little Kp would likely cause the arm to move too slowly and too little Kd would cause the arm to have a larger offset when it tries to reach it's target goal.

### tuning_analysis

I predicted that with a low Kp and low Kd, the arm would react super slowly and have a huge offset and the results in the actual test are similar, where the shoulder sometimes reaches the target but tends to overshoot and take too long to respond the overshooting. Gravity compensation seems to change how quickly it takes for the arm to brake or slow down so it doesn't overshoot it's target as much. This works exceptionally well when combined with a stiffer tuning of High Kp and High Kd.