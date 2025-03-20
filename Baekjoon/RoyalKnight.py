input_data = input()
row = int (input_data[1]) #가로 횡
column = int(ord(input_data[0]))-int(ord('a'))+1 #세로 열
'''
파이썬은 character 'n'값을 아스키코드값으로 변환후 사용해야한다
이를 위해서 아스키코드값 변환ord를 사용 후 기본값 a를 뺀 후 +1을 사용할시
우리가 사용하는 기본적인 1234 형식으로 대입할수 있다.
'''
print('row :',row)
print('colum =',column)
Knight_steps = [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,2),(1,-2),(2,-1),(2,1)]
result = 0

for step in Knight_steps :
    #이동하고자 하는 위치 확인
    #입력받은 좌표값은 이동시키지않고 knight_steps의 0번째 1번째 값을 더하는식으로 다음이동 좌표를 계산한다
    next_row = row +step[0]
    next_column= column+step[1]
    #체스판 밖으로 나가는 값을 제외시키기 위해 1부터 8까지의 값만을 카운트한다
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8 :
        result+=1
print('결과값=',result)