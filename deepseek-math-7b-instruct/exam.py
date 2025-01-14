 # Python program to calculate max score possible
def find_max_score(friendAnswers):
    yourScore = 0; totalQuestions = len(friendAnswers) - friendAnswers[::-1].index('T') + 2 if 'F' in set(friendAnswers) else None  
    return (min((totalQuestions, int("".join(['T']*len(set([a for a in friendAnswers]))))), key=lambda x:x)[0] - totalQuestions+1)+ yourScore;
# Generator time: 4.7594 seconds