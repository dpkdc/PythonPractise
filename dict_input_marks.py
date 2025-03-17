student={}

mark1=int(input("enter maths marks:"))
mark2=int(input("enter english marks:"))
mark3=int(input("enter hindi marks:"))

student.update({"maths":mark1})
student.update({"english":mark2})
student.update({"hindi":mark3})

print(student)
print(student["english"])