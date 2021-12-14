def Similarity(s1,s2,similarities):
    print(s1,s2,similarities)
    score = 0
    for i in range(len(s1)):
        for j in range(len(similarities)):
            if s1[i] in similarities[j] and s2[i] in similarities[j] and s1[i]!=s2[i]:
                score+=1
    similarity = (score*100)/len(s1)
    print("The similarity is ",similarity)

if __name__ == "__main__":
    s1 = list(input("Enter the first sequence: "))
    s2 = list(input("Enter the second sequence: "))
    similarities = []
    NS = int(input("How many similar elements : "))
    for i in range(NS):
        a = input("Enter the similar element: ")
        b = int(input("How many elements is it similar to :"))
        similarities.append([])
        similarities[i].append(a)
        for j in range(b):
            c = input("What is it similar to :")
            similarities[i].append(c)
    Similarity(s1,s2,similarities)


