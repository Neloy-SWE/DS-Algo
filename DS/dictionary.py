# https://www.tutorialspoint.com/python_data_structure/python_dictionary_data_structure.htm

'''
dictionary r key unique ar type same hote hobe.
value duplicate hote pare.
{} er vetor key value nite hoi ar : dara key value separate kora thake.
'''

dict1 = {} # empty dictionary
dict2 = {"Name": "Neloy", "Age": 19}
dict3 = {"Name": "Neel", "Age": 18, "Class": 7}
print(dict1,dict2)
print(f"dict2:\nName: {dict2['Name']}\nAge: {dict2['Age']}")
print(f"dict3:\nName: {dict3['Name']}\nAge: {dict3['Age']}\nClass: {dict3['Class']}")

dict3["Age"] = 23
print(f"after update dict3:\nName: {dict3['Name']}\nAge: {dict3['Age']}\nClass: {dict3['Class']}")

dict4 = {1: "Hello", 2: "World"}
print(dict4)

dict4.clear()
print(f"after clear dict4, dict4 is: {dict4}")

del dict4 # delete entire dictionary

del dict2["Age"]

# print(f"delete one entry: age from dict2: {dict2['Age']}") error dibe
print(f"delete one entry: age from dict2: {dict2}")