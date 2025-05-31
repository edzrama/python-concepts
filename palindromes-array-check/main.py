def reverse_word(word):
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word

def is_palindrome(word):
    return word == reverse_word(word)

def check_all_palindromes(arr):
    for word in arr:
        if not is_palindrome(word):
            return False
    return True


words = ["anna", "level", "madam","kayak", "deed"]
print(check_all_palindromes(words))  # Output: True

words = ["hello", "world"]
print(check_all_palindromes(words))  # Output: False