"""
#n,m을 띄워쓰기로 가져오고
n,m=map(int,input().split())
#결과값 저장용 변수선언
result = 0
#min,max함수 사용
for i in range(n) :
    data = list(map(int,input().split())) #행과 열 값을 띄워쓰기로 list형식으로 가져온다
    print("data:",data)
    min_value=min(data) #data리스트값중 제일 작은값을  min_value변수에 입력3
    print("min_value:",min_value)
    result =max(result,min_value) #result와 min_value값중 큰값을 result변수에 입력
    print("result:",result)
print(result)
"""
n,m=map(int,input().split())
result=0
for i in range(n) :
    data = list(map(int,input().split()))
    min_value=9999 #값을 선언시 0과같은 작은값을 넣으면 사용자가 입력하는값보다 더 작아서 오류가 발생할수있다.
    for a in data :
        min_value=min(min_value,a)
    result = max(min_value, result)


print(result)