#!/usr/bin/env python3
"""
Writing a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier
Callable[[arg_type1, arg_type2, ...], return_type]
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returning a function """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
