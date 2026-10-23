# Mission 2

## comparison

Looking at the three windows, the MAE for them did not have much of a pattern, it started with 0.0737 initially before dropping to 0.071 and then increasing back to 0.0724 when the window was 11, so not much pattern to if the MAE is caused by window size or not, and the response_time remained 1.1 throughout all window sizes. As for the Medians, the MAE consistently increased from 0.0702 to 0.072 and finally 0.0847 while the response_delay kept getting shorter and shorter.

## fusion_choice

For the 3 fusion weights, at 0.25, 0.50, and 0.75, as the weight increased the response_delay got significantly faster but at the cost of the error rate increasing starting at 0.0702 to 0.072 and finally 0.0847. The best weight to use here would be 0.50 because it would use and equal amount of information from Sensor A which is noisier and 0.50 from Sensor B which is a lot steadier though more bias. By mixing .50 weight for each, you get a relatively good result where the error is average and the response delay is also average, not too high, not too small.

## manual_average

4.167

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

Error even higher than previous , response time fastest

## responsiveness

Smoothing would be how noisy sensor readings get reduced and responsiveness is how quickly the robot reacts to changes, Looking at the response_delay specifically the median section, the responsiveness got quicker as the weight of sensor A increased, however the smoothing also decreased as Sensor A is more noisy than Sensor B. If the delay was long, it could mean a nearby person may feel unsafe around a robot that could stop way later than its supposed to, possibly introducing harm.

## selected

0
