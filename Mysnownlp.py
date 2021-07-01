#--------------------------------------------------------------------------------------------------------------------------
# 語意分析 推薦
#--------------------------------------------------------------------------------------------------------------------------
from snownlp import SnowNLP

def Mysnownlp(inputname,myComment,myName,myID,myLen):

    MyID = myID
    MyName = myName
    MyComment = myComment
    Inputname = inputname
    MyLen = myLen
    
    ScoreList = []        
    for x in range(MyLen): 
        if myName[x] == inputname:continue
        s = SnowNLP(MyComment[x])
        Score = 0
        Count = 0
        scoList = []
        for sentence in s.sentences:
            Score += SnowNLP(sentence).sentiments
            Count += 1

        scoList.append(MyID[x])
        scoList.append(Score/Count)
        ScoreList.append(scoList)
        ScoreList = sorted(ScoreList,reverse=True,key = lambda s: s[1])
    
    ResultList = []
    for e,f in ScoreList:
        ResultList.append(e)    

    return ResultList[0:5]