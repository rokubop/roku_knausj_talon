from talon import Module, cron

class SpeedController:
    def __init__(self, acceleration=20, max_velocity=10):
        self.velocity = 0
        self.acceleration = acceleration
        self.max_velocity = max_velocity
        self.job = None

    def go(self):
        if self.job:
            cron.cancel(self.job)

        self.job = cron.interval("16ms", self.accelerate)

    def release(self):
        if self.job:
            cron.cancel(self.job)

        if self.velocity <= 4:
            print("decelerating slowly")
            self.velocity = 1
            self.job = cron.interval("16ms", self.decelerate_slow)
        else:
            print("decelerating normally")
            self.job = cron.interval("16ms", self.decelerate)

    def accelerate(self):
        self.velocity += self.acceleration * 0.016  # 16ms = 0.016 seconds
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity

        print(f"Current velocity: {self.velocity} m/s")

    def decelerate(self):
        self.velocity -= self.acceleration * 0.016 / 2 # 16ms = 0.016 seconds
        if self.velocity <= 0.05:
            self.velocity = 0
            cron.cancel(self.job)
            self.job = None

        print(f"Current velocity: {round(self.velocity) + 1} m/s")

    def decelerate_slow(self):
        self.velocity -= self.acceleration * 0.016 / 16  # 16ms = 0.016 seconds
        if self.velocity <= 0.05:
            self.velocity = 0
            cron.cancel(self.job)
            self.job = None

        print(f"Current velocity: {round(self.velocity) + 1} m/s")


speed_controller = SpeedController()

mod = Module()

@mod.action_class
class Actions:
    def pedal_speed_controller_down():
        """pedal_speed_controller_down"""
        speed_controller.go()

    def pedal_speed_controller_up():
        """pedal_speed_controller_up"""
        speed_controller.release()
