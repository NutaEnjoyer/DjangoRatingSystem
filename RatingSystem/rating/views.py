from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


top_menu = []

def index(request):
	return HttpResponse("Hello")


class MainPage(ListView):
	model = Person
	template_name = 'main_page.html'
	context_object_name = 'persons'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Main page'
		return context


class PersonView(DetailView):
	model = Person
	slug_url_kwarg = 'person_slug'
	context_object_name = 'person'
	template_name = 'person.html'

	def get_queryset(self):
		resp = self.model.objects.filter(slug=self.kwargs['person_slug'])
		return resp

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = context['person'].name
		return context
