student = {
    "name": "fredo",
    "academic_year": "senior",
    "units": [
        {
            "name": "Web Development",
            "credits": 3,
            "grade": "A"
        },
        {
            "name": "Network and System Administration",
            "credits": 3,
            "grade": "B"
        },
        {
            "name": "Java",
            "credits": 3,
            "grade": "C"
        }
    ]
}

# Create a grade weight mapping dictionary
grade_weight_mapping = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "E": 0
}

# Calculate total credits and weighted sum of grade points
total_credits = sum(course["credits"] for course in student["units"])
weighted_sum = sum(grade_weight_mapping[course["grade"]] * course["credits"] for course in student["units"])

# Calculate GPA
if total_credits > 0:
    gpa = weighted_sum / total_credits
else:
    gpa = 0  # To handle division by zero

# Add total_credits and GPA to the student dictionary
student["total_credits"] = total_credits
student["GPA"] = gpa

# Access and print the updated student dictionary
print("Student Information:")
print("Name:", student["name"])
print("Academic Year:", student["academic_year"])
print("Total Credits:", student["total_credits"])
print("GPA:", student["GPA"])
