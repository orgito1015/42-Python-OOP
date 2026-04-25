import alchemy
from alchemy.elements import (
    create_fire,
    create_water,
    create_earth,
    create_air,
)


def main():
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): ", create_fire())
    print("alchemy.elements.create_water(): ", create_water())
    print("alchemy.elements.create_earth(): ", create_earth())
    print("alchemy.elements.create_air(): ", create_air())

    print("\nTesting package-level access (controlled by __init__.py):")
    print("alchemy.create_fire(): ", alchemy.create_fire())
    print("alchemy.create_water(): ", alchemy.create_water())
    try:
        print("alchemy.create_earth(): ", alchemy.create_earth())
    except AttributeError as e:
        print(f"alchemy.create_earth(): {e}")
    try:
        print("alchemy.create_air(): ", alchemy.create_air())
    except AttributeError as e:
        print(f"alchemy.create_air(): {e}")

    metadata = (
        f"\nVersion: {alchemy.__version__},\nAuthor: {alchemy.__author__}"
    )
    print("Package Metadata:", metadata)


if __name__ == "__main__":
    main()
