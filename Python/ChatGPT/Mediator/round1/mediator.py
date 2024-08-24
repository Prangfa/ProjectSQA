# mediator.py
class Mediator:
    def __init__(self):
        self.colleagues = []

    def register(self, colleague):
        self.colleagues.append(colleague)
        colleague.set_mediator(self)

    def send(self, message, sender):
        for colleague in self.colleagues:
            if colleague != sender:
                colleague.receive(message)

class Colleague:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def send(self, message):
        if self.mediator:
            self.mediator.send(message, self)

    def receive(self, message):
        raise NotImplementedError("Subclasses should implement this!")

class ConcreteColleagueA(Colleague):
    def receive(self, message):
        print(f"ConcreteColleagueA received: {message}")

class ConcreteColleagueB(Colleague):
    def receive(self, message):
        print(f"ConcreteColleagueB received: {message}")
