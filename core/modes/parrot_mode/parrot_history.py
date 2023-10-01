from talon import Module, actions, speech_system

mod = Module()

parrot_history = []

def on_phrase(j: dict):
    global parrot_history

    words = j.get("text")

    text = actions.user.history_transform_phrase_text(words)

    if text is not None:
        parrot_history.append({
            'text': text,
            'type': 'default' if j.get('samples') else 'mimic',
        })
        parrot_history = parrot_history[-20 :]
        # print(parrot_history)

speech_system.register("phrase", on_phrase)

@mod.action_class
class ParrotHistory:
    def get_parrot_history():
        """Get parrot history"""
        global parrot_history
        return parrot_history
