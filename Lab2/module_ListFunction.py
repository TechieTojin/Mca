def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def calculate_sum(lst):
    return sum(lst)

def calculate_average(lst):
    return sum(lst) / len(lst) if lst else 0

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
