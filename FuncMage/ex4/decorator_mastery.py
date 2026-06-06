"""
Exercise 4: Master's Tower - Decorator Mastery and Class Methods

Decorators enable separation of concerns by wrapping cross-cutting behaviour
(timing, validation, retry logic) around functions without modifying them.
@staticmethod belongs to the class namespace but receives no implicit first
argument (no self/cls) — it is a plain function logically grouped with the
class. Instance methods always receive self and can access instance state.
"""

import time
import functools
from collections.abc import Callable


# ---------------------------------------------------------------------------
# spell_timer
# ---------------------------------------------------------------------------

def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints a function's execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


# ---------------------------------------------------------------------------
# power_validator
# ---------------------------------------------------------------------------

def power_validator(min_power: int) -> Callable:
    """Decorator factory: validates the power argument before calling."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Works for standalone (power first) and methods (self, power, ...)
            power = kwargs.get("power")
            if power is None:
                int_args = [a for a in args if isinstance(a, int)]
                power = int_args[0] if int_args else None
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ---------------------------------------------------------------------------
# retry_spell
# ---------------------------------------------------------------------------

def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory: retries a failing function up to max_attempts."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# ---------------------------------------------------------------------------
# MageGuild
# ---------------------------------------------------------------------------

class MageGuild:
    """A guild that validates mage names and casts spells with power checks."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name >= 3 chars, letters and spaces only."""
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # spell_timer
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    # retry_spell
    print("\nTesting retrying spell...")
    attempt_counter = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise RuntimeError("Spell unstable!")

    print(unstable_spell())

    attempt_counter[0] = 0

    @retry_spell(max_attempts=3)
    def eventually_works() -> str:
        attempt_counter[0] += 1
        if attempt_counter[0] < 3:
            raise RuntimeError("Not ready yet!")
        return "Waaaaaaagh spelled !"

    print(eventually_works())

    # MageGuild
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Aldric"))
    print(MageGuild.validate_mage_name("X2"))

    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Candle"))
