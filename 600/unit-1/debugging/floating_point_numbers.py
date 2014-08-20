""" 
  OVERVIEW
  This lecture starts with a brief explanation of why floating point numbers are only an approximation of the real numbers. Most of the lecture is about a systematic approach to debugging.


  why base 2?
  - because it is easy to build switches in eletronic hardware;
  - it is easy to represent a number as a sequence of 'on' and 'off' bits;

  binary approximation to decimal 0.1
  - 0.00011001100110011001110011... (infinity)

  computer approximation:
  - 0.10000000000000000555111512312343244234324334042343242343240

  print statement in python of the computer approximation (17 digits long):
  - 0.1000000000000001

 """

""" avoid to compare 2 point float numbers or use a approximation approach """

def close(x, y, epsilon = 0.00001):
  return abs(x - y) < epsilon

def floatPointNumberEvidence():
  x = 0.0
  iterations = 100000
  for i in xrange(iterations):
    x += 0.1
  print x # prints 10000.0, because print automatically rounds
  print repr(x)
  print 10.0*x == iterations # is it true? why not?
  if close(10.0*x, iterations):
    print 'Close enough enough'

floatPointNumberEvidence()