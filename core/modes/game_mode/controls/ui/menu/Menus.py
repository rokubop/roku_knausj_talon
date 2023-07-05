from talon import actions, Module

mod = Module()


@mod.action_class
class Menus:
    def game_manual_save():
        """"""
        return

    def game_quick_save():
        """"""
        actions.key("f5")

    def game_quick_load():
        """Load quick save. Left blank to be overridden if needed."""
        return

    def game_menu():
        """"""
        actions.key("escape")

    def game_character_sheet_show():
        """Show character sheet"""
        actions.key("c")

    def game_crafting_menu_show():
        """Show or hide crafting menu"""
        actions.key("o")

    def game_quest_log_show():
        """Show or hide quest log or journal"""
        actions.key("j")

    def game_bestiary_show():
        """Show or hide glossary/bestiary/index/notebook"""
        actions.key("n")