from textutils import truncate


def test_short_text_unchanged():
    assert truncate("hello", 10) == "hello"


def test_exact_length_unchanged():
    assert truncate("hello", 5) == "hello"


def test_truncated_text_fits_max_len():
    assert truncate("hello world", 8) == "hello..."


def test_tiny_max_len_never_exceeded():
    assert len(truncate("hello world", 2)) <= 2
