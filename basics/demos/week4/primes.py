'''create functions that can find out if number is prime, can find a prime number within a range of value and computer N, used in RSA encryption'''

def isPrime(number):
  for i in range(2,number,1):
    if number % i == 0:
      return False  
  return True   

#print(isPrime(25))

def findPrime(start, end):
  for stuff in range(start, end+1):
    if isPrime(stuff):
      return stuff
#print(findPrime(28, 120))      

def encrypt():
  x = int(input("Provide an integer: "))
  y = int(input("Provide a second integer (larger): "))
  p1 = findPrime(x,y)
  x = int(input("Provide an integer: "))
  y = int(input("Provide a second integer (larger): "))
  p2 = findPrime(x,y)
  return p1*p2

print(encrypt())