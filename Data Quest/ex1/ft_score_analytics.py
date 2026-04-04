import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )
else:
    scores = []

    i = 1
    while i < len(sys.argv):
        try:
            value = int(sys.argv[i])
            scores.append(value)
        except ValueError:
            print(f"Invalid parameter: ’{sys.argv[i]}’")
        i += 1
    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
            )
    else:
        total = sum(scores)
        count = len(scores)
        average = total / count
        hight = max(scores)
        low = min(scores)
        score_range = hight - low
        print("Scores processed:", scores)
        print("Total players:", count)
        print("Total score:", total)
        print("Average score:", average)
        print("Hight score:", hight)
        print("Low score:", low)
        print("Score range:", score_range)
