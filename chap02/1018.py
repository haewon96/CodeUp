# 1018 : [기초-입출력] 시간 입력받아 그대로 출력하기
"""
time = list(map(str, input().split(':')))
print(time[0] + ':' + time[1])
"""

h, m = map(int, input().split(':'))
print(h, m, sep=':')
# print('%d:%d'%(h, m))