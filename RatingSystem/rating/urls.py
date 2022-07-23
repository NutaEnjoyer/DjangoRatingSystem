from django.urls import path

from . import views

urlpatterns = [
	path('', views.MainPage.as_view(), name='main_page'),
	path('index/', views.index, name='index'),
	path('about_author/', views.index, name='about_author'),
	path('login/', views.index, name='login'),
	path('signup/', views.index, name='signup'),
	path('person/<slug:person_slug>', views.PersonView.as_view(), name='person'),
]