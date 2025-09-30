def group_indices(numbers: list[int]) -> dict[int, list[int]]:

    indices = {}

    for i, num in enumerate(numbers):
        indices.setdefault(num, []).append(i)
        
    return indices

numbers = [1, 2, 1, 3, 2, 1]
print(group_indices(numbers))