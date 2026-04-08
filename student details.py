
student_name=input("enter student name: ")
DOB=input("enter date of birth: ")
reg_no=(input("enter reg no: "))
department=input("enter department: ")
marks= {
"maths":int(input("enter maths marks: ")),
 "english":int(input("enter english marks: ")),
 "science":int(input("enter science marks: ")),
 "social":int(input("enter social marks: ")),
 "physical_education":int(input("enter physical education marks: "))
}
total_marks=marks["maths"]+marks["english"]+marks["science"]+marks["social"]+marks["physical_education"]
print("----student_details-----")
print("student name: ", student_name)
print("DOB: ", DOB)     
print("reg no: ", reg_no)
print("department: ", department)
print("marks: ", marks)
print("total marks: ", total_marks)

    

