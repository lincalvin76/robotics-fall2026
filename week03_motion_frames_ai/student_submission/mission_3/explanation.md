# Mission 3

## Ai Disclosure

ChatGPT was used for creating code and understand some parts of the code. Personally reviewed the difference in values that the AI provided me and had to change those values, examples being using 90 degress instead of 45, having the radius be 0.40m instead of 0.30, checking these values and verifying them to the assignment.

## Assigned Pattern

alternating_arcs

## Assumptions

The AI for some reason assumed that the arc turns left 90 degree then right 90 degrees when it should be always alternating 45 degree instead, it's also constantly using the same values for linear_x, angle, It does properly assign the correct units of m/s for v and rad/s for omega.  It also assumed how many segments it should return because it only return's a list of 2.

## Evidence Analysis

The important tests established that the robot would follow the proper pattern moving in arcs that alternated the angles from positive to negative, this was shown in the results with the start_pose and end_pose being relatively near each other at least within the same pos/negative axis, with minor changes in either the x or y to indicate movement. These tests do not establish consistent values or any delays in the robots response, additional condition/test that would be needed is resetting the robot back to 0,0 at the start of each run and testing it on a different computer with different frame settings to visualize timing differences.

## Live Pending

False

## Modifications

 I asked it to change to 45 degrees as it was originally set to 90 when the assignment wants 45 and all it really changed was just the turn value math to be dividing pi by 4.0 instead of 2.0, it also returned 4 segments this time instead of the original 2. Using the relationships nothing much really changed besides forcing the duration to be a positive number. 

## Original Output

For alternating_arcs, I’d implement it as two equal 90° arcs with opposite turn directions. That gives a simple, testable pattern:

First arc: turn left 90°
Second arc: turn right 90°
linear_x = 0.20 m/s
angular_z = ±0.40 rad/s
Radius = v / |ω| = 0.20 / 0.40 = 0.50 m
Each arc lasts π/2 / 0.40 ≈ 3.927 s
Total time ≈ 7.854 s
Final heading change ≈ 0 rad
Assuming ideal motion, final displacement ≈ 1.0 m

That stays comfortably inside all the stated bounds.

build_pattern

Replace only the function with:

build_pattern implementation
def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern."""
    if pattern_name == "alternating_arcs":
        # Two 90-degree arcs with opposite curvature.
        # v = 0.20 m/s, omega = +/-0.40 rad/s
        # radius = v / |omega| = 0.50 m
        linear_x = 0.20
        angular_z = 0.40
        quarter_turn = 3.141592653589793 / 2.0
        duration = quarter_turn / angular_z

        return [
            Segment(
                linear_x=linear_x,
                angular_z=angular_z,
                duration=duration,
            ),
            Segment(
                linear_x=linear_x,
                angular_z=-angular_z,
                duration=duration,
            ),
        ]

    raise ValueError(f"Unknown pattern name: {pattern_name}")
Why this works

For a constant-velocity arc:

$$ R = \frac{v}{|\omega|} $$

So:

$$ R = \frac{0.20}{0.40}=0.50\text{ m} $$

For a 90° arc:

$$ t = \frac{\pi/2}{0.40} \approx 3.927\text{ s} $$

The first arc turns the robot +π/2, and the second turns it −π/2, so ideally:

$$ \Delta\theta = \frac{\pi}{2}-\frac{\pi}{2}=0 $$

The two arcs also produce approximately 0.5 m of forward displacement each, giving about 1.0 m total distance from the starting point.

This should therefore give you expected values approximately:

Check	Expected
Final distance	1.00 m
Final angle	0 rad
Arc radius	0.50 m
Total duration	7.85 s
Max linear speed	0.20 m/s
Max angular speed	0.40 rad/s

All are within your evaluator tolerances of ±0.02 m, ±0.04 rad, and ±0.02 m radius.

Tests I'd run
Pattern selection
build_pattern("alternating_arcs") returns exactly 2 segments.
build_pattern("something_else") raises ValueError.
Bounds
Every segment has abs(linear_x) <= 0.22.
Every segment has abs(angular_z) <= 0.80.
Every duration is <= 30.
Total duration is <= 60.
Arc radius

Check:

abs(segment.linear_x / segment.angular_z)

should equal 0.50 m for both segments.

Angle
First arc: +π/2
Second arc: −π/2
Total: approximately 0 rad.
Final distance
With ideal constant-velocity integration, verify approximately 1.00 m.

Important assumption: your prompt doesn't include the actual course specification for the required alternating-arc distance/angle/radius. I'm assuming the intended target is two 90° arcs of radius 0.50 m, which produces the clean 1 m forward / 0 rad final orientation result. If your course handout specifies different target values, those values should determine linear_x, angular_z, and the arc angles instead.

## Original Prompt

"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by build_pattern.
"""
from future import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
linear_x: float
angular_z: float
duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
"""Return ordered, bounded motion segments for the assigned pattern.

Supported assignments are ``rounded_rectangle``, ``l_path``, and
``alternating_arcs``. Do not include the final stop; the ROS wrapper always
publishes it and the evaluator verifies it.
"""
raise NotImplementedError("Mission 3: review the AI output and implement your assigned pattern")

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py. The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command. Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s). Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name. Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total. Do not replace the wrapper or course checks. Explain assumptions and propose tests.
Return ordered, bounded motion segments for the assigned pattern. Supported assignments are rounded_rectangle, l_path, and alternating_arcs. Do not include the final stop; the ROS wrapper always publishes it and the evaluator verifies it.
the checks for success are the final distance being within 0.02m, angle being within 0.04 rad, and arc radius being within 0.02.

## Original Source

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern."""
    if pattern_name == "alternating_arcs":
        # Two 90-degree arcs with opposite curvature.
        # v = 0.20 m/s, omega = +/-0.40 rad/s
        # radius = v / |omega| = 0.50 m
        linear_x = 0.20
        angular_z = 0.40
        quarter_turn = 3.141592653589793 / 2.0
        duration = quarter_turn / angular_z

        return [
            Segment(
                linear_x=linear_x,
                angular_z=angular_z,
                duration=duration,
            ),
            Segment(
                linear_x=linear_x,
                angular_z=-angular_z,
                duration=duration,
            ),
        ]

    raise ValueError(f"Unknown pattern name: {pattern_name}")

## Problems

The duration time seems a little short as the assignment gives us at most 30 seconds per segment and up to 60 seconds but the timing seems to only go up to 4 seconds per segment which might be fine. I checked if this timing seemed fine and it said it was okay but depended on what the assignment evaluator expects.

## Saved Specification

The intended sequence is a bunch of wave like arcs where it'll arc upwards then back downwards before repeating the same steps again. Speeds are strictly within 0.22m and 0.80rad, with each wave being at most 30 seconds and the entire action taking only 60 seconds. Finishes facing the initial starting position, the checks for success are the final distance being within 0.02m, angle being 0.04 rad, and arc radius being 0.02.

## Specification

The intended sequence is a bunch of wave like arcs where it'll arc upwards then back downwards before repeating the same steps again. Speeds are strictly within 0.22m and 0.80rad, with each wave being at most 30 seconds and the entire action taking only 60 seconds. Finishes facing the initial starting position, the checks for success are the final distance being within 0.02m, angle being 0.04 rad, and arc radius being 0.02.

## Test Plan

A pattern behavior should be seeing it make the wave, as its constant moving forward and only changing the angular_z after each duration, Velocity limit test would be checking if it's under the required 0.22m/s. A stop test could be placing something in front of the robot to see if it would stop immediately, or if it crosses some threshold of its expected/predicted place it should stop as well.

## Live Issue


