
def average_grade (person) :
    count_grades =0
    sum_of_grades = 0
    for course_grades in person.grades.values():
        count_grades += len(course_grades)
        for grade in course_grades :
            sum_of_grades += grade
    return round(sum_of_grades / count_grades , 2)

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
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

lecturer_1 = Lecturer('Another', 'Buddy')
lecturer_1.courses_attached += ['Python']
 
best_student.rate_lecturer(lecturer_1, 'Python', 10)
best_student.rate_lecturer(lecturer_1, 'Python', 10)
best_student.rate_lecturer(lecturer_1, 'Python', 9)

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 10)
