from typing import Generator, Literal

def fibonacci(n: int) -> Generator[Literal[1], None, None]:
    nmr1 = nmr2 = 1
    for i in range(n):
        yield nmr1
        nmr1, nmr2 = nmr2, nmr1 + nmr2
        