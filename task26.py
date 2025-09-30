def merge_dicts(a: dict, b: dict) -> dict:
    
    merged = a.copy()
    merged.update(b)
    return merged

a = {"x": 1, "y": 2}
b = {"y": 5, "z": 9}
print(merge_dicts(a, b))