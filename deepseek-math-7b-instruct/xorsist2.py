 def solve(N, a, b):
	ans = [i for i in range(1,N+1)] # Initialize list of numbers from 1 to n as the ans (possible persons)
	xor_values=[]   # will be used later. initialize empty values here itself so that we don't need any condition checking while adding elements into it	
	for i in range(len(ans)):   	# Iterate over every element of list 'numbers'. This is required as Python doesn't support O(1) time indexing on lists (which would have been needed if this problem had asked for a specific person instead). So we iterate through all possible persons.
		xor_values.append([ans[i]^j  for j in range(0,2**len(format(max(a,b),'b')))])   # Calculate XOR of every element with numbers from '1 to max value asked'(here its a binary number having length equal to the maximum bits present iin format converted string representation of b and store all these values into another list named "xor_values" which will be used later.
	xors = [i for sub in xor_values[:a-1] for i in sub]+[max(ans)+1 if max(ans)<b else -1 ]+ 	[sub[-2::-1][0]for j,l in enumerate(reversed(xor_values))if ans and l:
		for k ,i in reversed(list(enumerate(l))) :   # check for each possible xoring number from 'a' to b whether it is present within the list of XOR values. If not then break as we need only those persons who are possessed i,e person no = 0 and if any possesed has already been found by now so that further calculation can be avoided
			if ans[k] ==i :   # Person number equal to xoring value is present in the list of possible numbers. So remove this from possibilities as he cannot possess anything more than one thing(here its a joke on those who think python supports OOP ).  Also break further calculation for current 'a'
				ans[k] = None;break # Remove number and also stop checking other persons with same xoring value. As if we find any possesed then no need to check others as they cannot possess anything more than one thing(here its a joke on those who think python supports OOP ) 
	return "Enginn"*(0 in ans)+str([i+1 for i,j in enumerate(ans)if j][-1])*("Gunnar "*(-max(ans)<b)) # As we started from 'zero' so "+one"(or adding one to the numbers obtained earlier is necessary as python starts indexing at 0. Also -ve sign with max helps us out when ans empty i,e no possesed number was found for given range of a and b
# Generator time: 16.8430 seconds