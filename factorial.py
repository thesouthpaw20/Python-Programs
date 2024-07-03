factorial_dict = {}

def factorial(n):
    if n in factorial_dict:
        return factorial_dict[n]
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    factorial_dict[n] = result
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num}:", factorial(num))
print("Factorials stored:", factorial_dict)
