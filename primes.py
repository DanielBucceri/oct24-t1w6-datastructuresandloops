#output if a number is prime 
# number is prime iff it is divisable buy 1 and itself only 

# 16 -> 1, 2 , 8 , 4 - > not prime
#17 -> 1, 17 -> Prime

number = 16
while number < 100:
    
    for i in range(2, number):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print('Is prime')
    print(number)
    number += 1