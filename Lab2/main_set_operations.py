#set implementing
from set_operations import *
s1={1,3,5,2,5,10,11}
s2={3,6,8,34,61,5}
print(type(s1))
print("To add an element to a set:")
ele=int(input("enter a element to add:"))
print("After adding element:",add_element(s1,ele))

print("To remove an element to a set:")
ele1=int(input("enter a element to remove:"))
print("After removing element:",remove_element(s1,ele1))

print("Union of 2 sets:",union_sets(s1, s2))
print("intersection of 2 sets:",intersection_sets(s1, s2))

print("difference of two sets: ",difference_sets(s1, s2))

print("if set S1 is a subset of set S2:",is_subset(s1, s2))

print("the length of a given set is :",set_length(s1))

print("all unique subsets of a given set:\n",unique_subsets(s1))
