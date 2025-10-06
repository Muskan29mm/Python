# Python Program to insert the new item ate beginning

dict_1 = {'a':'1', 'b':'2', 'c':'3'}
item_to_be_inserted = ('d','4')

# Convert dictionary items to a list
items_list = list(dict_1.items())

item_to_be_inserted_list = [item_to_be_inserted]


both = item_to_be_inserted_list + items_list

resultant_dict = dict(both)

print("Resultant dictionary is:"+str(resultant_dict))

