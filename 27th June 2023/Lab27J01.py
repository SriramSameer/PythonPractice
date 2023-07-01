# Class and Object
# Data Members - name, age, id, course_enrollment
# Methods - read(), attend_class(), parctice(), doQuiz, doAssignment()

class PyATBStudents:
    # Data Members
    name = None
    age = None
    gender = None
    course_name = None
    email = None

    # Methods
    def do_quiz(self):
        print("Do Something")

    def do_assignment(self):
        print("Do Something")


student1 = PyATBStudents()
student1.do_quiz()