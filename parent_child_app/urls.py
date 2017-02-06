from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'pc'
urlpatterns = [
    url(r'^parents/$', views.parents, name='parents'),
    
    # (?P<>...) is a named parameter parent_id that can be picked up in the view 
    url(r'^children/(?P<parent_id>\d+)/$', views.children, name='children'),
]
