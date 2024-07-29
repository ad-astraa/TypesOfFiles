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

def calculate_overall_scores(self):
        students = self.read_all_students()
        for student in students:
            grades = list(map(int, student[3:]))  # Assuming grades are from the fourth column onwards
            overall_score = sum(grades) / len(grades) if grades else 0
            print(f"Student ID: {student[0]}, Name: {student[1]}, Overall Score: {overall_score:.2f}")

    def display_students(self):
        students = self.read_all_students()
        for student in students:
            print(student)

def main():
    filename = 'gradebook.csv'
    gradebook = Gradebook(filename)

    while True:
        print("\nGradebook System")
        print("1. Add Student")
        print("2. Update Grades")
        print("3. Calculate Overall Scores")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            student_data = input("Enter student details (ID, Name, Class, Grades...): ").split(',')
            gradebook.add_student(student_data)
        elif choice == '2':
            student_id = input("Enter student ID to update grades: ")
            new_grades = input("Enter new grades (comma-separated): ").split(',')
            gradebook.update_grades(student_id, new_grades)
        elif choice == '3':
            gradebook.calculate_overall_scores()
        elif choice == '4':
            gradebook.display_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

