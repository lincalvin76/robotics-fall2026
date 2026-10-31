# mission_1

## diagnosis
For normal_1 and independent_mug they both gave different results where normal_1 provided us with a box that did have a box on the mug, the detector selected this because it's morphology mask show's a very visible cup with handle shape while all the other spots are small noise values, making selection a lot easier. For the independent_mug however it failed to select the region, the reasoning for this is because my values mainly selected darker values so when the mask was created because of the darker values being selected, the shadow's on the cup were the only pixels that were made bright and everything else was dark leaving half the cup uncaptured. It then proceeded to only select the handle as it was disconnected from everything else.

## limitations
Increasing the brightness value made the box select basically nothing, the mask also just became fully white. The reasoning for this is because when a higher brightness value is accepted pretty much everything on the image will have some brightness making it more suspectable to being captured. Limitations for a different cup or background are the the colors mainly where if the background matches the same shade as the cup or if they're both super bright like a white color.
