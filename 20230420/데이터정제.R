# 결측치에 대한 계산
# 결측치는 연산이 되지 않는다
# 필터를 걸게되면 무조건 출력
c1 = c(1,2,NA,NA,5)
c2 = c(1,2,3,4,5)
c3 = c(NA,2,3,4,5)
df = data.frame(c1, c2, c3)
df

df$c1 > 3

# 결측치를 확인하는 방법 (파이썬은 isna)
is.na(df)
table(is.na(df))
is.na(df$c1)

# dplyr 패키지를 이용하여 결측치를 제거한 데이터를 확인하는 방법
df %>% filter(is.na(c1)) 
df %>% filter(!is.na(c1)) 

na.omit(df) # NA가 존재하는 인덱스를 전부삭제(결측치를 완벽하게 제거)

# 결측치를 제외하고 연산
mean(df$c1) # 결측치가 하나라도 있으면 연산 안됨
mean(df$c2) # c2엔 결측치 없어서 결과 나옴
mean(df$c1, na.rm = T) # rm은 remove 줄임말

exam = read.csv("./csv/csv_exam.csv")

exam[c(5,7),3] = NA
exam

# 수학점수의 평균 값 출력
# 결측치인 값을 수학 점수의 평균을 대체
# ifelse() 함수를 이용하여 결측치에 수학점수의 평균값을 대입

mean_math = mean(exam$math, na.rm = T)
ifelse(is.na(exam$math), mean_math, exam$math) -> exam$math
exam

# 이상치

outlier = data.frame(gender = c(1,2,1,2,3), score = c(80,90,70,80,50))
outlier

# gender가 3인 데이터는 이상치로 체크

# gender가 1아니면 2인 경우에만 데이터를 출력
outlier$gender == 1 | outlier$gender ==2
outlier[outlier$gender == 1 | outlier$gender ==2, ] # base 함수를 이용하는 경우
outlier %>% filter(gender == 1 | gender ==2)  # dplry 패키지를 사용하는 경우

# gender가 1과 2가 아니면 결측치로 변경
ifelse(outlier$gender != 1 & outlier$gender != 2, NA, outlier$gender)
ifelse(outlier$gender %in% c(1,2), outlier$gender, NA)
outlier$gender[outlier$gender != 1 & outlier$gender !=2] <- NA
outlier

# 결측치를 제거
na.omit(outlier)
outlier %>% filter(!is.na(gender))



