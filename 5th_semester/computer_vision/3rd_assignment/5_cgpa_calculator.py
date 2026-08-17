# (e) Using python array list and take 6 courses number show the GP and GPA of that semester.

marks = []
total_gp = 0

for i in range(6):
    mark = int(input(f"Enter marks for course {i + 1} :"))
    marks.append(mark)

for m in marks:
    if m >= 85:
        gp = 4.0
    elif m >= 80:
        gp= 3.7
    elif m >= 75:
        gp = 3.3
    elif m >= 70:
        gp = 3.0
    elif m >= 65:
        gp = 2.7
    elif m >= 60:
        gp = 2.3
    elif m >= 55:
        gp = 2.0
    elif m >= 50:
        gp = 1.7
    else:
        gp = 0.0
    total_gp += gp
    
gpa = total_gp / 6

print("\n _____________ Result____________")

print("Marks List:",marks)
print("Total Grade points :", total_gp)
print("Gpa of Semester:", round(gpa,2))

