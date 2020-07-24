def fibonacci(n):
	"""
	A very simple fibonacci program to test if the code
	still works after injecting my virus.
	"""
	if n < 0:
		print("There is no negative fibonacci number.")
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(15))