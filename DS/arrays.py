# array fixed length

# https://www.tutorialspoint.com/python_data_structure/python_arrays.htm

from array import *
# from array import array


a1 = array('i', [1, 2, 6, 2, 7, 8])
print(f"element of a1 at index 4 is: {a1[4]}\n")

print("all element of a1")
for i in a1:
    print(i)

print("\nelement insert:")

a1.insert(5, 11)
for i in a1:
    print(i)

"""
ekhane a1 er last index holo 5. tobe jodi ami 5 er kom kono index e insert kortam tahole sei element majhe
giye bosto ar nicher element gula ek ghor niche neme jeto. jodi 5 er besi 10 ba 12 jekono index e insert
kortam tahole seta sobar ses e add hoto. index related kono error asto na.
"""

print("\ninsert element at index 10 which is not declared")
a1.insert(10, 13)
for i in a1:
    print(i)


print("\ndelete element")
a1.remove(2)
for i in a1:
    print(i)

print("\nremove element according to index")
a1.pop(1)
for i in a1:
    print(i)

"""
remove method first element remove kore. multiple value thakle porer gula theke jai. ar pop method index
onusare element remove kore
"""

print("\nsearch index of value 8:")
print(a1.index(8))

# ekhane multiple value thakle suru te jeta pabe setar index print korbe

print("\nupdate 8 to 5")
a1[4]=5
for i in a1:
    print(i)