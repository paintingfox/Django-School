from basic import models
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School
    template_name = "basic_app/school_list.html"

class SchoolDetailView(DetailView):
     # defining conetxt object name by default it is school_list because of we are using Listview
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolDetailUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School
    template_name = 'basic_app/update.html'
    
class SchoolDetailCreateView(CreateView):
    fields = ('name', 'principal', 'loaction')
    model = models.School
    template_name = 'basic_app/update.html'

