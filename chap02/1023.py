# 1023 : [기초-입출력] 실수 1개 입력받아 부분별로 출력하기
"""
f = float(input())
print(round(f))
print(int(round(f - round(f), 6) * 1e6))
"""

integer, real = map(int, input().split('.'))
print(integer)
print(real)

