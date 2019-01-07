
class StateMachine:

    def __init__(self):
        self.state = {}
        self.active_state = None

    def add_state(self, state):
        self.state[state.name] = state

    def think(self):
        if self.active_state:
            self.active_state.do_action()
            new_state_name = self.active_state.check_condition()
            if new_state_name:
                self.set_state(new_state_name)

    def set_state(self, new_state_name):
        if self.active_state:
            self.active_state.exit_action()
        self.active_state = self.state[new_state_name]
        self.active_state.entry_action()
