string = input("Enter string: ")
n = int(input("Enter number of characters in substrings: "))
if len(string) % n != 0:
    print("string not divideable into equal substrings.")
    exit(0)
List = []
for i in range(0 , len(string), n):
    List.append(string[i: i+n])


for substring in List:
    if substring != List[0]:
        print("Substrings are not equal")
        exit(1)

for substring in List:
    print(substring, end = ' ')