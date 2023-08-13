from talon import Module, actions, app

# virtual keyboard
def register_keyboard():
    keys = [
	    actions.user.hud_create_virtual_key('1', 'One'),
	    actions.user.hud_create_virtual_key('2', 'Two'),
	    actions.user.hud_create_virtual_key('3', 'Three'),
	    actions.user.hud_create_virtual_key('4', 'Four'),
	    actions.user.hud_create_virtual_key('5', 'Five'),
	    actions.user.hud_create_virtual_key('6', 'Six'),
	    actions.user.hud_create_virtual_key('7', 'Seven'),
	    actions.user.hud_create_virtual_key('8', 'Eight'),
	    actions.user.hud_create_virtual_key('9', 'Nine')
	]
    actions.user.hud_register_virtual_keyboard('example_keyboard', keys)

app.register('ready', register_keyboard)

# dwell toolbar
def register_dwell_toolbar():
    keys = [
	    actions.user.hud_create_virtual_key('shift-a', 'A'),
	    actions.user.hud_create_virtual_key('shift-b', 'B'),
	    actions.user.hud_create_virtual_key('shift-c', 'C'),
	    actions.user.hud_create_virtual_key('shift-d', 'D'),
	    actions.user.hud_create_virtual_key('shift-e', 'E')
	]
    actions.user.hud_register_dwell_toolbar('example_toolbar', keys)

app.register('ready', register_dwell_toolbar)


# regions

mod = Module()

@mod.action_class
class Actions:

    def add_yellow_cursor():
        """Add a yellow icon to the cursor tracker"""
        yellow_cursor = [actions.user.hud_create_screen_region('cursor_example', 'FFF000')]
        actions.user.hud_publish_screen_regions('cursor', yellow_cursor, 1)

    def add_red_cursor():
        """Add a red icon to the cursor tracker"""
        red_cursor = [actions.user.hud_create_screen_region('cursor_example', 'FF0000')]
        actions.user.hud_publish_screen_regions('cursor', red_cursor, 1)

    def add_split_cursor_regions():
        """Shows a red icon when looking at the top of the screen, and a yellow icon otherwise"""
        split_cursors = [
            actions.user.hud_create_screen_region('cursor_example', 'FF0000', '', '', 0, 0, 0, 1920, 100),
            actions.user.hud_create_screen_region('cursor_example', 'FFF000')
        ]
        actions.user.hud_publish_screen_regions('cursor', split_cursors, 1)

    def clear_screen_regions():
        """Clear all cursor and screen regions"""
        actions.user.hud_clear_screen_regions('cursor', 'cursor_example')
        actions.user.hud_clear_screen_regions('screen', 'screen_example')

    def add_example_screen_regions():
        """Adds an example view of screen regions"""
        regions = [
            actions.user.hud_create_screen_region('screen_example', 'FF0000', '', 'Always visible', 0, 0, 0, 200, 200),
            actions.user.hud_create_screen_region('screen_example', '00FF00', '', 'Hover only', 1, 0, 200, 200, 200),
            actions.user.hud_create_screen_region('screen_example', '0000FF', '', 'Hover off', -1, 0, 400, 200, 200)
        ]
        regions[0].text_colour = 'FFFFFF'
        regions[0].vertical_centered = False
        regions[2].text_colour = 'FFFFFF'
        actions.user.hud_publish_screen_regions('screen', regions, 1)

# polling

from talon import actions, cron, app, Module

# Starts counting whenever it is enabled
class CountingPoller:
    enabled = False
    content = None
    counting_job = None
    current_count = 0
    topic = "counting"

    def enable(self):
        if not self.enabled:
            self.enabled = True
            self.publish_count() # Immediately publish the current count to the HUD
            self.counting_job = cron.interval("1s", self.count_up) # Increase the count every second

    def disable(self):
        if self.enabled:
            self.enabled = False
            # Clean up all the counting related crons/ registered events
            cron.cancel(self.counting_job)

    def count_up(self):
        self.current_count += 1
        self.publish_count()

    def publish_count(self):
        topic = self.topic # The topic to publish
        topic_type = "status_icons" # The type of topic to publish
        icon = None # The status bar icon, in this case, we do not want any
        text = str(self.current_count) # The text to display in the status bar
        accessible_text = text + " is the current count" # Accessible text that can in the future be used for screen readers
        status_icon = self.content.create_status_icon(topic, icon, text, accessible_text )
        self.content.publish_event("status_icons", self.topic, "replace", status_icon)

    # Disable the counting on the status bar completely
    # As the topic is removed from the widget, the poller won't restart when the widget is enabled again
    def disable_counting(self):
        self.disable()
        self.current_count = 0

        # Remove the topic and the content from the status bar
        self.content.publish_event("status_icons", self.topic, "remove")

# Create a single poller that we can use in action definitions below
counting_poller = CountingPoller()

# Register the poller to the HUD whenever the file is reloaded
def append_poller():
    actions.user.hud_add_poller(counting_poller.topic, counting_poller)
app.register("ready", append_poller)

# Add actions to bind in a .talon file
mod = Module()
@mod.action_class
class Action:

    def start_counting():
        """Starts counting on the Talon HUD status bar"""
        global counting_poller
        actions.user.hud_activate_poller(counting_poller.topic)

    def pause_counting():
        """Pauses the counting on the Talon HUD status bar"""
        global counting_poller
        actions.user.hud_deactivate_poller(counting_poller.topic)

    def stop_counting():
        """Removes the counting from the Talon HUD status bar"""
        global counting_poller
        counting_poller.disable_counting()