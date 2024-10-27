string = input("Enter string: ")
n_string = ""

while len(string) != 0:
    min = string[0]
    for i in range(len(string)):
        if string[i] < min:
            min = string[i]
    n_string += min
    string = string.replace(min, "", 1)

print(f"String after re-arranging: {n_string}")
        