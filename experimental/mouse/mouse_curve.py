import numpy as np
import time
from talon import cron, Module, Context
import win32api, win32con
from .interactive.core.continuous_trigger import ContinuousTrigger

def mouse_move(dx, dy):
    print(f"Moving mouse by dx: {dx}, dy: {dy}")
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), 0)

class MouseMovementGenerator:
    def __init__(self, easing_function):
        self.duration = 0
        self.total_dx = 0
        self.total_dy = 0
        self.start_time = None
        self.running = False
        self.cron_job = None
        self.easing_function = easing_function

    def start_movement(self, degree, duration, distance):
        if self.running:
            self.stop()

        self.duration = duration
        self.start_time = time.time()
        self.running = True

        self.total_dx = distance * np.cos(np.radians(degree))
        self.total_dy = distance * np.sin(np.radians(degree))

        if not self.cron_job:
            self.cron_job = cron.interval("16ms", self.update_position)

    def update_position(self):
        if self.start_time is None or not self.running:
            return

        elapsed = time.time() - self.start_time
        if elapsed >= self.duration:
            self.stop()
            return

        t = elapsed / self.duration
        eased_t = self.easing_function(t)

        current_dx = self.total_dx * eased_t
        current_dy = self.total_dy * eased_t

        delta_dx = current_dx - (self.total_dx * self.easing_function(max(0, t - (16 / 1000))))
        delta_dy = current_dy - (self.total_dy * self.easing_function(max(0, t - (16 / 1000))))

        mouse_move(delta_dx, delta_dy)

    def stop(self):
        self.running = False
        if self.cron_job:
            cron.cancel(self.cron_job)
            self.cron_job = None

    def is_running(self):
        return self.running

# Example usage
def ease_in_out_cubic(t):
    return t * t * (3 - 2 * t)

mod = Module()

# def mouse_move(dx, dy):
#     # Implement the actual mouse movement here
#     pass

class DurationBasedMovementGenerator:
    def __init__(self, easing_function, min_speed, max_speed):
        self.duration = 0
        self.start_time = None
        self.running = False
        self.cron_job = None
        self.easing_function = easing_function
        self.min_speed = min_speed
        self.max_speed = max_speed

    def start_movement(self, duration, direction_degree):
        if self.running:
            self.stop()

        self.duration = duration
        self.start_time = time.time()
        self.running = True
        self.direction_degree = direction_degree

        if not self.cron_job:
            self.cron_job = cron.interval("16ms", self.update_position)

    def update_position(self):
        if self.start_time is None or not self.running:
            return

        elapsed = time.time() - self.start_time
        if elapsed >= self.duration:
            self.stop()
            return

        t = elapsed / self.duration
        eased_t = self.easing_function(t)

        # Calculate the current speed based on eased_t and the min/max thresholds
        current_speed = self.min_speed + (self.max_speed - self.min_speed) * eased_t

        # Calculate the movement delta based on the current speed and direction
        delta_dx = current_speed * np.cos(np.radians(self.direction_degree))
        delta_dy = current_speed * np.sin(np.radians(self.direction_degree))

        mouse_move(delta_dx, delta_dy)

    def stop(self):
        self.running = False
        if self.cron_job:
            cron.cancel(self.cron_job)
            self.cron_job = None

    def is_running(self):
        return self.running

# Example of an easing function
def linear_ease(t):
    return t

# # Example usage
# generator = DurationBasedMovementGenerator(linear_ease, min_speed=1, max_speed=10)
# generator.start_movement(duration=5, direction_degree=45)  # 5 seconds movement at 45 degrees


movement_generator = MouseMovementGenerator(ease_in_out_cubic)
@mod.action_class
class Actions:
    def mouse_move_curve(degree: int, duration: int, distance: int):
        """Move the mouse in a curve"""
        global movement_generator
        movement_generator.start_movement(degree, duration, distance)

    def mouse_move_curve_stop():
        """Stop the mouse in a curve"""
        global movement_generator
        movement_generator.stop()

    def mouse_move_curve_is_moving():
        """check if the mouse is moving"""
        global movement_generator
        return movement_generator.is_running()



# movement_generator.start_movement(45, 2, 100)  # Move 45 degrees for 2 seconds, distance 100

def ease_in_cubic(t):
    return t * t * t

def ease_in_quadratic(t):
    return t * t

def ease_in_out_cubic(t):
    return t * t * (3 - 2 * t)

def ease_in_out_quadratic(t):
    return np.where(t < 0.5, 2 * t * t, -1 + (4 - 2 * t) * t)

def ease_out_cubic(t):
    p = 1 - t
    return 1 - (p * p * p)

def ease_out_quadratic(t):
    return -t * (t - 2)

def flick_with_bounce(t, overshoot=1.25, stiffness=2.5):
    if t < 0.5:
        return 0.5 * (2 * t) ** 2
    elif t < 0.9:
        return 0.5 * (2 * t - 1) ** 2 + 0.5
    else:
        return -0.5 * (2 * t - overshoot) ** (2 * stiffness) + 1

# def on_trigger_start():
#     """
#     Function to be called when the noise or keypress is detected.
#     """
#     global start_time
#     start_time = time.time()
#     initial_curve = ease_in_cubic
#     movement_generator = MouseMovementGenerator(initial_curve)
#     movement_generator.start_movement(degree=45, duration=2, distance=100)

# def on_trigger_end():
#     """
#     Function to be called when the noise or keypress ends.
#     """
#     global start_time
#     duration = time.time() - start_time
#     final_curve = ease_out_cubic
#     movement_generator = MouseMovementGenerator(final_curve)
#     movement_generator.start_movement(degree=45, duration=duration, distance=100)

# ctx = Context()
# ctx.matches = r"""
# mode: user.parrot
# os: windows
# """

# movement_generator = MouseMovementGenerator(ease_in_cubic)
# generator = DurationBasedMovementGenerator(linear_ease, min_speed=1, max_speed=10)
# generator.start_movement(duration=5, direction_degree=45)  # 5 seconds movement at 45 degrees
# def on_start():
#     print("on_start")
#     # movement_generator.start_movement(degree=45, duration=1, distance=500)
#     generator.start_movement(duration=5, direction_degree=45)  # 5 seconds movement at 45 degrees

# def on_stop():
#     print("on_stop")
#     movement_generator.stop()

# hiss = ContinuousTrigger(on_start, on_stop)

# @ctx.action_class("user")
# class Actions:
#     def parrot_hiss():
#         hiss.start()

#     def parrot_hiss_stop():
#         hiss.stop()

# as long as the hiss has started I want to start ramping up until a final number
