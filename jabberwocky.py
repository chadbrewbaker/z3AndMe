from z3 import *

s = Solver()
num = Int('num')
s.add( num > 300)
s.add( num % 13 == 7)
s.add( num % 7 == 0)
s.add( num % 5 != 0)
s.add( num % 3 != 0) 
if( s.check() == unsat):
	print 'FAIL'
else:
	print s.model()
