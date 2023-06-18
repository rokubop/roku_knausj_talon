from talon import Module, actions, Context

mod = Module()
mod.tag("game_skills")

mod.list(
    "game_skill_keyword",
    desc=
    "All keywords for an ability. May be overridden to suite a games setting or personal preferences."
)
mod.list(
    "game_spell_keyword",
    desc=
    "All keywords for a magic spell. May be overridden to suite a games setting or personal preferences."
)
ctx = Context()
ctx.lists["user.game_skill_keyword"] = {"ability", "perk", "skill", "kill"}
ctx.lists["user.game_spell_keyword"] = {"power", "spell", "pell", "cast"}


@mod.action_class
class Actions:

    def game_skill_learn():
        """Learn a skill. No binding by default. Needs to be overridden."""
        return

    def game_skill_unlearn():
        """Unlearn a skill. Defaults to user.game_skill_learn()"""
        actions.user.game_skill_learn()

    def game_skill_use():
        """Use selected skill. No binding by default."""
        return

    def game_skill_duration_end():
        """End the duration of an enduring skill. No biding by default."""
        return

    def game_skill_tree_show():
        """Show or hide skill tree/ability menu etc"""
        actions.key("k")

    def game_skill_show_all():
        """Show or hide all available skills. No biding by default."""
        return

    def game_spell_tree_show():
        """Show or hide spell tree. Defaults to calling actions.user.game_skill_tree_show().
        Defined as a separate action for games that differentiate between skill and spell controls."""
        actions.user.game_skill_tree_show()

    def games_spellbook_show():
        """Show or hide spellbook. No biding by default."""
        return

    def game_spell_use():
        """Use selected spell. Defaults to calling actions.user.game_skill_use().
        Defined as a separate action for games that differentiate between skill and spell controls."""
        actions.user.game_skill_use()