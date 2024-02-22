from ..typings import Profile

# acceleration_linear
#       _____________
#     *
#   *
# *
#
acceleration_linear = lambda t, max: 1 + min(t / 0.5, max)

# deceleration_cubic
# ------.,
#          ` .
#              `
#                `.
#                  \
deceleration_cubic = lambda t: (1 - (t / (t + 1) ** 0.5)) ** 3

profile_default: Profile = {
    # linear increase until max
    "acceleration_curve": acceleration_linear,
    "deceleration_curve": deceleration_cubic,
    "base_speed": 15,
    "max_speed": 1.3
}