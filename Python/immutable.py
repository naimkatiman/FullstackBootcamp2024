from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    student_id: int
    name: str
    age: int
    major: str

# Example of creating an instance of Student
student_1 = Student(student_id=123, name="Alice", age=20, major="Computer Science")

# Trying to change the name attribute will raise an error
# student_1.name = "Bob"  # This line would raise a dataclass.FrozenInstanceError if uncommented

print(student_1)
