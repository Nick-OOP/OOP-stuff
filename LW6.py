import pickle

class Course_grades:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grade = []

    def create_course_grade(self):
        self.course_name = input("Enter the course name: ")
        self.stu_ID = input("Enter the IDs of the students in this course (seperated only by a comma): ").split(',')
        self.stu_grade = input("Enter the grades of the students in this course (seperated only by a comma): ").split(',')

while 1:
    print("-----------------------------------------------")
    print("1. Create a course and dump to file")
    print("2. Open file and print file content in window")
    print("3. Exit")
    print("-----------------------------------------------")
    x = input("Enter your choice: ")

    if x == "1":
        with open("grades_info.dat", "ab") as file:
            grade = Course_grades()
            grade.create_course_grade()
            pickle.dump(grade, file)
    elif x == "2":
        with open("grades_info.dat", "rb") as file:
            while 1:
                try:
                    course = pickle.load(file)
                    print(f"Course Name: {course.course_name}, \nStudent IDs: {course.stu_ID}, \nGrades: {course.stu_grade}")
                except EOFError:
                    break
    elif x == "3":
        break
    else:
        print("Please enter a valid input")