def solution(n, m, section):
    answer = 0  # 칠한 횟수
    i = 0  # section을 순회할 인덱스

    while i<len(section):
        start=section[i]
        end=start+m-1
        answer+=1

        while i<len(section)and section[i]<=end:
            i+=1
    return answer
