 def count_unread(n):
    # initialize an empty set to store read messages for each person
    reads = [set() for _ in range(n)]
    
    total_messages = 0
    unread_messages = n -1   # all other members as initial unread message count, plus one more because the sender also has an unread messages initially. For eg: A sends a msg to B and C (initially no read), so for each of them it is like they have 2+1=3(n-1 + s)unread msgs where n = total members in group,s senders id
    
    # calculate the number unread messages after sending mth message by reading all previous sent msg (m - i), and also adding one for current sender's own message. So it will be like ((n-1) * count of msgs(i)) + 1 till we reach to a given sequence
    def calculate_unread():   # s is the last id send in that case no need extra parameter (as this function should only used for first time sending). Also, it's just another way as written by author. But I would prefer using unread msgs calculation logic from my above solution because of more clarity and understanding
        nonlocal total_messages   # we use `nonlocal` to access the global variables in a nested function scope (in this case 'total messages'). Without it, Python will produce an error as local variable is not found.  This line allows us read/write privilege on our globals inside calculate unread fn
        nonlocal reads     # similarly for list of sets(reads) which are also global to me in my opinion but since its a nested function I'm using 'nonlocal'. Please correct if i m wrong with this understanding.  Will be great help from u expert like you (YT). Thanks!
        
        unread_messages = total_messages // n +1   # use integer division to get the number of messages sent by each member, plus one for current sender's own message   
        reads[total_messages % n] |= set(range((n - 1) * (unread_messages), unread_messages))     # update read history with new msgs from this send. We use 'or equals` operator `|=`, which adds the elements in right hand side to left, but does not change anything if any element of rhs is already present lhs
        total_messages += 1    # increment for next message (s)   by sender s and calculate unread messages after sending this mth msg. It will be like ((n-1)*(m - i)) + current count as we read all previous sent msgs till now including the last one just send
        return sum([len((reads[i] - set([s])) & reads[(total_messages+i) % n]) for i in range(n)])  # calculate total unread messages. We get this by subtracting current sender's id from all other members read history and taking intersection with next member (since no two message sent at same time so only one can be the last), then adding that to each of their previous counts
        
    return count_unread(n)
# Generator time: 17.5344 seconds