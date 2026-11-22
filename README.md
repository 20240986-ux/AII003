# AII003
AII003 Student Class Diagram Homework 20240986


classDiagram
    class Student {
        -String studentNo
        -String name
        -String major
        -int year
        -double cgpa
        -List~String~ courses
        +Student(studentNo, name, major, year)
        +addCourse(courseCode) void
        +removeCourse(courseCode) void
        +setCgpa(newCgpa) void
        +checkDeanList() boolean
        +printSummary() void
    }
