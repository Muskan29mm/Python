list_1 = [('Nakul', 93), ("Shivansh", 45), ("Samved", 34),
          ('Yash', 88), ("Vidya", 45)]

dict_1 = dict()

for student, score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)

