def fibonacci(num):
    n = 1
    sum = 0
    count = 0
    while True:
        print(sum, end = " ")
        count += 1
        if count == num:
            break
        sum += n
        print(n, end=" ")
        count += 1
        if count == num:
            break
        n += sum

number = int(input("Enter number of terms in fibonacci series: "))
fibonacci(number)