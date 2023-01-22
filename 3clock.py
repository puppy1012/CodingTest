h=int(input())
#h는 입력받는 값
count =0
#카운트용 변수선언
for i in range(h+1) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) +str(j)+str(k) :
                count +=1

print(count)