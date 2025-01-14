 import re
keys = 'A A# B C C# D E F G G#'.split()
alts_major=['C','Dm']+['G'+i for i in ['b','' ,'#']]+[k+'M'for k in keys]  + [('Bdm')]*2
alts = alts_major[:-1]    #last one is duplicate of C major, so remove it.   Alts minor are same as those with 'm'.    
regex=r"([A-G][b#]?)([a-z]+)" 
def alt(test):
 try:         m = re.match(regex , test)        note_numb,altnty    =   (keys+['Am'])[m.group(1)+'M'],m.group(2).upper()      return alts[note_numb][alts[note_numb].index(altnty)] if altnty else 'UNIQUE!'
 except:  pass #print ('no match')
# Generator time: 7.5947 seconds