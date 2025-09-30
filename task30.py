def filter_non_zero(d: dict[str, int]) -> dict[str, int]:

    result = {}

    for k, v in d.items():
        if v != 0:
            result[k] = v
            
    return result

data = {"a": 0, "b": 5, "c": 0, "d": 7}
print(filter_non_zero(data))