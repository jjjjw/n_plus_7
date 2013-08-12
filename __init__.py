from n_plus_7 import NPlus7


def n_plus_7(text: str, n: int = 7) -> str:
    global _n_plus_7
    if _n_plus_7 is None:
        _n_plus_7 = NPlus7()

    return _n_plus_7(text, n)
