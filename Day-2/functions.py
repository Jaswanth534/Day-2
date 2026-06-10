#functions - functions is a block of code which only runs when it is called.
#def - it is used to define a function.

def greet(): 
    print('Hello, wlcm to python')

greet() # calling the function

def welcome(name):
    print(f"welcome {name}")

welcome('John')
welcome('Bob')
welcome('Alice')

#multiple parameters
def men(name, age):
    print(f" Hello {name}, you are {age} years old.")
men('John', 24)


# functions should usually return values

def add(a, b):
    print(a + b)
result = add(10, 20)
print(result)

# reusable code - functions allow us to reuse code without having to write it again and again.

# without functions
price = 1000
gst = price * 18 / 100
total = price + gst
print(total)
 
m_price = 1000
c_gst = m_price * 18 / 100
total = m_price + c_gst
print(total)                  # without functions we have to write again and again for diff prices.

# with functions
def calculate_gst(price):
    gst = price * 18 /100
    total = price + gst

    return total
print(calculate_gst(1000))
print(calculate_gst(2000))   # with functions one logic use many time for diff prices.

# A good function should:
 # 1. do one specific task/job
 # 2. acceinput through parameters
 # 3. return output with return statement
 # 4. Be reusabl3 anywhere in the program.

 