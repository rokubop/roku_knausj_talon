from talon import Module, actions, Context

mod = Module()
mod.tag("game_weapons")
ctx = Context()


@mod.action_class
class Actions:

    def game_weapon_draw():
        """Draw weapon. Defaults to pressing h key"""
        actions.key("h")

    def game_weapon_hide():
        """Hide drawn weapon. Defaults to calling actions.user.game_weapon_draw()"""
        actions.user.game_weapon_draw()

    def game_weapon_drop():
        """Drop used weapon. No binding by default."""
        return

    def game_weapon_melee_show():
        """Show quick access menu for melee weapons or draw melee weapon.
        No binding by default"""
        return

    def game_weapon_ranged_show():
        """Show quick access menu for ranged weapons or draw ranged weapon.
        No binding by default"""
        return

    def game_weapon_thrown_show():
        """Show quick access menu for thrown weapons or draw throne weapon.
        No binding by default"""
        return
