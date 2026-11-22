# AII003
AII003 Student Class Diagram Homework 20240986

## Student Class Diagram
This diagram represents the `Student` class structure and corresponds to the implementation in `student.py`.

```mermaid
classDiagram
    class Student {
        -String studentNo
        -String name
        -String dept
        -int term
        -double gpa
        -List~String~ courses
        +Student(studentNo, name, dept, term)
        +enrollCourse(courseCode) void
        +removeCourse(courseCode) void
        +setGpa(gpa) void
        +isHonor() boolean
        +printProfile() void
    }
