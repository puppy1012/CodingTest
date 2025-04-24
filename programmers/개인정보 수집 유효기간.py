def solution(today, terms, privacies):
    # 1. 오늘 날짜를 일수로 변환
    today_days = date_to_days(today)

    # 2. 약관 종류별 유효기간 매핑
    term_dict = {}
    for term in terms:
        type_, duration = term.split()
        term_dict[type_] = int(duration)

    # 3. 파기해야 할 개인정보 번호를 저장할 리스트
    answer = []

    # 4. 각 개인정보에 대해 파기 여부 판단
    for idx, privacy in enumerate(privacies):
        date_str, term_type = privacy.split()
        collected_days = date_to_days(date_str)
        expiry_days = collected_days + (term_dict[term_type] * 28)

        if expiry_days <= today_days:
            answer.append(idx + 1)  # 번호는 1부터 시작
    return answer


# 날짜를 일수로 변환하는 함수
def date_to_days(date_str):
    year, month, day = map(int, date_str.split('.'))
    return (year * 12 * 28) + (month * 28) + day
