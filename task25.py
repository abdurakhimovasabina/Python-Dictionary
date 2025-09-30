def group_by_age(people: list[dict[str, int| str]]) -> dict[int, list[str]]:
    group = {}
    for person in people:
        group.setdefault(person['age'], []).append(person['name'])


    return group


people = [
    {
        "name": "ali",
        "age": 12
    },
     {
        "name": "vali",
        "age": 16
    },
     {
        "name": "sami",
        "age": 16
    },
     
]

result = group_by_age(people)
print(result)
