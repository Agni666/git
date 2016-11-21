import math
from tools import check

l=[2,3,4]
tym=0.0
if check(l)==True:
	for i in l:
		tym+=i^2
	s=math.sqrt(tym/len(l))
print s
