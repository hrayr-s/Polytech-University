import json

from django.http import HttpResponse

from university.models import Department, Exam, Faculty, Group, AbsenceLog, Points, Profession, Staff, Student, Subject, \
    Deferral


def delete(request, **kwargs):
    items = []
    model = None
    if 'id' in kwargs:
        id = kwargs['id']
        items.append(id)
    if request.method == 'POST':
        items = request.POST.getlist('items[]')
        print(request.POST)
    if 'model' in kwargs:
        if kwargs['model'] == 'ամբիոն':
            model = Department
        elif kwargs['model'] == 'քննություններ':
            model = Exam
        elif kwargs['model'] == 'ֆակուլտետ':
            model = Faculty
        elif kwargs['model'] == 'խումբ':
            model = Group
        elif kwargs['model'] == 'մատյան':
            model = AbsenceLog
        elif kwargs['model'] == 'գնահատական':
            model = Points
        elif kwargs['model'] == 'մասնագիտություն':
            model = Profession
        elif kwargs['model'] == 'աշխատակազմ':
            model = Staff
        elif kwargs['model'] == 'ուսանողներ':
            model = Student
        elif kwargs['model'] == 'առարկաներ':
            model = Subject
        elif kwargs['model'] == 'տարեկետում':
            model = Deferral
        else:
            model = None
    try:
        model.objects.filter(id__in=items).delete()
        errors = "Success"
    except:
        errors = "Can't delete Items"
    return HttpResponse(json.dumps({'errors':errors}), content_type='application/json')