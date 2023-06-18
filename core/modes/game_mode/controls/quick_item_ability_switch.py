from talon import Module, actions, Context

mod = Module()
mod.list("game_number_shortcuts")
mod.list("game_previous_keyword")
mod.list("game_next_keyword")

scroll_amount = mod.setting(
    "game_item_ability_switch_scroll_amount",
    type=int,
    default=0,
    desc="Scroll amount to switch between a singular tool, weapon, skill or spell")

ctx = Context()
ctx.lists["user.game_previous_keyword"] = {
    "previous", "prev", "pre", "pray", "last", "left"
}
ctx.lists["user.game_next_keyword"] = {"next", "ness", "nest", "net", "neck", "right"}
ctx.lists["user.game_number_shortcuts"] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

@mod.action_class
class Actions:

    def game_weapon_switch_previous():
        """Switch selected weapon. Defaults to scrolling up by user.game_item_switch_scroll_amount"""
        actions.mouse_scroll(y=-scroll_amount.get())

    def game_weapon_switch_next():
        """Switch selected weapon. Defaults to scrolling down by user.game_item_switch_scroll_amount"""
        actions.mouse_scroll(y=scroll_amount.get())

    def game_tool_switch_previous():
        """Switch selected tool or trap, like in a souls-like game.
        Defaults to scrolling up by user.game_item_switch_scroll_amount"""
        actions.mouse_scroll(y=-scroll_amount.get())

    def game_tool_switch_next():
        """Switch selected tool or trap, like in a souls-like game.
        Defaults to scrolling down by user.game_item_switch_scroll_amount"""
        actions.mouse_scroll(y=scroll_amount.get())

    def game_skill_switch_previous():
        """Switch selected skill.
        Defaults to scrolling up by user.game_item_switch_scroll_amount"""
        actions.mouse_scroll(y=-scroll_amount.get())

    def game_skill_switch_next():
        """Switch selected skill.
        Defaults to scrolling down by user.game_item_switch_scroll_amount"""
        actions.mouse_scroll(y=scroll_amount.get())

    def game_spell_switch_previous():
        """Switch selected spell. Defaults to calling actions.user.game_skill_use().
        Defined as a separate action for games that differentiate between skill and spell controls."""
        actions.user.game_skill_switch_previous()

    def game_spell_switch_next():
        """Switch selected spell. Defaults to calling actions.user.game_skill_use().
        Defined as a separate action for games that differentiate between skill and spell controls."""
        actions.user.game_skill_switch_next()