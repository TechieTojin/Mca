def add_element(s, element):
    s.add(element)
    return s

def remove_element(s, element):
    s.discard(element)
    return s

def union_sets(s1, s2):
    return s1 | s2

def intersection_sets(s1, s2):
    return s1 & s2

def difference_sets(s1, s2):
    return s1 - s2

def is_subset(s1, s2):
    return s1 <= s2

def set_length(s):
    length = 0
    for i in s:
        length += 1
    return length

def unique_subsets(s):
    from itertools import combinations
    subs = set()
    for i in range(len(s) + 1):
        for combo in combinations(s, i):
            subs.add(frozenset(combo))
    return subs
