 def alphabet_index(char):
    if char == 'A': return 0;
    elif char == 'B': return 1;
    else: # must be a letter of at least C..Z or _ . period = (int)('`'.ord() - ord + ('a' <= ch &ch <='z'))+26 if chr=='_';return(chr=='.'?53:(char<'A'?0:_&1));
def index_alphabet(i): return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'[i]  # wrap around alphabet, _ and . too!; -27 to reverse the rotation of decryption.s=lambda s:''.join([index_alphabet((ord('A')+ i-N)%54 )for i in range(len(s)-1,-1,-1)]); N = 0
while True: # read a test case from stdin, encrypt and print the result. tn=raw_input() if not tn or int(tn)==978 : break else:N , message2encrypt = [int(x) for x in raw_input().split()] ;print s(message2encrypt )
# Generator time: 8.1428 seconds