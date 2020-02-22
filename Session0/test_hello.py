def add(x,y):
    print("Hello add\n")
    ''' run test with print, youcan add -s
    pytest -s Session0/test_hello.py '''
    return x + y

def sub(x,y):
    return x - y

def test_add():
    assert add(4, 5) == 9

def test_sub():
    assert sub(4, 5) == -1
