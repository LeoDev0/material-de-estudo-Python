class Student:

  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_name(self):
    return self.name

  def get_grade(self):
    return self.grade

class Course:
  
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False

  def get_average_grade(self):
    grades = []
    for student in self.students:
      grades.append(student.get_grade())

    return sum(grades) / len(grades)



s1 = Student('Leo', 26, 98)
s2 = Student('John', 19, 88)
s3 = Student('Mike', 20, 67)

c1 = Course('Computer Science', 2)
c1.add_student(s1)
c1.add_student(s2)

print(c1.get_average_grade())
