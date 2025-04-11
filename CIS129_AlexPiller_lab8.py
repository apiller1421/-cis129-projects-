def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Clean string
    stack = list(s)  # Use list as stack
    return s == ''.join(reversed(stack))  # Compare with reversed

print(is_palindrome("Radar"))          # True
print(is_palindrome("Refer"))          # True
print(is_palindrome("Dad"))            # True
print(is_palindrome("Deed"))           # True
print(is_palindrome("School"))         # False
print(is_palindrome("I did, did I?"))  #True
