def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:

    groups = {}

    for student in students:
        group = student["group"]
        name = student["name"]
        groups.setdefault(group, []).append(name)
        
    return groups

students = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Karim", "group": "B"}
]
print(group_students(students))