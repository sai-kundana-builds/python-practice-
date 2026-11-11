#1.Square Function 
def square(n):
    return n*n
result = square(5)
print(result)

# 2.Addition Function 
def addition(a,b):
    return a+b
result = addition(10,20)
print(result)

# 3.Even or Odd Function
def check(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"
result = check(6)
print(result)

# 4.Largest of Two Numbers
def largest(a,b):
    if a>b:
        return a
    else:
        return b
result = largest(88,26)
print(result)

# 5.Multiplication Function 
def multiply(a,b):
    return a*b
result = multiply(58,43)
print(result)

# 6.Average Function
def average(a,b,c):
    return (a+b+c)/3
result = average(60,70,80)
print(result)

# 7.Factorial Function
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
        return result
print(factorial(5))