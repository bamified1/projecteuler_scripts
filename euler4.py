#  Create a palindrome from the product of two 3--digit numbers


def palindrome(a, b):
    s = str(a*b)
    new_s = ""
    middle = s[(len(s) - 1)//2:(len(s)+2)//2]
    for i in range(len(s)):
        if i != middle:
            new_s = new_s + s[i]
    return new_s


print(palindrome(101, 223))
