import pytest

@pytest.fixture
def start_up():
    print("\n case start\n")

def prepare_up():
    print("\n case start\n")

def test_one(start_up):
    print("\n case end\n")
    assert 0 == 0
