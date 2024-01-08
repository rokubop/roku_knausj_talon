from talon import Module, Context, actions, ctrl

mod = Module()

def create_flex_tag(name: str):
    mod.tag(f"flex_{name}", desc=f"Tag for {name}")
    ctx = Context()
    ctx.matches = f"tag: user.flex_{name}"
    return ctx