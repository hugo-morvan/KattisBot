 def solve(N, s):
    ans = []
    
    for i in range(len(s)): # Iterate through all contestants to find the minimum percentage of votes required. If a contestant's score is lowest (and therefore tied with others), no one will be eliminated and we need not calculate anything further as this problem asks us about being guaranteed, which means 100% for sure
        min_percent = None # variable to hold the minimum percentage of votes required by any given contestant so far. Initially set it at none (no value) because if no one's score is lowest yet then we don't know how much should be calculated next, until a new record low emerges or an existing tie breaks
        
        for j in range(101): # iterate through all possible percentages of votes that the contestant can get (from 0% to max inclusive), starting from lowest percentage and going up one by one each time. This is because if a certain amount gets us eliminated, surely getting more will not save you
            temp_sum = sum([max(s[k] - s[i], 0) / (N * j + N - i) for k in range(len(s))]) # iterate through all contestants again to calculate the new scores after this contestant gets additional votes, and store it temporarily. The max function is used here because we can't have negative points
            if temp_sum < s[i] / j: 
                min_percent = (j + N - i) * sum([s[k]/N for k in range(len(s))]) # this condition means that after getting additional votes, the new lowest score is greater than or equal to current contestant's original pre-vote scores. So we have found a better option and should save it
                break # no need to check further as there won't be any lower percentage of vote which can guarantee not elimination this time around  (no point in continuing the loop)           
        if min_percent is None:min_percent = 'IMPOSSIBLE!'
        ans.append(format((j + N - i), '.5f')) # append to result list and format as required by problem, adding a decimal place for cases when percentage might not be an integer (e.g., 1/3)        
    return 'Case #{}: {}'.format(N+1, " ".join([str(a) if type(a)==float else str(int(round(a,0))) for a in ans]))
# Generator time: 14.4721 seconds