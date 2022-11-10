# https://www.tutorialspoint.com/python_data_structure/python_2darray.htm

a = [[1,2,3], [10, 20, 300], [40, 50, 60, 70]]

# print 2d array
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

print("\naccess a value (3rd value of 2nd element of a):")
print(a[1][2])

print("\ninsert a new value in 1st element of a:")

a[0].insert(3,4)
for i in a:
    for j in i:
        print(j, end=" ")
    print()

print("\nupdate a value of element 2 of a:")
a[1][2]=25
for i in a:
    for j in i:
        print(j, end=" ")
    print()

print("\ndelete last element of a:")
del a[2]
for i in a:
    for j in i:
        print(j, end=" ")
    print()