tag: user.game_skills
and mode: user.game
-
# game_skill_keyword is by default one of: skill, kill, ability, perk
# it can be modified to suit a game's setting or individual needs
^{user.game_skill_keyword} learn$:
	user.game_skill_learn()
^{user.game_skill_keyword} unlearn$:
	user.game_skill_unlearn()

^{user.game_skill_keyword} tree [show]$:
	user.game_skill_tree_show()
^{user.game_skill_keyword} list [all] [show]$:
	user.game_skill_show_all()

[selected] {user.game_skill_keyword} [use]:
	user.game_skill_use()
{user.game_skill_keyword} (done | no | stop | end):
	user.game_skill_duration_end()

{user.game_skill_keyword} [switch] {user.game_previous_keyword} | kip:
	user.game_skill_switch_previous()
{user.game_skill_keyword} [switch] {user.game_next_keyword} | kap:
	user.game_skill_switch_next()
	
^spell tree [show]$:
	user.game_spell_tree_show()
^spellbook [show]$:
	user.game_spellbook_show()

# game_spell_keyword is by default one of: spell, pell, power, cast
# it can be modified to suit a game's setting or individual needs
[selected] {user.game_spell_keyword} [use]:
	user.game_spell_use()
{user.game_spell_keyword} [switch] {user.game_previous_keyword} | zip:
	user.game_spell_switch_previous()
{user.game_spell_keyword} [switch] {user.game_next_keyword} | zap:
	user.game_spell_switch_next()