"""
Exercise 2: Memory Depths - Lexical Scoping and Closures

Closures let inner functions "remember" variables from their enclosing scope
even after that scope has returned. `nonlocal` is allowed because it binds a
name to the nearest enclosing (non-global) scope — keeping state local to the
closure and preserving functional purity. `global` is forbidden because it
introduces shared mutable state visible everywhere, breaking encapsulation and
making functions impure and hard to reason about.
"""

from collections.abc import Callable


def mage_counter() -> Callable:
    """Return an independent counting closure starting at 0."""
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> Callable:
    """Return a closure that accumulates power on top of an initial base."""
    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies a specific enchantment to any item."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a private key-value store via store/recall callables."""
    _vault: dict = {}

    def store(key: str, value: object) -> None:
        _vault[key] = value

    def recall(key: str) -> object:
        return _vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # mage_counter — two independent counters
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    # spell_accumulator
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    # enchantment_factory
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    # memory_vault
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
