from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Doner, BloodDoner


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signuphome(request):
    return render(request, 'signup_page.html')


def searchorgan(request):
    return render(request, 'organ_search.html')


def searchblood(request):
    return render(request, 'blood_search.html')


class SearchOrganView(LoginRequiredMixin, ListView):
    model = Doner
    template_name = 'organ_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Doner.objects.filter(
            Q(blood_group=query) | Q(organ=query)
        )


class SearchBloodView(LoginRequiredMixin, ListView):
    model = BloodDoner
    template_name = 'blood_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return BloodDoner.objects.filter(
            Q(blood_group=query) | Q(place=query)

        )


class OrgandataView(LoginRequiredMixin, ListView):
    model = Doner
    context_object_name = 'doner'
    template_name = 'organdata.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doner'] = context['doner'].filter(user=self.request.user)
        return context


class OrganRegisterFormCreate(LoginRequiredMixin, CreateView):
    model = Doner
    fields = ['name', 'age', 'gender', 'blood_group', 'organ', 'phone_number', 'place', 'status']
    success_url = reverse_lazy('organ-data')
    template_name = 'organ_register.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrganRegisterFormCreate, self).form_valid(form)


class OrgandataUpdate(LoginRequiredMixin, UpdateView):
    model = Doner
    fields = ['name', 'age', 'gender', 'blood_group', 'organ', 'phone_number', 'place', 'status']
    success_url = reverse_lazy('organ-data')
    template_name = 'organ_register.html'


class OrgandataDelete(LoginRequiredMixin, DeleteView):
    model = Doner
    fields = '__all__'
    success_url = reverse_lazy('organ-data')
    template_name = 'organ_delete.html'

class BloodDataView(LoginRequiredMixin,ListView):
    model = BloodDoner
    context_object_name = 'blood'
    template_name ='blooddata.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blood'] = context['blood'].filter(user=self.request.user)
        return context

class BloodRegisterFormCreate(LoginRequiredMixin,CreateView):
    model = BloodDoner
    fields = ['name', 'age', 'gender', 'blood_group', 'phone_number', 'place', 'status']
    template_name = 'blood_register.html'
    success_url = reverse_lazy('blood-data')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BloodRegisterFormCreate, self).form_valid(form)

class BloodDataUpdate(LoginRequiredMixin,UpdateView):
    model = BloodDoner
    fields = ['name', 'age', 'gender', 'blood_group', 'phone_number', 'place', 'status']
    template_name = 'blood_register.html'
    success_url = reverse_lazy('blood-data')


class BloodDataDelete(LoginRequiredMixin,DeleteView):
    model = BloodDoner
    template_name = 'blood_delete.html'
    success_url = reverse_lazy('blood-data')

