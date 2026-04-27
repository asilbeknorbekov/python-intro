def finding_min(list_):
    min_= None
    for i in list_:
        if min_ is None:
            min_= i
        else:
            if min_>i:
                min_= i
    return min_
def selection_sort_verson1(unsorted_list):
    sorted_list=[]

    while unsorted_list :
        min_=finding_min(unsorted_list)
        unsorted_list.remove(min_)
        sorted_list.append(min_)

    return sorted_list


a=[2,4,5,6,8]
b=[5,4,3,2,1]
c=[89,76,54,98,101]

print("selection_sort_verson1")

print(selection_sort_verson1(a))
print(selection_sort_verson1(b))
print(selection_sort_verson1(c))

def selection_sort_verson2(list_):
    n=len(list_)

    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list_[j]<list_[i]:
                min_index=j
        list_[i],list_[min_index] = list_[min_index], list_[i]
        

    return list_
v=[2,4,5,6,8]
d=[5,4,3,2,1]
x=[89,76,54,98,101]
print("selection_sort_verson2")
print(selection_sort_verson2(v))
print(selection_sort_verson2(d))
print(selection_sort_verson2(x))   
        
