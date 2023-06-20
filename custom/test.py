from talon import Module

mod = Module()

def fibonacci(n: str):
    if n == 'world':
        print('yo')


@mod.action_class
class Actions:
    def test_one(whatever: str):
        """test"""
        if whatever == 'world':
            print('yo')