eng=int(input("english: "))
maths=int(input("maths: "))
isl=int(input("islamiat: "))
sci=int(input("science: "))
comp=int(input("computer: "))
total_marks=500
obtained_marks=eng+maths+isl+sci+comp
percentage=(obtained_marks*100)/total_marks
if percentage>=80:
    print("your grade is A+")
elif percentage>=70:
    print("your grade is A")
elif percentage>=60:
    print("your grade is B")
elif percentage>=50:
    print("your grade is C")
elif percentage>=40:
    print("your grade is D")
else:
    print("you are failed")