num = input("Enter number to test: ")
if not num.isnumeric():
    print("Number is invalid.")
    exit(0)
switch = 0
for i in range(len(num)-1):
    if switch == 0:
        if num[i] > num[i+1]:
            switch = 1
            continue
    else:
        if num[i] < num[i+1]:
            print("Number is not a hill number")
            exit(0)

print("Number is a hill number")
