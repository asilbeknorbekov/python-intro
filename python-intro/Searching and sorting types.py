
"""Searching and Sorting """

##  SEARCHING
def Binary_search(arr,target):
    start=0
    end=len(arr)-1

    while start <= end:
        middle=(start+end)//2
        if arr[middle]==target:
            return middle
        if arr[middle]>target:
            end=middle-1
        else:
            start=middle+1
    return -1
arr=[1,2,3,4,5,6]
target=6

#print(Binary_search(arr,target))


##  SORTING


def buble_sorting(arr):
    for i in range(len(arr)):
        for z in range(1,len(arr)-i):
            if arr[z-1]>arr[z]:
                arr[z-1],arr[z]=arr[z],arr[z-1]
                print(arr)
    return arr
arr=[5, 3, 1, 4]
#print(buble_sorting(arr))
        

def selection_sorting(arr):
    for i in range(len(arr)):
        min_=i
        for z in range(i+1,len(arr)):
            if arr[min_]>arr[z]:
                min_=z
        arr[i],arr[min_]=arr[min_],arr[i]
        print(arr)
    
    return arr
arr=[5, 3, 1, 4]
#print(selection_sorting(arr))


def insertion_sorting(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key
        print(arr)
    return arr

arr=[5, 3, 1, 4]
print(insertion_sorting(arr))
                
                
                

