tag: user.game_character_sheet
and mode: user.game
-
# This tag exists so that the same voice command
# along with its shorthand commands
# don't have to be paste into every game that uses them
# I just find it less annoying to set the tag
# than to define the same voice command for every game that uses them
(hero | character | car) [sheet] | sheet:
	user.game_character_sheet_show()