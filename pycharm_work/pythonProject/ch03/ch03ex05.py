grade = 'f'
score = int(input("성적은?>> "))

while not(score in range(0,101)) :
        print("error!")
        score = int(input("성적 다시 입력!!>> "))

if score >= 90 :
             grade = 'a'
elif score >= 80 :
             grade = 'b'
elif score >= 70 :
             grade = 'c'
elif score >= 60 :
             grade = 'd'

num = score % 10
if num > 7 :
                grade = str(grade) + "+"
elif num < 3 :
                grade = str(grade) + "-"

print("{}점은 {}학점!!".format(score, grade))