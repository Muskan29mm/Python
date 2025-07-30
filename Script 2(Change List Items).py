# Change List Items

# Change Item value
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "mango"
print(thislist)

# Change a range of item values
thislist1 = ["Pineapple", "banana", "mango", "cherry", "apple", "melon", "grapes"]
thislist1[2:5] = ["pomegranate", "raspberry", "kiwi"]
print(thislist1)

# If you insert or change more items than you defined actually(originally) in list the new items will be inserted where you specified, and the remaining items will move accordingly
thislist3 = ["apple", "banana", "cherry"]
thislist3[1:2] = ["watermelon", "papaya"]
print(thislist3)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist4 = ["apple", "banana", "cherry"]
thislist4[1:3] = ["watermelon"]
print(thislist4)

# Insert() method
thislist5 = ["apple", "mango", "cherry", "banana"]
thislist5.insert(2, "papaya")
print(thislist5)