from django.conf.urls import url

from .views import index, detail, templ

urlpatterns = [
    url(r'^$', index),
    url(r'^detail/(?P<slug>(\w|-)+)$', detail),
    url(r'^templ$', templ),
]