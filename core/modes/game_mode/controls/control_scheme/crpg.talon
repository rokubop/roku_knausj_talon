tag: user.game_genre_crpg
and mode: user.game
-
settings():
    user.mouse_hide_mouse_gui = 1

tag(): user.game_mouse_enabled
tag(): user.game_camera_zoom

[shortcut] {user.game_number_shortcuts}:
	key(game_number_shortcuts)

heal:
	user.game_heal()
[potion] drink | pot:
	user.game_potion_drink()

(inventory | equipment | bag) [show]:
    user.game_inventory_show()
(character sheet | car sheet) [show]:
	user.game_character_sheet_show()
(journal | quest log) [show]:
	user.game_quest_log_show()

[objects] (highlight | hi):
    user.game_interactable_objects_highlight_start()
[objects] (highlight | hi) (end | stop | no):
    user.game_interactable_objects_highlight_stop()