from django.urls import path
from .views import SchoolListView, SchoolDetailView, SchoolDetailUpdateView
from django.conf.urls import url
from basic import views

app_name = 'basic_app'
urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name="list"),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(),name='detail'),
    url(r'^update(?P<pk>[-\w]+)/$', views.SchoolDetailUpdateView.as_view(), name='update')
]