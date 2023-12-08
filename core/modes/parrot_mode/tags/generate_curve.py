import numpy as np

def generate_curve(steps=40, curve_type='flick', max_val=40, round_values=True):
    curve_values = []

    if curve_type == 'flick':
        # 'flick' curve - starts at max speed and then quickly decelerates
        # The curve uses an exponential decay formula
        b = 5 / steps  # Decay rate, adjusted for the number of steps
        curve_values = [max_val * np.exp(-b * step) for step in range(steps)]
    else:
        raise ValueError("Unsupported curve type. Currently only 'flick' is implemented.")

    # Rounding the curve values if round_values is True
    if round_values:
        curve_values = [int(round(val)) for val in curve_values]

    # Creating a dictionary for the curve
    curve = {step: curve_values[step] for step in range(steps)}

    return curve

# Example usage for a 'flick' curve
curve = generate_curve(steps=40, curve_type='flick', max_val=40, round_values=True)
print(curve)
