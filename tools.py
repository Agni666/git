def check(L):
	if (type(L)==list or type(L)==tupple):
		for i in L:
			if type(i)!=int:
				return False
		return True
	return False
print check([1,2,3])
