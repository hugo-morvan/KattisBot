 def calc_prob(m, n, t, p):
    import math
     # number of ways m people out of M 
    num = (math.comb(n , min(t*p-1+max(0,(min(462)-389)),M)))  
     
    return round((num/float(m**int(N))))
# Generator time: 4.2835 seconds