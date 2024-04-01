class Job:
    type = None
    salary = None
    hourWorked = None

    def __init__(self, type, salary, hourWorked):
        self.type = type
        self.salary = salary
        self.hourWorked = hourWorked

    def display(self):
        print(
            f"Job type: {self.type}\nSalary: {self.salary}\nHours worked: {self.hourWorked}"
        )


class Teacher(Job):
    subject = None
    position = None

    def __init__(self, subject, position):
        self.type = "Teacher"
        self.salary = "$ Nowhere near enough"
        self.hourWorked = "All of them"
        self.subject = subject
        self.position = position

    def display(self):
        print(
            f"Job type: {self.type}\nSalary: {self.salary}\nHours worked: {self.hourWorked}\nSubject: {self.subject}\nPosition: {self.position}"
        )


class Doctor(Job):
    Speciality = None
    experience = None

    def __init__(self, speciality, experience):
        self.type = "Doctor"
        self.salary = "$ Doing very nicely thank you"
        self.hourWorked = "50"
        self.speciality = speciality
        self.experience = experience

    def display(self):
        print(
            f"Job type: {self.type}\nSalary: {self.salary}\nHours worked: {self.hourWorked}\nSpeciality: {self.speciality}\nYears of Experience: {self.experience}"
        )


print("🌟Jobs Jobs Jobs!🌟\n")
lawyer = Job(type="Lawyer", salary="$ Squillions", hourWorked=68)
lawyer.display()

print()
teacher = Teacher(subject="Computer Science", position="Classroom Teacher")
teacher.display()

print()
doctor = Doctor(speciality="Pediatric Consultant", experience="7")
doctor.display()
