class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return self._mid_grade() < other_student._mid_grade()

    def rate_Lecturer(self, lecturer, course, grade):
        marks = [0,1,2,3,4,5,6,7,8,9,10]
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade in marks:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 
        
    def _mid_grade(self):
        list_grad = []
        for grad in self.grades.values():
            for num in grad:
                list_grad.append(num)
        avg = sum(list_grad)/len(list_grad)
        return avg
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._mid_grade()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"       
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self._mid_grade() < other_lecturer._mid_grade()
    
    def _mid_grade(self):
        list_grad = []
        for grad in self.grades.values():
            for num in grad:
                list_grad.append(num)
        avg = sum(list_grad)/len(list_grad)
        return avg
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._mid_grade()}"

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        marks = [0,1,2,3,4,5,6,7,8,9,10]
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade in marks:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
    
# Проверяющие дз
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git', 'Введение в программирование']
# Студенты
some_student = Student('Ruoy', 'Eman', 'your_gender')
student_1 = Student('Ivan', 'Dav', 'm')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
# Лекторы
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git', 'Введение в программирование']
lecturer_1 = Lecturer('Stepan', 'Kot')
lecturer_1.courses_attached += ['Python', 'Git', 'Введение в программирование']
# Действия
some_student.rate_Lecturer(lecturer_1, 'Python', 7)
some_student.rate_Lecturer(lecturer_1, 'Git', 7)
some_student.rate_Lecturer(lecturer_1, 'Python', 7)
lecturer_1._mid_grade()

some_student.rate_Lecturer(some_lecturer, 'Python', 10)
some_student.rate_Lecturer(some_lecturer, 'Git', 7)
some_student.rate_Lecturer(some_lecturer, 'Python', 10)
some_lecturer._mid_grade()

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 7)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_student._mid_grade()

some_reviewer.rate_hw(student_1, 'Python', 7)
some_reviewer.rate_hw(student_1, 'Git', 7)
some_reviewer.rate_hw(student_1, 'Python', 7)
student_1._mid_grade()
# Выводы по дз
print(some_reviewer)
print()
print(some_lecturer)
print()
print(lecturer_1)
print()
print(some_student)
print()
print(student_1)
print()
print(some_student < student_1)
print(lecturer_1 < some_lecturer)

list_student = [some_student, student_1]

def mid_grade_students(stud, cour):
  for student in stud:
    if cour in student.grades:
      list_grade = student.grades[cour]
      mid = sum(list_grade)/len(list_grade)
      return mid
  
print(mid_grade_students(list_student, 'Python'))

list_lecturer = [some_lecturer, lecturer_1]

def mid_grade_lecturers(lect, cour):
  for lecturer in lect:
    if cour in lecturer.grades:
      list_grade = lecturer.grades[cour]
      mid = sum(list_grade)/len(list_grade)
      return mid
  
print(mid_grade_lecturers(list_lecturer, 'Git'))