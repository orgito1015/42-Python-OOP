import math


def get_player_post():
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = user_input.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coords = []

        for part in parts:
            try:
                coords.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                break
        else:
            return tuple(coords)


print("=== Game Coordinate System ===")

print("\nGet a first set of coordinates")
pos1 = get_player_post()

print("Got a first tuple:", pos1)
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

dist1 = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
print("Distance to center:", round(dist1, 4))

print("\nGet a second set of coordinates")
pos2 = get_player_post()

dist2 = math.sqrt(
    (pos2[0] - pos1[0])**2 +
    (pos2[1] - pos1[1])**2 +
    (pos2[2] - pos1[2])**2
)
print("Distance between the 2 sets of coordinates:", round(dist2, 4))
