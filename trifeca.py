#the function receives a word and checks whether it has three consecutive pairs of identical letters in it
def trifeca(word):   
    pairs=[]
    count=0
    for i in range(0,len(word)-1):
        pairs.append(word[i:i+2])
    for i in range(0,len(pairs)-3):
        if pairs[i][0]==pairs[i][1] and pairs[i+2][0]==pairs[i+2][1] and pairs[i+4][0]==pairs[i+4][1]:
            count+=1
        else:
            count+=0
    if count>0:
        return True
    else:
        return False
