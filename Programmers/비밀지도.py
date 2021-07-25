def solution(n, arr1, arr2):
    mat1 = []
    mat2 = []

    # n*n 의 정사각 행렬 만들기 
    for i in arr1:
        mat1.append(list(format(i, 'b').zfill(n)))
    for j in arr2:
        mat2.append(list(format(i, 'b').zfill(n)))

    # 답 matrix 만들기
    ans = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if mat1[x][y] == '0' and mat2[x][y] == '0':
                ans[x][y] = ' '
            else:
                ans[x][y] = '#'

    # list 만들기
    rst = []
    for row in ans:
        rst.append(''.join(row))

    answer = rst
    return answer

import itertools
