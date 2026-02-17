2.Write a Python script that analyzes a text file containing student grades and generates a comprehensive report. (7 marks)
Input CSV Format:
csv
StudentID,Name,Math,Physics,Chemistry,Biology
S001,Alice Johnson,85,90,88,92
S002,Bob Smith,78,82,75,80
S003,Carol White,92,88,95,90
S004,David Brown,70,68,72,75
Requirements:
Read the CSV file
Create a class Student to store each student's information
Calculate individual student averages
Generate a report showing:
oTotal number of students
oClass average for each subject
oOverall class average
oTop 3 students by overall average
oStudents who scored above 90 in any subject
oSubject-wise highest and lowest scores
Handle file not found exceptions
Write formatted output to a text file
"""

from statistics import mean
class Student:
    def __init__(self, student_id, name, math, physics, chemistry, biology):
        self.student_id = student_id
        self.name = name
        self.math = int(math)
        self.physics = int(physics)
        self.chemistry = int(chemistry)
        self.biology = int(biology)

    def average(self):
        return (self.math + self.physics + self.chemistry + self.biology) / 4

def generate_report(input_file, output_file):
    students = []
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split(",")
                students.append(Student(*data))
    except FileNotFoundError:
        print("File not found")
        return

    if not students:
        print("No student data found.")
        return

    total_students = len(students)

    avg_math = mean([i.math for i in students])
    avg_physics = mean([i.physics for i in students])
    avg_chemistry = mean([i.chemistry for i in students])
    avg_biology = mean([i.biology for i in students])

    overall_avg = mean([i.average() for i in students])

    top_3 = sorted(students, key=lambda i: i.average(), reverse=True)[:3]

    above_90 = [i for i in students if any(score > 90 for score in [i.math, i.physics, i.chemistry, i.biology])]

    subjects = {
        "Math": [i.math for i in students],
        "Physics": [i.physics for i in students],
        "Chemistry": [i.chemistry for i in students],
        "Biology": [i.biology for i in students]
    }

    with open(output_file, "w") as f:
        f.write("STUDENT REPORT\n")
        f.write(f"Total Students: {total_students}\n\n")

        f.write("Class Average Per Subject:\n")
        for sub, scores in subjects.items():
            f.write(f"{sub}: {mean(scores):.2f}\n")
        f.write(f"\nOverall Class Average: {overall_avg:.2f}\n\n")

        f.write("Top 3 Students:\n")
        for s in top_3:
            f.write(f"{s.name} ({s.student_id}) - Avg: {s.average():.2f}\n")
        f.write("\nStudents scoring above 90 in any subject:\n")
        for s in above_90:
            f.write(f"{s.name} ({s.student_id})\n")
        f.write("\nSubject-wise Highest and Lowest Scores:\n")
        for sub, scores in subjects.items():
            f.write(f"{sub} -> Highest: {max(scores)}, Lowest: {min(scores)}\n")

    print("Report generated successfully!")

generate_report("students.txt", "report.txt")
