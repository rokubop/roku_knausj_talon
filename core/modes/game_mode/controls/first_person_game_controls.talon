mode: user.game
and tag: user.first_person_game_controls
-
tag(): user.game_basic_movement
tag(): user.game_camera_controls
tag(): user.game_sprint_controls

#miscellaneous movement
jump:
    user.game_jump()
crouch | duck:
	user.game_crouch()
roll | dodge | doo:
	user.game_dodge()
long roll | long dodge | [sausage] dog:
	user.game_long_dodge()
dive:
	user.game_dive_start()
dive done:
	user.game_dive_stop()

#basic interactions
use [it | that]:
    user.game_use()
long use | using | user:
	user.game_long_use()
hold use:
	user.game_hold_use()
(release | real | don't) use:
	user.game_release_use()

(loot | search) (it | that):
	user.game_loot()
	
take | pick [up] | gather:
    user.game_take()
take <number>:
	user.game_take_number(number)
take many:
	user.game_take_all()

talk (with | to):
    user.game_talk()

heal:
	user.game_heal()
[potion] drink | pot:
	user.game_potion_drink()

stealth kill | put out | eliminate:
	user.game_stealth_kill()
[stealth] choke:
	user.game_stealth_choke()

[fast] [equip | switch] {user.game_number_shortcuts}:
	user.game_number_shortcut(game_number_shortcuts)
	
[weapon] reload | red:
    key(r)

# basic user interface
map show:
	user.game_map_show()
(inventory | equipment | bag) [show]:
    user.game_inventory_show()
(character sheet | car sheet) [show]:
	user.game_character_sheet_show()
(journal | quest log) [show]:
	user.game_quest_log_show()