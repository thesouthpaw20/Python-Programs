def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))

while not is_palindrome(num):
    reversed_num = reverse_number(num)
    num += reversed_num
    print(f"Reversed: {reversed_num}, Sum: {num}")

print(f"Palindrome: {num}")
