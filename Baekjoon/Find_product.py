'''
def Find_product(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return Find_product(array,target,start,mid-1)
    else:
        return Find_product(array,target,mid+1,end)

n=int(input())
n_number=list(map(int,input().split()))
n_number.sort()
m=int(input())
m_number=list(map(int,input().split()))

for i in m_number:
    result=Find_product(n_number,i,0,n-1)
    if result!=None:
        print('Yes',end=' ')
    else:
        print('No',end=' ')
'''
n=int(input())
array=set(map(int,input().split()))
m=int(input())
x=list(map(int,input().split()))
for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('No',end=' ')