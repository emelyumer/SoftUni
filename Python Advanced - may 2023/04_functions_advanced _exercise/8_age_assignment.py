def age_assignment(*names, **ages):
    match = {}
    for letter, age in ages.items():
        for name in names:
            if name.startswith(letter):
                match[name] = age
    sorted_matches = dict(sorted(match.items(), key=lambda item: item[0]))
    return '\n'.join([f"{person_name} is {person_age} years old." for person_name, person_age in sorted_matches.items()])


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))