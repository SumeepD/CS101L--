name = input("Who are we calcuating grades for? ==>")
labs = int(input("Enter the Labs grade? ==>"))
exams = int(input("Enter the EXAMS grade? ==>"))
attend = int(input("Enter the Attendance grade? ==>"))
grade1 = int(labs * 0.7)
grade2 = int(exams * 0.2)
grade3 = int(attend * 0.1)
total = int(grade1 + grade2 + grade3)
print("The weighted grade for", name, "is", total)
if(total >= 90 and total <= 100):
  print(name, "has a letter grade of A")

elif(total >= 80 and total <=89):
	print(name, "has a letter grade of B")

elif(total >= 70 and total <=79):
  print(name, "has a letter grade of C")

elif(total >= 60 and total <=69):
  print(name, "has a letter grade of D")

elif(total >= 0 and total < 59):
  print(name, "has a letter grade F")