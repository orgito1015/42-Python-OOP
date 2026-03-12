# 🌿 Growing Code — Python Functional Programming Foundations

**Growing Code** is a beginner-friendly, garden-themed project that introduces the core building blocks of Python programming. Each exercise focuses on a single concept in isolation so you can master one idea before the next one is introduced. By the end, you will have a solid functional programming foundation ready to support the Object-Oriented Programming concepts in [CodeCultivation](../CodeCultivation/).

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Learning Progression](#learning-progression)
- [Exercise Details](#exercise-details)
  - [ex0 — Hello, Garden!](#ex0--hello-garden)
  - [ex1 — Plot Area Calculator](#ex1--plot-area-calculator)
  - [ex2 — Harvest Total](#ex2--harvest-total)
  - [ex3 — Plant Age Check](#ex3--plant-age-check)
  - [ex4 — Water Reminder](#ex4--water-reminder)
  - [ex5 — Counting to Harvest (Two Approaches)](#ex5--counting-to-harvest-two-approaches)
  - [ex6 — Garden Summary](#ex6--garden-summary)
  - [ex7 — Seed Inventory](#ex7--seed-inventory)
- [How to Run](#how-to-run)
- [Concepts Reference](#concepts-reference)

---

## Project Overview

| Exercise | File(s) | Core Concept |
|----------|---------|-------------|
| ex0 | `ft_hello_garden.py` | Defining and calling a function |
| ex1 | `ft_plot_area.py` | User input, type conversion, arithmetic |
| ex2 | `ft_harvest_total.py` | Multiple inputs, accumulation |
| ex3 | `ft_plant_age.py` | Conditional logic (`if/else`) |
| ex4 | `ft_water_reminder.py` | Practical conditionals for decision-making |
| ex5 | `ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py` | Iteration vs. recursion |
| ex6 | `ft_garden_summary.py` | Combining inputs, variables, and formatted output |
| ex7 | `ft_seed_inventory.py` | Function parameters, type hints, multi-branch conditionals |

---

## Learning Progression

```
ex0  →  Write your first function
ex1  →  Read user input and compute a result
ex2  →  Combine multiple inputs into a total
ex3  →  Make a decision with if/else
ex4  →  Apply conditionals to a real scenario
ex5  →  Count with loops — then do it again with recursion
ex6  →  Put input, logic, and output together
ex7  →  Use typed function parameters and multiple conditions
```

---

## Exercise Details

---

### ex0 — Hello, Garden!

**File:** `ex0/ft_hello_garden.py`  
**Concept:** Defining a function, calling `print()`

The simplest possible exercise: define a named function and have it print a message. This establishes the `def` keyword, the relationship between a function definition and a function call, and the use of `print()`.

**What the code does:**
- Defines a function called `ft_hello_garden()`
- Prints a greeting to the garden community when called

**Code:**
```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

**Expected output:**
```
Hello, Garden Community!
```

---

### ex1 — Plot Area Calculator

**File:** `ex1/ft_plot_area.py`  
**Concepts:** `input()`, `int()` type conversion, multiplication

A garden plot's area is length × width. This exercise practices reading two numbers from the user and computing a result.

**What the code does:**
- Prompts the user for the plot's `length` and `width`
- Converts the string input to integers with `int()`
- Calculates `area = length × width`
- Prints the result

**Code:**
```python
def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print("Plot area:", area)
```

**Example interaction:**
```
Enter length: 5
Enter width: 4
Plot area: 20
```

---

### ex2 — Harvest Total

**File:** `ex2/ft_harvest_total.py`  
**Concepts:** Multiple inputs, addition, accumulation

After three days of harvesting, you want to know the total. This exercise practices reading several inputs and summing them.

**What the code does:**
- Asks the user for three daily harvest amounts
- Converts each to an integer
- Adds them together and prints the total

**Code:**
```python
def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print("Total harvest:", total)
```

**Example interaction:**
```
Day 1 harvest: 10
Day 2 harvest: 15
Day 3 harvest: 8
Total harvest: 33
```

---

### ex3 — Plant Age Check

**File:** `ex3/ft_plant_age.py`  
**Concepts:** `if/else` statement, comparison operators, conditional output

Not every plant is ready to harvest at the same time. This exercise uses a simple threshold check to decide what message to display.

**What the code does:**
- Asks the user how many days old the plant is
- If age > 60 days → prints "Plant is ready to harvest!"
- Otherwise → prints "Plant needs more time to grow."

**Code:**
```python
def ft_plant_age():
    days = int(input("Enter plant age in days: "))

    if days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
```

**Example interactions:**
```
Enter plant age in days: 75
Plant is ready to harvest!
```
```
Enter plant age in days: 30
Plant needs more time to grow.
```

---

### ex4 — Water Reminder

**File:** `ex4/ft_water_reminder.py`  
**Concepts:** Practical `if/else`, integer comparison

A real-world application of conditional logic: remind the gardener to water the plants only if it has been more than 2 days.

**What the code does:**
- Asks the user how many days since they last watered their plants
- If days > 2 → prints "Water the plants!"
- Otherwise → prints "Plants are fine"

**Code:**
```python
def ft_water_reminder():
    days = int(input("Days since last watering: "))

    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
```

**Example interactions:**
```
Days since last watering: 3
Water the plants!
```
```
Days since last watering: 1
Plants are fine
```

---

### ex5 — Counting to Harvest (Two Approaches)

**Files:** `ex5/ft_count_harvest_iterative.py` and `ex5/ft_count_harvest_recursive.py`  
**Concepts:** `for` loops, recursion, helper functions, base cases

This is the most conceptually rich exercise in the project. The same problem — count from Day 1 to Day N, then announce harvest time — is solved in two fundamentally different ways.

#### Iterative approach (`ft_count_harvest_iterative.py`)

Uses a `for` loop with `range()` to count up from 1 to N.

```python
def ft_count_harvest_iterative():
    n = int(input("Days until harvest: "))

    for i in range(1, n + 1):
        print("Day", i)

    print("Harvest time!")
```

#### Recursive approach (`ft_count_harvest_recursive.py`)

Uses a nested helper function that calls itself. The base case (`day > n`) stops the recursion.

```python
def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(day, n):
        if day > n:
            print("Harvest time!")
            return
        print("Day", day)
        helper(day + 1, n)

    helper(1, n)
```

**Expected output (for `n = 3`):**
```
Days until harvest: 3
Day 1
Day 2
Day 3
Harvest time!
```

Both functions produce identical output — the difference is purely in *how* they achieve it.

---

### ex6 — Garden Summary

**File:** `ex6/ft_garden_summary.py`  
**Concepts:** String input, combining multiple pieces of data, formatted output

This exercise practices bringing together user-supplied text information into a meaningful summary — a skill used constantly in real applications.

**What the code does:**
- Asks for the garden's name (kept as a string)
- Asks for the number of plants (also kept as a string, not converted)
- Prints a three-line summary: name, plant count, and a fixed status message

**Code:**
```python
def ft_garden_summary():
    name = input("Enter garden name: ")
    number = input("Enter number of plants: ")
    print("Garden:", name)
    print("Plants:", number)
    print("Status: Growing well!")
```

**Example interaction:**
```
Enter garden name: Sunset Garden
Enter number of plants: 12
Garden: Sunset Garden
Plants: 12
Status: Growing well!
```

---

### ex7 — Seed Inventory

**File:** `ex7/ft_seed_inventory.py`  
**Concepts:** Function parameters, type hints (`str`, `int`, `-> None`), `str.capitalize()`, multi-branch `if/elif/else`

The final exercise steps up the function design: instead of reading input inside the function, data is passed in as **parameters**. Type hints are used to document the expected types, and a multi-branch conditional produces different output based on the unit type.

**What the code does:**
- Accepts three parameters: `seed_type` (str), `quantity` (int), and `unit` (str)
- Capitalizes `seed_type` for consistent output formatting
- Prints a different message depending on whether `unit` is `"packets"`, `"grams"`, or `"area"`
- Prints `"Unknown unit type"` for any unrecognized unit

**Code:**
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
```

**Example calls and output:**
```python
ft_seed_inventory("tomato", 5, "packets")
# → Tomato seeds: 5 packets available

ft_seed_inventory("basil", 200, "grams")
# → Basil seeds: 200 grams total

ft_seed_inventory("grass", 50, "area")
# → Grass seeds: covers 50 square meters

ft_seed_inventory("rose", 10, "bottles")
# → Unknown unit type
```

---

## How to Run

Each exercise is a standalone Python 3 file. Run any of them directly:

```bash
python3 "Growing Code/ex0/ft_hello_garden.py"
python3 "Growing Code/ex1/ft_plot_area.py"
python3 "Growing Code/ex2/ft_harvest_total.py"
python3 "Growing Code/ex3/ft_plant_age.py"
python3 "Growing Code/ex4/ft_water_reminder.py"
python3 "Growing Code/ex5/ft_count_harvest_iterative.py"
python3 "Growing Code/ex5/ft_count_harvest_recursive.py"
python3 "Growing Code/ex6/ft_garden_summary.py"
python3 "Growing Code/ex7/ft_seed_inventory.py"
```

> **Note:** Exercises ex0 through ex6 define a function but do not call it automatically. To run them interactively, open a Python shell and call the function manually, for example:
> ```python
> from ft_hello_garden import ft_hello_garden
> ft_hello_garden()
> ```

---

## Concepts Reference

| Concept | First Introduced | Description |
|---------|-----------------|-------------|
| `def` | ex0 | Defines a named, reusable block of code |
| `print()` | ex0 | Outputs text to the console |
| `input()` | ex1 | Reads a line of text from the user |
| `int()` | ex1 | Converts a string to an integer |
| Arithmetic operators (`+`, `*`) | ex1–ex2 | Perform calculations on numeric values |
| `if/else` | ex3 | Executes different code depending on a condition |
| Comparison operators (`>`, `==`) | ex3–ex4 | Compare values to produce a boolean result |
| `for` loop / `range()` | ex5 | Repeats a block of code a set number of times |
| Recursion | ex5 | A function that calls itself to solve a smaller version of the same problem |
| Base case | ex5 | The condition that stops a recursive function |
| Helper function | ex5 | A nested function that does the recursive work |
| String formatting | ex6 | Combining strings and variables in output |
| Function parameters | ex7 | Named inputs passed into a function at call time |
| Type hints | ex7 | Annotations that document expected parameter and return types |
| `str.capitalize()` | ex7 | Returns a copy of the string with the first letter uppercased |
| `if/elif/else` | ex7 | Multi-branch conditional for three or more outcomes |
