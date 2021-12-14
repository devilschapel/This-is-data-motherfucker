def Swap(A,a,b):
    A[a] = A[a]^A[b]
    A[b] = A[a]^A[b]
    A[a] = A[a]^A[b]

def Heapify(A, N, i):
    largest = i
    l = 2*i+1
    r= 2*i+2

    if l<N and A[l]>A[largest]:
        largest = l

    if r<N and A[r]>A[largest]:
        largest = r

    if largest != i:
        Swap(A,largest,i)
        Heapify(A,N,i)


def buildHeap(A,N):
    for i in range((N//2)-1,-1,-1):
        Heapify(A,N,i)

def Heap_Sort(A,N):
    buildHeap(A,N)
    for i in range(N-1,0,-1):
        Swap(A,i,0)
        Heapify(A , i, 0)

if __name__ == "__main__":
    A = [40,10,30,20,50,60,15]
    N = len(A)
    Heap_Sort(A,N)
    print("Sorted Array is :",A)