num = int(input())
def reverse(num, rev = 0):
    if not num:
        return rev
    return reverse(num//10, rev * 10 + num % 10)
def is_palindrome(num):
    if reverse(num) == num:
        return True
    return False
print(is_palindrome(num))