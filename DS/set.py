# https://www.tutorialspoint.com/python_data_structure/python_sets.htm

# set is a collection of unique elements 
"""
When it is set to random each run Python will generate different hashes 
for the same items. That's why you get different order.
"""


set1 = {"a", "c", "b"}
print(set1)
for i in set1:
    print(i)
print("\nadd new item in set:")
set1.add(1) # set e multiple type element rakha jai. 
print(set1)
print("\nremove an item from set:")
set1.discard("e") # ekhane "e" nai. but error dei ni.
set1.discard("c")
print(set1)

print("\nUnion of sets:")
setA = {"sun", "mon", "sat"}
setB = {"sat", "mon", "wed"}
union = setA | setB
print(union)
print("\nIntersection of sets:")
intersection = setA & setB
print(intersection)

print("\nDifference of sets:")
difference1 = setA - setB
difference2 = setB - setA
print(difference1, difference2)

print("\n check subset & super set:")
subset = difference1 <=union
superSet = union >= difference2
print(subset, superSet)
