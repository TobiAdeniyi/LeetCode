"""Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward."""

class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

    def isPalindromeNoString(self, x):
        if x < 0:
            return False
        xx = []
        xx.append(x % 10)
        while (x >= 10):
            x = floor(x / 10)
            xx.append(x % 10)
        return xx == xx[::-1]