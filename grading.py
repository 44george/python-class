#grading
math = int(input("enter math: "))
python = int(input("enter python: "))
research = int(input("enter research: "))
average_score = ((math+python+research)/3)
print(average_score)
if average_score >=70 and average_score <=100:
    grade=("A")
    print(grade)
elif average_score >=60 and average_score <=69:
    grade=("B")
    print(grade)
elif average_score >=59 and average_score <=59:
    grade=("c")
    print(grade)
elif average_score >=40 and average_score <=49:
    grade=("D")
    print(grade)
else:
    grade=("fail")
    print(grade)