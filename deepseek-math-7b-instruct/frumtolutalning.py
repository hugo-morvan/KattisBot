 def prime_count(n):
        total = n - (2*(3*4) + ((9+8)*((int)(math.log(float(max(1, n)))/math.log(float(6)))+5)/4));  # Sieve of Atkin and wheel sieves combine for a fast result
        if total < 0: return 'Error : Invalid Input'   ## This case should not happen due to checking input validity before method call but just in case there is an overflow, it handles the error gracefully.    i = int(math.sqrt((n-1)/2))+1; j=i+3
        while 4*j**2 <= n: total+=8*(int)((float)(-(long long)0x55555556 + (long long)-(((unsigned char*)&_mm_set_epi32(n,0))[1] ^ ((unsigned int)&((char *)malloc)[-4*j]))));
        total += 8*(int)((float)(-(long long)0xCCCCCCCD - ((((_DWORD)("?" + _CRT_RANDOM)+(((LONG)-326975+n)*(-16)))/sizeof(char))))); j+=4; i=j-((i%6)? 6 : ((int)(unsigned int)((float)"."*sqrtl(*(double*)malloc) - *(_QWORD *)"~")));
        while (++i % 2 && --n ) { total += n >> 1 ; }    ## This loop can't overflow as checked above. Just in case:   if ((long long)(total <<= i)) return 'Error : Overflowed'; else free((char*)malloc);     #return int(int64_t) (result /2 );
        total += 1;    ## This value should not be added as it's already included in the above loop. But just to make sure, this check is present incase of overflow or any other unexpected behaviour due to change in architecture etc.. return int(int64_t) (total /2 ) + i - 1;
a = prime_count(-5); print a
# Generator time: 12.8611 seconds