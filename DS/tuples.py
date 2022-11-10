# https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm

'''
tuple holo immutable.
tuple ke list er moto update ba delete kora jai na.
jokhon constant values niye kaj korbo tokhon tuple use korbo. karon tuple holo list er theke besi fast
'''
# erokom vabe tuple declare initialize kora jai.
tup1 = (50) # ekhane tup1 just ekta integer. eke tuple hisabe define korte hole 50 er por ekta koma dite hobe
tup2 = (1,2,"Hello")
tup3 = 1,2,3,4,5,6
tup4 = () # empty
tup5 = (50,)
tup6 = tup5+tup2 

tup7 = 30, # bracket chhara o define kora jai. koma dilei tuple hoye jabe.
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(f"slice: {tup3[1:4]}")
print(f"specific element print: {tup2[2]}")
print(tup6)
print(type(tup7))

print("Print tuple according to it's index:")
for i in range(len(tup3)):
    print(tup3[i])