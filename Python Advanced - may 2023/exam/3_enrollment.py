def gather_credits(credits, *courses):
    my_credits = 0
    my_courses = []
    for course in courses:
        name, credit = course

        if credits <= my_credits:
            break

        if name not in my_courses:
            my_credits += credit
            my_courses.append(name)

    if my_credits >= credits:
        my_courses.sort()
        return f"Enrollment finished! Maximum credits: {my_credits}.\nCourses: {', '.join(my_courses)}"
    return f"You need to enroll in more courses! You have to gather {credits - my_credits} credits more."



print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
