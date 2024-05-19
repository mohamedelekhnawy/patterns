
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        self._state = state
        print(f"Originator: Setting state to {state}")

    def get_state(self):
        return self._state

    def save_state_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def get_state_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")


class Caretaker:
    def __init__(self):
        self._memento_list = []

    def add(self, state):
        self._memento_list.append(state)

    def get(self, index):
        return self._memento_list[index]


originator = Originator()
caretaker = Caretaker()

originator.set_state("State #1")
originator.set_state("State #2")
caretaker.add(originator.save_state_to_memento())

originator.set_state("State #3")
caretaker.add(originator.save_state_to_memento())

originator.set_state("State #4")

print("Current State: " + originator.get_state())
originator.get_state_from_memento(caretaker.get(0))
print("First saved State: " + originator.get_state())
originator.get_state_from_memento(caretaker.get(1))
print("Second saved State: " + originator.get_state())
