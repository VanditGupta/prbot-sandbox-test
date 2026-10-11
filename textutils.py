"""Tiny text helpers."""


def truncate(text: str, max_len: int) -> str:
    """Return text cut to at most max_len characters, ending with '...' when cut."""
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return "..."[:max_len]
    return text[: max_len - 3] + "..."
