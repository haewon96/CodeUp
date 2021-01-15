# 1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기
data = input()
count = 1e4

for d in data:
    print('[' + str(int(int(d) * count)) + ']')
    count /= 10

"""
print('[' + str(int(data[0]) * 10000) + ']')
print('[' + str(int(data[1]) * 1000) + ']')
print('[' + str(int(data[2]) * 100) + ']')
print('[' + str(int(data[3]) * 10) + ']')
print('[' + str(int(data[4])) + ']')
"""