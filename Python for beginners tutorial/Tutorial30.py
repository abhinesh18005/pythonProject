# Recursions: Recursive Vs Iterative Approach


#QUIZ : Calculate fibbonacci secquence

# 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input("Enter the number :-"))
print("The fibonacci of the number is :-", fibonacci(number))



