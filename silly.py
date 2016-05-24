from z3 import *

s = Solver()
cherry = Int('cherry')
cherries = Int('cherries')
grape = Int('grape')
banana = Int('banana')
s.add( (grape + grape + grape) == 30)
s.add( (grape + banana + banana) == 18)
s.add( (banana - cherries) == 2)
if( s.check() == unsat):
	print 'FAIL'
else:
	print s.model()
