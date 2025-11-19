print("---------------------------------------")
print("****welcome to our aplication****")
print("please enter your information below")
print("---------------------------------------")

student_name=input("enter your name: ")
student_surname=input("enter your surname: ")
student_birthyear=int(input("birthyear: "))
student_school=input("enter your school name: ")
student_id=input("enter your ID number: ")
student_field=input("enter your field of study: ")
student_gender=input("your gender: ")
ac_year=int(input("enter your academic year: "))
parent_name=input("enter one parent name: ")
parent_number=int(input("enter parent phone number: "))
start_year=int(input("enter your start year: "))
student_size=float(input("enter your size: "))
print("thank you for your information!")

student_age = 2025 - student_birthyear
delivrement_year = ac_year
expiration_year = delivrement_year + 1
finiss_year = start_year + 3

valide=True
mesage_valide="your student card is valide"
mesage_not_valide="your student card is not valide"
carte=mesage_valide 

print("--------------------------------------------------")
print(f"**********{student_school} Student Card**********")
print("--------------------------------------------------")
print(f"Name: {student_name}")
print(f"Surname: {student_surname} ")
print(f"Age: {student_age} ")
print(f"size:{student_size} m")
print(f"Field of Study: {student_field} ")
print(f"ID Number: {student_id}")   
print(f"Gender: {student_gender} ")
print(f"Academic Year: {ac_year} ")
print(f"Parent Name: {parent_name} ")   
print(f"Parent Phone Number: {parent_number} ")
print(f"Delivrement Year: {delivrement_year} ")
print(f"Expiration Year: {expiration_year} ")
print(f"Start Year: {start_year} ")
print(f"Finiss Year: {finiss_year} ")
print(f"Card Status: {carte} ")
print("--------------------------------------------------")

