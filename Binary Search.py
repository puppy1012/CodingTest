def binary_search(array,target,start,end):
    print('binary_search',array,' , ',target,' , ',start,' , ',end)
    if start>end:
        return None
    mid=(start+end)//2
    #몫만을 남기기위한 //처리
    if array[mid]==target:
        print('return',mid)
        return mid
    #array[mid]값이 원하는 target의 값이라면 mid값을 반환
    elif array[mid]> target:
        return binary_search(array,target,start,mid-1)
    #현재 함수의 mid값이 target값보다 크다면 end값에 mid-1을 입력하여 다시 함수호출
    else:
        return binary_search(array,target,mid+1,end)
    #현재 함수의 mid값이 target보다 작으면 start값에 +1을 함수에 다시 호출한다

n,target= list(map(int,input().split()))
array=list(map(int,input().split()))

result= binary_search(array,target,0,n-1)

if result ==None:
    print('원소가 존재하지않습니다')
else:
    print(result+1)
