x='ABC12321CBA579ABA975'

def longest_palandrom(string):
	longest_length = 0
	test = []
	for i, item in enumerate(x):
		do_break = False
		if len(test) >= 2:
			do_break = test[-2] == item
		if do_break:
			test2 = [test[-1]]
			for j in range(i, len(string)):
				if test[::-1][:len(test2)] == test2:
					if len(test2) > longest_length:
						longest_length = len(test2)
				else:
					test = []
					break
				test2.append(string[j])
		test.append(item)
	return longest_length*2-1

print(longest_palandrom(x))