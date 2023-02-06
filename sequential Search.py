#순차탐색이란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
'''
def sequential_serach(n,target,array):
    for i in range (n):
        if array[i] ==target:
            return i+1



print("생성할 원소 개수를 입력한 다음 한 칸 띄우고 찾을 문자열을 입력하세요.")
input_data=input().split()
n=int(input_data[0])

target=input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다")
array=input().split()

print(sequential_serach(n,target,array))
'''
#이진탐색 binary serach = 시작점,끝점,중간점을 통해
#찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는데이터를 찾는것이 이진탐색과정이다

def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target :
        return mid
    elif array[mid]>target :
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n,target=list(map(int,input().split()))

array=list(map(int,input().split()))

result= binary_search(array,target,0,n-1)
if result == None :
    print("원소가 존재하지않습니다.")
else :
    print(result +1)

