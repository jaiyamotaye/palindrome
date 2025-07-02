word = "madam"
is_palindrome = word == word[::-1]

print("Is Palindrome: ",is_palindrome)



def main():
    print("Welcome to the Description Collector!")
    description = input("Please enter a description of your request: ")

    # Optional: Do something with the description
    print("\nYou entered the following description:")
    print(f"\"{description}\"")

if __name__ == "__main__":
    main()
