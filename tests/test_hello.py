from hello import hello

def test_hello():
    assert hello() == 'Hello World!'
    assert hello('Martians') == 'Hello Martians!'
