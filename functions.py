# fuinctions - Reusable collection of code that performs a particular task

#declare function
def greet(name, age, country="australia"):
    print(f"Hello {name}! You are {age}? Damn thats old")
    print(f"{name} is from {country}")

#call function
person = "Daniel"
age = 29
greet(person, age) # greet(age=age, name = person) can also do explicit instead o positional like  instead of person placed in name postion.

def even_or_odd(num):
    if num % 2 == 0:
        return 'even'
        
    else:

        return "odd"
        
#when returning value with fucntion you can still print as below
print(even_or_odd(5)) 

even_or_odd(10)
even_or_odd(11123124141341231252345425)