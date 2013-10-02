#http://www.youtube.com/watch?v=S5tD47NZx7w
import os
import sys

#class MyDivision:
#  def NaiveDiv(divident, divisor):
#    quotient = 0
#    while divident >= divisor:
#      divident -= divisor
#      print divident
#      quotient = quotient +1
#      print quotient
#    return quotient

#  def OptDivide(divident, divisor):
#    quotient = 0
#    currentQuotientBase = 1
#    currentDivisor = divisor
#    while divident >= divisor:
#      if divident >= currentDivisor:
#        divident -= currentDivisor
#        quotient += quotient

def NaiveDiv(divident, divisor):
  quotient = 0
  while divident >= divisor:
    divident -= divisor
    print 'divident = ', divident
    quotient = quotient +1
    print 'quotient = ', quotient
  return quotient

def OptDiv(divident, divisor):
  quotient = 0
  currentQuotientBase = 1
  currentDivisor = divisor
  print '\n'
  print 'OptDiv(divident, divisor)'
  print 'curentDivisor = divisor : ', currentDivisor
  while divident >= divisor:
    print '-'*40
    print 'while divident >= divisor:'
    print '-'*40
    print 'divident = ', divident, 'divisor = ', divisor
    if divident >= currentDivisor:
      print '-'*40
      print 'if divident >= currentDivisor:'
      print '-'*40
      divident = divident - currentDivisor
      print 'divident -= divident - currentDivisor : ', divident
      quotient = quotient + currentQuotientBase
      print 'quotient += currentQuotientBase : ', quotient
      currentDivisor = currentDivisor*2
      print 'currentDivisor = *2 : ', currentDivisor
      currentQuotientBase = currentQuotientBase*2
      print 'currentQuotientBase = *2 : ', currentQuotientBase
    else:
      print '-'*40
      print 'else:'
      print '-'*40
      currentDivisor = currentDivisor/2
      #currentDivisor = currentDivisor>>1
      print 'currentDivisor = /2 : ', currentDivisor
      currentQuotientBase = currentQuotientBase/2
      #currentQuotientBase = currentQuotientBase>>1
      print 'currentQuotientBase = /2 : ', currentQuotientBase
  return quotient

def main():
  divident = int(sys.argv[1])
  divisor = int(sys.argv[2])
  print 'input is: ', divident, divisor
  print '-'*40
  print 'Naive result: ', NaiveDiv(divident, divisor) 
  print '-'*40
  print 'Opt result: ', OptDiv(divident, divisor)
  print '-'*40
  #MyDiv = MyDivision()
  #print MyDiv.NaiveDiv(divident,divisor)
  #print 'Naive: 1000/2=', MyDiv.NaiveDiv(1000,2)
  sys.exit(0)
  print 'Opt: 1000/2=', OptDiv(1000,2)

if __name__ == '__main__':
  main()
