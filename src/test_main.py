import pytest
from main import hello_world

def test_hello_world(capsys):
    """Test that hello_world function prints the expected message."""
    hello_world()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
    
def test_hello_world_no_errors():
    """Test that hello_world function executes without errors."""
    try:
        hello_world()
        assert True
    except Exception as e:
        assert False, f"hello_world() raised an exception: {e}"
