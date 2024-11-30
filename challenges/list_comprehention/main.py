
# 1. Simple Transformation

squares = [x**2 for x in range(10)]

print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. Filtering Items
evens = [x for x in range(10) if x % 2 == 0]

print(evens)
# Output: [0, 2, 4, 6, 8]

# 3. Transformation with Filtering
even_squares = [x**2 for x in range(10) if x % 2 == 0]

print(even_squares)
# Output: [0, 4, 16, 36, 64]

# 4. Nested Loops
combinations = [(x, y) for x in range(3) for y in range(3)]

print(combinations)
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

