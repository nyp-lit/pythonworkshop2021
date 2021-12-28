
first_test = float(input("enter score for first test: "))
second_test = float(input("enter score for second test: "))
first_exam = float(input("enter score for first exam: "))
second_exam = float(input("enter score for second exam: "))

tests = ((first_test + second_test) / 200) * 50
exams = ((first_test + second_test) / 200) * 50
final_marks = tests + exams

print(f"your final marks is {final_marks}")

