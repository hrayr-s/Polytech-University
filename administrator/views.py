from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from administrator import forms
from university.models import Student, Group


class home(generic.TemplateView):
    template_name = 'administrator/admin.html'
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('administration:list-students'))

class Students(generic.TemplateView):
    template_name = 'administrator/student/index.html'

    def get_context_data(self, **kwargs):
        context = super(Students, self).get_context_data(**kwargs)
        students = Student.objects.all()
        request = self.request
        page = 1
        if 'page' in self.kwargs:
            page = self.kwargs['page'] or 1
            if 'students' in request.session:
                request.session['students']['page'] = page
            else:
                request.session['students'] = {}
                request.session['students']['page'] = page
        elif 'students' in request.session:
            if page in request.session.get('students'):
                page = request.session.get('students')['page']

        paginator = Paginator(students, 12)
        try:
            studentlist = paginator.page(page)
        except PageNotAnInteger:
            studentlist = paginator.page(1)
        except EmptyPage:
            studentlist = paginator.page(paginator.num_pages)

        context['students'] = studentlist
        return context

    @staticmethod
    def add(request):
        form = forms.addStudent(request.POST or None)
        groups = Group.objects.all()
        if request.method =="POST" and form.is_valid():
            form.save()

        context = {}
        context['form'] = form
        context['groups'] = groups

        return render(request, 'administrator/student/add.html', context)

