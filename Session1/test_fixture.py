import pytest
class Box(object):
    def __init__(self, size, color):
        self.__size = size
        self.__color = color
    def __str__(self):
        return "Box size:%d,color:%s"%(self.__size,self.__color)

    def expandBox(self, fact):
        self.__size = fact *  self.__size
        return self.__size

@pytest.fixture
def prepare_Box():
    box = Box(10,"Yellow")
    return box

@pytest.fixture
def prepare_fact():
    return 2

def test_BoxExpand(prepare_Box,prepare_fact):
    assert prepare_Box.expandBox(prepare_fact) == 20