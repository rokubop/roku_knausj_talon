from talon import Module

mod = Module(
    """This module aggregates sets of voice commands as tags for quickly adding the whole set to your game voice control scheme.
Each tag shall provide a set of controls characteristic to a video game genre (user.game_action_rpg tag)
or to a more abstract video game category (user.first_person_game_controls tag).""")

mod.tag("first_person_game_controls")
mod.tag("game_action_rpg")
mod.tag("game_genre_crpg")
mod.tag("game_side_scroller")