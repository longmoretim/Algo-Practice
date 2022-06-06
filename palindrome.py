#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.


def palindrome(num):
    newNum = [int(x) for x in str(num)]
    return (newNum == list(reversed(newNum)))

print(palindrome(1234))
print(palindrome(121))
#palindrome(1234)