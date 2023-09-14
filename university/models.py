from django.db import models

from MediaManagement.models import Image


class Student(models.Model):
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=72)
    surname = models.CharField(max_length=36)
    group = models.ForeignKey('university.Group', on_delete=models.DO_NOTHING)
    birthday = models.DateField(blank=True, null=True)
    joined = models.DateField()
    email = models.CharField(max_length=255, blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.DO_NOTHING)
    state_order = models.BooleanField(default=False)
    tuition_fee = models.IntegerField(default=0)
    phone = models.IntegerField()

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.surname


class Group(models.Model):
    name = models.CharField(max_length=10)
    profession = models.ForeignKey('university.Profession', on_delete=models.DO_NOTHING)
    created = models.DateField(verbose_name='Ստեղծման Տարի')
    lecturers = models.ManyToManyField('university.Staff')

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey('university.Faculty', on_delete=models.DO_NOTHING)
    years = models.IntegerField()
    remote = models.BooleanField(default=False, blank=True, verbose_name='հեռակա')
    subjects = models.ManyToManyField('university.Subject')

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=150)
    shortname = models.CharField(max_length=10)
    dean = models.OneToOneField('university.Staff', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Staff(models.Model):
    fullname = models.CharField(max_length=25)
    works_since = models.DateField(blank=True, null=True)
    type = models.ForeignKey('WorkerType', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'worker'
        verbose_name_plural = 'Workers'


class WorkerType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    lecturers = models.ManyToManyField('university.Staff')
    course = models.IntegerField()  # Semestr
    lessons = models.IntegerField(verbose_name='Սեմեստրի լեկցիաների քանակը')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=150)
    shortname = models.CharField(max_length=50)
    manager = models.OneToOneField('university.Staff', unique=True, related_name='department',
                                   on_delete=models.DO_NOTHING)
    teachers = models.ManyToManyField('university.Staff', related_name='departments')

    def __str__(self):
        return self.name


class AbsenceLog(models.Model):
    student = models.ForeignKey('university.Student', on_delete=models.DO_NOTHING)
    group = models.ForeignKey('university.Group', on_delete=models.DO_NOTHING)
    loose = models.BooleanField(default=True)
    minute = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.student) + ' ' + str(self.minute)


class Deferral(models.Model):
    student = models.ForeignKey('university.Student', on_delete=models.DO_NOTHING)
    semester = models.IntegerField(verbose_name='Տարկետման սեմեստր')
    length = models.IntegerField(verbose_name='Ժամկետ')
    current_group = models.ManyToOneRel('self', 'group', field_name="currgroup")

    def __str__(self):
        return str(self.student) + ' - ' + str(self.semester) + ' - ' + str(self.length)


class Points(models.Model):
    value = models.FloatField()
    student = models.ForeignKey('university.Student', on_delete=models.PROTECT)
    type = models.ForeignKey('PointType', on_delete=models.DO_NOTHING)
    exam = models.ForeignKey('Exam', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.student) + " -> " + str(self.subject) + " == " + str(self.value)


class ExamType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PointType(models.Model):
    name = models.CharField(max_length=255)


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    type = models.ForeignKey(ExamType, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    lecturer = models.ForeignKey(Staff, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.type.name + ' քննություն ' + self.subject.name + ' առարկայից ' + str(self.date) + ' օրը'
