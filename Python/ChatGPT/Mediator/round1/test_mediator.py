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

def test_send_message_to_all_colleagues(setup_mediator):
    mediator, colleague_a, colleague_b = setup_mediator

    with pytest.raises(Exception) as excinfo:
        colleague_a.send("Hello, ColleagueB!")
    assert "ConcreteColleagueB received: Hello, ColleagueB!" in str(excinfo.value)

def test_no_message_sent_when_no_mediator(setup_mediator):
    mediator, colleague_a, colleague_b = setup_mediator
    colleague_a.set_mediator(None)
    
    with pytest.raises(Exception) as excinfo:
        colleague_a.send("No mediator message!")
    assert "ConcreteColleagueB received: No mediator message!" not in str(excinfo.value)

def test_message_receiving(setup_mediator):
    mediator, colleague_a, colleague_b = setup_mediator

    # Capture output
    from io import StringIO
    import sys

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    colleague_a.send("Testing message")

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    assert "ConcreteColleagueB received: Testing message" in output
