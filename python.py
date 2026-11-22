class Student:
    def __init__(self, student_no: str, name: str, dept: str, term: int):
        self.student_no = student_no
        self.name = name
        self.dept = dept
        self.term = term
        self.gpa: float = 0.0
        self.courses: list[str] = []
    def enroll_course(self, course_code: str) -> None:
        if course_code not in self.courses:
            self.courses.append(course_code)
    def remove_course(self, course_code: str) -> None:
        if course_code in self.courses:
            self.courses.remove(course_code)
    def set_gpa(self, gpa: float) -> None:
        self.gpa = gpa
    def is_honor(self) -> bool:
        return self.gpa >= 3.5
    def print_profile(self) -> None:
        print(f"{self.student_no} | {self.name} | {self.dept} | Term {self.term} | GPA: {self.gpa} | Honor: {self.is_honor()} | Courses: {self.courses}")
if __name__ == "__main__":
    s = Student("20240986", "Ali Veli", "AI", 1)
    s.enroll_course("AI1003")
    s.set_gpa(3.65)
    s.print_profile()
