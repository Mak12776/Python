
def test_generate():
    assert len(generate()) == 30
    assert len(generate(length = 20)) == 20