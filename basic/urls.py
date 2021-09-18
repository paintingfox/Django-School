from django.urls import path
from .views import SchoolListView, SchoolDetailView, SchoolDetailUpdateView,SchoolDetailCreateView,SchoolDetailDeleteView,StudentCreateView
from django.conf.urls import url

app_name = 'basic_app'
urlpatterns = [
    url(r'^$', SchoolListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$',SchoolDetailView.as_view(),name='detail'),
    url(r'^create/$',SchoolDetailCreateView.as_view(),name='create'),
    url(r'^stCreate/$',StudentCreateView.as_view(),name='stCreate'),
    url(r'^update(?P<pk>[-\w]+)/$',SchoolDetailUpdateView.as_view(),name='update'),
    url(r'^delete(?P<pk>[-\w]+)/$',SchoolDetailDeleteView.as_view(),name='delete'),
   ]