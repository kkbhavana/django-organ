from .import views
from django.urls import path

from .views import SearchView

urlpatterns = [
 path('', views.home, name='home'),
 path('search_for_organ/',views.searchorgan,name='search_organ'),
 path('search/',SearchView.as_view(),name='search-result'),

]