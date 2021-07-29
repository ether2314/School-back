from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
sex_choie = (
    ('male', 'male'),
    ('female', 'female')
)

state_choice = (
    ('enugu', 'enugu'),
    ('Anambra', 'Anambra'),
    ('Kano', 'Kano'),
    ('Imo', 'Imo'),
    ('Bauchi', 'Bauchi'),
    ('Kastina', 'Kastina'),
    ('Abuja', 'Abuja'),
)
time_slots = (
    ('8:00 - 10:00', '8:00 - 10:00'),
    ('8:00 - 9:00', '8:00 - 9:00'),
    ('9:00 - 10:00', '9:00 - 9:00'),
    ('9:00 - 11:00', '9:00 - 11:00'),
    ('10:00 - 11:00', '10:00 - 11:00'),
    ('10:00 - 12:00', '10:00 - 12:00'),
    ('11:00 - 12:00', '11:00 - 12:00'),
    ('12:00 - 13:00', '12:00 - 13:00'),
    ('13:00 - 14:00', '13:00 - 14:00'),
    ('13:00 - 15:00', '13:00 - 15:00'),
    ('14:00 - 15:00', '14:00 - 15:00'),
    ('14:00 - 16:00', '14:00 - 16:00'),
    ('15:00 - 16:00', '15:00 - 16:00'),
    ('15:00 - 17:00', '16:00 - 17:00'),
    ('16:00 - 17:00', '16:00 - 17:00'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)
ClassLevel = (
    ('First Year', 'First Year'),
    ('Second Year', 'Second Year'),
    ('Third Year', 'Third Year'),
    ('Fourth Year', 'Fourth Year'),
    ('Fifth Year', 'Fifth Year'),
    ('Final Year', 'Final Year')
)

classlvl = (
    ('100lvl', '100lvl'),
    ('200lvl', '200lvl'),
    ('300lvl', '300lvl'),
    ('400lvl', '400lvl'),
    ('500lvl', '500lvl')
)


class Faculty(models.Model):
    id = models.CharField(primary_key='True', max_length=6)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.CharField(primary_key='True', max_length=6)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    Date_of_Birth = models.DateField(blank=False, help_text='yy-mm-dd')
    phone_no = models.DecimalField(max_digits=11, decimal_places=0)
    sex = models.CharField(max_length=10, choices=sex_choie)
    state = models.CharField(max_length=50, choices=state_choice)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    Date_of_Birth = models.DateField(blank=False, help_text='yy-mm-dd')
    phone_no = models.DecimalField(max_digits=11, decimal_places=0)
    sex = models.CharField(max_length=10, choices=sex_choie)
    state = models.CharField(max_length=50, choices=state_choice)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=6, help_text='department_name(EE),Faculty(E)XXX')
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=4)
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)

    def __str__(self):
        return self.name


class StuClass(models.Model):
    id = models.CharField(primary_key='True', choices=classlvl, max_length=6, blank=False)

    def __str__(self):
        return self.id


class Studlevel(models.Model):
    id = models.CharField(primary_key='True', choices=ClassLevel, max_length=12, unique=False, blank=False)

    def __str__(self):
        return self.id


class TimeTable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_level = models.ForeignKey(StuClass, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'class_level', 'dept', 'teacher'))

    def __str__(self):
        dept = Department.objects.get(id=self.dept_id)
        cr = Course.objects.get(id=self.course_id)
        le = Lecturer.objects.get(id=self.teacher_id)
        cl = StuClass.objects.get(id=self.class_level_id)

        return '%s : %s : %s : %s' % (le.name, cr.short_name, dept.name, cl)


class Time_Table(models.Model):
    names = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    time_table = models.CharField(max_length=30, choices=time_slots, blank=False)
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, blank=False)
