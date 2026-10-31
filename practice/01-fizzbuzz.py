# Problem 1: FizzBuzz
# https://pythoncompiler.io/python/50-python-practice-problems/#problem-1
#
# Write fizzbuzz(n) that returns a list of strings for the numbers 1 to n: "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both, and the number itself (as a string) otherwise.
#
# fizzbuzz(5)  ->  ["1", "2", "Fizz", "4", "Buzz"]
#
# Passes all 4 tests (2 of them hidden) on pythoncompiler.io.

def fizzbuzz(n):
    fizz_buzz = []
    for i in range(1,(n+1)):
      if(i%3 == 0 and i%5 == 0 ):
        fizz_buzz.append("FizzBuzz")
      elif(i%5 == 0):
        fizz_buzz.append("Buzz")
      elif(i%3 == 0):
        fizz_buzz.append("Fizz")
      else:
        fizz_buzz.append(str(i))
    return fizz_buzz
