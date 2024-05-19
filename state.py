class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("State A")

class ConcreteStateB(State):
    def handle(self):
        print("State B")

class Context:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()

context = Context(ConcreteStateA())
context.request()  # State A
context.set_state(ConcreteStateB())
context.request()  # State B
