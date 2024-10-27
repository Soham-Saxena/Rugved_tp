List = list(map(int,input("Enter number: ")))
for i in range(1, len(List), 2):
    List[i] *= 2
    if List[i]*2 > 9:
        List[i] = (List[i])%10 + (List[i])//10
sum = sum(List)
if sum % 10 == 0:
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")