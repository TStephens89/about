def is_palindrome(palindrome):
    palindrome = palindrome.lower().replace(' ', '')
    return palindrome == palindrome[::-1]
print(is_palindrome("lol"))