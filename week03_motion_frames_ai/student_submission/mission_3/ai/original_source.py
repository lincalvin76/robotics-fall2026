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