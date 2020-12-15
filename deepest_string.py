## Test problem with example inputs at bottom

def deepest_string(input):
	level = 0
	deepest_level = 0
	output = []
	sub_string = ''
	for item in input:
		if item == "(":
			sub_string = ''
			level += 1
			if deepest_level < level:
				deepest_level += 1
				output = []
		elif item == ")":
			if deepest_level == level:
				output.append(sub_string)
			level -= 1
		else:
			if deepest_level == level:
				substring += item
	if deepest_level = 0: 
		output.append(substring)
	return output


input = 'ab'
input = 'ab()'
input = ''


input = 'ab(cd)ef(gh)((ij))'
output = ['ij']


input = 'ab(cd)ef(gh)'
output = ['cd','gh']
