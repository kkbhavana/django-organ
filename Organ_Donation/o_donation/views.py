from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Doner


# Create your views here.
def home(request):
    return render(request,'home.html')

def searchorgan(request):
    return render(request, 'organ_search.html')


class SearchView(LoginRequiredMixin,ListView):
    model = Doner
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Doner.objects.filter(
            Q(blood_group=query) | Q(organ=query)
        )

