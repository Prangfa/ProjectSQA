# mediator.py

class Mediator:
    def __init__(self):
        self._colleagues = []

    def register(self, colleague):
        self._colleagues.append(colleague)
        colleague.set_mediator(self)

    def send(self, message, sender):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)

class Colleague:
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def send(self, message):
        if self._mediator:
            self._mediator.send(message, self)

    def receive(self, message):
        raise NotImplementedError("Subclass must implement this method")

class ConcreteColleagueA(Colleague):
    def receive(self, message):
        print(f"ConcreteColleagueA received: {message}")

class ConcreteColleagueB(Colleague):
    def receive(self, message):
        print(f"ConcreteColleagueB received: {message}")
