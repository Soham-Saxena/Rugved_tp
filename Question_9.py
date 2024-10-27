string = input("Enter string: ")
n = int(input("Enter number to shift characters by: "))
n_string = ''

for i in string:
    if i.isupper():
        asci = ord(i)
        shifted = asci + n
        if ((shifted) > 90):
            asci = 64 + (shifted - (shifted//90)*90)
            n_string += chr(asci)
        else:
            n_string += chr(shifted)
    elif i.islower():
        asci = ord(i)
        shifted = asci + n
        if ((shifted) > 122):
            asci = 94 + (shifted - (shifted//122)*122)
            n_string += chr(asci)
        else:
            n_string += chr(shifted)
    else:
        n_string += i
print(f"string after encryption: {n_string}")