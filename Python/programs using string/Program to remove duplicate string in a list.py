# Python program to remove duplicate string in a list

my_list = ['Apple','Banana','Cherry','Orange','Apple','Cherry']

unique_list = list(set(my_list))     # convert to set becuase set automatically remove duplicate and after removal convert back to list

print("List after removing duplicates:", unique_list)
