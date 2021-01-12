# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기
y, m, d = map(int, input().split('.'))
print('%04d'%y, '%02d'%m, '%02d'%d, sep='.')
# print('%04d.%02d.%02d'%(y, m, d))