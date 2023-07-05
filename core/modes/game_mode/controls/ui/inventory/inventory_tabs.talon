mode: user.game
and tag: user.game_inventory_tabs
-
(inventory | bag) [go] {user.game_inventory_tabs}:
    user.game_inventory_tab_go(game_inventory_tabs)
(inventory | bag) next:
    user.game_inventory_tab_next()
(inventory | bag) last:
    user.game_inventory_tab_previous()