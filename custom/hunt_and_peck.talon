# tag: browser
# -
# # Show and hide hints
# hints refresh: user.rango_command_without_target("refreshHints")
# hints (toggle | switch): user.rango_command_without_target("toggleHints")
# hints on [{user.rango_hints_toggle_levels}]: 
#   user.rango_command_without_target("enableHints", rango_hints_toggle_levels or "global")
# hints off [{user.rango_hints_toggle_levels}]: 
#   user.rango_command_without_target("disableHints", rango_hints_toggle_levels or "global")
# hints reset {user.rango_hints_toggle_levels}: 
#   user.rango_command_without_target("resetToggleLevel", rango_hints_toggle_levels)
# toggle show:
#   user.r