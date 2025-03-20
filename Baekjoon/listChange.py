n,k = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#오른차순으로 제일 작은거부터
a.sort()
#내림차순으로 제일 큰것부터 앞으로
b.sort(reverse=True)
for i in range (k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
print(sum(a))

'''
n= n번째까지 원소를 받음
k= k번만큼 a와 b의 값을 서로 바꾼다
a,b는 리스트형식으로 작동되며 공백으로 입력된다
a의 값이 최대가 되기위해서 a는 정순으로
b는 역순으로 sort를 진행하여 i번째일때 비교하여 변경할수있도록 한다

'''