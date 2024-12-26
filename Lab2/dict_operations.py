# (a) Function to merge multiple dictionaries
def merging_Dict(*args):
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

# (b) Function to find common keys in multiple dictionaries
def common_keys(*args):
    if not args:
        return set()
    common_keys = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys &= set(dictionary.keys())
    return common_keys

# (c) Function to invert a dictionary, swapping keys and values
def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
        else:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
    return inverted_dict


# Demonstrating the functions with examples
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'b': 2, 'c': 3, 'e': 6}

# (a) Merging dictionaries
merged = merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# (b) Finding common keys
common_keys_result = common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)

# (c) Inverting a dictionary
inverted = invert_dict(dict1)
print("Inverted Dictionary:", inverted)

