def is_substring(str1, str2):
    return str1 in str2

def count_occurrences(char, string):
    return string.count(char)

def replace_substring(str1, str2, str3):
    return str1.replace(str2, str3)

def to_capital(string):
    return string.upper()

while True:
    print("Select operation:")
    print("1. Check if a string is a substring of another string")
    print("2. Count occurrences of a character")
    print("3. Replace a substring with another substring")
    print("4. Convert to capital letters")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '1':
        str1 = input("Enter the substring: ")
        str2 = input("Enter the main string: ")
        print("Is substring:", is_substring(str1, str2))
    elif choice == '2':
        char = input("Enter the character: ")
        string = input("Enter the string: ")
        print("Occurrences:", count_occurrences(char, string))
    elif choice == '3':
        str1 = input("Enter the main string: ")
        str2 = input("Enter the substring to replace: ")
        str3 = input("Enter the new substring: ")
        print("New string:", replace_substring(str1, str2, str3))
    elif choice == '4':
        string = input("Enter the string: ")
        print("Capital letters:", to_capital(string))
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
