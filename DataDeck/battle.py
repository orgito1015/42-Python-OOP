from ex0 import AquaFactory, Creature, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Verify factory creates describable and attackable creatures."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    factory_a: CreatureFactory, factory_b: CreatureFactory
) -> None:
    """Make base creatures from two factories fight."""
    print("Testing battle")
    creature_a: Creature = factory_a.create_base()
    creature_b: Creature = factory_b.create_base()
    print(f"{creature_a.describe()} vs. {creature_b.describe()}")
    print("fight!")
    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)
