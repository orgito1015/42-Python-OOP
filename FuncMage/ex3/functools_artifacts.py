"""
Exercise 3: Ancient Library - Functools Treasures

functools.reduce enables powerful left-fold aggregation over any sequence
using a binary function, replacing explicit loops with declarative composition.
functools.lru_cache memoizes pure functions by storing results keyed on
arguments — turning exponential recursive calls into linear ones by avoiding
redundant computation (Fibonacci(30) drops from ~1M calls to 31).
"""

import functools
import operator
from collections.abc import Callable
from typing import Any


# ---------------------------------------------------------------------------
# spell_reducer
# ---------------------------------------------------------------------------

_OPERATIONS: dict[str, Callable] = {
    "add": operator.add,
    "multiply": operator.mul,
    "max": max,
    "min": min,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the named binary operation."""
    if not spells:
        return 0

    if operation not in _OPERATIONS:
        raise ValueError(
            f"Unknown operation '{operation}'. "
            f"Choose from: {list(_OPERATIONS.keys())}"
        )

    op = _OPERATIONS[operation]

    if operation in ("max", "min"):
        return functools.reduce(op, spells)

    return functools.reduce(op, spells)


# ---------------------------------------------------------------------------
# partial_enchanter
# ---------------------------------------------------------------------------

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Return three specialised enchanters pre-filled with power=50
    and a fixed element, using functools.partial.
    """
    return {
        "fire": functools.partial(base_enchantment, power=50, element="fire"),
        "ice": functools.partial(base_enchantment, power=50, element="ice"),
        "lightning": functools.partial(
            base_enchantment, power=50, element="lightning"
        ),
    }


# ---------------------------------------------------------------------------
# memoized_fibonacci
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, accelerated by lru_cache."""
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# ---------------------------------------------------------------------------
# spell_dispatcher
# ---------------------------------------------------------------------------

def spell_dispatcher() -> Callable[[Any], str]:
    """
    Build and return a singledispatch function that handles spells
    based on their argument type.
    """
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    spells = [10, 20, 30, 40]

    # spell_reducer
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print(f"Empty list: {spell_reducer([], 'add')}")
    try:
        spell_reducer(spells, "unknown")
    except ValueError as e:
        print(f"Error caught: {e}")

    # partial_enchanter
    print("\nTesting partial enchanter...")

    def base_enchantment(target: str, power: int, element: str) -> str:
        return f"{element.capitalize()} enchantment on {target} for {power}"

    enchanters = partial_enchanter(base_enchantment)
    for name, enchanter in enchanters.items():
        print(f"  {enchanter(target='Sword')}")

    # memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    for n in (0, 1, 10, 15):
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    # spell_dispatcher
    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast(["fire", "ice", "lightning"]))
    print(cast(3.14))
