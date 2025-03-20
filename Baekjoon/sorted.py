array=[7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array=[7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

#key 매개변수를 입력으로 사용가능하다
array=[('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]
result= sorted(array,key=setting)
print(result)

#정렬 라이브러리는 항상 최악의 경우에도 NlogN 시간복잡도를 보장한다

#단순정렬상황시 기본 정렬 라이브러리 사용,데이터 범위 한정시 계수 정렬을 사용하자.

'''
1.정렬 라이브러리로 풀 수 있는 문제
2.정렬 알고리즘의 원리에 대해 물어보는 문제
3.더 빠른 정렬이 필요한 문제
'''
n=int(input())
#n개의 정수를 입력받아 리스트에 저장
array=[]
for i in range(n):
    array.append(int(input()))

array= sorted(array,reverse=True)

for i in array:
    print(i,end=' ')