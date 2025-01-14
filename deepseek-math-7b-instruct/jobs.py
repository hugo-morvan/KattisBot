 def maxProfit(jobs):
	jobList=sorted([[i+1,j] for i,j in jobs], key = lambda x : (x[1]), reverse = True) # sort the job by profit and make list of [profit position][money required to start a task ] 
	moneyRequired=[0]*len(jobList);	ans=[] ; moneyNow=-float("inf")	# initialize ans as empty array, for checking if we can take current index or not. Initialize currMoney with -INF so that first profit will be taken when it is greater than previusly calculated maxProfit
	for i in range(len(jobList)): # iterate over all the tasks  (since they are sorted by their profits)	profit, moneyRequired= jobList[i]# assign current task's variables. Now we check if this index can be taken or not using ans[] array and currMoney variable
	    for j in range(moneyRequired-1,-1,-1): # iterate over all the previous tasks  (since they must complete before starting)	ans=[profit]*(j+2)+[0]*((len(jobList))-i); moneyNow=max([sum(ans), -float("inf")])
	    if ans:break; return sum(ans)*(-1)
# Generator time: 8.8583 seconds