# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI 39536
- email: calvin.lin80@login.cuny.edu
- name: Calvin Lin

## concepts.observation

Increasing the noise causes the sensor readings to be more scattered and causes it to oscillate and give many different distance results, increasing the bias causes the truth line to move which determines how often the results were actually the correct distance away.

## final.course_reflection

This activity was a bit difficult for me for some reason as a lot of the material when I was reading through the assignment made little sense to me, It took me a while to get started on some of the missions especially Mission 3 as I just wasn't sure what it was asking for, it was a bit unclear. It was interesting to see how changing some values could affect the delay rates and error rates however I wasn't really sure what every single filter meant. 

## final.synthesis

Measurement properties, estimation choices, and deployment context are connected because with measurement properties such as noise, bias, and variance shows how sensor values could affect the error rate from the truth and with the incorrect estimates, the following estimation choices would also suffer because without the right estimated, wrong choices would be made. As shown in mission 2, changing the weights of sensors and methods also affects how rates of errors and delays are estimated, an example of this affecting choice being if an estimate of delay was none, the choice could be to continue moving and stop exactly, however in deployment context this would cause possible injuries or issues as the measurement values were off, so the estimations were off, causing the choices to also be slightly off, which makes deployment dangerous because of this cascading problem starting from measurement to deployment. Mission 3 shows this through 7 scenario tests and how much danger each movement could cause and what the delays may look like depending on its filter and what happens if the sensor readings are missing.

## mission_1.bias

0

## mission_1.bias_vs_variance

Looking at the statistics it seems like the bias is normal because it goes along the average of all the points but the variance is very low since there's not a lot of differing points/readings leading to a lot of the numbers being the exact same. Bias describes how far the truth is from the data while variance describes how different the data is from each other.

## mission_1.dropouts

6

## mission_1.mean

2

## mission_1.median

2

## mission_1.more_samples

More samples may not necessarily remove tis sensor's main problem because there's just not a lot of noise or variance meaning even if more samples were added it would likely still be the same number and nothing much would change.

## mission_1.outliers

1

## mission_1.prediction

For biased readings, the mean would be way further compared to the average amount for the readings, The variance would not change but there would definitely be more bias.  As for noisy readings, the readings may vary a lot more from each other meaning there's a lot more different points , the mean could be slightly different but would stay relatively the same as a non noisy sensor. Lot less bias would be seen.

## mission_1.prediction_draft

For biased readings, the mean would be way further compared to the average amount for the readings, The variance would not change but there would definitely be more bias.  As for noisy readings, the readings may vary a lot more from each other meaning there's a lot more different points , the mean could be slightly different but would stay relatively the same as a non noisy sensor. Lot less bias would be seen.

## mission_1.profile

quantized

## mission_1.robot_consequence

If the robot used these measurements for determining when to brake, it would brake 2m away a majority of the times but there are outliers that could cause it to suddenly brake way earlier than expected, the consequence for this would be a human possibly bumping into the robot while following it and having it stop all of a sudden.

## mission_1.variance

0.004

## mission_2.comparison

Looking at the three windows, the MAE for them did not have much of a pattern, it started with 0.0737 initially before dropping to 0.071 and then increasing back to 0.0724 when the window was 11, so not much pattern to if the MAE is caused by window size or not, and the response_time remained 1.1 throughout all window sizes. As for the Medians, the MAE consistently increased from 0.0702 to 0.072 and finally 0.0847 while the response_delay kept getting shorter and shorter.

## mission_2.fusion_choice

For the 3 fusion weights, at 0.25, 0.50, and 0.75, as the weight increased the response_delay got significantly faster but at the cost of the error rate increasing starting at 0.0702 to 0.072 and finally 0.0847. The best weight to use here would be 0.50 because it would use and equal amount of information from Sensor A which is noisier and 0.50 from Sensor B which is a lot steadier though more bias. By mixing .50 weight for each, you get a relatively good result where the error is average and the response delay is also average, not too high, not too small.

## mission_2.manual_average

4.167

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

Error even higher than previous , response time fastest

## mission_2.responsiveness

Smoothing would be how noisy sensor readings get reduced and responsiveness is how quickly the robot reacts to changes, Looking at the response_delay specifically the median section, the responsiveness got quicker as the weight of sensor A increased, however the smoothing also decreased as Sensor A is more noisy than Sensor B. If the delay was long, it could mean a nearby person may feel unsafe around a robot that could stop way later than its supposed to, possibly introducing harm.

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

Scenarios where people suddenly walk in front of the robot requires immediate stopping. This change should reduce error rate and slightly higher delay

## mission_3.Warehouse.prediction_draft

Scenarios where readings are noisy may raise error rates and cause delays. Should be lower error rates but higher delay to baseline

## mission_3.context_comparison

For both the warehouse and assistance robot the 2 parameters that I changed were just the filter and what to do with missing readings, which were exponential and insufficient evidence. There were 2 other minor differences where assistive had the stopping threshold of 0.95 and caution margin of 0.20 compared to warehouse of 0.75 and 0.10, this is show the importance of not causing dangers to humans especially when they're in need of assistance compared to warehouse components and item damage. Both policies use the same filter and missing reading fallback however the warehouse false-safe rate remained at 0.0062, even though it made the assistance robot drop to 0, showing that this setting alone doesn't guarantee complete safety. This evidence alone shows that there's no 1 policy that's good for all robot's and every robot needs their own policy otherwise people could get injured.

## mission_3.error_costs

For the Warehouse robot, false-safe could cause warehouse workers to be injured or equipment to be damaged. Unnecessary stops could reduce profit within the warehouse and the workers would face a lot of delays. Looking at the baseline and revised results, the unnecessary-stop rate reduced from 0.0561 to 0 but the false-safe rate still remained at 0.0062 meaning the robot still made unsafe decisions at the same rate but stopped making unnecessary stops. As for the Assistive robot, false-safe affects person receiving the assistance they could be injured, unnecessary stops could cause the person that needs assistance to wait a really long time and cause possible dangers.  For Assistive, the revised results managed to reduce the false-safe rate as well as the delay rate both to 0 from its initial baseline.

## mission_3.limitations

The seven tests help establish how a robot policy may work in a simulated environment showing stop rates and false-safe rates however it does not establish if it is safe for a real world scenario. A simulated scenario especially only 7 of them cannot cover every obstacle, environment condition, people movement, and other events. For the warehouse robot a warehouse safety manager could be consulted to check worker traffic patterns and how much fail-safe should be allowed, For the assistive robot possibly any caregivers or accessibility specialists. The tests that should be conducted would be using sudden approaches with a human dummy from different angles and maybe even causing temporary sensor losses.
