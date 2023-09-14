from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return HttpResponseRedirect(redirect_to=reverse('administration:adminHome'))
