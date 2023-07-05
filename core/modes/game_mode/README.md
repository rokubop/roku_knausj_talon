# Table of contents

1. [Game mode](#game-mode)
    1. [What is it?](#what-is-it)
    1. [Why is this a thing?](#why-is-this-a-thing)
1. [Features](#features)
    1. [Modularity](#modularity)
    1. [Predefined control schemes](#predefined-control-schemes)
    1. [Shorthand commands](#shorthand-commands)
    1. [Hot-swappable noise controls](#hot-swappable-noise-controls)
    1. [First/third person camera movement](#firstthird-person-camera-movement)
    1. [Automated setup and cleanup](#automated-setup-and-cleanup)
1. [Difficulties when gaming by voice](#difficulties-when-gaming-by-voice)
    1. [Latency vs. difficulty](#latency-vs-difficulty)
    1. [Camera movement](#camera-movement)
1. [How to use it?](#how-to-use-it)
    1. [External modifications (required)](#external-modifications-required)
        1. [mouse.py](#mousepy)
        1. [modes.talon](#modestalon)
    1. [Hot-swappable noise controls](#hot-swappable-noise-controls-1)
    1. [First/third person camera movement](#firstthird-person-camera-movement-1)
    1. [Character movement](#character-movement)
    1. [Automated setup and cleanup](#automated-setup-and-cleanup-1)
    1. [Customization](#customization)
    1. [Ready control schemes](#ready-control-schemes)

# Game mode

## What is it?
The underlying code is supposed to provide a generic voice/noise command interface for hands-free gaming with [Talon Voice](https://talonvoice.com/), alongside most common keybindings for in-game actions that are inherent to many video games, such as:
* controlling the player character's movement,
* moving the camera,
* trading a number of items,
* aiming a weapon or
* using an item.

## Why is this a thing?
Many people have been separately developing their own game modes and game controls for specific games in mind, like [Dark Souls controls by chaosparrot.](https://github.com/chaosparrot/talon_darksouls) But as of now, there is no community-maintained game mode or generic voice interface for gaming with talon. This one was made public with the hope that it simplifies getting back into gaming for people affected with disabilities by providing boilerplate code that can be used with any game.

# Features

## Modularity
Most of the voice commands are provided in functional sets that can be turned on with tags in .talon files for any game. Examples include:
* ``user.game_movement`` for [moving around](./controls/movement/basic_movement_controls.talon),
* ``user.game_map`` for [map management](./controls/ui/map/map.talon),
* ``user.game_weapon_aim`` for [aiming weapons](./controls/weapon/aim/weapon_aim.talon).

This way the same voice commands don't need to be declared each time for every game separately and can be reused throughout different games, which simplifies getting used to voice controls for new users.

Of course, not all games are made identical and need the same interface and therefore there will always be the need for customization for a specific title.

## Predefined control schemes
Alongside functional sets of voice commands there are also a couple of genre/game type-specific control schemes. Those control schemes include sets of game mode features, settings and voice commands bundled together under a single tag and are supposed to simplify writing game-specific control schemes for a whole genre or a type of game. Examples include:
* [first/third person perspective game](./controls/control_scheme/first_person_game_controls.talon),
* [actionRPG](./controls/control_scheme/action_rpg_controls.talon),
* [cRPG](./controls/control_scheme/crpg.talon).

## Shorthand commands
Many in-game actions need to be performed quickly, instead the game becomes unplayable. At least, that's the case for combat-oriented games. Saying "weapon aim start" and "weapon aim stop" each time for pressing and releasing the right mouse button is not enough. That's why most combat and more commonly used in-game interactions come with a shorthand voice command, for example:
* ``"aim"`` is the command that toggles aiming both on and off while tracking the current aim state,
* instead of reloading with ``"weapon reload"`` you can just say ``"red"``,
* you can also change movement direction while running by issuing a quick ``"west"`` (or ``"we"``) command *as opposed to:* first stopping the PC's movement, then changing direction, and only then starting PC's movement again.

## Hot-swappable noise controls
With some interactions a shorthand command is not enough because of the latency that comes from speech detection itself. If you are subscribed to Talon beta, you may use parrot integration to control your game with different mouth sounds. But since Talon provides instantaneous pop and hiss detection for free, you can just stick to those 2. The problem is - there are likely many more in-game interactions that require an instantaneous response.

That is what the [hot-swappable noise binding](./controls/noise/noise_controls.talon) is for - changing the active noise binding on the fly. You may provide a deafult binding with settings in a .talon file. If you want to change the binding mid-game, you can say eg. ``"pop move"`` to be able to toggle character movement on/off with a pop sound and ``"hiss long click"`` in order to press LMB with a hiss (and release it when you stop hissing). When you need more movement precision, you may swap that for ``"hiss move"``, so that the character moves only when you hiss continuously.

## First/third person camera movement
Camera control in first (and third) person perspective is one of the bigger difficulties to overcome with hands-free gaming. There is a set of voice commands and settings that takes care of simple camera movement. All can be activated with the ``user.game_camera_controls`` tag and are integrated into the first/third person perspective game voice control scheme under the tag: ``user.first_person_game_controls``.

## Automated setup and cleanup
[Upon disabling the game mode](game_mode.py#L22), keys frequently used in video games are released so that the user doesn't have to release them manually. 

Similarly, automated game setup and cleanup happens on launching, closing, focusing back in and out of the game window, see the following code for details: [game_controls_setup.py](./game_controls_setup.py).

# Difficulties when gaming by voice

## Latency vs. difficulty
First-person video games require a certain amount of hand-to-eye coordination that can rarely be met with voice commands. Speech is very slow compared to key presses and will not provide the sufficient speed when playing competitive or action-packed games. However, it can provide a way for playing single-player games, even action RPGs if played on easier difficulty levels. There is no shame in turning down the difficulty level (even if you're not using alternative input). Games are supposed to be fun, after all.

## Camera movement
Camera movement can be achieved with voice controls but it's hard to control a fast game with voice controls. Let alone, use voice controls for aiming a weapon. If you can use a mouse to move the camera, please do so.

If you cannot use a traditional mouse but sill can move your head, consider buying a cheap wireless smart TV remote with gyroscopic mouse functionality, or an "air mouse". They still won't be enough to play competitive shooters but if you lower the difficulty level, you may still enjoy an action game. It is best used with high mouse sensitivity say so that you don't have to squint at the center of the monitor when you turn your head left and right.

You may still want to use a voice command for turning around, though, as setting mouse sensitivity to very high values just to be able to turn the camera around  with your head tends to generate jittery camera movement and is not ideal. Alternatively, you may bind ``user.game_turn_camera_around()`` to a keypress  with Talon and then use foot switches bound to that key to quickly turn around.

Credits to [u/MrDrumble on r/disabledgamers](https://np.reddit.com/r/disabledgamers/comments/9z9nim/my_lowcost_handsfree_gaming_setup_suggestions/) for coming up with the air mouse solution. You can watch it in action on MrDrumble's YouTube channel: [Cheap, Hands-Free PC Gaming Setup](https://www.youtube.com/watch?v=5NbK83dt6sI).

# How to use it?
Almost everything is included in this directory so you can just copy and paste it onto your own repository to start using it. There are just 2 modification outside of this directory that need to be made.

## External modifications (required)

### mouse.py
I modified [mouse.py](./../../../plugin/mouse/mouse.py) so that the default ``on_pop()`` uses a custom ``user.mouse_hold`` setting instead of the hardcoded value of 16000 nanoseconds. My noise controls also use that setting so if you start using just the game mode code without taking my mouse.py file then you will be getting errors/warnings about an undefined setting.

There is also the custom ``user.mouse_enable_hiss`` setting that needs to be declared and set to false in order to use his with the hot swappable noise binding.

### modes.talon
The command enabling the game mode is defined in [modes.talon](../modes.talon). Other commands were also modified so that enabling any other mode turns off the game mode.

## Hot-swappable noise controls
You may provide a deafult binding with 4 settings in a .talon file, like so:
```
settings():
# do not use the default pop handler - must be set to 0 in order to use the hot-swappable noise controls
    user.mouse_enable_pop_click = 0
# call actions.user.game_dodge() on pop
    user.game_noise_pop_binding_default = "dodge"
# do not use the default hiss handler - must be set to 0 in order to use the hot-swappable noise controls - this is a custom setting from this repo
    user.mouse_enable_hiss = 0
# no default binding for hiss
    user.game_noise_hiss_binding_default = "off"
```
See [noise_controls.py](./controls/noise/noise_controls.py) and [noise_controls.talon](./controls/noise/noise_controls.talon) for more details, [available actions](./controls/noise/noise_controls.py#L40) and their [names and aliases](./controls/noise/noise_controls.py#L12) for use with the default binding settings and voice commands. Those mappings can be expanded in code if you find yourself in need of more available bindings.

## First/third person camera movement
To be able to use the camera controls, set the ``user.game_camera_controls`` tag for your game and define 3 settings:
```
settings():
# say the amount for turning around 180 degrees
	user.game_turn_around_mouse_delta = 500
# the amount for turning sideways left and right 90 degrees
	user.game_turn_horizontally_mouse_delta = 300
#  the amount for turning the camera vertically
	user.game_turn_vertically_mouse_delta = 100

tag(): user.game_camera_controls
```
The values for the settings are game-specific and depend on mouse sensitivity. They need to be found out by trial and error. Usually, the amount for turning around will be less than 2 * ``user.game_turn_horizontally_mouse_delta``.

Now you'll be able to use ``camera turn around``, ``camera turn right``, ``camera turn left``, ``camera turn up``, ``camera turn down`` to control the camera. It is encouraged to use the short forms of those commands, that is: ``round``, ``rye``, ``let``, ``up``, ``down``. You can combine the direction names with "big/little/tiny" (shorthands: "be/lee/tea") for bigger or smaller movements: ``"be rye"``, ``"big up"``, or ``"camera turn big left"``.

The direction names are defined in the list: [``user.game_camera_direction``](./controls/camera/CameraActions.py#L49) and may therefore be modified to suit individual needs.
See [camera_controls.talon](controls/camera/camera_controls.talon) and [CameraActions.py](controls/camera/CameraActions.py) for details.

## Character movement
Similarly to the camera movement direction list, character movement direction names are defined in the [``user.game_directions``](./controls/movement/BasicMovementActions.py#L15) list and can be modified with game-specific contexts. 2 contexts for WSAD/arrow keys are already provided and can be enabled in .talon files with tags: [``user.wsad_game_controls``](./controls/movement/movement_keys/wsad_controls.py) or [``user.game_basic_movement_arrows``](./controls/movement/movement_keys/basic_movement_controls_arrows.py).

If you want to use your own direction names with the standard voice commands for movement, be sure to enable the [``user.game_basic_movement``](./controls/movement/BasicMovementActions.py#L15) tag in your game control scheme.

## Automated setup and cleanup
To achieve automated setup and cleanup, the user needs to provide a list of their games and their respective app.names in a file under: [games.csv](../../../settings/games.csv), like so:
```
AppName,Icon
Talos,
Darkest.exe,Darkest Dungeon
```
An icon to be displayed on the status bar can be provided when using [chaosparrot's Talon HUD](https://github.com/chaosparrot/talon_hud). The icons need to be stored under [``game_icons``](./game_icons) in png format. If the user doesn't provide an icon name explicitly, the name assumed by default is: ``{AppName}.PNG``, eg., ``Talos.PNG`` or ``Darkest.exe.PNG``. Using icons is fully optional.

The list of game keys is returned by the [``user.get_held_game_keys()``](controls/BasicGameActions.py#L227) action. Like any action, it can be overridden to suit your game. If a certain game requires additional cleanup or setup, you may override the [``user.custom_game_cleanup()``](controls/BasicGameActions.py#L240) and [``user.custom_game_setup()``](controls/BasicGameActions.py#L236) actions.

## Customization
Feel free to customize everything as you like. I couldn't have provided an interface that is ideal for every game that exists because there are just so many mechanics in games that it is impossible to fit everything in here. You will need to customize keybindings for your games by overwriting actions. You will likely find a generic action in need of an additional parameter due to how your game handles trading or attack. See Gothic I & II [attack mode change](https://github.com/ziemus/talon_voice_games/blob/master/Gothic/gothic12_common.py#L77), [attack action override](https://github.com/ziemus/talon_voice_games/blob/master/Gothic/gothic12_common.py#L127) and [conditional attack on pop](https://github.com/ziemus/talon_voice_games/blob/master/Gothic/gothic12_common.py#L145), for example.

## Ready control schemes
Predefined game control schemes made for a specific type of a game like [first/third person perspective game](./controls/control_scheme/first_person_game_controls.talon) and [actionRPG](./controls/control_scheme/action_rpg_controls.talon) already come with camera and movement controls enabled.

If you want to see what a control scheme for a specific game looks like, take a look at my other repository where I store my game voice control schemes, [talon_voice_games](https://github.com/ziemus/talon_voice_games).

Just a quick heads up, I do not usually maintain the games that I've completed and do not play anymore so they might not be fully integrated with the capabilities of the core game mode or they might not work 100%.