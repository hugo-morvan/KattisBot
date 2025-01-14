 import sys
def chess_board():  # read input from standard input (sys)	
	n = int(next(input()).split()[0])	# number rows in board and numbers of integers on each row are equal, hence only one parameter n is passed as argument to function. next() method reads the first line which contains N followed by K separated by space 	and split(' ') splits that into two parts
	k = int(next(input()).split()[0])	# number dominoes available (K)	
	if k > n:				 # if total possible rows to be covered with dominos is more than actual row count, set it equal the column size.  It means we have many less columsn then required for covering all cells using that fewers no ofdominos(k). So need find largest sum by coverin each domino two cell
		k = n				 # this will be used to calculate dominos (2*1) placed row wise in board. hence only one parameter is passed as argument 	to function chess_board() which contain k, no of rows or columns(n). next line contains integers written on each field separated by space
	nums = [int(x) for x in input().split()] # reads all numbers from the second last row to first and store them into num list.  (since we have already considered N number if lines of int as rows, hence this will start with n+1 line which is nextline after blank one.)
	nums = sorted(nums)[::-1]			 # sort all integers in descending order for getting highest possible sum by selecting largest and second large numbers (for each domino) to place row wise or columnwise.  hence only num parameter passed as argument into function chess_board() which contain list of integer
	ans = [nums[i]+nums[i+1] if i*2 <= k else max(nums[:k]) for i in range(0, len(nums), 2)] # this will place each domino's largest sum by considering the two numbers (in descending order) and keep adding that to ans. till we cover all K dominos required
	return n*3 - k + max(ans)*k/n				# for getting final output multiply maximum integer in list with number of rows covered, then subtract from total possible row count * 2 subtracted by actual used no's (for each domino) and divided it into sum. this will give the largest expected value that can be achieved
print(chess_board())
# Generator time: 14.0525 seconds