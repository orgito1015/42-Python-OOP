"""
Exercise 0: Lambda Sanctum - Mastering Anonymous Functions
"""

from collections.abc import Callable  # noqa: F401


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level (descending)."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by minimum power level."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by adding '* ' prefix and ' *' suffix."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate power statistics across all mages."""
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(powers, key=lambda x: x),
        'min_power': min(powers, key=lambda x: x),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'divination'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'combat'},
        {'name': 'Shadow Cloak', 'power': 78, 'type': 'stealth'},
        {'name': 'Arcane Tome', 'power': 88, 'type': 'knowledge'},
    ]

    mages = [
        {'name': 'Aldric', 'power': 95, 'element': 'fire'},
        {'name': 'Seraphine', 'power': 72, 'element': 'water'},
        {'name': 'Bramwell', 'power': 88, 'element': 'earth'},
        {'name': 'Lyra', 'power': 60, 'element': 'wind'},
        {'name': 'Dorian', 'power': 81, 'element': 'shadow'},
    ]

    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("\nTesting power filter (min_power=80)...")
    strong_mages = power_filter(mages, 80)
    print(" ".join(map(lambda m: m['name'], strong_mages)))

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max: {stats['max_power']} | "
        f"Min: {stats['min_power']} | "
        f"Avg: {stats['avg_power']}"
    )
