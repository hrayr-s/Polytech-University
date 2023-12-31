from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from administrator.forms import PointsForm
from university.models import Group, Student, Points, PointType, Exam


@method_decorator(login_required, name='dispatch')
class Add(generic.FormView):
    template_name = 'administrator/points/add.html'
    model = Points
    form_class = PointsForm
    success_url = reverse_lazy('administration:add-point')

    def get_context_data(self, **kwargs):
        context = super(Add, self).get_context_data(**kwargs)
        groups = Group.objects.filter()
        students = Student.objects.all()
        types = PointType.objects.all()
        exams = Exam.objects.all()

        context['groups'] = groups
        context['students'] = students
        context['types'] = types
        context['exams'] = exams
        return context

    def form_valid(self, form):
        form.save()
        return super(Add, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class Edit(generic.UpdateView):
    template_name = 'administrator/points/edit.html'
    model = Points
    form_class = PointsForm

    def get_context_data(self, **kwargs):
        context = super(Edit, self).get_context_data(**kwargs)
        points = self.model.objects.get(id=self.kwargs['pk'])
        groups = Group.objects.filter()
        students = Student.objects.all()
        types = PointType.objects.all()
        exams = Exam.objects.all()

        context['points'] = points
        context['groups'] = groups
        context['students'] = students
        context['types'] = types
        context['exams'] = exams
        return context

    def get(self, request, *args, **kwargs):
        super(Edit, self).get(request, *args, **kwargs)
        form = self.form_class(instance=self.object)
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form))

    @method_decorator(login_required, name='dispatch')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST or None, instance=self.object)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Գնահատականը հաջողությամբ Խմբագրվել է։')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self.request, 'Սխալ! ' + str(form.errors))
            return self.render_to_response(
                self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('administration:edit-point', kwargs={'pk': int(self.kwargs['pk'])})


class List(generic.TemplateView):
    template_name = 'administrator/points/index.html'

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        points = Points.objects.all()
        request = self.request
        page = 1
        if 'page' in self.kwargs:
            page = self.kwargs['page'] or 1
            if 'points' in request.session:
                request.session['points']['page'] = page
            else:
                request.session['points'] = {}
                request.session['points']['page'] = page
        elif 'points' in request.session:
            if page in request.session.get('points'):
                page = request.session.get('points')['page']

        paginator = Paginator(points, 12)
        try:
            points = paginator.page(page)
        except PageNotAnInteger:
            points = paginator.page(1)
        except EmptyPage:
            points = paginator.page(paginator.num_pages)

        context['points'] = points
        context['paginator'] = points
        return context
