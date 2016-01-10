#File Name: ps1.py
#Author: Chaitra Kothari
#Date: Oct 27th, 2015
#Description: This program computes and prints 1000th prime number


#-------------------PART 1-------------------------------------
#generate a list of positive odd numbers
oddNum = []
primeNum = []
count = 4000
oddNum.append(1)
primeNum.append(2)
primeNum.append(3)
i = 1
while count > 0:
	i += 2
	oddNum.append(i)
	count -= 1
	


#test whether given odd number is prime
for odd in oddNum:
	if all(prime < odd and odd % prime != 0 for prime in primeNum):
		primeNum.append(odd)
print primeNum[:1000]


#-----------------------------PART 2--------------------------------
from math import *

n = 5
result = 0
for prime in primeNum[:n]:
	result += log(prime)
print 'sum of log of', n, 'prime numbers is:', result
print 'ratio of sum of logs to n:', float(result) / n
