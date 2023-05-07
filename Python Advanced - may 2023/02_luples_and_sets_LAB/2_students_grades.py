number_of_student = int(input())
all_students_grade = {}
for st in range(number_of_student):
    st_name, grade = input().split()
    if st_name not in all_students_grade:
        all_students_grade[st_name] = []
        all_students_grade[st_name].append(float(grade))
    else:
        all_students_grade[st_name].append(float(grade))
for key, value in all_students_grade.items():
    all_grade = ' '.join(map(lambda v: f'{v:.2f}', value))
    average_grade = sum(value) / len(value)
    print(f"{key} -> {all_grade} (avg: {average_grade:.2f})")

