keys = ["name", "Roll No", "Maths", "Physics", "Urdu", "English", "Computer"]
students = []  

def get_valid_marks(subject):
    """Function to get valid marks between 0 and 100"""
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def calculate_percentage_and_grade(student):
    """Function to calculate percentage and grade"""
    subjects = ["Maths", "Physics", "Urdu", "English", "Computer"]
    total_marks = sum(student[subject] for subject in subjects)
    percentage = total_marks / len(subjects)

    
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"  
    student["Total Marks"] = total_marks
    student["Percentage"] = f"{percentage:.2f}%"
    student["Grade"] = grade

while True:
    student = {}  
    for key in keys:
        if key in ["Maths", "Physics", "Urdu", "English", "Computer"]:  
            student[key] = get_valid_marks(key) 
        else:
            student[key] = input(f"Enter {key}: ")  

    calculate_percentage_and_grade(student)  
    students.append(student)  

    choice = input("Do you want to add more students? (Y/N): ").strip().upper()
    if choice != "Y":
        break  

print("\n📌 Student Data:")
for i, student in enumerate(students, start=1):
    print(f"\n🎓 Student {i}:")
    for key, value in student.items():
        print(f"  {key}: {value}")
