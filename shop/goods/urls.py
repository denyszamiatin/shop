from django.conf.urls import url
from django.views.generic import ListView

from .views import index, detail, templ
from .models import Good

urlpatterns = [
    url(r'^$', index),
    url(r'^detail/(?P<slug>(\w|-)+)$', detail),
    url(r'^templ$', ListView.as_view(model=Good, paginate_by=1)),
]
