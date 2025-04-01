def solution(wallpaper):
    """
    문자열을 통해 바탕화면의 크기가 입력된다.
    .은 공백 , #은 파일이 존재한다
    최소한의 드래그를 통해 처리해라
    드래그의 시작점이 (lux, luy), 끝점이 (rdx, rdy)라면 정수 배열 [lux, luy, rdx, rdy]를 return하면 됩니다.

    1.파일 위치 찾기-2중 for문
    2.드래그 범위 구하기-#의 각 위치의 min,max값을 구한뒤 max+1
    (드래그또한 슬라이드방식이기에 +1을통해서 처리)
    3.정답 반환 형식 맞추기
    """
    # file_list=[]
    # for i in range(len(wallpaper)):
    #     for j in range(len(wallpaper[0])):
    #         if wallpaper[i][j] == "#":
    #             file_list.append((i,j))
    # min_row=min(pos[0] for pos in file_list)
    # max_row = max(pos[0] for pos in file_list)
    #
    # min_col = min(pos[1] for pos in file_list)
    # max_col = max(pos[1] for pos in file_list)
    # answer = [min_row,min_col,max_row+1,max_col+1]
    # return answer
    a,b=[],[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]=="#":
                a.append(i)
                b.append(j)

    return [min(a),min(b),max(a)+1,max(b)+1]