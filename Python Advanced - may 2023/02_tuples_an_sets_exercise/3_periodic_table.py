n_lines = int(input())
unique_chemical_elements = set()
for _ in range(n_lines):
    elements = input().split()
    for el in elements:
        unique_chemical_elements.add(el)
print(*unique_chemical_elements, sep="\n")
