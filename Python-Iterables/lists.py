for x in [1, 2, 3, 4]:
    print(x)

for x in [1, 2, 3, 4]:
    print(20 * x)

print([name[0] for name in ["Elie", "Tim", "Matt"]])

print([x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0])

print([x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]])

print([name[::-1].lower() for name in ["Elie", "Tim", "Matt"]])

print([c for c in "first" if c in "third"])

print([n for n in range(1, 101) if n % 12 == 0])

print([c for c in "amazing" if c not in "aeiou"])

print([list(range(3)) for _ in range(3)])

print([list(range(10)) for _ in range(10)])
