#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Armstrong number

while True:
    number = input("enter a positive number :")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "It is an invalid entry. Don't         use non-numeric, float, or negative values!")
    elif int(number) >= 0:
        for i in range(digits):
            summ += int(number[i]) ** digits
        if summ == int(number):
            print(number, "is an Armstrong number.")
            break
        else:
            print(number, "is not an Armstrong number.")
            break


# In[ ]:


# Prime number

n = int(input("enter a number to check if it is a prime or not:"))

count = 0

for i in range(1, n+1) :
    if not (n % i) : count += 1

if (n == 0) or (n == 1) or (count >=3) : print(n, "is not a prime number.")
else : print(n, "is a prime number")


# In[ ]:





# In[ ]:




