# session_state.py

class SessionState:
    def __init__(self):
        self._state = {}

    def __getattr__(self, name):
        return self._state.get(name, None)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self._state[name] = value

session_state = SessionState()
