# Daily Log

# ✅ Day 1-6 - String Logic + Tuple/Set/Counter Recap

## 🧠 Topics Covered
- Tuple vs List
- Set basics (uniqueness, no order)
- Using `collections.Counter` for frequency count
- String reversal and word manipulation
- Real-world logic: building sentence logic with string functions

## ✅ Challenges Solved
- Reverse word order in a sentence
- Reverse only words starting with vowels
- Count unique and most-visited cities
- Daily sales repetition finder with Counter

## 📌 Notes
- Tuples are immutable; lists are mutable.
- Use sets when uniqueness matters.
- Counter is a fast and Pythonic way to count frequencies.
- For string manipulation, always break into list → manipulate → join back.

## 📍 Next Topic
- String indexing, slicing tricks
- Hidden logic inside string methods
- Pattern-based string puzzles

---

# ✅ Day 7 Topics Covered:
- String slicing deep dive
- Reversing logic
- Extracting structured data from logs
- Solved challenge: Extracted Date, Time, Message from a log line

# 🧠 Skills Practiced:
- Indexing and slicing strings
- Using split(), join(), reversed()
- Parsing and reconstructing string info
- Practicing real-world logging patterns

---


# ✅ Day 8 Topics Covered:
Python Dictionaries: Deep Practice

.get() method and default values

Nested Dictionary Access and Updates

Iterating over .items() and .values()

Dictionary Comprehensions

🔍 Challenges Solved:
Safely retrieving non-existing keys using .get()

Accessing and modifying nested values (skills, projects)

Iterating employee dictionary to filter based on salary

Building dictionary with even numbers and their squares

🧠 What I Learned:
Difference between direct key access vs .get()

How to loop through nested dictionaries efficiently

When and how to use dictionary comprehensions

Clean coding practices with real-world data models


# ✅ Day 9 Topics Covered:
- Dictionary Comprehension ✅
- Nested Dictionary Iteration ✅

**Challenges Solved:**
- 📦 Inventory stock filter:
  ```python
  inventory = {
      "pen": 10,
      "pencil": 0,
      "notebook": 5,
      "eraser": 0
  }
  in_stock = {item: f"In Stock ({c})" for item, c in inventory.items() if c > 0}
🎓 Increase student marks by +5:

python
Copy
Edit
grades = {
    "Alice": {"Math": 88, "Science": 76, "English": 92},
    "Bob": {"Math": 67, "Science": 90, "English": 78},
    "Charlie": {"Math": 95, "Science": 85, "English": 87}
}
new_grades = {
    name: {sub: m + 5 for sub, m in s.items()}
    for name, s in grades.items()
}
What I Learned:

How to iterate and modify nested dictionaries using comprehension.

Real-world use cases like inventory filtering and report card updates.

Importance of clean variable naming for better readability.


# ✅ Day 10 Topics Covered:

.get() method (safe key access)

dict.items() and iteration

Dictionary Comprehension (basic and nested)

Conditional logic inside comprehension

Real-world-style dictionary transformation

Challenges Solved:

Extracting high-rated items from product reviews

Mapping employee names to salary categories using nested dictionaries
