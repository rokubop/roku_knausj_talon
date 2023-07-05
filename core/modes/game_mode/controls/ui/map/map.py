from talon import Module, actions

mod = Module()
mod.tag("game_map")


@mod.action_class
class Actions:

    def game_map_show():
        """Show game map. M by default."""
        actions.key("m")

    def game_map_hide():
        """Hide game map. Defaults to user.game_map_show() if not overridden."""
        actions.user.game_map_show()

    def game_map_marker_place():
        """Place a marker on the map. RMB by default."""
        actions.user.game_click(1)

    def game_map_marker_clear():
        """Clear a marker from the map. Defaults to user.game_map_marker_place() if not overridden."""
        actions.user.game_map_marker_place()

    def game_map_center():
        """Center game map. G by default."""
        actions.key("g")

    def game_map_rotate():
        """Rotate game map. Not bound by default, needs to be overridden."""
        return

    def game_map_floor_up():
        """Center game map. Page up by default."""
        actions.key("pageup")

    def game_map_floor_down():
        """Center game map. Page down by default."""
        actions.key("pagedown")

    def game_map_filters_show():
        """Show list of map filters. Tab by default."""
        actions.key("tab")

    def game_map_filters_hide():
        """Hide list of map filters. Defaults to user.game_map_filters_show() if not overridden."""
        actions.user.game_map_filters_show()

    def game_map_filter_toggle():
        """Turn a single map filter on/off. Needs to be overridden, otherwise it doesn't do anything."""
        return

    def game_map_filters_toggle_all():
        """Turn all map filters on/off. Needs to be overridden, otherwise it doesn't do anything."""
        return

    def game_map_zoom_in():
        """Zoom in the map. Defaults to a singular scroll up.
        Adjust the setting: user.mouse_wheel_down_amount to adjust the zoom amount."""
        actions.user.mouse_scroll_up()

    def game_map_zoom_out():
        """Zoom out the map. Defaults to a singular scroll down.
        Adjust the setting: user.mouse_wheel_down_amount to adjust the zoom amount."""
        actions.user.mouse_scroll_down()

    def game_map_zoom_in_continuous():
        """Zoom in the map continuously. Defaults to a singular scroll up.
        Adjust the setting: user.mouse_continuous_scroll_amount to adjust the zoom amount.
        """
        actions.user.mouse_scroll_up_continuous()

    def game_map_zoom_out_continuous():
        """Zoom out the map continuously. Defaults to a singular scroll down.
        Adjust the setting: user.mouse_continuous_scroll_amount to adjust the zoom amount.
        """
        actions.user.mouse_scroll_down_continuous()

    def game_map_zoom_continuous_stop():
        """Stop continuous map zoom. Defaults to user.mouse_scroll_stop().
        See also the settings: user.mouse_enable_pop_stops_scroll, user.mouse_enable_hiss_stops_scroll"""
        actions.user.mouse_scroll_stop()
