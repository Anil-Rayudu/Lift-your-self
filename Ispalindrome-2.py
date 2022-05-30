def ispalindrome(a):
    c=list(a.lower())
    if c[:] == c[::-1]:
        return f"{a} is a palindrome"
    else:
        return f"{a} is not a palindrome"
    
print (ispalindrome(input()))