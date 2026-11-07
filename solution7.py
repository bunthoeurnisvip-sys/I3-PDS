def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

def is_palindrome(n):
    return n == reverse_number(n)

test_nums =(2026, 12321, 9875)
for num in test_nums:
    print(f"Number: {num} Digit Sum: {digit_sum(num)}, Reversed Number: {reverse_number(num)}, Is Palindrome: {is_palindrome(num)}")

palindrome_count = 0
for i in range(10, 999):
    if is_palindrome(i):
        palindrome_count += 1
print(f"Total palindromic numbers between 10 and 999: {palindrome_count}")