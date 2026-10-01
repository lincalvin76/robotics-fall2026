"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
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
    if pattern_name == "alternating_arcs": 
        # Four 45-degree arcs: # +45, -45, +45, -45 degrees. 
        # v = 0.18 m/s 
        # omega = +/-0.60 rad/s 
        # radius = v / |omega| = 0.30 m 
        linear_x = 0.18
        angular_z = 0.60 
        forty_five_degrees = 3.141592653589793 / 4.0 
        duration = abs(forty_five_degrees / angular_z)
    
        return [ 
            Segment(linear_x, angular_z, duration), 
            Segment(linear_x, -angular_z, duration), 
            Segment(linear_x, angular_z, duration), 
            Segment(linear_x, -angular_z, duration), 
        ] 

    raise ValueError(f"Unknown pattern name: {pattern_name}")
