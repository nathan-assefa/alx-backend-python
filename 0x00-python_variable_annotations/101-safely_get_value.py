#!/usr/bin/env python3
"""
Given the parameters and the return values, add type
annotations to the function
"""


from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Adding type annotation"""
    if key in dct:
        return dct[key]
    else:
        return default


""" *************** Any vs T(TypeVar)? **********
Any: Represents a wildcard type that accepts any data type,
     bypassing type checking and allowing any value to be assigned
     to the variable. It is less type-safe and not recommended for
     most cases in type annotations.

T: Represents a generic type variable that is determined based on
   the argument provided during the function call. It allows you to
   create more flexible functions while still preserving type safety,
   as the actual type is resolved at runtime based on the call context.
"""

""" ***** How T provides type-safty while Any not? *********
T provides better type safety because it allows you to statically define
a specific type that is consistent throughout each function call. The
type of T is determined when the function is called, and it remains
constant within the scope of that call. This helps catch type errors at
compile time and ensures that the function behaves correctly with the
expected data types.

On the other hand, when using Any, you lose type safety because Any
represents a wildcard type that can accept any value of any data type.
With Any, you can freely change the data type inside the function without
any type checking. While this can provide flexibility, it also means that
type errors are not caught at compile time, leading to potential runtime
errors and unexpected behavior.

Let's illustrate this with a simple example:

Example with T:

from typing import TypeVar

T = TypeVar('T')

def print_twice(data: T) -> None:
    print(data)
    print(data)

# Calling the function with an integer
print_twice(42)  # Output: 42\n42

# Calling the function with a string
print_twice("Hello")  # Output: Hello\nHello

# Attempting to change the type inside the function (type-safe)
def add_one(data: T) -> T:
    return data + 1  # Error: Unsupported operand type(s) for +: 'T' and 'int'


In this example, the print_twice function uses T as a generic
type variable. Each time the function is called, T represents a
specific data type (e.g., int, str). Attempting to perform unsupported
operations (like adding an integer to a generic type T) will raise
a type error at compile time.

Example with Any:

from typing import Any

def print_twice_any(data: Any) -> None:
    print(data)
    print(data)

# Calling the function with an integer
print_twice_any(42)  # Output: 42\n42

# Calling the function with a string
print_twice_any("Hello")  # Output: Hello\nHello

# Changing the type inside the function (no type-checking)
def add_one_any(data: Any) -> Any:
    return data + 1  # No error, but may lead to unexpected behavior

# Calling the function with a string (unexpected behavior)
result = add_one_any("Hello")
print(result)  # Output: Hello1 (no type-checking leads to concatenation)

from typing import Any

def print_twice_any(data: Any) -> None:
    print(data)
    print(data)

# Calling the function with an integer
print_twice_any(42)  # Output: 42\n42

# Calling the function with a string
print_twice_any("Hello")  # Output: Hello\nHello

# Changing the type inside the function (no type-checking)
def add_one_any(data: Any) -> Any:
    return data + 1  # No error, but may lead to unexpected behavior

# Calling the function with a string (unexpected behavior)
result = add_one_any("Hello")
print(result)  # Output: Hello1 (no type-checking leads to concatenation)
"""
