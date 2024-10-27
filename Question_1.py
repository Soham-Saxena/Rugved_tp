def triple_and(a, b, c):
    if a*b*c != 0:
        return 1
    else:
        return 0

a = int(input("Enter 3 numbers (enter after each input):\n"))
b = int(input(""))
c = int(input(""))

print(triple_and(a, b, c))