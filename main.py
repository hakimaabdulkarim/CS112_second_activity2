student_name = input("student name: ")
ID = input("id#:")
course_section = input("course and section:")
first_quarter_grade = eval(input("first grading:"))
second_quarter_grade = eval(input("second grading:"))
third_quarter_grade = eval(input("third grading:"))
fourth_quarter_grade = eval(input("fourth quarter grade:"))

ave = (first_quarter_grade + second_quarter_grade + third_quarter_grade + fourth_quarter_grade)/ 4

print("student_name", student_name)
print("id", ID)
print("course_section", course_section)
print("first_quarter_grade", first_quarter_grade)
print("second_quarter_grade", second_quarter_grade)
print("third_quarter_grade", third_quarter_grade)
print("fourth_quarter_grade", fourth_quarter_grade)
print("final average", ave)