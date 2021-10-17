def factorial(n):
  prod = 1
  for i in range(1,n+1):
    prod = prod*i
  return prod


if __name__=='__main__':
   print(f"factorial of 5 = {factorial(5)}")
