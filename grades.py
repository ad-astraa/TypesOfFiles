import csv

class Gradebook:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self, student_data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(student_data)
        print(f"Student {student_data[1]} added successfully!")

    def update_grades(self, student_id, new_grades):
        students = self.read_all_students()
        found = False
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for student in students:
                if student[0] == student_id:
                    student[3:] = new_grades  # Assuming grades start from the fourth column
                    found = True
                    print(f"Grades for student {student_id} updated successfully!")
                writer.writerow(student)
        if not found:
            print(f"Student {student_id} not found.")

    def read_all_students(self):
        students = []
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            students = list(reader)
        return students
