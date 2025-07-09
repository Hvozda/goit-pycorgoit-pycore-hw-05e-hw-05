
import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r'(?<=\s)(\d+\.\d=)(?=\s)'
    for match in re.findall(pattern, f" {text} "):

        def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
            return sum(func(text))
        
