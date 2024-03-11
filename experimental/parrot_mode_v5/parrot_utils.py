from talon import Module, actions, cron

mod = Module()

combo_chain = ""
combo_job = None

def no_op():
    pass

def parrot_combo_stop():
    global combo_chain, combo_job
    if combo_job:
        cron.cancel(combo_job)
        combo_job = None
    actions.user.on_parrot_combo_stop({"combo": combo_chain})
    combo_chain = ""

@mod.action_class
class Actions:
    def parrot_combo(name: str):
        """Helper for combos. Define `ctx` callbacks `on_parrot_combo(ev: dict)` and/or `on_parrot_combo_stop(ev: dict)`"""
        global combo_chain, combo_job
        if combo_job:
            cron.cancel(combo_job)

        combo_chain = combo_chain + f" {name}" if combo_chain else name
        actions.user.on_parrot_combo({"combo": combo_chain})
        # parrot_combo_stop()
        combo_job = cron.after("300ms", parrot_combo_stop)

    def on_parrot_combo(ev: dict):
        """Called on each individual combo action"""
        no_op()

    def on_parrot_combo_stop(ev: dict):
        """Called when a complete combo is finished"""
        no_op()
