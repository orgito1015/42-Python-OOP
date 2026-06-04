from ex0 import AquaFactory, Creature, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """Run a tournament where each opponent fights every other once."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    creatures_strategies: list[tuple[Creature, BattleStrategy]] = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]
    for i in range(len(creatures_strategies)):
        for j in range(i + 1, len(creatures_strategies)):
            creature_a, strategy_a = creatures_strategies[i]
            creature_b, strategy_b = creatures_strategies[j]
            print("* Battle *")
            print(
                f"{creature_a.describe()} vs. "
                f"{creature_b.describe()} now fight!"
            )
            try:
                for action in strategy_a.act(creature_a):
                    print(action)
                for action in strategy_b.act(creature_b):
                    print(action)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
