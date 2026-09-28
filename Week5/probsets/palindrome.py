# num = input("Enter a palindrom: ")
# if num[:2]:
#     print("Palindrome")
# else:
#     print("This is not a palindrome")

num = int(input("Enter a palindrome: "))
if num < 0:
    print("Not a Palindrome")
else:
    temp = num
    reverse = 0
    while temp != 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if reverse == num:
        print("Palindrome")
    else:
        print("Not a palindrome")

  
