import numpy as np

def generate_curve(steps: int = 40, curve_type: str = 'flick', max_val: int = 40, round_values: bool = True, transition_point: float = 0.5):
    """Generates a dictionary of values for a given curve type from 0 to steps-1."""
    curve_values = []

    if curve_type == 'constant_then_drop':
        constant_end_step = int(steps * transition_point)
        constant_values = [max_val for _ in range(constant_end_step)]

        drop_steps = steps - constant_end_step
        drop_values = [max_val * (1 - (step / drop_steps)) for step in range(drop_steps)]

        curve_values = constant_values + drop_values
    elif curve_type == 'flick':
        b = 5 / steps  # Decay rate
        curve_values = [max_val * np.exp(-b * step) for step in range(steps)]
    else:
        raise ValueError("Unsupported curve type. Currently only 'constant_then_drop' and 'flick' are implemented.")

    if round_values:
        curve_values = [int(round(val)) for val in curve_values]

    curve = {step: curve_values[step] for step in range(steps)}

    return curve


# Example usage for a 'flick' curve
curve = generate_curve(steps=40, curve_type='flick', max_val=40, round_values=True)
print(curve)
curve = generate_curve(steps=100, curve_type='constant_then_drop', max_val=5, round_values=True, transition_point=0.75)
print(curve)
