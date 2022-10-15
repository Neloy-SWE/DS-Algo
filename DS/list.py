# https://www.tutorialspoint.com/python_data_structure/python_lists_data_structure.htm

list1 = [1, 2, "Hello", "World", 5.5]
print(f"total list: {list1}")
print(f"value of 0 index: {list1[0]}\n\n")
print(f"value from 2 to 3 {list1[2:4]}\n\n")
print("update list at index 1:")
list1[1]="update"
print(f"updated list: {list1}\n\n")

print("delete element")
del list1[1]
print(f"after delete element 1: {list1}\n\n")
print("add new element")
list1.append(4)
list1.append(5.5)
list1.append(4)
print(list1)
list1.remove(5.5)
print("\n\nremove a element")
print(list1)
print("\n\nusing pop method")
list1.pop(0)
print(list1)
