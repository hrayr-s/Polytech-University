from django.urls import re_path as url, include

from administrator import function
from administrator.viewpy import Ambion, Fakultet, Group, Matyan, Points, Profession, Staff, Subject, Student, Exam
from administrator.views import Home

app_name = 'administrator'

urlpatterns = [
    url(r'^$', Home.as_view(), name='adminHome'),
    url(r'^ամբիոն/', include([
        url(r'^ավելացնել$', Ambion.Add.as_view(), name="add-ambion"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Ambion.Edit.as_view(), name="edit-ambion"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Ambion.List.as_view(), name="list-ambions"),
    ])),
    url(r'^ֆակուլտետ/', include([
        url(r'^ավելացնել$', Fakultet.Add.as_view(), name="add-faculty"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Fakultet.Edit.as_view(), name="edit-faculty"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Fakultet.List.as_view(), name="list-faculties"),
    ])),
    url(r'^խումբ/', include([
        url(r'^ավելացնել$', Group.Add.as_view(), name="add-group"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Group.Edit.as_view(), name="edit-group"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Group.List.as_view(), name="list-groups"),
    ])),
    url(r'^մատյան/', include([
        url(r'^ավելացնել$', Matyan.Add.as_view(), name="add-matyan"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Matyan.Edit.as_view(), name="edit-matyan"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Matyan.List.as_view(), name="list-matyans"),
    ])),
    url(r'^գնահատական/', include([
        url(r'^ավելացնել$', Points.Add.as_view(), name="add-point"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Points.Edit.as_view(), name="edit-point"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Points.List.as_view(), name="list-points"),
    ])),
    url(r'^մասնագիտություն/', include([
        url(r'^ավելացնել$', Profession.Add.as_view(), name="add-profession"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Profession.Edit.as_view(), name="edit-profession"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Profession.List.as_view(), name="list-professions"),
    ])),
    url(r'^աշխատակազմ/', include([
        url(r'^ավելացնել$', Staff.Add.as_view(), name="add-worker"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Staff.Edit.as_view(), name="edit-worker"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Staff.List.as_view(), name="list-staff"),
    ])),
    url(r'^առարկաներ/', include([
        url(r'^ավելացնել$', Subject.Add.as_view(), name="add-subject"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Subject.Edit.as_view(), name="edit-subject"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Subject.List.as_view(), name="list-subjects"),
    ])),
    url(r'^ուսանողներ/', include([
        url(r'^ավելացնել$', Student.Add.as_view(), name="add-student"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Student.Edit.as_view(), name="edit-student"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Student.List.as_view(), name="list-students"),
    ])),
    url(r'^տարեկետում/', include([
        url(r'^ավելացնել$', Subject.Add.as_view(), name="add-tareketum"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Subject.Edit.as_view(), name="edit-tareketum"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Subject.List.as_view(), name="list-tareketum"),
    ])),
    url(r'^քննություններ/', include([
        url(r'^ավելացնել$', Exam.Add.as_view(), name="add-exam"),
        url(r'^(?P<pk>[0-9]+)/խմբագրել$', Exam.Edit.as_view(), name="edit-exam"),
        url(r'^(?:/ցուցակ)?(?:/page-(?P<page>[0-9]+))?$', Exam.List.as_view(), name="list-exams"),
    ])),

    url(r'^(?P<model>.*)/ջնջել/(?P<id>[0-9]+)$', function.delete, name='delete-item-single'),
    url(r'^(?P<model>.*)/ջնջել$', function.delete, name='delete-items'),
]
