names = ("Bing","Bong","Harry","Mike")

for index, name in enumerate(names):  # Hmmm ?
    print(f'{index+1}. {name}')

    # list all nnumberrs between 10 to 100 and state if they are odd / even 
for num in range(10, 101):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} be odd")


#ternary example of above
for num in range(10, 101):
    print(f'{num} is {'even' if num % 2 == 0 else 'odd'}')
    
    
# for else  = What do at end of for loop  ? 
for i in range (10):
    print(i)
    if i > 5:
        break
else:
    print("loop finito")