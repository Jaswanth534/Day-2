# if else - if condition is true then do something otherwise do something else.

marks = 85

if marks >= 90:
    print('Grade A')
else:
    print('Grade B')   

# 
age  = 18

if age >= 18:
    print('you are eligible to vote')
elif age >= 20:
    print('You are an adult ')
else:
    print('you are not eligible to vote')


password = 'python1234'
if password == 'python123':
    print('Login successful')
else:
    print('Wrong password')    
    
#multiple conditions

age = 23
salary = 20000

if age >= 18 and salary >= 18000:
    print('you are eligible for loan')

#multilple conditions with or

is_student = False
is_employee = True

if is_student or is_employee:
    print('Access Granted')

# using functions with if else

def check_voting(age):
    if age >= 18:
        return 'Eligible'
    else:
        return 'Not eligible'
result = check_voting(20)
print(result)

# Data Analyst example

def sales_target(sales):
    if sales >= 100000:
        return 'Achieved'
    else:
        return 'Not Achievd'
amount = sales_target(90000)
print(amount)

# AI/ML example

def classify_temp(temp):
    if temp >= 30:
        return 'Hot'
    else:
        return 'Normal'
temperature = classify_temp(35)
print(temperature)