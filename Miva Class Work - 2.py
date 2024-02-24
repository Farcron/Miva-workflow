# Sign Factory

# This function check if a word is a palindrome
def is_word_palindrome(word):
    return word == word[::-1]


# The four words in each box
sign_box1 = input("Word in box 1: ")
sign_box2 = input("Word in box 2: ")
sign_box3 = input("Word in box 3: ")
sign_box4 = input("Word in box 4: ")

# Checking if any word in any box is a palindrome
if any(is_word_palindrome(word) for word in [sign_box1, sign_box2, sign_box3, sign_box4]):
    print("Open")  # If at least one palindrome found, open the box

else:
    print("Trash")  # If no palindrome found, discard the entire box

message = "hello"
reversed_word = message[::-1]
print(reversed_word)
