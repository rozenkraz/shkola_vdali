from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.start),
    url(r'student$', views.student),
    url(r'uchitel$', views.uchitel),
    url(r'add_urok$', views.add_urok),

]