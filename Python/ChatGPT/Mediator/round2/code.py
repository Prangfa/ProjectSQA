class Mediator:
    def __init__(self):
        self.participants = {}

    def register(self, participant):
        self.participants[participant.name] = participant
        participant.mediator = self

    def send(self, message, from_participant_name, to_participant_name):
        if to_participant_name in self.participants:
            to_participant = self.participants[to_participant_name]
            to_participant.receive(message, from_participant_name)
        else:
            print(f"Participant {to_participant_name} not found.")

class Participant:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def send(self, message, to_participant_name):
        if self.mediator:
            self.mediator.send(message, self.name, to_participant_name)
        else:
            print("Mediator is not set.")

    def receive(self, message, from_participant_name):
        print(f"{self.name} received a message from {from_participant_name}: {message}")

# Example usage
if __name__ == "__main__":
    # Create mediator
    mediator = Mediator()
    
    # Create participants
    alice = Participant("Alice")
    bob = Participant("Bob")
    charlie = Participant("Charlie")

    # Register participants with the mediator
    mediator.register(alice)
    mediator.register(bob)
    mediator.register(charlie)
    
    # Participants communicate through the mediator
    alice.send("Hello Bob!", "Bob")
    bob.send("Hi Alice!", "Alice")
    alice.send("Hi Charlie!", "Charlie")
    charlie.send("Hello Alice and Bob!", "Alice")
    charlie.send("Hello Alice and Bob!", "Bob")
