# 1029 : [기초-데이터형] 실수 1개 입력받아 그대로 출력하기2
d = float(input())    # 입력값 : 3.14159
print('%.11f'%d)      # 출력값 : 3.14159000000
print(round(d, 11))   # 출력값 : 3.14159

"""
### 서식 지정자 (format specifier) : 특정 자료형을 표현하는 방법

# '%s'% : 문자열 자료형 <- String
# '%d'% : 정수 자료형   <- Decimal Integer
# '%f'% : 실수 자료형   <- Floating Point(부동 소수점)를 Fixed Point(고정 소수점)로 표현
                         (1) 기본적으로 소수점 이하 6자리까지 표시
                         (2) '%.자릿수f'% : 소수점 자릿수 변경 - %f 사이에 .자릿수 지정\

# 정렬하기             <- 서식지정자의 %와 서식 지정 문자(s,d,f) 사이에 길이(숫자) 넣기
                         '%길이s'%, '%길이d'%, '%길이.자릿수f'% 
                         오른쪽 정렬 (+) / 왼쪽 정렬 (-)

# 여러 개의 값 표현하기  <- ex) '%d는 정수, %f는 실수, 그리고 %s는 문자열입니다.'%(1, 1.1, 'hello)
"""