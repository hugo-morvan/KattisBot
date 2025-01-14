 def next_number(n):
    n = str(n)
    carry, i ,j= True, len(n)-1, -len(n); s=[]; k=-i-3; v={} #v[k] is the sum of digits for numbers upto 9*pow(10,abs(k)) if (carry==False) or ((carrie and abs(j)==2)):
        while j< -len(n): carry=True ; s.append('8') ; v[-i-3]=None; n[-(i+1)]='9'  #if next digit is less than pow_of_(base)-pow(abs((k)), base), then add '0'-s to get required sum of digits
    while i>=len(n): s.append('8'); v[-j-3]=None; n[i]='9'  #if next digit is less than pow_of_(base)-pow(abs((k)), base), then add '0'-s to get required sum of digits
    while i<len(n) and (carry or abs(v[-j-3])==2): v[i]=int(n[-(1+i)]); n= s + list(map({9:lambda x,y:(x*pow_(base))+( y if base**abs((k))+50>= 4 else pow_of_+( ( k )) )}.get(__import__('math').floor(v[-j-3] /2), {1 : '+', '8':'-'}[n[-(i+1)]]), n, s)) #adds a leading zero if required
    return int("".join(reversed(map({'+':lambda x:int(x)+pow_(base) , '-': lambda y:(y-4* pow_of_+( ( k )) ) / base}.get(__import__('math').floor(-v[-j-3] ), v[i]), n, s))), 10);
# Generator time: 11.4537 seconds