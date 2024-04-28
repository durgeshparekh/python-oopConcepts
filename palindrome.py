print('Enter your number')
number = int(input())
temp = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if temp == reverse:
    print('Number is Palindrome')
else:
    print('Number is not Palindrome')

