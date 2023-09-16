# Fonction calcul gpa par etu
def calculate_gpa(student):
    grade_weight_mapping = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "E": 0
    }

    total_credits = sum(course["credits"] for course in student["units"])
    weighted_sum = sum(grade_weight_mapping[course["grade"]] * course["credits"] for course in student["units"])

    if total_credits > 0:
        return weighted_sum / total_credits
    else:
        return 0

student1 = {
    "name": "John Doe",
    "academic_year": "Sophomore",
    "units": [
        {"name": "Web Development", "credits": 3, "grade": "A"},
        {"name": "Network and System Administration", "credits": 3, "grade": "B"},
        {"name": "Java", "credits": 3, "grade": "C"}
    ]
}

student2 = {
    "name": "Alice Smith",
    "academic_year": "Freshman",
    "units": [
        {"name": "Python Programming", "credits": 3, "grade": "A"},
        {"name": "Data Structures", "credits": 3, "grade": "A"},
        {"name": "Statistics", "credits": 3, "grade": "B"}
    ]
}

student3 = {
    "name": "Bob Johnson",
    "academic_year": "Junior",
    "units": [
        {"name": "Machine Learning", "credits": 3, "grade": "A"},
        {"name": "Database Management", "credits": 3, "grade": "B"},
        {"name": "Software Engineering", "credits": 3, "grade": "C"}
    ]
}

# creation array pour stocker les etudiants
students_array = [student1, student2, student3]

# Sort array par nom alpha des etudiants
sorted_by_name = sorted(students_array, key=lambda x: x["name"])

# Sort array par Gpa ascendant
sorted_by_gpa_asc = sorted(students_array, key=calculate_gpa)

# Sort array par Gpa descendant 
sorted_by_gpa_desc = sorted(students_array, key=calculate_gpa, reverse=True)

# Print sorted lists
print("Students sorted by name (alphabetical order):")
for student in sorted_by_name:
    print("Name:", student["name"])

print("\nStudents sorted by GPA (ascending order):")
for student in sorted_by_gpa_asc:
    print("Name:", student["name"], "| GPA:", calculate_gpa(student))

print("\nStudents sorted by GPA (descending order):")
for student in sorted_by_gpa_desc:
    print("Name:", student["name"], "| GPA:", calculate_gpa(student))
