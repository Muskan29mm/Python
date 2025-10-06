# Python program to merge two dictionaries

def Merge(dict1, dict2):
    return(dict2.update(dict1))

dict1 = {
    "a": 10,
    "b": 20
}
dict2 = {
    "c": 30,
    "d": 40
}
Final_dict = (Merge(dict1, dict2))
print(dict2)

