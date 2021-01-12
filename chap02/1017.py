# 1017 : [기초-입출력] 정수 1개 입력받아 3번 출력하기
n = int(input())
print(n, n, n, sep=' ')   # print(n, n, n, ) 기본값 생략 가능

"""
print(n, end=' ')
print(n, end=' ')
print(n, end=' ')
"""

# end : print 함수가 끝난 후 넣을 문자 지정    (기본값 : 계행 \n)
# sep : print 함수의 값들 사이에 넣을 문자 지정 (기본값 : 공백 1칸)