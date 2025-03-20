def binary_serach(array,target,start,end,repeat):
    #start값이 end값을 넘어간다는건 끝까지 탐색을 했지만 목표값을 찾지못했다는것이다.
    #binary_search는 정렬된값을 받는것을 기본으로한다.
    print(target,'  ',start,'  ',end)

    repeat+=1
    if start>end:
        return None
    #mid값을 start+end의 값의 몫으로 지정한다
    #지정시 항상 array의 중간위치값을 얻을수가있다.
    mid=(start+end)//2
    #array의 mid번째 자리의 값이 target값과 일치한다면 mid값을 반환한다.
    if array[mid]==target:
        return mid,repeat
    #array의 mid번째 변수값이 target값보다 높다면
    elif array[mid]>target :
        return binary_serach(array,target,start,mid-1,repeat)
    else:
        return binary_serach(array,target,mid+1,end,repeat)

n,target = list(map(int,input().split()))

array=list(map(int,input().split()))
global repeat
repeat=0

result,repeat=binary_serach(array,target,0,n,repeat)

if result== None:
    print('원소값이 존재하지않습니다')
else:
    print(result,repeat)