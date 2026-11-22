# AII003
AII003 Student Class Diagram Homework 20240986



```mermaid
classDiagram
    class Student {
        -String studentId
        -String fullName
        -String department
        -int semester
        -double gpa
        -List~String~ enrolledCourses
        +Student(studentId, fullName, department, semester)
        +registerCourse(courseCode) void
        +dropCourse(courseCode) void
        +updateGpa(newGpa) void
        +isHonorStudent() boolean
        +getStudentProfile() void
    }
