#거의 정렬된 상태에서의 입력이 주어진다면 퀵정렬보다는 선택정렬이 더 정답일확률이 높다
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j

    array[i],array[min_index]=array[min_index],array[i]

print(array)

array=[3,5]
array[0],array[1] = array[1],array[0]
print(array)

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    print('for i의 값은',i)
    #start,end,step i부터 0까지 -1만큼 진행하라
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            print('스위칭 작업 진행중')
            print(array[j],'랑',array[j-1],'값이')
            array[j],array[j-1]=array[j-1],array[j]
            print(array[j-1], '랑', array[j], '값으로 변경됨')
        else:
            break
print(array)
