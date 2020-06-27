'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
'''

def palindrome(num):
    return str(num) == str(num)[::-1]


print(palindrome(121) == True)
print(palindrome(10) == False)