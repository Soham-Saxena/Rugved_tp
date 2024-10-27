def anagram(string1, string2):
    if list(string1.upper()).sort() == list(string2.upper()).sort():
        return 1
    else:
        return 0
    
string1 = input("Enter first string to check: ")
string2 = input("Enter second string to check: ")

if anagram(string1, string2):
    print("The given strings are anagrams")
else:
    print("The given strings are not anagrams")