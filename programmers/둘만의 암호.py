"""
아스키 코드(ord, chr)로 문자 간 거리 계산 및 이동 처리
skip 문자는 건너뛰고 index만큼 이동하되, 'z'를 넘으면 'a'로 순환
문자 연산과 조건 분기를 수치 기반으로 단순하게 처리 가능
"""
def solution(s, skip, index):
    skip_set=set(skip)
    answer = ''
    for char in s:
        count=0
        next_char=ord(char) #아스키 숫자형식으로 변환
        #skip 문자는 건너뛰고 index만큼 이동하되, 'z'를 넘으면 'a'로 순환
        while count<index:#count가 index만큼
            next_char+=1
            if next_char>ord('z'):#z를 넘어갈시 대문자로 넘어가기에
                next_char=ord('a')#a로 초기화
            if chr(next_char) not in skip_set:#비교를 위해 ord로 변환한걸 chr로 재변환
                count+=1#이후 문자열 비교를 통해 count추가 할지 확인

        answer+=chr(next_char)


    return answer

print(solution("aukks","wbqd",5))