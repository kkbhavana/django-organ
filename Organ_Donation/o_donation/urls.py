from .import views
from django.urls import path

from .views import SearchView, RegisterFormCreate, MydataFormView, MydataUpdate

urlpatterns = [
 path('', views.home, name='home'),
 path('search_for_organ/',views.searchorgan,name='search_organ'),
 path('search/',SearchView.as_view(),name='search-result'),
 path('my_data/',MydataFormView.as_view(),name='data'),
 path('registerform/',RegisterFormCreate.as_view(),name='register'),
 path('updateform/<int:pk>/',MydataUpdate.as_view(),name='update'),
]