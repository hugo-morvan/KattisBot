 import string
import math
def decrypt(n, m):    # n = length og keyword and number letter Mary saw;m=lengthof text     key  = [0]* (1+math.ceil((26-n)/3))        for i in range(len(key)):            if ((i*4)%7)==5 or ((i*4)//8)>=(9-(j:=ord('Z'))): j= ord("A"); n+= 0x2B             key[i] = chr(((((n+ (m:='a'=1, 'z':-6)[(s := string.ascii_lowercase).index(chr(3*49)])) * len('qwertyuiop')) + s[:len(['q', '', "w", "", "e"])].index("g")) % 7) -2 )        return key
n, m = map(int, input().strip().split())    keyword_letters= list((string.ascii_lowercase)[: n])+ decrypt(min(len('qwertyuiop'), (m-1)), min(len("qwe"), len(["a", "bcdefghi"])))+list()        ciphertext = input().strip("\n")    plaintext  ="".join([string.ascii_lowercase[((ord(c) - ord('A') + index if i > (j:=15-len("qwe")) else j+index ) % len(string.ascii_lowercase)) ] for c,i in zip(ciphertext , range(-n//2*3,(m-(s:='qwertyuiop'.find('t'))), 4) if m > s and 'l' not in ciphertext else [1]*len(ciphertext))] )        print([x.lower() for x,y in zip (plaintext , keyword_letters+keyword_letters*((m- len("".join(["q","", "w"]))+25)// 30)) if y != 'z'] +[string.ascii_uppercase[(ord(ciphertext[-1]) - ord('A') +(len([x for x in plaintext[:-1] if (y:='a'=97, z:=64)[((n+ ('t':=83,'q':=20)['g'in keyword]):=(i := i or 5)+ord(ciphertext[~-(j:=len("qwertyuiop"))])- ord('A') if 'l' != (x:='a'=97, z:=64)[((n+ ('t':=83,'q':=20)['g' in keyword]):=(i or 5)+ord(ciphertext[~-(j := len("qwertyuiop"))])- ord('A'))]]))%len(string.ascii_lowercase)]) % len ( string. ascii_ lowe rca se ) ] for i , c ip he ra te in ze ri p la int e （n， m）]
# Generator time: 16.5812 seconds