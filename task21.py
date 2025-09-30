def count_names(names: list[str]) -> dict[str, int]:
    unique_names = set()
    for name in names:
        unique_names.add(name)
    result = {}
    for name in unique_names:
        result[name] = names.count(name)

    return result

names = ['ali', 'vali', 'gani', 'sami', 'ali', 'gani', 'gani']
result = count_names(names)
print(result)