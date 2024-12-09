import pickle


class Course_grades:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grade = []

    def create_course_grades():
        course_name = input("Enter the course name: ")
        stu_ID = input("Enter the student's ID: ")
        stu_grade = input("Enter the student's grade: ")

        return Course_grades(course_name, stu_ID, stu_grade)


with open("grades_info.dat", "ab") as file:


with open("grades_info.dat", "rb") as file:

    while 1:
        try:
            course = pickle.load(file)
            print(course)
        except EOFError:
            break
