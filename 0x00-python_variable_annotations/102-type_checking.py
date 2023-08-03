#!/usr/bin/env python3
"""
Using mypy to validate the following piece of code and apply
any necessary changes.
"""
from typing import List, Tuple, Union


def zoom_array(lst: List[int], factor: Union[int, float] = 2) -> List[int]:
    """validating the code using mypy"""
    zoomed_in: List[int] = [item for item in lst for i in range(int(factor))]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
