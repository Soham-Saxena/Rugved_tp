s = input("Enter string: ")
List = list(s)
List.sort()
s = ''
for character in List:
    s += character
print(s)
index = -2
i = 0
count = 1
for i in range(0, len(s) - 1):
    if (s[i] != s[i+1]):
        print(f"{s[i]} : {count}")
        count = 1
    else:
        count += 1
print(f"{s[len(s)-1]} : {count}")