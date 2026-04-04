import random

ALL_ACHIEVEMENTS = [
    "First Steps", "Speed Runner", "Boss Slayer", "Treasure Hunter",
    "Master Explorer", "Untouchable", "Survivor", "Strategist",
    "Crafting Genius", "World Savior", "Collector Supreme", "Unstoppable",
    "Sharp Mind", "Hidden Path Finder"
]

PLAYERS = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set:
    """Generate a random set of achievements for a player."""
    count = random.randint(4, 9)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    """Main function to run the achievement tracker system."""
    print("=== Achievement Tracker System ===\n")

    player_achievements: dict[str, set] = {}
    for player in PLAYERS:
        player_achievements[player] = gen_player_achievements()

    for player, achievements in player_achievements.items():
        print(f"Player {player}: {achievements}")

    all_achievements = set.union(*player_achievements.values())
    print(f"\nAll distinct achievements: {all_achievements}")

    common_achievements = set.intersection(*player_achievements.values())
    print(f"\nCommon achievements: {common_achievements}")

    print()
    for player, achievements in player_achievements.items():
        others = set.union(
            *[ach for p, ach in player_achievements.items() if p != player]
        )
        unique = set.difference(achievements, others)
        print(f"Only {player} has: {unique}")

    print()
    for player, achievements in player_achievements.items():
        missing = set.difference(all_achievements, achievements)
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
