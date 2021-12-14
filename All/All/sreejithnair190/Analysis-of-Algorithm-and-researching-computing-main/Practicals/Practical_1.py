from random import randrange

def partition(arr,pivot_index = 0):
    i = 0
    if pivot_index!=0:
        arr[0],arr[pivot_index]=arr[pivot_index],arr[0]

    for j in range(len(arr)-1):
        if arr[j+1]<arr[0]:
            arr[j+1],arr[i+1]=arr[i+1],arr[j+1]
            i+=1
    arr[0],arr[i]=arr[i],arr[0]
    return arr,i

def RSelect(arr,element):
    if len(arr)==1:
        return arr[0]
    xpart = partition(arr,randrange(len(arr)))
    arr = xpart[0]
    j = xpart[1]

    if j==element:
        return arr[j]

    elif j>element:
        return RSelect(arr[:j],element)

    elif element>j:
        element = element - j - 1
        return RSelect(arr[(j+1):],element)

if __name__ == "__main__":
    arr = [3, 1, 8, 4, 7, 9]
    for element in range(len(arr)):
        print(RSelect(arr, element),end=" ")
