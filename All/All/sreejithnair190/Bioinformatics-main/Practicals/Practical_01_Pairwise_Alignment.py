def Pairwise_Alignment(s1 , s2):
    value = 0
    gap(s1,s2)
    print(s1,s2)
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            value+=1
            score.append(1)
        else:
            score.append(0)
    print(score,end=" ")
    print("\n",value)

def gap(s1 , s2):
    if len(s1) == len(s2):
        return
    else:
        insertGap = int(input("Enter the position to enter the gap"))
        if len(s1)>len(s2):
            s2.insert(insertGap,'-')
        else:
            s1.insert(insertGap,'-')

if __name__ == "__main__":
    s1 = list(input("Enter the first sequence: "))
    s2 = list(input("Enter the second sequence: "))
    score = []
    Pairwise_Alignment(s1, s2)
