import random
def partition(sample,start,end):
         print("Sample:",sample)
         pivot=sample[end]
         print(pivot)
         index=start
         print(index)
         current=start
         print(current)
         while(current<end):
                  if(sample[current]<=pivot):
                           print(sample[index])
                           print(sample[current])
                           sample[index],sample[current]=sample[current],sample[index]
                           index+=1
                  current+=1
         sample[index],sample[end]=sample[end],sample[index]
         print("After partition:",sample)
         return index

def quickSort(sample,start,end):
         if(start<end):
                  index=partition(sample,start,end)
                  quickSort(sample,start,index-1)
                  quickSort(sample,index+1,end)

sample=random.sample(range(0,20),10)
print(sample)
quickSort(sample,0,9)
