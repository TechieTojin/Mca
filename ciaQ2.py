class EducationalResource:
    def __init__(self, title):
        self.title = title
    
    def GetCourseDetails(self):
        pass

class Course(EducationalResource):
    def __init__(self, title, instructor, credit, course_code):
        super().__init__(title)
        self.instructor = instructor
        self.credit = credit
        self.course_code = course_code
        self.enrollment_status = False

    def Enroll(self):
        if self.enrollment_status:
            print("Student is enrolled in the course before itself.")
        else:
            self.enrollment_status = True
            print("Student enrolled in course")

    def DropCourse(self):
        if not self.enrollment_status:
            print("Student is not enrolled in the course.")
        else:
            self.enrollment_status = False
            print("Student dropped the course")

    def GetCourseDetails(self):
        details = ("Course Title: " + self.title + "\n" +"Instructor: " + self.instructor + "\n" +"Credits: " + str(self.credit) + "\n" +"Course Code: " + self.course_code)
        print(details)

    def AddToCurriculum(self):
        print("Course added to curriculum: " + self.title + ".")


courseA = Course("Basics Of Python", "ABC", 3, "MCA121")
courseB = Course("NumPy", "DEF", 4, "MCA122")

courseA.Enroll()
courseA.DropCourse()
courseA.GetCourseDetails()  
courseA.AddToCurriculum() 


courseB.Enroll()  
courseB.GetCourseDetails() 
courseB.AddToCurriculum()
