def array_diff(a: list, b: list) -> list:
    b_set = set(b)
    return [x for x in a if x not in b_set]

def sum_pairs(nums: list, sum: int) -> list: 
    seen = set()
    for x in nums:
        if sum - x in seen:
            return [sum - x, x]
        seen.add(x)
    return None

def remove_duplicate_ids(obj: dict) -> dict:
    sorted_keys = sorted(obj.keys(), key=lambda k: int(k))
    char_owner = {}
    for key in sorted_keys:
        seen_in_array = set()
        for char in obj[key]:
            if char not in seen_in_array:
                char_owner[char] = key
                seen_in_array.add(char)
 
    result = {}
    for key in sorted_keys:
        seen_in_array = set()
        filtered = []
        for char in obj[key]:
            if char not in seen_in_array and char_owner[char] == key:
                filtered.append(char)
                seen_in_array.add(char)
        result[key] = filtered
 
    return result
# В данной функции определите самостоятельно, что она принимает, а что возвращает
def lazy():
    """Решение для Задачи 4"""
    
