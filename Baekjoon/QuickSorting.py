array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    #원소가 1개인 경우 종료한다
    if start >=end:
        return
    #피벗은 첫번째 원소이다
    pivot = start
    left = start+1
    right= end
    while left <= right:
        #피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
        #피벗보다 작은 데이터를 찻을때까지 반복
        while right >start and array[right] >= array[pivot]:
            right -=1
        #값이 엇갈린다면 작은 데이터와 피벗을 교체한다
        if left >right:
            array[right],array[pivot]=array[pivot],array[right]
        #엇갈리지않는다면 작은데이터와 큰 데이터를 서로 교체한다.
        else:
            array[left],array[right]=array[right],array[left]
    #위의 작업은 1차적인 분류작업이다
    #위의 작업이 모두 끝난뒤 왼쪽과 오른쪽 부분에서 각각의 정렬 수행을 한다
    quick_sort(array,start,right -1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort1(array):
    #리스트가 하나의 원소값을 가지고있으면 반환을 해라 이미 끝났다
    if len(array) <=1:
        return array
    pivot =array[0]#피벗은 리스트의 첫번째 원소
    tail= array [1:]#피벗을 제외한 리스트값
    left_side = [x for x in tail if x<=pivot] #분할된 왼쪽 부분이다
    right_side = [x for x in tail if x>pivot] #분할된 오른쪽 부분이다

    return quick_sort1(left_side)+ [pivot]+quick_sort1(right_side)
print(quick_sort1(array))