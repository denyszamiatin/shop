from django.conf.urls import url

from .views import add, view, change

urlpatterns = [
    url(r'^add$', add),
    url(r'^view$', view),
    url(r'^change$', change),
]