def chunk(items: list, size: int) -> list[list]:
    """Split items into lists of at most `size` elements."""
    if size < 1:
        raise ValueError("size must be >= 1")
    return [items[i : i + size] for i in range(0, len(items), size)]


def clamp(value: float, low: float, high: float) -> float:
    """Limit value to the range [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    return max(low, min(value, high))
