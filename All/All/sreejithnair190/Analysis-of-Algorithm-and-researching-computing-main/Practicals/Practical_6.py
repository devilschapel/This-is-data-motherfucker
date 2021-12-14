def Counting_Sort(arr):
    output = [0]*256
    count = [0]*256
    ans = [""]*len(arr)

    for i in arr:
        count[ord(i)] +=1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])]-=1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

if __name__ == "__main__":
    arr = "advancedalgorithm"
    print(f"The original array is: {arr}",end=" ")
    print()
    ans  = Counting_Sort(arr)
    print(f"The array after performing Counting Sort: {ans}",end=" ")