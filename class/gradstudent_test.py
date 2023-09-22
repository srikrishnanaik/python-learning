#!/usr/bin/env python3
from gradstudent import GradStudent

def main():
    grad_student = GradStudent("James", "Anthropology", 25000)
    print("     Major:", grad_student.major)
    print("     Name:", grad_student.name)
    print("Stipend:", grad_student.stipend)
    print(grad_student)

if __name__ == "__main__":
    main()