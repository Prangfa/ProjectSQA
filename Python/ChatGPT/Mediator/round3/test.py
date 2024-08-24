# test_mediator.py

import pytest
from mediator import Mediator, ConcreteColleagueA, ConcreteColleagueB

@pytest.fixture
def setup_mediator():
    mediator = Mediator()
    colleague_a = ConcreteColleagueA()
    colleague_b = ConcreteColleagueB()
    mediator.register(colleague_a)
    mediator.register(colleague_b)
    return mediator, colleague_a, colleague_b

def test_mediator_send_message(setup_mediator):
    mediator, colleague_a, colleague_b = setup_mediator

    # Capture the output of the print statements
    from io import StringIO
    import sys

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Send a message from colleague_a
    colleague_a.send("Hello, Colleague B!")

    # Get the printed output
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    # Check if the message was received by colleague_b
    assert "ConcreteColleagueB received: Hello, Colleague B!" in output
    assert "ConcreteColleagueA received: Hello, Colleague B!" not in output
