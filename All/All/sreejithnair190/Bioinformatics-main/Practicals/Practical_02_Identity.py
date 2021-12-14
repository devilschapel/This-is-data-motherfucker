def Identity(s1,s2):
    score = 0
    Gap(s1,s2)
    print(s1,s2)
    total_Elements = len(s1)*len(s2)
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            score+=1
    identity = (score/total_Elements)*100
    print("The Matching score is ",score)
    print("The Identity is ",identity)


def Gap(s1,s2):
    if len(s1) == len(s2):
        return
    else:
        insertGap = int(input("Enter the position of gap to be inserted: "))
        if len(s1)>len(s2):
            s2.insert(insertGap,'-')
        else:
            s1.insert(insertGap,'-')

if __name__=="__main__":
    s1 = list(input("Enter Sequence 1: "))
    s2 = list(input("Enter Sequence 2: "))
    Identity(s1,s2)