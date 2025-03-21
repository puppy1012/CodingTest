def solution(name, yearning, photo):
    """
    문자열 배열 name
    그리움 점수 배열 yearning
    계산해야하는 문자열 배열photo
    for문을 두번 중첩하게되면 비효율적이니까 딕셔너리?를 이용해보자
    name을 key로 yearning을 i로 생각하고 photo의 문자열을 for문으로 돌리면서
    결과값을 list로 저장했다 return하기
    """
    score_mapping={}#딕셔너리
    for i in range(len(name)): #mapping작업
        score_mapping[name[i]]=yearning[i]
    result=[]#결과값 저장용 리스트
    for person in photo:#photo의 여러 리스트를 나누기위함
        total_score=0#photo안의 여러리스트의 점수 계산용
        for score in person:
            if score in score_mapping:#이름에맞는 점수 확인후
                total_score+=score_mapping[score]#점수 합산
        result.append(total_score)#계산 끝나면 결과값 저장용 리스트에 저장

    return result