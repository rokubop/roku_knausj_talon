from talon import Module, actions

mod = Module()
mod.tag("game_inventory_tabs")
mod.list("game_inventory_tabs", desc="Tab names for inventory sections/tabs.")


@mod.action_class
class Actions:

    def game_inventory_tab_go(game_inventory_tabs: str):
        """Go to the specified inventory section."""
        return 0

    def game_inventory_tab_next():
        """Go to the next inventory tab."""
        return 0

    def game_inventory_tab_previous():
        """Go to the previous inventory tab."""
        return 0
