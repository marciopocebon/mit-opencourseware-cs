"""
  OVERVIEW
  This lecture finishes the discussion of dictionaries, then introduces inductive reasoning and recursion. Examples include generating the Fibonacci sequence and solving the Towers of Hanoi problem.
"""

"""
Check yourself:
- what is recursion?
- what is a recursive case?
- what is a base case?
"""

""" 
 Problem sets
 - successive approximaition and a wordgame
"""

""" 
ANNOTATIONS
  
  modular abstraction
    - isolate an procedure in one place

  divide and conquer
    .definition
      - take a hard problem, and break it up into simpler pieces
    .benefits
      - small problems are easier to solve
      - solutions to small problems can easily be combined to solve the original problem

  recursion (an implementation of the divide and conquer technique)
    .definition
      - a way of describing problems
      - a way of designing solutions
    .base case
      - describe the simplest version of the problem
      - direct anwer
    .inductive case
    - reduce to a simpler version of the same problems
    - other simpler operations

    example:
    x^n = x*x*x...x
    x^n = n = 0 -> x = 1 (base case)
    x^n = x*(n-1) (base case)
"""

def simpleExp(x, n):
  # base case 
  if n == 0:
    return 1
  else:
    # smaller version of the same problem
    return x * simpleExp(x, n-1)

""" 
  Palindrome
  .definition
  - is a word, phrase, number, or other sequence of symbols or elements, whose meaning may be interpreted the same way in either forward or reverse direction

  base case:
  - if both the first and the last word are equal, then it is a palindrome

 """

def isPalindrome(setence):
  if len(setence) <= 1:
    return True
  else:
    return setence[0] == setence[-1] and isPalindrome(setence[1:-1])

def normalizeSetence(setence):
  return setence.replace(" ", "").lower()

setences = [
"Amor, Roma",
"A Santa dog lived as a devil God at NASA",
"Animal loots foliated detail of stool lamina",
"No, I'm not"
]

for setence in setences:
  print "is %s a palindrome?" % setence,
  setence = normalizeSetence(setence)
  print isPalindrome(setence)

""" 
!!! Break problems into simpler versions of the same problem
"""

""" FIBONACCI """

def fib(x):
  if x <= 1:
    return 1
  else:
    return fib(x-2) + fib(x-1)

print fib(0)