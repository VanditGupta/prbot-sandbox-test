from textutils import truncate


def test_short_text_unchanged():
    assert truncate("hello", 10) == "hello"


def test_exact_length_unchanged():
    assert truncate("hello", 5) == "hello"
