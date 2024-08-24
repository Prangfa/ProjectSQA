import unittest

class TestMediatorPattern(unittest.TestCase):
    def setUp(self):
        """Set up the mediator and participants for testing."""
        self.mediator = Mediator()
        self.alice = Participant("Alice")
        self.bob = Participant("Bob")
        self.charlie = Participant("Charlie")
        self.mediator.register(self.alice)
        self.mediator.register(self.bob)
        self.mediator.register(self.charlie)

    def test_participant_registration(self):
        """Test if participants are correctly registered with the mediator."""
        self.assertEqual(self.mediator.participants['Alice'], self.alice)
        self.assertEqual(self.mediator.participants['Bob'], self.bob)
        self.assertEqual(self.mediator.participants['Charlie'], self.charlie)

    def test_send_message(self):
        """Test if messages are correctly sent between participants through the mediator."""
        with self.assertLogs(level='INFO') as log:
            self.alice.send("Hello Bob!", "Bob")
            self.assertIn("Bob received a message from Alice: Hello Bob!", log.output)

        with self.assertLogs(level='INFO') as log:
            self.bob.send("Hi Alice!", "Alice")
            self.assertIn("Alice received a message from Bob: Hi Alice!", log.output)

    def test_send_message_to_nonexistent_participant(self):
        """Test sending a message to a participant who is not registered."""
        with self.assertLogs(level='INFO') as log:
            self.alice.send("Hello Nonexistent!", "Nonexistent")
            self.assertIn("Participant Nonexistent not found.", log.output)

    def test_send_message_without_mediator(self):
        """Test sending a message when a participant has no mediator set."""
        no_mediator_participant = Participant("NoMediator")
        with self.assertLogs(level='INFO') as log:
            no_mediator_participant.send("Hello?", "Alice")
            self.assertIn("Mediator is not set.", log.output)

if __name__ == "__main__":
    unittest.main()
