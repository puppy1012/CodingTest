def solution(cards1, cards2, goal):
    i,j=0,0
    #검증해야하는 문장수만큼 for문
    for word in goal:
        #각 word가 cards뭉치에 순차적으로 사용되는지 확인
        if i<len(cards1) and cards1[i]==word:
            i+=1
        elif j<len(cards2) and cards2[j]==word:
            j+=1
        else:
            #예외 적용시 바로 No반환
            return "No"
        #검증이 완료되면 별도 절차없이 바로 yes 반환
    return "Yes"