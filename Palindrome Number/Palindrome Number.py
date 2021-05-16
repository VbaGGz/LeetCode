def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

print(isPalindrome(456654))
print(isPalindrome(55))
print(isPalindrome(79))
print(isPalindrome(456456))