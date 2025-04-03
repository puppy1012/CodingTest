def solution(keymap, targets):
    # 1. 각 문자를 누르는데 필요한 최소 횟수를 저장할 딕셔너리
    min_press = {}

    # 2. keymap의 각 문자열을 순회
    for key in keymap:
        for idx, char in enumerate(key):
            # char를 누르려면 idx+1번 눌러야 함 (0-based index → 1-based 횟수)
            if char in min_press:
                # 이미 저장된 값이 있다면 더 작은 값으로 업데이트
                min_press[char] = min(min_press[char], idx + 1)
            else:
                # 처음 나오는 문자라면 그냥 저장
                min_press[char] = idx + 1

    # 3. 결과를 저장할 리스트
    answer = []

    # 4. 각 target 문자열을 순회
    for target in targets:
        total = 0  # 이 문자열을 치는데 필요한 총 횟수

        for char in target:
            if char in min_press:
                # 해당 문자를 누르는 최소 횟수를 누적
                total += min_press[char]
            else:
                # 해당 문자가 keymap에 없으면 -1로 처리하고 중단
                total = -1
                break

        # 현재 target 문자열에 대한 결과 추가
        answer.append(total)

    # 5. 최종 결과 반환
    return answer
