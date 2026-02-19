# prime number
'''num = int(input("Enter the number: "))
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")'''


# prime number upto 100
'''for num in range(2, 101):
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            break
    else:
1        print(num, end=" ")'''

# Palindrone number
'''num = input("Enter number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

# Palindrone String
'''str = input("Enter string: ")
if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''


#List duplicate removing
'''lst = [1,2,2,3,4,4,5]
new_lst = list(set(lst))
print(new_lst)'''

# guess number
'''number = 5   
guess = int(input("Guess number: "))

if guess == number:
    print("Correct")
else:
    print("Wrong")'''

# Flattering list
'''lst = [[1,2],[3,4],[5]]
flat = []

for i in range(len(lst)):
    for j in range(len(lst[i])):
        flat.append(lst[i][j])

print(flat)'''


# fibonacci series


