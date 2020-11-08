
# EX 2.6
"""
num = int(input("Enter a number between 0 and 1000: "))
last_digit = num % 10
middle_value = (num // 10) % 10
first_digit = num // 100

sum_digits = last_digit + middle_value + first_digit

print("The sum of the digits is : ",sum_digits)

"""

# EX 2.7
# Please uncomment the solution below
"""
minutes = int(input("Enter the number of minutes: "))
num_year = minutes//525600
num_days = (minutes % 525600)//1440

print(minutes,"minutes is approximately", num_year, "years", num_days,"days")
"""

# Ex 2.9
# Please uncomment the solution below
"""
ta = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
v = float(input("Enter the wind speed that is greater than 2 in miles per hour: "))
twc =  35.74 + 0.6215*ta - 35.75*v**0.16 + 0.4275*ta*v**0.16

print("The wind chill index is: ", twc)
"""
# EX. 2.21
# Please uncomment the solution below

saving = float(input("Enter the monthly saving amount: "))
rate = 1+0.00417
comp_interest = saving*(rate + rate**2 + rate**3 + rate**4 + rate**5 + rate**6)
print("After the sixth month, the account value is ",comp_interest)


