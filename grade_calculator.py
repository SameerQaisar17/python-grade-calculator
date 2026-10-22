print("===== STUDENT GRADE CALCULATOR =====")

student_name = input("Enter student name: ").strip()

while not student_name:
    print("Student name cannot be empty.")
    student_name = input("Enter student name: ").strip()


def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (out of 100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


print("\nWelcome,", student_name)

maths = get_marks("Maths")
physics = get_marks("Physics")
computer_science = get_marks("Computer Science")

total = maths + physics + computer_science
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

if average >= 60:
    result = "PASS"
else:
    result = "FAIL"

print("\n===== STUDENT RESULTS =====")
print("Student:", student_name)
print("Maths:", maths)
print("Physics:", physics)
print("Computer Science:", computer_science)
print("Total Marks:", round(total, 2), "/ 300")
print("Average:", round(average, 2), "%")
print("Grade:", grade)
print("Result:", result)