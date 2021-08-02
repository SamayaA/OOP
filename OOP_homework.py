
def average_grade (person) :
    count_grades = 0
    sum_of_grades = 0
    for course_grades in person.grades.values():
        count_grades += len(course_grades)
        sum_of_grades += sum(course_grades)
    return round(sum_of_grades / count_grades , 2)

def average_course_grade (students_list , course):
    sum_grades = 0
    count_grades = 0
    for num in range(0, len(students_list)) :
        sum_grades += sum(students_list[num].grades[course])
        count_grades += len(students_list[num].grades[course])
    return round(sum_grades / count_grades , 2)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) :
        output = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade(self)}\nКурсы в процессе изучения: {",".join(map(str,self.courses_in_progress))}\nЗавершенные курсы:{",".join(map(str , self.finished_courses))}'
        return output
    
    def __lt__ (self , other) :
        return average_grade(self) < average_grade(other)

    def __gt__ (self , other) :
        return average_grade(self) > average_grade(other)
    
    def __eq__ (self , other) :
        return average_grade(self) == average_grade(other)

    def __ne__ (self , other) :
        return average_grade(self) != average_grade(other)
    
    def __le__ (self , other) :
        return average_grade(self) <= average_grade(other)

    def __ge__ (self , other) :
        return average_grade(self) >= average_grade(other)
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self) :
        output = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {average_grade(self)}'
        return output

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) :
        output = f'\nИмя: {self.name}\nФамилия: {self.surname}'
        return output
        
    def __lt__ (self , other) :
        return average_grade(self) < average_grade(other)

    def __gt__ (self , other) :
        return average_grade(self) > average_grade(other)
    
    def __eq__ (self , other) :
        return average_grade(self) == average_grade(other)

    def __ne__ (self , other) :
        return average_grade(self) != average_grade(other)
    
    def __le__ (self , other) :
        return average_grade(self) <= average_grade(other)

    def __ge__ (self , other) :
        return average_grade(self) >= average_grade(other)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_2 = Student('Ayu', 'Oham', 'your_gender')
student_2.courses_in_progress += ['Python']

reviewer_1 = Reviewer('Some', 'Reviewer')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Another', 'Reviewer')
reviewer_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Some', 'Lecturer')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Another', 'Lecturer')
lecturer_2.courses_attached += ['Python']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

course = 'Python'
students_list = [student_1, student_2]
lecturer_list = [lecturer_1 , lecturer_2]

print(f'Средняя оценка у студентов за курс {course} равна {average_course_grade(students_list , course)}')
print(f'Средняя оценка у лекторов за курс {course} равна {average_course_grade(lecturer_list, course)}')