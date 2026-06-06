"""
Exercise 1: Higher Realm - Functions Operating on Functions

Callable is imported from collections.abc (recommended over typing.Callable
since Python 3.9+). callable() is a built-in that returns True if an object
appears callable (i.e. has a __call__ method), useful for runtime validation.
"""

from collections.abc import Callable


# ---------------------------------------------------------------------------
# Sample spells — follow the contract: (target: str, power: int) -> str
# ---------------------------------------------------------------------------

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} fire damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} lightning damage"


def frost(target: str, power: int) -> str:
    return f"Frost slows {target} for {power} ice damage"


# ---------------------------------------------------------------------------
# Higher-order functions
# ---------------------------------------------------------------------------

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a new spell that casts both spells and returns a tuple."""
    if not (callable(spell1) and callable(spell2)):
        raise TypeError("Both arguments must be callable spells.")

    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell with power scaled by multiplier."""
    if not callable(base_spell):
        raise TypeError("base_spell must be a callable.")
    if multiplier <= 0:
        raise ValueError("multiplier must be a positive integer.")

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only fires when condition(*args) is True."""
    if not (callable(condition) and callable(spell)):
        raise TypeError("Both condition and spell must be callable.")

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells in order, collecting results."""
    if not all(callable(s) for s in spells):
        raise TypeError("All items in spells must be callable.")

    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]

    return sequence


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    target = "Dragon"
    power = 10

    # spell_combiner
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined(target, power)
    print(f"Combined spell result: {result1}, {result2}")

    # power_amplifier
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {power}, Amplified: {power * 3}")
    print(f"  {fireball(target, power)}")
    print(f"  {mega_fireball(target, power)}")

    # conditional_caster
    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(
        lambda t, p: p >= 20,
        fireball
    )
    print(f"  Power {power}  -> {high_power_only(target, power)}")
    print(f"  Power 25     -> {high_power_only(target, 25)}")

    # spell_sequence
    print("\nTesting spell sequence...")
    barrage = spell_sequence([fireball, heal, lightning, frost])
    for outcome in barrage(target, power):
        print(f"  {outcome}")

    # callable() runtime check
    print("\nRuntime callable() checks...")
    print(f"  fireball is callable: {callable(fireball)}")
    print(f"  42 is callable:       {callable(42)}")
    print(f"  'hello' is callable:  {callable('hello')}")
