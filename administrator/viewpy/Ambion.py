from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from administrator.forms import Department as AmbionForm
from university.models import Department, Staff


@method_decorator(login_required, name='dispatch')
class Add(generic.FormView):
    template_name = 'administrator/ambion/add.html'
    model = Department
    form_class = AmbionForm
    success_url = reverse_lazy('administration:add-ambion')

    def get_context_data(self, **kwargs):
        context = super(Add, self).get_context_data(**kwargs)
        workers = Staff.objects.filter(type=1)

        context['workers'] = workers
        return context

    def form_valid(self, form):
        print(form)
        form.save()
        return super(Add, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class Edit(generic.UpdateView):
    template_name = 'administrator/ambion/edit.html'
    model = Department
    form_class = AmbionForm

    def get_context_data(self, **kwargs):
        context = super(Edit, self).get_context_data(**kwargs)
        ambion = self.model.objects.get(id=self.kwargs['pk'])
        workers = Staff.objects.filter(type=1)
        context['ambion'] = ambion
        context['workers'] = workers
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
            messages.success(self.request, 'Ամբիոնը հաջողությամբ Խմբագրվել է։')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self.request, 'Սխալ! '+ str(form.errors))
            return self.render_to_response(
              self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('administration:edit-ambion', kwargs={'pk': int(self.kwargs['pk'])})

class List(generic.TemplateView):
    template_name = 'administrator/ambion/index.html'

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        ambionlist = Department.objects.all()
        request = self.request
        page = 1
        if 'page' in self.kwargs:
            page = self.kwargs['page'] or 1
            if 'ambions' in request.session:
                request.session['ambions']['page'] = page
            else:
                request.session['ambions'] = {}
                request.session['ambions']['page'] = page
        elif 'ambions' in request.session:
            if page in request.session.get('ambions'):
                page = request.session.get('ambions')['page']

        paginator = Paginator(ambionlist, 12)
        try:
            ambionlist = paginator.page(page)
        except PageNotAnInteger:
            ambionlist = paginator.page(1)
        except EmptyPage:
            ambionlist = paginator.page(paginator.num_pages)

        context['ambions'] = ambionlist
        context['paginator'] = ambionlist
        return context