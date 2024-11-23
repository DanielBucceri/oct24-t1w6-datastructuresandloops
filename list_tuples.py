numbers = [13, 2 , 23, 534]
print(numbers)

print(numbers[-1]) # negative index = starts from 0 still but interats over the other way coming basckwards

numbers.insert(2, 5)
print(numbers)

numbers.append(13)

numbers.pop(2) # removes by index
print(numbers)

numbers.remove(2) #removes by value
print(numbers)

popped_value = numbers.pop(2)
print(numbers)
print(popped_value)

numbers.remove(13)  # if multiple matching values. Only first removed
print(numbers)


numbers.sort(reverse=True)
print(numbers)

print(numbers.count(13))

names = ("Bing","Bong","Harry","Mike")
print(names)
print(type(names[2]))

# tuples same as lists but cant be changed . Faster to run