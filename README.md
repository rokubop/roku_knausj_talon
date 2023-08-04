# roku_talon

Fork of [talonhub/community](https://github.com/talonhub/community) for my personal Talon commands

## Custom Apps
- [Audacity](apps/audacity/audacity.talon)
- [Blender](apps/blender/blender.talon)
- [FL Studio](apps/flstudio/fl_studio.talon)
- [DaVinci Resolve](apps/davinci_resolve/davinci_resolve.talon)
- [Clip Studio](apps/clipstudio/clipstudio.talon)
- [MPC Player](apps/mpc/mpc.talon)
- [Obsidian](apps/obsidian/obsidian.talon)
- [YouTube](web/youtube.talon)

## Custom Games
- [Card Survival Tropical Island](games/card_survival_tropical_island.talon)
- [Planet of Lana](games/planet_of_lana.talon)
- [The Forgotten City](games/planet_of_lana.talon)

## Custom Features
- [Talon restart](plugin/talon_helpers/talon_helpers.py)
- [Windows powershell command](update-repos.ps1) or [shell command](update-repos.sh) to update all of repositories sibling to current directory
- [Parrot palate for repeat and tut for doing the opposite](custom/parrot.py)
- [Inserting mock data into fields](plugin/mock_data/mock_data.talon)
- [window max/min/restore for windows](core/windows_and_tabs/window_and_tabs_win_roku.py)
- pokey_talon style centralized [terms for select/teleport/delete/find/list](core/terms_roku.py)
- [ziemus's game_mode](https://github.com/ziemus/knausj_talon/tree/main/core/modes/game_modehttps://github.com/ziemus/knausj_talon/tree/main/core/modes/game_mode)
  - added [game_side_scroller](core/modes/game_mode/controls/control_scheme/game_side_scroller.py)
  - added [automatic game mode switching](games/automatic_game_mode.py)
- [Andreas' lorem ipsum generator](plugin/lorem_ipsum/)
- [Andreas' mouse commands](plugin/mouse/mouse.py) which work nicely with dragging and using the pop sound to stop
- pokey_talon based [line edit commands](core/edit/edit_roku.talon) (tug / drain / step / north / south / head / tail / pour / drink / disk) and [symbols](plugin/symbols/symbols.talon)

## Code Features
- [pokey based chain commands for javascript](lang/javascript/javascript.talon)
- [cursorless snippets](cursorless-snippets/)
