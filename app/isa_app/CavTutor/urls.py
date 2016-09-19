from django.conf.urls import url

from . import views, models

urlpatterns = [
    url(r'^api/v1/(?P<model>[a-z]+)/(?P<action>[a-z0-9]+)$', views.api_handler),
]
