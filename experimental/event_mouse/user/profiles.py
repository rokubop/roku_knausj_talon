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
deceleration_quartic = lambda t: (1 - (t / (t + 1) ** 0.5)) ** 4

acceleration_none = lambda t, max: 1

deceleration_none = lambda t: 0

profile_default: Profile = {
    "name": "dash",
    "acceleration_curve": acceleration_linear,
    "deceleration_curve": deceleration_quartic,
    "base_speed": 14,
    "max_speed": 1.3
}

profile_dash = profile_default

profile_nav: Profile = {
    "name": "nav",
    "acceleration_curve": acceleration_none,
    "deceleration_curve": deceleration_none,
    "base_speed": 3,
    "max_speed": 16
}