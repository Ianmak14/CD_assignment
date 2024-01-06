import main 

def test_index():
    assert main.index() == 'Hello, world!'
    
def test_welcome():
    assert main.welcome() == 'To bad this is the last assignment!'
