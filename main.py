def factorial(n):
    if n < 1:
      return 1
    return n * factorial(n -1) 


if __name__ == '__main__' :
   n = 5
   print('The Factorial of n is ',
factorial (n))