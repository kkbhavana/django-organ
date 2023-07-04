from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Doner


# Create your views here.
def home(request):
    return render(request, 'home.html')

def searchorgan(request):
    return render(request, 'organ_search.html')


class SearchView(LoginRequiredMixin, ListView):
    model = Doner
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Doner.objects.filter(
            Q(blood_group=query) | Q(organ=query)
        )


class MydataFormView(LoginRequiredMixin, ListView):
    model = Doner
    context_object_name = 'doner'
    template_name = 'mydata.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doner'] = context['doner'].filter(name=self.request.user)
        return context


class RegisterFormCreate(LoginRequiredMixin, CreateView):
    model = Doner
    fields = '__all__'
    success_url = reverse_lazy('data')
    template_name = 'register.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegisterFormCreate, self).form_valid(form)


class MydataUpdate(LoginRequiredMixin, UpdateView):
    model = Doner
    fields = '__all__'
    success_url = reverse_lazy('data')
    template_name = 'register.html'
