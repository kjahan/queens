def check_rows(A):
	"""
	Check if all rows in 2-dimensional matrix don not have more than one queen
	"""
	for i in range(len(A)):
		# compute sum of row #i
		if sum(A[i]) > 1:
			return False
	return True