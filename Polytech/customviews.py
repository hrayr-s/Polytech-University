import json

from django.http import HttpResponse
from django.views import generic


class JsonView(generic.TemplateView):

    # Ovveriding TemplateView.get to return json Data
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.returnHttpResponseJson(self.getJson(context))

    def getJson(self, diction):
        return json.dumps(diction)
        # return serializers.serialize('json', diction)

    def returnHttpResponseJson(self, json):
        return HttpResponse(json, content_type='application/json')


class JsonModelView(generic.TemplateView):

    # Overriding TemplateView.get to return json Data
    def get(self, request, *args, **kwargs):
        try:
            self.modelObject = self.model.objects.get(id=kwargs['pk'])
        except:
            self.modelObject = None
        context = self.get_context_data(**kwargs)
        return self.returnHttpResponseJson(self.getJson(context))

    def getJson(self, diction):
        return json.dumps(diction)

    def returnHttpResponseJson(self, json):
        return HttpResponse(json, content_type='application/json')
