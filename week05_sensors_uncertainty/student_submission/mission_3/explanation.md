# Mission 3

## Assistive.prediction_draft

Scenarios where people suddenly walk in front of the robot requires immediate stopping. This change should reduce error rate and slightly higher delay

## Warehouse.prediction_draft

Scenarios where readings are noisy may raise error rates and cause delays. Should be lower error rates but higher delay to baseline

## context_comparison

For both the warehouse and assistance robot the 2 parameters that I changed were just the filter and what to do with missing readings, which were exponential and insufficient evidence. There were 2 other minor differences where assistive had the stopping threshold of 0.95 and caution margin of 0.20 compared to warehouse of 0.75 and 0.10, this is show the importance of not causing dangers to humans especially when they're in need of assistance compared to warehouse components and item damage. Both policies use the same filter and missing reading fallback however the warehouse false-safe rate remained at 0.0062, even though it made the assistance robot drop to 0, showing that this setting alone doesn't guarantee complete safety. This evidence alone shows that there's no 1 policy that's good for all robot's and every robot needs their own policy otherwise people could get injured.

## error_costs

For the Warehouse robot, false-safe could cause warehouse workers to be injured or equipment to be damaged. Unnecessary stops could reduce profit within the warehouse and the workers would face a lot of delays. Looking at the baseline and revised results, the unnecessary-stop rate reduced from 0.0561 to 0 but the false-safe rate still remained at 0.0062 meaning the robot still made unsafe decisions at the same rate but stopped making unnecessary stops. As for the Assistive robot, false-safe affects person receiving the assistance they could be injured, unnecessary stops could cause the person that needs assistance to wait a really long time and cause possible dangers.  For Assistive, the revised results managed to reduce the false-safe rate as well as the delay rate both to 0 from its initial baseline.

## limitations

The seven tests help establish how a robot policy may work in a simulated environment showing stop rates and false-safe rates however it does not establish if it is safe for a real world scenario. A simulated scenario especially only 7 of them cannot cover every obstacle, environment condition, people movement, and other events. For the warehouse robot a warehouse safety manager could be consulted to check worker traffic patterns and how much fail-safe should be allowed, For the assistive robot possibly any caregivers or accessibility specialists. The tests that should be conducted would be using sudden approaches with a human dummy from different angles and maybe even causing temporary sensor losses.
