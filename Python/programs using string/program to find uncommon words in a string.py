# Python program to find uncommon words in a string
def find_uncommon_words(str1, str2):
    words1 = set(str1.split())    # Convert these lists into sets to facilitate the set operations.
    words2 = set(str2.split())

    uncommon_words = (words1 - words2) | (words2 - words1)   # The union ('|') of these two sets gives the uncommon words.
    return uncommon_words

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

uncommon_words = find_uncommon_words(string1, string2)
print("Uncommon words:", uncommon_words)
