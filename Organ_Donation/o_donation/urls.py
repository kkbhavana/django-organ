from .import views
from django.urls import path

from .views import SearchOrganView, OrganRegisterFormCreate, OrgandataView, OrgandataUpdate, OrgandataDelete, \
 SearchBloodView, BloodDataView, BloodRegisterFormCreate, BloodDataUpdate, BloodDataDelete

urlpatterns = [
 path('', views.home, name='home'),
 path('search_for_organ/',views.searchorgan,name='search_organ'),
 path('search_for_blood/',views.searchblood,name='search_blood'),
 path('search-organ/',SearchOrganView.as_view(),name='organ-result'),
 path('search-blood/',SearchBloodView.as_view(),name='blood-result'),
 path('organ_data/',OrgandataView.as_view(),name='organ-data'),
 path('blood_data/',BloodDataView.as_view(),name='blood-data'),
 path('organ_register_form/',OrganRegisterFormCreate.as_view(),name='register_organ'),
 path('blood_register_form/',BloodRegisterFormCreate.as_view(),name='register_blood'),
 path('organ_update_form/<int:pk>/',OrgandataUpdate.as_view(),name='update-organ'),
 path('blood_update_form/<int:pk>/',BloodDataUpdate.as_view(),name='update-blood'),
 path('organ_delete_form/<int:pk>/',OrgandataDelete.as_view(),name='delete-organ'),
 path('blood_deleteform/<int:pk>/',BloodDataDelete.as_view(),name='delete-blood'),

]