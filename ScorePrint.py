n=int(input())
#key값으로 리스트 입력

array=[]
#입력방식 = key값(문자),value값(정수)
for i in range(n):
    #들어오는값을 띄워쓰기로 분리
    input_data=input().split()
    #리스트에 append시킨다.
    #현재 key값(문자)가 먼저들어오고, value값(정수)가 2번째로 들어오는것을 알수있다.
    array.append((input_data[0],int(input_data[1])))
#lambda함수 사용, 키를 이용, student의 1번 즉 점수를 기준으로 정렬한다
array=sorted(array,key=lambda student:student[1])
for student in array:
    print(student[0],end=' ')

'''
리스트.sort()는 본체의 리스트를 정렬해서 변환
sorted(리스트)= 본체 리스트가 아닌 정렬한 새로운 리스트를 반환한다.
'''