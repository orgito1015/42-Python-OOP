# 🌳 CodeCultivation — Object-Oriented Programming with Python

**CodeCultivation** is a progressive, garden-themed curriculum for learning Object-Oriented Programming (OOP) in Python. Starting from the absolute basics of program structure, each exercise introduces one new concept and builds directly on the last — like a plant growing one layer at a time.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Learning Progression](#learning-progression)
- [Exercise Details](#exercise-details)
  - [ex0 — Planting Your First Seed](#ex0--planting-your-first-seed)
  - [ex1 — Garden Data Organizer](#ex1--garden-data-organizer)
  - [ex2 — Plant Growth Simulator](#ex2--plant-growth-simulator)
  - [ex3 — Plant Factory](#ex3--plant-factory)
  - [ex4 — Garden Security System](#ex4--garden-security-system)
  - [ex5 — Specialized Plant Types](#ex5--specialized-plant-types)
  - [ex6 — Garden Analytics Platform](#ex6--garden-analytics-platform)
- [How to Run](#how-to-run)
- [Concepts Reference](#concepts-reference)

---

## Project Overview

| Exercise | File | Core OOP Concept |
|----------|------|-----------------|
| ex0 | `ft_garden_intro.py` | Program structure, variables, type hints |
| ex1 | `ft_garden_data.py` | Class definition, constructor, instance attributes |
| ex2 | `ft_plant_growth.py` | Instance methods, state modification |
| ex3 | `ft_plant_factory.py` | Object creation patterns, collections |
| ex4 | `ft_garden_security.py` | Encapsulation, private attributes, getters/setters, validation |
| ex5 | `ft_plant_types.py` | Inheritance, `super()`, method overriding, polymorphism |
| ex6 | `ft_garden_analytics.py` | Nested classes, inheritance chains, `@classmethod`, `@staticmethod` |

---

## Learning Progression

```
ex0  →  Understand Python program structure
ex1  →  Create your first class and objects
ex2  →  Give objects behavior with methods
ex3  →  Create and manage many objects at once
ex4  →  Protect your data with encapsulation
ex5  →  Extend classes through inheritance
ex6  →  Master advanced OOP patterns
```

---

## Exercise Details

---

### ex0 — Planting Your First Seed

**File:** `ex0/ft_garden_intro.py`  
**Concepts:** Program structure, variables, type hints, f-strings, `main()` pattern

This exercise establishes the foundation for every program in this series: the `main()` function pattern, annotated variables, and formatted output.

**What the code does:**
- Declares three string variables: `plant_name`, `plant_height`, and `plant_age`
- Prints a formatted welcome banner using f-strings
- Wraps everything inside a `main()` function with a `-> None` return type hint
- Uses the `if __name__ == "__main__":` guard for safe script execution

**Key code excerpt:**
```python
def main() -> None:
    plant_name: str = "Rose"
    plant_height: str = "25cm"
    plant_age: str = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}")
    print(f"Age: {plant_age}")
```

**Expected output:**
```
=== Welcome to My Garden ===
Plant: Rose
Height: 25cm
Age: 30 days
=== End of Program ===
```

---

### ex1 — Garden Data Organizer

**File:** `ex1/ft_garden_data.py`  
**Concepts:** Class definition, `__init__` constructor, instance attributes, object instantiation

This exercise introduces the `class` keyword and demonstrates why grouping related data into an object is more powerful than using separate variables.

**What the code does:**
- Defines a `Plant` class with a constructor that accepts `name`, `height`, and `age`
- Stores each value as a typed instance attribute (`self.name`, `self.height`, `self.age`)
- Creates three distinct plant objects: `Rose`, `Sunflower`, and `Cactus`
- Displays each plant's data by accessing its attributes directly

**Key code excerpt:**
```python
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

rose = Plant("Rose", 25, 30)
print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
```

**Expected output:**
```
=== Garden Plant Registry ===
Rose: 25cm, 30 days old
Sunflower: 80cm, 45 days old
Cactus: 15cm, 120 days old
```

---

### ex2 — Plant Growth Simulator

**File:** `ex2/ft_plant_growth.py`  
**Concepts:** Instance methods, state modification, object behavior over time

Objects aren't just data containers — they can also perform actions. This exercise adds methods to the `Plant` class to simulate real-world behavior.

**What the code does:**
- Extends the `Plant` class with three methods:
  - `grow()` — increments `self.height` by 1 cm
  - `age_plant()` — increments `self.age` by 1 day
  - `get_info()` — returns a formatted summary string
- Uses a `for` loop to simulate 7 consecutive days of growth
- Tracks and reports the total height gained

**Key code excerpt:**
```python
def grow(self) -> None:
    self.height += 1

def age_plant(self) -> None:
    self.age += 1

def get_info(self) -> str:
    return f"{self.name}: {self.height}cm, {self.age} days old"
```

**Expected output:**
```
=== Day 1 ===
Rose: 25cm, 30 days old
=== Day 7 ===
Rose: 32cm, 37 days old
Growth this week: +7cm
```

---

### ex3 — Plant Factory

**File:** `ex3/ft_plant_factory.py`  
**Concepts:** Batch object creation, lists, iteration over objects

In real programs you often need to manage dozens or hundreds of objects at once. This exercise demonstrates how to create a collection of objects and iterate over them efficiently.

**What the code does:**
- Creates a list of 5 `Plant` objects in a single concise block
- Iterates over the list with a `for` loop to print each plant's info
- Reports the total count using `len()`

**Key code excerpt:**
```python
plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]

for plant in plants:
    print(f"Created: {plant.get_info()}")

print(f"Total plants created: {len(plants)}")
```

**Expected output:**
```
=== Plant Factory Output ===
Created: Rose (25cm, 30 days)
Created: Oak (200cm, 365 days)
Created: Cactus (5cm, 90 days)
Created: Sunflower (80cm, 45 days)
Created: Fern (15cm, 120 days)
Total plants created: 5
```

---

### ex4 — Garden Security System

**File:** `ex4/ft_garden_security.py`  
**Concepts:** Encapsulation, private attributes (name mangling), getters, setters, input validation

Encapsulation is one of the four pillars of OOP. This exercise shows how to protect an object's internal state from being set to invalid values.

**What the code does:**
- Introduces the `SecurePlant` class with **private attributes** using double underscore name mangling: `__name`, `__height`, `__age`
- Provides **getter methods** (`get_name()`, `get_height()`, `get_age()`, `get_info()`) for safe read access
- Provides **setter methods** (`set_height()`, `set_age()`) that **validate** the input before updating state — negative values are rejected with a descriptive message
- Demonstrates a failed validation attempt to show the protection in action

**Key code excerpt:**
```python
class SecurePlant:
    def __init__(self, name: str):
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
```

**Expected output:**
```
=== Garden Security System ===
Plant created: Rose
Height updated: 25cm [OK]
Age updated: 30 days [OK]
Invalid operation attempted: height -5cm [REJECTED]
Security: Negative height rejected
Current plant: Rose (25cm, 30 days)
```

---

### ex5 — Specialized Plant Types

**File:** `ex5/ft_plant_types.py`  
**Concepts:** Inheritance, `super().__init__()`, method overriding, polymorphism, specialized behaviors

Inheritance lets you create specialized versions of a class without rewriting shared logic. This exercise builds a small class hierarchy of plant types.

**What the code does:**
- Defines a base `Plant` class with shared attributes (`name`, `height`, `age`) and a `get_basic_info()` method
- Creates three subclasses, each adding unique attributes and behaviors:
  - **`Flower`** — adds `color` attribute and a `bloom()` method; overrides `get_info()`
  - **`Tree`** — adds `trunk_diameter` attribute and a `produce_shade()` method that calculates shade area (`diameter × 1.56`); overrides `get_info()`
  - **`Vegetable`** — adds `harvest_season` and `nutritional_value`; provides `get_nutrition_info()`; overrides `get_info()`
- Uses `super().__init__()` in every subclass to reuse the parent constructor

**Class hierarchy:**
```
Plant
├── Flower       (+ color, bloom())
├── Tree         (+ trunk_diameter, produce_shade())
└── Vegetable    (+ harvest_season, nutritional_value, get_nutrition_info())
```

**Key code excerpt:**
```python
class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"
```

**Expected output (excerpt):**
```
=== Garden Plant Types ===
Rose (Flower): 25cm, 30 days, red color
Rose is blooming beautifully!
Oak (Tree): 500cm, 1825 days, 50cm diameter
Oak provides 78 square meters of shade
Tomato (Vegetable): 80cm, 90 days, summer harvest
Tomato is rich in vitamin C
```

---

### ex6 — Garden Analytics Platform

**File:** `ex6/ft_garden_analytics.py`  
**Concepts:** Nested classes, multi-level inheritance, `@classmethod`, `@staticmethod`, class variables, `isinstance()`

The capstone exercise of this series. It combines everything learned so far and introduces several advanced OOP patterns used in professional Python codebases.

**What the code does:**

**`Plant` hierarchy (3-level inheritance chain):**
```
Plant
└── FloweringPlant    (+ flower_color, is_blooming)
    └── PrizeFlower   (+ prize_points)
```

**`GardenManager` class — the management layer:**
- **Class variable** `total_gardens` tracks how many gardens have been created globally
- **Instance attributes**: `owner` name, a `plants` list, and a nested `GardenStats` instance
- **`add_plant(plant)`** — adds a plant and uses `isinstance()` to detect whether it is a regular plant, flowering plant, or prize flower before updating statistics
- **`grow_all_plants()`** — iterates all plants, calls `grow()` on each, and records the growth in stats
- **`get_garden_score()`** — calculates a total score based on plant heights, with bonus points for `PrizeFlower` objects
- **`display_report()`** — prints a full summary of the garden and its statistics

**Special method types:**
| Method | Type | Purpose |
|--------|------|---------|
| `create_garden_network(owners)` | `@classmethod` | Create multiple `GardenManager` instances at once |
| `is_valid_height(height)` | `@staticmethod` | Utility function to validate a height value (0–10,000 cm) |
| `get_total_gardens()` | `@classmethod` | Return the value of the class variable `total_gardens` |

**`GardenStats` — the nested statistics tracker:**
- Lives inside `GardenManager` as `GardenManager.GardenStats`
- Tracks: total plants added, cumulative growth, and a breakdown by plant type (regular / flowering / prize)
- Provides a `get_summary()` method used by `display_report()`

**Key code excerpt:**
```python
class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        def record_plant_added(self, plant_type: str) -> None:
            self.plants_added += 1
            if plant_type in self.plant_types:
                self.plant_types[plant_type] += 1

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        return [cls(owner) for owner in owners]

    @staticmethod
    def is_valid_height(height: int) -> bool:
        return height >= 0 and height <= 10000
```

**Expected output (excerpt):**
```
=== Garden Management System Demo ===
Added Oak Tree to Alice's garden
Added Rose to Alice's garden
Added Sunflower to Alice's garden
Alice is helping all plants grow...
...
=== Alice's Garden Report ===
Plants in garden:
- Oak Tree: 101cm
- Rose: 26cm, red flowers (blooming)
- Sunflower: 51cm, yellow flowers (blooming), Prize points: 10
Plants added: 3, Total growth: 3cm
...
Garden scores - Alice: 188, Bob: 45
Total gardens managed: 2
```

---

## How to Run

Each exercise is a standalone Python 3 script:

```bash
python3 CodeCultivation/ex0/ft_garden_intro.py
python3 CodeCultivation/ex1/ft_garden_data.py
python3 CodeCultivation/ex2/ft_plant_growth.py
python3 CodeCultivation/ex3/ft_plant_factory.py
python3 CodeCultivation/ex4/ft_garden_security.py
python3 CodeCultivation/ex5/ft_plant_types.py
python3 CodeCultivation/ex6/ft_garden_analytics.py
```

---

## Concepts Reference

| Concept | First Introduced | Description |
|---------|-----------------|-------------|
| `class` keyword | ex1 | Defines a blueprint for objects |
| `__init__` | ex1 | Constructor called when an object is created |
| Instance attributes (`self.x`) | ex1 | Data stored on each individual object |
| Instance methods | ex2 | Functions that operate on `self` |
| State modification | ex2 | Methods that change attribute values |
| Private attributes (`__x`) | ex4 | Name-mangled attributes hidden from external access |
| Getters & setters | ex4 | Methods that provide controlled read/write access |
| Encapsulation | ex4 | Bundling data + validation inside a class |
| `super().__init__()` | ex5 | Calling the parent class constructor |
| Inheritance | ex5 | Creating a specialized class from a base class |
| Method overriding | ex5 | Redefining a parent method in a subclass |
| Polymorphism | ex5 | Different classes sharing the same method interface |
| `isinstance()` | ex6 | Checking an object's type at runtime |
| Class variables | ex6 | Attributes shared by all instances of a class |
| Nested classes | ex6 | A class defined inside another class |
| `@classmethod` | ex6 | Method bound to the class, not an instance |
| `@staticmethod` | ex6 | Utility method with no reference to class or instance |
| Inheritance chains | ex6 | Multi-level inheritance (grandparent → parent → child) |
